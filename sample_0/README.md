# Exercise 0: Introduction to pandas for Data Analysis

[Back to the course README](../README.md)

## What is this?

Security work produces a lot of data: login records, firewall logs, alerts. Reading thousands of lines by hand does not work. **pandas** is a Python library that loads tabular data (like a spreadsheet or CSV file) and lets you filter, count, group, and sort it with a few lines of code.

This exercise is a short warm-up before [sample_1](../sample_1/README.md). You will analyze a tiny log of 30 synthetic login events and answer: **was there a suspicious pattern?**

All data is fabricated for classroom practice. The `203.0.113.x` address is a documentation-only range, so it does not belong to any real system.

## Files

| File | Purpose |
| --- | --- |
| [requirements.txt](requirements.txt) | Lists the packages to install (`pandas`). |
| [login_events.csv](login_events.csv) | The data: 30 login events with `timestamp`, `username`, `src_ip`, `outcome`. |
| [analyze.py](analyze.py) | Step-by-step pandas analysis. Read it top to bottom. |

## Part 1: Set up

You need Python 3.9 or newer. Check it in a terminal opened in this folder:

```
python --version
pip --version
```

(On macOS/Linux, use `python3` and `pip3`.)

### Optional: create a virtual environment

A virtual environment (venv) keeps this project's packages separate from the rest of your computer.

```
python -m venv .venv
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # macOS/Linux
```

Your prompt will show `(.venv)` when it is active.

### Install pandas

`requirements.txt` is a plain text file listing the packages a project needs. Ours has one line:

```
pandas>=2.0,<4.0
```

`pip` is Python's package installer. Install everything in the file with:

```
pip install -r requirements.txt
```

Confirm it worked:

```
python -c "import pandas; print(pandas.__version__)"
```

If you see a version number, you are ready.

## Part 2: Use pandas

Run the whole script first to see the output:

```
python analyze.py
```

Then work through the steps below. Better yet, type them yourself in the Python prompt (`python`) or a new file.

### Step 1: Load the data

```python
import pandas as pd

df = pd.read_csv("login_events.csv", parse_dates=["timestamp"])
```

`df` is a **DataFrame**: a table with rows and named columns. `parse_dates` converts the timestamp text into real date/time values so you can sort and group by time.

### Step 2: Look before you analyze

```python
df.head()      # first 5 rows
df.shape       # (30, 4) = 30 rows, 4 columns
df.dtypes      # the type of each column
```

Always check the data first. Are the columns what you expected? Are there missing values?

### Step 3: Count values

```python
df["outcome"].value_counts()
```

Expected: 21 `success` and 9 `failed`.

### Step 4: Filter rows

```python
failed = df[df["outcome"] == "failed"]
```

The condition inside `[...]` keeps only rows where it is true. `failed` is a new, smaller DataFrame with 9 rows.

### Step 5: Group and summarize

```python
failed.groupby("src_ip").size().sort_values(ascending=False)
```

This counts failed logins per source IP. One address, `203.0.113.50`, has 6 of the 9 failures.

### Step 6: Add a calculated column

```python
df["hour"] = df["timestamp"].dt.hour
df.groupby("hour").size()
```

This shows how many events happened in each hour (UTC). Hour 9 is the busiest.

### Step 7: Combine steps to answer a question

```python
fail_counts = failed.groupby("src_ip").size()
fail_counts[fail_counts >= 3]
```

Which IPs had three or more failures? Only `203.0.113.50`.

### Step 8: Follow the lead

```python
ip = "203.0.113.50"
df[df["src_ip"] == ip].sort_values("timestamp")[["timestamp", "username", "outcome"]]
```

The timeline shows several failures in about 30 seconds, across two usernames (`frank`, then `admin`), ending in a **success** for `admin`.

## What does the evidence show?

- One external-looking IP made many fast failed attempts against more than one account.
- The last attempt, for `admin`, succeeded.
- This fits a password-guessing pattern, but the data alone does not prove it. We do not know whether `admin` was really taken over, what the account did afterward, or whether this was an authorized test.

Notice that the other failures (`carol`, `erin`, `bob`) each have a single failure followed by a success from the same internal IP. That looks like a mistyped password, which is normal.

## Practice questions

Answer each one with pandas, then write one sentence about what it means.

1. How many unique usernames appear? (`df["username"].nunique()`)
2. Which user has the most events?
3. List every successful login from `203.0.113.50`. What does it mean for that account?
4. Which usernames did `203.0.113.50` try? (`.unique()`)
5. How many seconds passed between the first failed attempt and the success from that IP? (Subtract two timestamps.)
6. Challenge: which hour had the highest share of failed logins?

## Common problems

| Problem | Fix |
| --- | --- |
| `'pip' is not recognized` | Use `python -m pip install -r requirements.txt`. |
| `ModuleNotFoundError: No module named 'pandas'` | Install it in the same Python you run, and activate your venv first. |
| `FileNotFoundError: login_events.csv` | Open the terminal in the `sample_0` folder, or use the full path. |
| `KeyError: 'Outcome'` | Column names are case-sensitive. Use `outcome`. |

## Next

Continue with [Exercise 1: Trace Login and Firewall Events](../sample_1/README.md), which uses the same ideas on 2,000 records.
