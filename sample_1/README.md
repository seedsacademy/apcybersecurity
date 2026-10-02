# Exercise 1: Trace the Digital Footprints — Login & Firewall Investigation

[⬅ Back to Course Roadmap](../README.md)

> [!NOTE]
> **Mission Briefing:** You are a junior security analyst working in a Security Operations Center (SOC). Your security monitoring system just captured **2,000 digital events** across the organization's network in a single workday. Most of it is regular employee activity—people clocking in, reading files, and going to lunch. But buried inside the noise, an unusual sequence of events took place. Your mission: uncover the timeline, analyze the clues, and write an evidence-based report!

---

## The Investigation Scenario

In [sample_logs.csv](sample_logs.csv), you have 2,000 records from a fictional company's network on September 15, 2026. The records include logins, logouts, file access requests, firewall blocks, and security policy changes.

> [!IMPORTANT]
> **Detective Alert — Don't Trust Row Order!**
> Different servers record events independently, and network packets arrive in batches. The records in this CSV have been shuffled. **Always sort and follow the `timestamp` column chronologically** rather than reading from top to bottom!

### Safe Training Environment
- All data was generated automatically using [generate_sample_logs.py](generate_sample_logs.py).
- External IP addresses use special reserved test numbers (like `203.0.113.x`).
- Everything here is simulated for classroom practice—no real systems or private user data are involved.

---

## Evidence Files in Your Case Folder

| File | Role in the Investigation |
| :--- | :--- |
| [sample_logs.csv](sample_logs.csv) | **The Evidence File:** 2,000 recorded log events waiting to be investigated. |
| [analyze_logs.py](analyze_logs.py) | **The Automated Analyzer:** A Python script using pandas that generates 8 different investigative summaries of the data. |
| [generate_sample_logs.py](generate_sample_logs.py) | **The Generator:** Creates or resets the 2,000 practice records. Running this will overwrite the CSV with a fresh set of events. |
| [requirements.txt](requirements.txt) | Lists required Python libraries (`pandas`). |

---

## Deciphering the Clues: CSV Log Fields

Every line in the log is a "digital footprint" containing 8 key pieces of information:

| Field Name | What it Represents | Real-World Analogy |
| :--- | :--- | :--- |
| `event_id` | Unique ID number for this specific row | An evidence tag number on an evidence bag |
| `timestamp` | Time the event occurred in UTC (Universal Time) | A timestamp stamped on a security camera video |
| `event_type` | Broad category: `login`, `file_access`, `firewall`, `logout`, or `policy_change` | The type of incident report |
| `username` | The account name involved (`unknown` if blocked by firewall before login) | The name badge shown at the door |
| `src_ip` | Source IP: the digital network address where the request came from | The return address on an envelope, or a caller ID |
| `action` | What the user or system tried to do: `authenticate`, `read`, `modify`, `deny`, `allow` | Trying to turn a doorknob or open a drawer |
| `outcome` | What happened: `success`, `failed`, `denied`, or `allowed` | Did the door open or remain locked? |
| `resource` | What they targeted: `/login`, a file path (e.g. `/docs/financial_q3.xlsx`), or `/tcp/22` (SSH remote login port) | The specific room or safe someone tried to enter |

---

## 🔎 The Missing Clues: What the Logs DON'T Tell You

In movies, a cybersecurity analyst glances at a screen for 3 seconds and yells *"I found the hacker!"* 

In the real world, a good investigator knows that **logs only tell part of the story**. Jumping to conclusions without enough evidence can get an innocent person locked out of their job or leave a real threat unnoticed!

Before you decide whether a real cyberattack occurred, ask yourself what critical pieces of context are missing from this log:

1. **Which computer logged this?**
   There is no hostname or computer ID. Did these events happen on a receptionist's laptop or an executive's server?
2. **Where was the network traffic heading?**
   We see the source IP (`src_ip`), but there is no destination IP address. Was someone connecting to a public web server or a private internal database?
3. **Why did the login fail?**
   Did the user type the wrong password? Was their Caps Lock on? Was their account expired, or did multi-factor authentication (MFA) reject their phone?
4. **Is this normal behavior for this person?**
   Does this employee usually log in at this hour? Do they work remotely or in the building?
5. **Was file access authorized?**
   If someone downloaded a financial spreadsheet, do company rules permit them to read that file as part of their daily job?
6. **Are these separate events linked to the exact same human?**
   Without a shared session ID, three failed logins and a successful login from the same IP could be two different people sharing the same household Wi-Fi router.

