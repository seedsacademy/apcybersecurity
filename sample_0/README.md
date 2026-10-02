# Exercise 0: Meet pandas — Your Data Superpower

[⬅ Back to Course Roadmap](../README.md)

> [!NOTE]
> **Who is this for?** Students who know basic Python (variables, loops, functions, lists, and dictionaries) and are ready to learn how real cyber detectives analyze massive piles of data.

---

## What is pandas?

Imagine you are given a spreadsheet with **100,000 login records** and asked to find who tried to hack into the school server. 

Opening that in Excel might crash your laptop. Writing nested Python `for` loops and `if` statements takes forever and gets messy fast.

That is where **pandas** comes in! 

**pandas** is Python's most popular tool for working with **tables** (data organized into rows and columns, just like Google Sheets or CSV files). It gives you superpowers to:
- 📂 **Load** huge files in a fraction of a second
- 🧹 **Clean up** messy or missing data
- 🔍 **Filter & Search** for suspicious clues in a single line of code
- 📊 **Summarize & Count** patterns instantly (like "How many failed logins happened per user?")
- 🔗 **Connect & Combine** different files together (like matching an IP address to a student or employee name)

> [!TIP]
> **Why do Cybersecurity Pros use it?**
> Security teams don't read log files line by line like a book. They use pandas to sift through millions of network events, spot abnormal spikes, and track down intruders!

---

## Why Not Just Use Plain Python?

You *can* read a CSV file using standard Python `for` loops and dictionaries. But watch what happens when you compare the two.

Run [plain_python_vs_pandas.py](plain_python_vs_pandas.py) to see both approaches solve the exact same question: *"How many failed logins came from each IP address?"*

```python
# --- Option A: Plain Python (needs a loop, an 'if', and a counter) ---
counts = Counter()
with open("login_events.csv", newline="") as f:
    for row in csv.DictReader(f):
        if row["outcome"] == "failed":
            counts[row["src_ip"]] += 1

# --- Option B: pandas (done in one readable line!) ---
df[df["outcome"] == "failed"].groupby("src_ip").size()
```

If your boss or teacher asks five follow-up questions:
- *"What about per hour?"*
- *"What about only for the admin account?"*
- *"Can we sort from highest to lowest?"*

In plain Python, you have to rewrite your loops every single time. In pandas, you just tweak a single line!

---

## Two Core Concepts to Know First

pandas works with two main building blocks:

| Building Block | What it is | Think of it like... |
| :--- | :--- | :--- |
| **`Series`** | A single column of data with an index label for each item | A single column in a spreadsheet, or a Python list with custom labels |
| **`DataFrame`** | A full table made of multiple Series sharing the same rows | An entire spreadsheet page with rows and column headers |

```text
       DataFrame (The Whole Table)
       +-----------+-----------+----------+
       | timestamp | username  | outcome  |  <-- Column Names
       +-----------+-----------+----------+
row 0  | 08:01:12  | alex      | success  |
row 1  | 08:02:45  | taylor    | failed   |  <-- Each vertical column
row 2  | 08:03:10  | admin     | failed   |      is a Series!
       +-----------+-----------+----------+
```

Most of learning pandas is simply learning how to ask questions to a **DataFrame**.

---

## Files in This Lab

| File | What it does |
| :--- | :--- |
| [requirements.txt](requirements.txt) | Tells Python which libraries to install (`pandas`). |
| [login_events.csv](login_events.csv) | 30 practice login records (`timestamp`, `username`, `src_ip`, `outcome`). |
| [users.csv](users.csv) | Company directory (`username`, `department`, `role`). We use this to connect tables. |
| [plain_python_vs_pandas.py](plain_python_vs_pandas.py) | Head-to-head comparison between regular Python loops and pandas. |
| [analyze.py](analyze.py) | **Start here!** A guided 8-step script with helpful explanations. |
| [showcase.py](showcase.py) | A quick tour showing 12 cool tricks pandas can do. |

> [!NOTE]
> **Safety Note:** All data in this lab is 100% fake and created for classroom practice. IP addresses starting with `203.0.113.x` are special test numbers reserved for textbooks and documentation (just like the fake `555-0100` phone numbers in movies!).

---

## Part 1: Setup Your Environment

Open your terminal or command prompt and check that Python is ready:

```bash
# Check your Python version (use python3 and pip3 on Mac/Linux)
python --version
pip --version
```

### Step 1: Create a Virtual Environment (Recommended)

A virtual environment is like a private workspace on your computer that keeps packages organized for this specific project without messing up other Python projects.

```powershell
# 1. Create the virtual environment folder named .venv
python -m venv .venv

# 2. Activate it!
.venv\Scripts\activate          # Windows PowerShell / Command Prompt
source .venv/bin/activate       # Mac / Linux
```

*(You will know it worked when you see `(.venv)` appear at the start of your terminal line!)*

### Step 2: Install pandas

We use `requirements.txt` so anyone can install the exact right tools with one command:

```bash
pip install -r requirements.txt
```

Verify that pandas installed successfully:

```bash
python -c "import pandas; print('pandas version:', pandas.__version__)"
```

*(Optional bonus: if you want to generate visual charts in `showcase.py`, run `pip install matplotlib`)*

---

## Part 2: Your First 8 Detective Steps

Run the guided analysis script in your terminal:

```bash
python analyze.py
```

Now, open [analyze.py](analyze.py) in your editor and look at the code side-by-side with your terminal output. Here are the 8 fundamental commands you just ran:

```python
import pandas as pd

# 1. Load the data (and automatically parse dates so Python understands time)
df = pd.read_csv("login_events.csv", parse_dates=["timestamp"])

# 2. Inspect the crime scene! (Always check your data before doing math)
df.head()                                  # Sneak peek at the first 5 rows
df.shape                                   # Size of the table: (number of rows, number of columns)
df.dtypes                                  # Data types: are numbers treated as integers? dates as timestamps?

# 3. Count categories
df["outcome"].value_counts()               # How many 'success' vs 'failed' logins occurred?

# 4. Filter for specific clues (Rows where outcome is 'failed')
failed = df[df["outcome"] == "failed"]

# 5. Group and summarize
failed.groupby("src_ip").size()            # Count failures per IP address

# 6. Extract time patterns
df["hour"] = df["timestamp"].dt.hour       # Extract just the hour (0-23) to see when logins happen
```

> [!IMPORTANT]
> **The Golden Rule of Data Analysis:** Always inspect your data first using `.head()`, `.shape`, and `.dtypes`. If Python thinks a date or number is just plain text (`object`), your math and filters will behave strangely!

---

## Part 3: What Else Can pandas Do?

Run the feature tour script:

```bash
python showcase.py
```

Here is a quick cheat sheet of pandas superpowers:

| # | Superpower | Code Example | Why Cyber Analysts Care |
| :---: | :--- | :--- | :--- |
| **1** | **Read any file** | `pd.read_csv()`, `pd.read_json()` | Logs come in CSV, JSON, Excel, and SQL formats. |
| **2** | **Instant stats** | `df.describe()` | Instantly see min, max, averages, and anomalies. |
| **3** | **Pick columns & rows** | `df[["username", "outcome"]]` | Hide irrelevant info and focus only on the clues you need. |
| **4** | **Filter with logic** | `df[(df["outcome"] == "failed") & (df["hour"] > 22)]` | Find suspicious activity (e.g., failures late at night). |
| **5** | **Group & Count** | `df.groupby("src_ip").size()` | Find who is making the most noise on the network. |
| **6** | **Join tables** | `df.merge(users, on="username")` | Link an anonymous username to their real department and job title. |
| **7** | **Pivot tables** | `df.pivot_table(...)` | Make easy-to-read cross-tables (like Users vs Outcomes). |
| **8** | **Time analysis** | `df.resample("1h").count()` | Detect sudden spikes or brute-force floods over time. |
| **9** | **Text searching** | `df["src_ip"].str.startswith("10.")` | Distinguish internal school devices from external internet IPs. |
| **10**| **Find missing clues**| `df.isna().sum()` | Identify missing fields or broken log records. |
| **11**| **Export reports** | `df.to_csv("report.csv")` | Save your evidence to share with your team or teacher. |
| **12**| **Plot charts** | `df["outcome"].value_counts().plot(kind="bar")` | Turn numbers into clear visual graphs for presentations. |

---

## What Does the Evidence Show?

Look closely at the output from **Step 7 and Step 8** in `analyze.py`:

