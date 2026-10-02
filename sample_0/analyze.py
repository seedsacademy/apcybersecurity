"""Step-by-step pandas introduction using login_events.csv.

Run it with:  python analyze.py
Each step prints a heading so you can match the output to the README.
"""
from pathlib import Path

import pandas as pd

CSV_FILE = Path(__file__).with_name("login_events.csv")


def step(title):
    print(f"\n=== {title} ===")


# Step 1: load the CSV into a DataFrame (a table with rows and columns).
# parse_dates turns the timestamp text into real date/time values.
df = pd.read_csv(CSV_FILE, parse_dates=["timestamp"])

# Step 2: look at the data before analyzing it.
step("First 5 rows")
print(df.head())

step("Shape (rows, columns)")
print(df.shape)

step("Column types")
print(df.dtypes)

# Step 3: count values in one column.
step("Logins by outcome")
print(df["outcome"].value_counts())

# Step 4: filter rows with a condition.
failed = df[df["outcome"] == "failed"]
step("Failed logins")
print(failed)

# Step 5: group rows and summarize each group.
step("Failed logins per source IP")
print(failed.groupby("src_ip").size().sort_values(ascending=False))

# Step 6: add a new column calculated from an existing one.
df["hour"] = df["timestamp"].dt.hour
step("Events per hour (UTC)")
print(df.groupby("hour").size())

# Step 7: combine steps to answer a question.
# Which IPs had 3 or more failed logins?
fail_counts = failed.groupby("src_ip").size()
suspicious = fail_counts[fail_counts >= 3]
step("IPs with 3+ failed logins")
print(suspicious)

# Step 8: follow up on a lead by showing every event from that IP in time order.
for ip in suspicious.index:
    step(f"Timeline for {ip}")
    print(df[df["src_ip"] == ip].sort_values("timestamp")[["timestamp", "username", "outcome"]])
