# Class 02: Investigate Suspicious Logins — Password Attacks & MFA

[⬅ Back to Course Roadmap](../README.md) | [📁 Dataset: logins.csv](logins.csv) | [💻 Analyzer Script](analyze_logins.py)

> [!NOTE]
> **Mission Briefing:** Passwords are the most common form of digital authentication, but they are also under constant attack. In this class, you will investigate simulated authentication records, detect automated password attacks (brute-force vs. password spraying), and evaluate multi-factor authentication (MFA) protections and their real-world tradeoffs.

---

## Course Alignment & AP Framework

- **Course:** AP Cybersecurity
- **Unit 1:** Introduction to Security
- **CED Topic:** **1.2 Passwords and Authentication**
- **Course Framework Skills:**
  - **Skill 1.B:** Differentiate between password attacks (brute force, dictionary, credential stuffing, password spraying).
  - **Skill 2.A:** Recommend account protections (MFA, rate limiting, lockout policies) and analyze usability tradeoffs.
  - **Skill 3.A:** Detect attack patterns in authentication logs.

### Learning Objectives & Essential Knowledge

| Objective ID | Learning Objective | Essential Knowledge Covered |
| :--- | :--- | :--- |
| **LO 1.2.A** | Distinguish between brute-force, dictionary, password spraying, and credential stuffing attacks. | **EK 1.2.A.1:** Brute force tests many passwords on one account; password spraying tests common passwords across many accounts to bypass lockouts. |
| **LO 1.2.B** | Evaluate authentication mechanisms (passwords, MFA, biometrics) and propose mitigations. | **EK 1.2.B.1:** Multi-Factor Authentication requires two or more distinct factors: something you know, something you have, something you are. |

---

## Lesson Plan & Pacing (50-Minute Period)

| Time | Phase | Focus |
| :--- | :--- | :--- |
| **00–05 min** | **Warm-up** | Password strength debate: Why is `Tr0ub4dor&3` worse than `correct-horse-battery-staple`? |
| **05–15 min** | **Instruction** | The 3 Authentication Factors + Password Attack Taxonomies (Brute Force vs Spraying). |
| **15–35 min** | **Lab Activity** | Run `python analyze_logins.py` and inspect [logins.csv](logins.csv) to trace attack patterns. |
| **35–45 min** | **Assessment** | AP-style FRQ prompt on account lockout policies and Denial of Service (DoS) tradeoffs. |
| **45–50 min** | **Debrief** | Summary: Why MFA stops 99% of password attacks. |

---

## Core Concepts: Authentication Under Attack

### The 3 Factors of Authentication
To count as Multi-Factor Authentication (MFA), credentials must come from **different categories**:
1. **Something you know:** Password, PIN, security question.
2. **Something you have:** Smartphone authenticator app, hardware security key (YubiKey), SMS code.
3. **Something you are:** Fingerprint, facial recognition, iris scan (biometrics).

> [!WARNING]
> A password plus a PIN is **NOT** multi-factor authentication—both are "something you know"!

### Anatomy of Password Attacks

| Attack Type | Pattern | Attacker Goal |
| :--- | :--- | :--- |
| **Brute Force** | 1 Account $\leftarrow$ 1,000s of rapid passwords | Crack a specific high-value target (e.g., `admin`). |
| **Password Spraying** | 1,000 Accounts $\leftarrow$ 1 or 2 common passwords (`Summer2026!`) | Avoid triggering account lockout thresholds! |
| **Credential Stuffing** | Millions of leaked username/password pairs tested automatically | Exploit users who reuse passwords across multiple websites. |

---

## Hands-on Lab Activity

Run the analyzer:

```powershell
cd class_02_suspicious_logins
python analyze_logins.py
```

### Student Investigation Tasks
1. **Identify the Brute Force Target:** Look at Section 2. Which IP conducted rapid attempts against the `admin` account? How many failed before succeeding?
2. **Unmask the Password Spray:** Look at Section 3. Notice how IP `198.51.100.14` tries user1, user2, user3, etc., using a script (`Python-Requests`). Why didn't an account lockout stop this attacker?
3. **Analyze MFA:** In Section 4, user `jordan` had a failed login followed by success. What caused the failure?

---

## Assessment: AP-Style Free Response Prompt

**Prompt:**  
A high school network administrator configures an account lockout policy: *"Any account with 3 failed logins will be locked for 24 hours."*  
- **Part A:** Explain how an external attacker could abuse this policy to launch a **Denial of Service (DoS)** against teachers and students.
- **Part B:** Propose an alternative mitigation (e.g., rate limiting / progressive delays or MFA) that stops password guessing without locking legitimate users out of their work.

---

## Teacher Guidance & Answer Key

- **Part A:** An attacker can script failed logins for every known student and teacher account (`student01`, `student02`, ...). After 3 attempts each, the entire school is locked out of their computers for 24 hours without the attacker ever needing valid credentials.
- **Part B:** Implement **Multi-Factor Authentication (MFA)** and **IP-based rate limiting (CAPTCHA / exponential backoff delays)**. This slows attackers down to a crawl without locking users out entirely.

---

[⬅ Previous Class 01: Social Engineering](../class_01_social_engineering/README.md) | [Next Class 03: Public Wi-Fi ➡](../class_03_public_wifi/README.md)