1. Filtering for failed logins shows that IP address `203.0.113.50` had **6 rapid failures** in a row!
2. First, it tried the username `frank` multiple times.
3. Then, it switched targets and tried `admin` multiple times.
4. Immediately after the failures, there is a **successful login** for `admin`!

> [!CAUTION]
> **Detective Thinking Check:**
> Does this *prove* the account was hacked?
> 
> **No, not by itself!** In cybersecurity, an alert is an **investigation lead**, not proof of guilt:
> - Could this be a real attacker trying a password-guessing dictionary attack? Absolutely.
> - Could it be a legitimate IT admin who forgot their password, tried their personal username first by mistake, and then finally typed the right admin password? Yes!
> - Could it be an authorized security test conducted by the school's tech staff? Also yes!
>
> To know for sure, you would need to investigate what happened *after* the login (e.g., did they download sensitive files?) and ask the user if they were at their desk.

Meanwhile, other users in the file had single failed logins followed right away by a success from their normal internal IP. Those look like everyday typos!

---

## Practice Challenges

Open Python or create a short test script using `login_events.csv` and `users.csv`. For each question, write the pandas code, run it, and write one sentence explaining what your result reveals:

1. **User Count:** How many unique usernames appear in the log? *(Hint: `.nunique()`)*
2. **Top User:** Which username has the highest total number of login attempts? *(Hint: `.value_counts()`)*
3. **Targeted Accounts:** Which specific usernames did the suspicious IP `203.0.113.50` try to log into? *(Hint: Filter by that IP, then use `.unique()` on the username column)*
4. **Time Gap:** How many seconds passed between the *first* failed attempt from `203.0.113.50` and its first *successful* login? *(Hint: Subtract the two timestamps)*
5. **Department Clues:** Merge `login_events.csv` with `users.csv` on the `username` column. Which department had the most failed logins?
6. **Flagging Outsiders:** Add a new column called `is_external` that is `True` when `src_ip` does *not* start with `10.`. *(Hint: `~df["src_ip"].str.startswith("10.")`)*
7. **⭐ Detective Challenge:** Calculate the failure rate for every user (`failed attempts / total attempts`) and sort from highest to lowest. Who has the highest failure percentage?

---

## Troubleshooting Guide: Don't Panic!

When coding, errors are just clues pointing you to the fix. Here are the most common ones:

| What you see | What it means | How to fix it |
| :--- | :--- | :--- |
| `'pip' is not recognized` | Your system path is missing pip, or Python isn't activated. | Run `python -m pip install -r requirements.txt`. |
| `ModuleNotFoundError: No module named 'pandas'` | pandas is not installed in the Python environment you are currently running. | Make sure your `.venv` is activated (look for `(.venv)` in prompt), then install pandas again. |
| `FileNotFoundError: login_events.csv` | Python is looking in the wrong folder. | Make sure your terminal is in the `sample_0` directory (`cd sample_0`). |
| `KeyError: 'Outcome'` | pandas couldn't find that column name. | Column names are case-sensitive! Use lowercase `'outcome'`. |
| `ValueError: Cannot use and / or` | You tried using Python's word `and` instead of pandas syntax. | In pandas, wrap each condition in `()` and use `&` (and) or `\|` (or): `(df["a"] > 1) & (df["b"] == 2)`. |

---

## Helpful Resources

Want to dive deeper? Check out these student-friendly tutorials:
- 📖 [10 Minutes to pandas (Official Quickstart)](https://pandas.pydata.org/docs/user_guide/10min.html) — Fast overview of essentials.
- 🎮 [Kaggle Pandas Micro-Course](https://www.kaggle.com/learn/pandas) — Free, interactive in-browser exercises.
- 🐍 [W3Schools Python pandas Tutorial](https://www.w3schools.com/python/pandas/default.asp) — Short examples you can test right in your browser.
- 📄 [Official pandas Cheat Sheet (PDF)](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf) — Great one-page summary to bookmark or print out.

---

## Ready for the Next Mission?

Now that you know the basics of pandas, let's step into a realistic cybersecurity investigation!

👉 Continue to [Exercise 1: Trace Login and Firewall Events](../sample_1/README.md) to inspect **2,000 digital records** and hunt down suspicious activity across a network!
