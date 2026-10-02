import argparse
from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = {
    "event_id",
    "timestamp",
    "event_type",
    "username",
    "src_ip",
    "action",
    "outcome",
    "resource",
}


def print_section(title: str, table: pd.DataFrame) -> None:
    print(f"\n{title}")
    print("-" * len(title))
    if table.empty:
        print("No matching records.")
    else:
        print(table.to_string(index=False))


def analyze_logs(log_path: Path, failed_login_threshold: int) -> None:
    events = pd.read_csv(log_path)
    missing_columns = sorted(REQUIRED_COLUMNS - set(events.columns))
    if missing_columns:
        raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")

    events["timestamp"] = pd.to_datetime(events["timestamp"], utc=True, errors="coerce")
    invalid_timestamps = int(events["timestamp"].isna().sum())
    if invalid_timestamps:
        raise ValueError(f"Found {invalid_timestamps} row(s) with invalid timestamps.")

    for column in ("event_type", "outcome", "username", "src_ip"):
        events[column] = events[column].fillna("").astype(str).str.strip()
    events["event_type"] = events["event_type"].str.lower()
    events["outcome"] = events["outcome"].str.lower()
    events = events.sort_values("timestamp")

    failed_login_mask = events["event_type"].eq("login") & events["outcome"].eq("failed")
    failed_logins = events.loc[failed_login_mask]
    denied_firewall = events.loc[
        events["event_type"].eq("firewall") & events["outcome"].eq("denied")
    ]

    print(f"Loaded {len(events)} events from {log_path}.")
    print("Indicators are investigation leads, not proof of compromise.")

    event_counts = events.groupby("event_type").size().reset_index(name="event_count")
    print_section("1. Events by type", event_counts)

    outcome_counts = events.groupby("outcome").size().reset_index(name="event_count")
    print_section("2. Events by outcome", outcome_counts)

    user_activity = (
        events.assign(is_failed_login=failed_login_mask)
        .groupby("username")
        .agg(
            total_events=("event_id", "count"),
            failed_logins=("is_failed_login", "sum"),
        )
        .reset_index()
        .sort_values(["failed_logins", "total_events"], ascending=False)
    )
    print_section("3. Activity by user", user_activity)

    source_activity = (
        events.groupby("src_ip")
        .agg(
            total_events=("event_id", "count"),
            unique_users=("username", "nunique"),
        )
        .reset_index()
        .sort_values("total_events", ascending=False)
    )
    print_section("4. Activity by source IP", source_activity)

    repeated_failures = (
        failed_logins.groupby(["src_ip", "username"])
        .size()
        .reset_index(name="failed_login_count")
        .query("failed_login_count >= @failed_login_threshold")
        .sort_values("failed_login_count", ascending=False)
    )
    print_section(
        f"5. Repeated failed logins (at least {failed_login_threshold})",
        repeated_failures,
    )

    denied_by_ip = (
        denied_firewall.groupby("src_ip")
        .size()
        .reset_index(name="denied_connection_count")
        .sort_values("denied_connection_count", ascending=False)
    )
    print_section("6. Denied firewall activity by source IP", denied_by_ip)

    events_by_hour = (
        events.assign(hour=events["timestamp"].dt.floor("h"))
        .groupby("hour")
        .size()
        .reset_index(name="event_count")
    )
    print_section("7. Events by hour (UTC)", events_by_hour)

    flagged_ips = set(repeated_failures["src_ip"])
    timeline_columns = [
        "event_id",
        "timestamp",
        "event_type",
        "username",
        "src_ip",
        "action",
        "outcome",
        "resource",
    ]
    flagged_timeline = events.loc[events["src_ip"].isin(flagged_ips), timeline_columns]
    print_section("8. Timeline for IPs with repeated failed logins", flagged_timeline)


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize and trace events in a CSV log.")
    parser.add_argument(
        "--log-file",
        type=Path,
        default=Path(__file__).with_name("sample_logs.csv"),
        help="CSV log to analyze (default: sample_logs.csv beside this script).",
    )
    parser.add_argument(
        "--failed-login-threshold",
        type=int,
        default=3,
        help="Minimum failures from one IP for one username to flag (default: 3).",
    )
    args = parser.parse_args()

    if args.failed_login_threshold < 1:
        parser.error("--failed-login-threshold must be at least 1")
    if not args.log_file.is_file():
        parser.error(f"log file does not exist: {args.log_file}")

    try:
        analyze_logs(args.log_file, args.failed_login_threshold)
    except (pd.errors.ParserError, ValueError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
