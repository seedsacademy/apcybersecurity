# Exercise 1: Trace Login and Firewall Events

[Back to the course README](../README.md)

## Goal

Use Python and `pandas` to summarize a realistic-sized log file, find patterns in routine activity, trace related events, and explain what the evidence does and does not show.

## Scenario

[sample_logs.csv](sample_logs.csv) contains 2,000 synthetic records from a fictional organization's systems during the workday on September 15, 2026 (UTC). It mixes login, file-access, firewall, policy-change, and logout events. Event IDs are assigned after the records are shuffled, so sort and compare timestamps rather than relying on row order. The varied routine activity makes unusual sequences harder to spot.

The records are generated reproducibly by [generate_sample_logs.py](generate_sample_logs.py). The external-looking IPs use documentation-only address ranges; all activity is fabricated for classroom practice. This is not a real security incident and must not be used to investigate public systems.

## Files

- [sample_logs.csv](sample_logs.csv): the input data, with 2,000 event records plus a header row.
- [analyze_logs.py](analyze_logs.py): the pandas analyzer. It displays eight views: event type, outcome, user activity, source-IP activity, repeated failed logins, denied firewall events, hourly volume, and a timeline for IPs that meet the repeated-login threshold.
- [generate_sample_logs.py](generate_sample_logs.py): deterministic sample-data generator. Running it overwrites `sample_logs.csv`.
- [requirements.txt](requirements.txt): Python package dependency for the analyzer.

## CSV Fields

| Field | Meaning |
| --- | --- |
| `event_id` | Identifier for this row; it does not link related events into a session. |
| `timestamp` | Time the event was recorded, in UTC (`Z`). |
| `event_type` | Category, such as `login`, `file_access`, or `firewall`. |
| `username` | Account associated with the event; `unknown` means the firewall record does not identify a user. |
| `src_ip` | Source IP address recorded for the event. |
| `action` | Action attempted, such as `authenticate`, `read`, or `deny`. |
| `outcome` | Result, such as `success`, `failed`, `denied`, or `allowed`. |
| `resource` | Target recorded in a compact form, such as `/login`, a file path, or `/tcp/22`. |

## What Is Missing?

This dataset is useful for practice, but it is not enough to prove that an account or system was compromised. Identify missing context before making a conclusion:

- **Which device produced each event?** There is no hostname, device ID, or separate log-source field.
- **What exactly happened on the network?** There are no separate destination IP, source/destination port, and protocol columns; `/tcp/22` is only a compact resource value.
- **Why did authentication fail or succeed?** The log has no failure reason, authentication method, MFA result, session ID, or account-lockout status.
- **Was the activity expected for this person and device?** There is no device/browser identifier, user role, normal schedule, or approved access list.
- **Was the file access authorized?** The log does not include file sensitivity, permissions, or an authorization decision.
- **Can events from different systems be reliably connected?** There is no shared request/session identifier or log-collection and integrity information.

Discuss how each missing detail could change the interpretation. A successful login after failed attempts is worth checking, but this data alone cannot establish who used the account or whether access was authorized.

## Run the Analyzer

From the project root, run:

```powershell
cd sample_1
python -m pip install -r requirements.txt
python analyze_logs.py
```

The sample CSV is already included. To regenerate the default 2,000 records, run `python generate_sample_logs.py` from `sample_1`; it overwrites `sample_logs.csv` with the same seeded data.

To generate a larger or separate practice dataset:

```powershell
python generate_sample_logs.py --rows 3000 --output larger_sample.csv
python analyze_logs.py --log-file larger_sample.csv
```

To analyze another CSV file or change the repeated-failure threshold:

```powershell
python analyze_logs.py --log-file path\to\events.csv --failed-login-threshold 4
```

## Student Tasks

Use the eight output sections to answer these questions. Support conclusions with event IDs, timestamps, and fields from the CSV.

1. How many events are recorded for each event type and outcome?
2. Which user has the most failed logins? Which user has the most total events?
3. Which source IP addresses generated the most events, and how many distinct usernames appear for each?
4. Which IP and username combination has at least three failed logins? What events follow those failures?
5. Which source IP has the most denied firewall events? What resource or port was targeted?
6. How does event volume change by hour? What limitations are there when drawing conclusions from a small sample?
7. Choose a source IP in the repeated-failure results and trace its events in timestamp order. Which sequence deserves investigation, and what benign explanation might also fit?
8. What additional logs or context would you request before deciding whether an account was compromised? Recommend one mitigation and explain its tradeoff.

## Facilitator Self-Check

Use this after attempting the questions to check that the output was read correctly:

- The file contains **2,000 records**. The type counts are 765 logins, 594 file-access events, 508 firewall events, 118 logouts, and 15 policy changes.
- The outcome counts are 1,470 successes, 437 allowed events, 77 denials, and 16 failures. These counts combine different event types, so an `allowed` firewall decision is distinct from a `success` login.
- The user summary shows Alice with 5 failed logins overall. Grouping by both username and source IP reveals that **Alice and `203.0.113.45` have 3 failed logins**, the only pair at the default threshold.
- That IP's timeline contains 8 events: three failed logins, a successful login, a file read, and three firewall denials for `/tcp/22`. The activity is spread across about 25 minutes, not adjacent CSV rows.
- The hourly summary covers the 08:00 through 16:00 UTC hours. Describe peaks or quieter periods from the output rather than infer normal behavior from a single day of synthetic data.

The expected conclusion is **a pattern that needs investigation, not proof of an attack**. A strong response separates observed facts from assumptions, names useful missing evidence, and considers a reasonable benign explanation.
