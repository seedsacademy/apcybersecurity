# Class 20: Explain Application Attack Paths — SQLi, XSS & Input Flaws

[⬅ Back to Course Roadmap](../README.md) | [💻 Application Attack Simulator](app_attacks_sim.py)

> [!NOTE]
> **Mission Briefing:** Web applications accept data from users all over the world: search boxes, login forms, and comments. But what happens when an attacker types computer code instead of a name? If an application trusts user input without checking it, attacks like **SQL Injection (SQLi)** and **Cross-Site Scripting (XSS)** can bypass firewalls and steal entire databases. In this class, you will analyze application attack paths!

---

## Course Alignment & AP Framework

- **Course:** AP Cybersecurity
- **Unit 5:** Securing Applications and Data
- **CED Topic:** **5.1 Application Attack Paths & Input Vulnerabilities**
- **Course Framework Skills:**
  - **Skill 1.C:** Explain application-layer attack vectors (SQLi, XSS, Path Traversal, Buffer Overflow).
  - **Skill 3.A:** Trace how unvalidated input compromises back-end databases and client browsers.

### Learning Objectives & Essential Knowledge

| Objective ID | Learning Objective | Essential Knowledge Covered |
| :--- | :--- | :--- |
| **LO 5.1.A** | Analyze common application attack vectors arising from improper input handling. | **EK 5.1.A.1:** SQL Injection alters SQL database query logic. Cross-Site Scripting injects malicious scripts into other users' web browsers. |
| **LO 5.1.B** | Describe the technical consequences of application exploitation. | **EK 5.1.B.1:** Exploitation leads to unauthorized database exfiltration, session cookie hijacking, and arbitrary remote code execution. |

---

## Hands-on Lab Activity

Run the attack simulator:

```powershell
cd class_20_application_attacks
python app_attacks_sim.py
```

### Student Activity: Input Vulnerability Deconstruction
Review the 3 attacks in the script:
1. Explain how `' OR '1'='1' --` tricks a database into returning true even with an invalid password.
2. What is the difference between an attack that targets the **server's database** (SQLi) vs. an attack that targets the **victim's web browser** (XSS)?
3. Why is "checking for bad words" (blacklisting) easily bypassed by clever attackers compared to parameterized queries?

---

## Assessment: AP-Style Free Response Prompt

**Prompt:**  
A school grading portal has a student search field that runs:  
`query = "SELECT * FROM students WHERE last_name = '" + user_input + "'"`  
An attacker inputs: `Smith' UNION SELECT username, password_hash, ssn FROM admin_users --`

- **Part 1:** Identify the specific attack being executed and explain what the attacker achieves.
- **Part 2:** Rewrite the Python/database query logic using **parameterized queries (prepared statements)** to make this attack impossible.

---

## Teacher Guidance & Answer Key

- **Part 1:** **SQL Injection (SQLi) via UNION-based extraction**. The injected single quote terminates the literal string, and the `UNION SELECT` command executes a secondary query appending sensitive administrative credentials and Social Security numbers to the displayed search results.
- **Part 2:**
  ```python
  # Secure implementation using parameterized query:
  cursor.execute("SELECT * FROM students WHERE last_name = %s", (user_input,))
  ```
  The database engine treats `user_input` purely as inert literal data, never as executable SQL syntax!

---

[⬅ Previous Class 19: Device Activity](../class_19_trace_device_activity/README.md) | [Next Class 21: File Permissions ➡](../class_21_file_permissions/README.md)
