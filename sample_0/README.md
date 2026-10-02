# Exercise 0: Meet pandas, the Python Data Analysis Library

[Back to the course README](../README.md)

**Audience:** students who already write basic Python (variables, loops, functions, lists and dictionaries) and have not used pandas.

## What is pandas?

**pandas** is the standard Python library for working with tabular data: anything shaped like a spreadsheet, a CSV file, or a database table. It gives you a fast, expressive way to **load, clean, filter, summarize, join, and export** data, often in one line per task.

Data scientists, analysts, and security teams use it because real data is too big and messy to handle with hand-written loops. Log files, alert exports, and network records are all tables.

### Why not just use plain Python?

You can read a CSV with the `csv` module and count things with a loop and a `Counter`. That works for one question, but each new question needs a new loop. Run [plain_python_vs_pandas.py](plain_python_vs_pandas.py) to see the same question answered both ways:

```python
# Plain Python: a loop and counting logic
counts = Counter()
with open("login_events.csv", newline="") as f:
    for row in csv.DictReader(f):
        if row["outcome"] == "failed":
            counts[row["src_ip"]] += 1

# pandas: one expression
df[df["outcome"] == "failed"].groupby("src_ip").size()
```

## Two ideas to learn first

| Object | What it is | Python analogy |
| --- | --- | --- |
| `Series` | One labeled column of values | A list with an index and a type |
| `DataFrame` | A table of Series that share the same row index | A dictionary of lists, or a spreadsheet |

Most of pandas is learning how to ask questions of a DataFrame.

## Files

| File | Purpose |
| --- | --- |
| [requirements.txt](requirements.txt) | Packages to install (`pandas`). |
| [login_events.csv](login_events.csv) | 30 synthetic login events: `timestamp`, `username`, `src_ip`, `outcome`. |
| [users.csv](users.csv) | Who each user is: `username`, `department`, `role`. Used to show joins. |
| [plain_python_vs_pandas.py](plain_python_vs_pandas.py) | Same task in plain Python and in pandas. |
| [analyze.py](analyze.py) | Guided 8-step analysis. Start here after setup. |
| [showcase.py](showcase.py) | A tour of 12 things pandas can do. |

All data is fabricated for classroom practice. The `203.0.113.x` address is a documentation-only range and does not belong to any real system.

## Part 1: Set up

Check that Python and pip are installed (use `python3` and `pip3` on macOS/Linux):

```
python --version
pip --version
```

### Create a virtual environment (recommended)

A virtual environment keeps this project's packages separate from the rest of your computer.

```
python -m venv .venv
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # macOS/Linux
```

Your prompt shows `(.venv)` when it is active.

### Install from requirements.txt

`requirements.txt` lists the packages a project needs, so anyone can recreate your setup. Ours has one line:

```
pandas>=2.0,<4.0
```

Install and verify:

```
pip install -r requirements.txt
python -c "import pandas; print(pandas.__version__)"
```

Optional, for the plot at the end of `showcase.py`:

```
pip install matplotlib
```

## Part 2: First steps

Run the guided analysis, then read [analyze.py](analyze.py) next to its output:

```
python analyze.py
```

The essentials, which you can also type in a Python prompt:

```python
import pandas as pd

df = pd.read_csv("login_events.csv", parse_dates=["timestamp"])  # load

df.head()                                  # first 5 rows
df.shape                                   # (rows, columns)
df.dtypes                                  # column types
df["outcome"].value_counts()               # count each value

failed = df[df["outcome"] == "failed"]     # filter rows
failed.groupby("src_ip").size()            # group and count

df["hour"] = df["timestamp"].dt.hour       # add a calculated column
```

Always inspect the data first with `head()`, `shape`, and `dtypes`. Check that the columns and types are what you expect before trusting any result.

## Part 3: What pandas can do

Run the tour:

```
python showcase.py
```

| # | Capability | Key code | Why it matters |
| --- | --- | --- | --- |
| 1 | Read many file types | `read_csv`, `read_excel`, `read_json`, `read_sql` | Data arrives in many formats. |
| 2 | Summarize instantly | `describe()` | Spot counts, ranges, and odd values quickly. |
| 3 | Select columns and rows | `df[["a","b"]]`, `iloc`, `loc` | Focus on the part you need. |
| 4 | Filter with conditions | `df[(cond1) & (cond2)]` | Find events that match a rule. |
| 5 | Group and aggregate | `groupby(...).agg(...)` | Per-user, per-IP, per-hour summaries. |
| 6 | Join tables | `merge(..., on="username")` | Add context like department to each event. |
| 7 | Pivot tables | `pivot_table(...)` | Compare categories side by side. |
| 8 | Time series | `set_index("timestamp").resample("2h")` | Count events per time window. |
| 9 | String tools | `.str.startswith()`, `.str.upper()` | Clean and match text. |
| 10 | Handle missing data | `isna()`, `fillna()`, `dropna()` | Real data has gaps. |
| 11 | Export results | `to_csv`, `to_excel` | Share findings. |
| 12 | Plot | `.plot(kind="bar")` | Make a chart straight from a table. |

## What does the data show?

Filtering for failures and grouping by IP reveals one source, `203.0.113.50`, with six quick failures across two accounts (`frank`, then `admin`), followed by a **success** for `admin`. This fits a password-guessing pattern. It does not prove the account was taken over: the data does not show what happened after the login, or whether this was an authorized test. The other single failures, each followed by a success from the same internal IP, look like ordinary typos.

## Practice

Use `login_events.csv` and `users.csv`. Write the code, then one sentence on what the result means.

1. How many unique usernames appear? (`nunique()`)
2. Which user has the most events? (`value_counts()`)
3. Which usernames did `203.0.113.50` try? (`unique()`)
4. How many seconds passed between the first failed attempt from that IP and its success? (Subtract two timestamps.)
5. Merge in `users.csv`. Which department had the most failed logins?
6. Add a column `is_external` that is `True` when `src_ip` does not start with `10.`.
7. Challenge: for each user, calculate the failure rate (`failures / events`) and sort from highest to lowest.

## Learn more: external tutorials

| Resource | Best for |
| --- | --- |
| [10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html) | Official quick tour of the core features. |
| [pandas Getting Started tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/) | Official step-by-step lessons with sample data. |
| [Kaggle Learn: Pandas](https://www.kaggle.com/learn/pandas) | Free, short, interactive lessons in the browser. |
| [Real Python: Using pandas to explore a dataset](https://realpython.com/pandas-python-explore-dataset/) | A guided walkthrough for Python programmers. |
| [W3Schools pandas tutorial](https://www.w3schools.com/python/pandas/default.asp) | Short examples you can run and edit. |
| [pandas cheat sheet (PDF)](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf) | A one-page reference to keep beside you. |
| [pandas API reference](https://pandas.pydata.org/docs/reference/index.html) | Look up any function and its options. |

## Common problems

| Problem | Fix |
| --- | --- |
| `'pip' is not recognized` | Use `python -m pip install -r requirements.txt`. |
| `ModuleNotFoundError: No module named 'pandas'` | Install into the same Python you run; activate your venv first. |
| `FileNotFoundError: login_events.csv` | Open the terminal in the `sample_0` folder. |
| `KeyError: 'Outcome'` | Column names are case-sensitive. Use `outcome`. |
| `ValueError` when combining conditions | Wrap each condition in parentheses and use `&` / `\|`: `(a) & (b)`. |

## Next

Continue with [Exercise 1: Trace Login and Firewall Events](../sample_1/README.md), which applies the same ideas to 2,000 records.
