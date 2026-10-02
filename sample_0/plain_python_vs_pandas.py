"""The same question answered two ways: plain Python vs pandas.

Question: how many failed logins did each source IP have?
Run it with:  python plain_python_vs_pandas.py
"""
import csv
from collections import Counter
from pathlib import Path

import pandas as pd

CSV_FILE = Path(__file__).with_name("login_events.csv")

# --- Plain Python: csv module + Counter ---
counts = Counter()
with open(CSV_FILE, newline="") as f:
    for row in csv.DictReader(f):
        if row["outcome"] == "failed":
            counts[row["src_ip"]] += 1

print("Plain Python:")
for ip, n in counts.most_common():
    print(f"  {ip}: {n}")

# --- pandas: load, filter, group ---
df = pd.read_csv(CSV_FILE)
result = df[df["outcome"] == "failed"].groupby("src_ip").size().sort_values(ascending=False)

print("\npandas:")
print(result)

# The plain version works for one question. When the next question is
# "per hour?", "per user?", "join with a department list?", pandas needs
# one more line each, while plain Python needs a new loop each time.
