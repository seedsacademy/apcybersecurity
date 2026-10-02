import argparse
import csv
import random
from datetime import datetime, timedelta, timezone
from pathlib import Path


FIELDNAMES = [
    "event_id",
    "timestamp",
    "event_type",
    "username",
    "src_ip",
    "action",
    "outcome",
    "resource",
]
SEED = 20260915
START_TIME = datetime(2026, 9, 15, 8, tzinfo=timezone.utc)
DAY_SECONDS = 9 * 60 * 60
USER_IPS = {
    "alice": "10.0.0.15",
    "bob": "10.0.0.21",
    "charlie": "10.0.0.33",
    "dana": "10.0.0.42",
    "eli": "10.0.0.53",
    "frank": "10.0.0.64",
    "service": "10.0.0.80",
    "guest": "10.0.0.99",
}
EXTERNAL_IPS = [
    "192.0.2.52",
    "192.0.2.88",
    "198.51.100.23",
    "198.51.100.77",
    "203.0.113.8",
    "203.0.113.17",
    "203.0.113.61",
    "203.0.113.88",
]
RESOURCES = [
    "/docs/team.txt",
    "/public/policies.pdf",
    "/reports/monthly-summary.pdf",
    "/reports/quarterly.pdf",
    "/shared/annual-report.csv",
    "/shared/grades.csv",
]


def format_timestamp(timestamp: datetime) -> str:
    return timestamp.isoformat(timespec="seconds").replace("+00:00", "Z")


def user_source_ip(randomizer: random.Random, username: str) -> str:
    if randomizer.random() < 0.12:
        return randomizer.choice(EXTERNAL_IPS)
    return USER_IPS[username]


def make_background_event(
    randomizer: random.Random,
    failed_login_counts: dict[tuple[str, str], int],
) -> dict[str, str]:
    timestamp = START_TIME + timedelta(seconds=randomizer.randrange(DAY_SECONDS))
    event_type = randomizer.choices(
        ["login", "file_access", "firewall", "logout", "policy_change"],
        weights=[38, 30, 26, 5, 1],
        k=1,
    )[0]

    if event_type == "login":
        username = randomizer.choice(list(USER_IPS))
        src_ip = user_source_ip(randomizer, username)
        pair = (src_ip, username)
        can_fail = failed_login_counts.get(pair, 0) < 2
        outcome = "failed" if can_fail and randomizer.random() < 0.025 else "success"
        if outcome == "failed":
            failed_login_counts[pair] = failed_login_counts.get(pair, 0) + 1
        action = "authenticate"
        resource = "/login"
    elif event_type == "file_access":
        username = randomizer.choice(list(USER_IPS))
        src_ip = user_source_ip(randomizer, username)
        action = "read"
        outcome = "success" if randomizer.random() < 0.985 else "denied"
        resource = randomizer.choice(RESOURCES)
    elif event_type == "firewall":
        username = "unknown"
        src_ip = (
            randomizer.choice(EXTERNAL_IPS)
            if randomizer.random() < 0.75
            else randomizer.choice(list(USER_IPS.values()))
        )
        protocol, port = randomizer.choice(
            [("tcp", 22), ("tcp", 80), ("tcp", 443), ("tcp", 445), ("tcp", 3389), ("udp", 53)]
        )
        action = "allow" if randomizer.random() < 0.88 else "deny"
        outcome = "allowed" if action == "allow" else "denied"
        resource = f"/{protocol}/{port}"
    elif event_type == "logout":
        username = randomizer.choice(list(USER_IPS))
        src_ip = USER_IPS[username]
        action = "sign_out"
        outcome = "success"
        resource = "/logout"
    else:
        username = "admin"
        src_ip = "10.0.0.10"
        action = randomizer.choice(["modify_policy", "rotate_certificate"])
        outcome = "success"
        resource = "/device-policy" if action == "modify_policy" else "/certificates"

    return {
        "timestamp": format_timestamp(timestamp),
        "event_type": event_type,
        "username": username,
        "src_ip": src_ip,
        "action": action,
        "outcome": outcome,
        "resource": resource,
    }


def investigation_events() -> list[dict[str, str]]:
    source_ip = "203.0.113.45"
    events = []
    for timestamp in (
        "2026-09-15T12:17:08+00:00",
        "2026-09-15T12:18:11+00:00",
        "2026-09-15T12:19:04+00:00",
    ):
        events.append(
            {
                "timestamp": format_timestamp(datetime.fromisoformat(timestamp)),
                "event_type": "login",
                "username": "alice",
                "src_ip": source_ip,
                "action": "authenticate",
                "outcome": "failed",
                "resource": "/login",
            }
        )

    events.extend(
        [
            {
                "timestamp": "2026-09-15T12:21:17Z",
                "event_type": "login",
                "username": "alice",
                "src_ip": source_ip,
                "action": "authenticate",
                "outcome": "success",
                "resource": "/login",
            },
            {
                "timestamp": "2026-09-15T12:23:31Z",
                "event_type": "file_access",
                "username": "alice",
                "src_ip": source_ip,
                "action": "read",
                "outcome": "success",
                "resource": "/reports/quarterly.pdf",
            },
        ]
    )

    for timestamp in (
        "2026-09-15T12:41:03Z",
        "2026-09-15T12:41:36Z",
        "2026-09-15T12:42:12Z",
    ):
        events.append(
            {
                "timestamp": timestamp,
                "event_type": "firewall",
                "username": "unknown",
                "src_ip": source_ip,
                "action": "deny",
                "outcome": "denied",
                "resource": "/tcp/22",
            }
        )
    return events


def generate_logs(output_path: Path, row_count: int) -> None:
    planted_events = investigation_events()
    if row_count < len(planted_events):
        raise ValueError(f"Row count must be at least {len(planted_events)}.")

    randomizer = random.Random(SEED)
    failed_login_counts: dict[tuple[str, str], int] = {}
    records = [
        make_background_event(randomizer, failed_login_counts)
        for _ in range(row_count - len(planted_events))
    ]
    records.extend(planted_events)
    randomizer.shuffle(records)

    for event_number, record in enumerate(records, start=1):
        record["event_id"] = f"E{event_number:04d}"

    with output_path.open("w", newline="", encoding="utf-8") as log_file:
        writer = csv.DictWriter(log_file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(records)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate deterministic synthetic cybersecurity logs.")
    parser.add_argument(
        "--rows",
        type=int,
        default=2000,
        help="Number of log records to generate (default: 2000).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("sample_logs.csv"),
        help="Output CSV path (default: sample_logs.csv beside this script).",
    )
    args = parser.parse_args()
    if args.rows < 1:
        parser.error("--rows must be at least 1")

    try:
        generate_logs(args.output, args.rows)
    except ValueError as error:
        parser.error(str(error))
    print(f"Generated {args.rows} synthetic log records at {args.output}.")


if __name__ == "__main__":
    main()