> [!CAUTION]
> **The Golden Rule of Cyber Defense:**
> A spike in failed logins is an **investigation lead**, NOT automatic proof of an attack. Always separate what the data *proves* from what you *assume*!

---

## Running the Log Analyzer

Make sure you are in the `sample_1` folder in your terminal:

```powershell
# 1. Move into the sample_1 folder
cd sample_1

# 2. Install requirements (if not already installed)
python -m pip install -r requirements.txt

# 3. Run the log analysis tool!
python analyze_logs.py
```

### Advanced Detective Options: Customizing Your Investigation

Want to run experiments with your analyzer? Try these command flags:

```powershell
# Flag IPs with at least 4 failed logins instead of 3:
python analyze_logs.py --failed-login-threshold 4

# Test with your own custom log file:
python analyze_logs.py --log-file path\to\my_logs.csv

# Generate a massive dataset with 5,000 events to test your computer's speed:
python generate_sample_logs.py --rows 5000 --output big_logs.csv
python analyze_logs.py --log-file big_logs.csv
```

---

## Student Detective Tasks

Run `python analyze_logs.py`. The script will output **8 numbered sections**. Use those output tables to answer the questions below. 

Make sure to support every answer with **specific numbers, timestamps, usernames, and event IDs**!

### Phase 1: The Big Picture (Sections 1–4)
1. **Overview:** How many total events were recorded for each `event_type` and each `outcome`?
2. **Top Targets:** Which username experienced the most failed logins? Which username generated the most total activity overall?
3. **Suspicious Sources:** Which source IP addresses generated the most total traffic? How many distinct usernames were associated with each top IP?

### Phase 2: Drilling Down on Red Flags (Sections 5–7)
4. **Repeated Failures:** Which specific IP address and username pair had at least 3 failed logins in a row? What happened right after those failures?
5. **Firewall Blocks:** Which source IP was blocked the most times by the firewall? What specific port or service (`resource`) was it trying to touch?
6. **Traffic by the Hour:** In which hours did network traffic peak? Why should an analyst be careful when trying to define "normal" behavior based on just one single day of records?

### Phase 3: Crime Scene Reconstruction (Section 8)
7. **Trace the Timeline:** Pick the flagged IP from Section 8 and follow its events chronologically:
   - What sequence of actions did this IP take from start to finish?
   - What makes this sequence look suspicious?
   - What is a possible **innocent / benign explanation** that could also explain this exact same sequence?

### Phase 4: Final Case Report
8. **Next Steps & Tradeoffs:**
   - What 2 additional pieces of evidence or log sources would you request before declaring an official security incident?
   - Propose **one mitigation** (security rule or policy change) to protect the system.
   - Explain one **tradeoff** of your mitigation: could it accidentally inconvenience real employees or slow down legitimate business?

---

## Detective Self-Check & Answer Key

After you have attempted the questions, use this guide to verify your findings:

- **Total Counts (Sections 1 & 2):**
  - Exactly **2,000 records** total.
  - Types: **765** logins, **594** file accesses, **508** firewall checks, **118** logouts, and **15** policy changes.
  - Outcomes: **1,470** successes, **437** allowed, **77** denied, and **16** failures. *(Note: Firewall blocks show as `denied`, while bad logins show as `failed`).*
- **User Activity (Section 3):**
  - User `alice` has **5 failed logins** across the entire day.
- **The Flagged IP (Sections 5 & 8):**
  - IP `203.0.113.45` targeting user `alice` is the **only pair** that triggered the default threshold with **3 failed logins**.
- **The Timeline Clues (Section 8):**
  - Across a span of roughly 25 minutes, `203.0.113.45`:
    1. Fails to log into `alice` 3 consecutive times (`authenticate` / `failed`).
    2. Successfully logs in as `alice` on the 4th attempt (`authenticate` / `success`).
    3. Reads a document (`file_access` / `read` / `allowed`).
    4. Triggers 3 firewall blocks trying to connect to `/tcp/22` (SSH remote shell port).
- **The Verdict:**
  - *Suspicious theory:* An external attacker guessed Alice's password, logged in, viewed a file, and then tried to scan or open an SSH terminal to gain deeper control of the network.
  - *Innocent theory:* Alice was working from a hotel or coffee shop, mistyped her password three times, logged in successfully, checked her work file, and her laptop's background backup software attempted to sync over SSH port 22, which the office firewall blocked.
  - A top-scoring report explains **both possibilities** and recommends gathering firewall destination logs and asking Alice before taking drastic action!

---

[⬅ Return to Course Roadmap](../README.md) | [Go to Exercise 0: pandas Warm-up ➡](../sample_0/README.md)
