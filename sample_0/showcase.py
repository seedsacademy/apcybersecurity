"""A tour of what pandas can do, using login_events.csv and users.csv.

Run it with:  python showcase.py
Each section prints a heading. Read the code, then compare it to the output.
"""
from pathlib import Path

import pandas as pd

HERE = Path(__file__).parent


def section(title):
    print(f"\n=== {title} ===")


# 1. Read data from a file (also: read_excel, read_json, read_sql ...)
logins = pd.read_csv(HERE / "login_events.csv", parse_dates=["timestamp"])
users = pd.read_csv(HERE / "users.csv")

# 2. Summarize everything at once
section("describe(): quick summary of every column")
print(logins.describe(include="all"))

# 3. Select columns and rows
section("Select columns, then rows by position (iloc)")
print(logins[["username", "outcome"]].iloc[:3])

# 4. Filter with conditions (combine with & and |)
section("Failed logins from outside the 10.x network")
external_failed = logins[(logins["outcome"] == "failed") & (~logins["src_ip"].str.startswith("10."))]
print(external_failed)

# 5. Group and aggregate several things at once
section("groupby + agg: per-user summary")
per_user = logins.groupby("username").agg(
    events=("outcome", "size"),
    failures=("outcome", lambda s: (s == "failed").sum()),
    first_seen=("timestamp", "min"),
)
print(per_user)

# 6. Merge (join) two tables, like SQL JOIN
section("merge: add department to each login")
joined = logins.merge(users, on="username", how="left")
print(joined[["timestamp", "username", "department", "outcome"]].head())

# 7. Pivot table: rows x columns summary
section("pivot_table: failures and successes per department")
print(joined.pivot_table(index="department", columns="outcome", values="username", aggfunc="count", fill_value=0))

# 8. Time series: resample into 2-hour buckets
section("resample: events per 2 hours")
print(logins.set_index("timestamp").resample("2h").size())

# 9. String tools
section("String methods: usernames in upper case")
print(logins["username"].str.upper().unique())

# 10. Missing data: pandas represents it as NaN and gives you tools for it
section("Missing data: left merge leaves NaN when there is no match")
extra = pd.DataFrame({"username": ["alice", "zoe"]}).merge(users, on="username", how="left")
print(extra)
print("Rows with a missing department:", extra["department"].isna().sum())

# 11. Save results
section("Export")
out = HERE / "failed_by_ip.csv"
logins[logins["outcome"] == "failed"].groupby("src_ip").size().to_csv(out, header=["failed_count"])
print(f"Wrote {out.name}")

# 12. Plot (needs matplotlib; skipped if it is not installed)
section("Plot")
try:
    ax = logins.groupby(logins["timestamp"].dt.hour).size().plot(kind="bar", title="Events per hour (UTC)")
    ax.figure.savefig(HERE / "events_per_hour.png")
    print("Wrote events_per_hour.png")
except ImportError:
    print("matplotlib not installed. Run: pip install matplotlib")
