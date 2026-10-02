# Class 24: Improve Application Defenses — Input Sanitization & Parameterization

[⬅ Back to Course Roadmap](../README.md) | [💻 Secure Code Remediation Lab](secure_code_lab.py)

> [!NOTE]
> **Mission Briefing:** The most secure firewall cannot protect a flawed web application. Security must be built directly into software code! By applying **Input Validation** (checking data at the door), **Parameterized Queries** (stopping SQL injection), and **HTML Output Encoding** (stopping XSS), developers build applications that can survive direct attacks from the internet. In this class, you will fix vulnerable code and verify the repair!

---

## Course Alignment & AP Framework

- **Course:** AP Cybersecurity
- **Unit 5:** Securing Applications and Data
- **CED Topic:** **5.5 Application Defenses & Secure Coding**
- **Course Framework Skills:**
  - **Skill 2.A:** Propose code-level and architectural defenses against web application vulnerabilities.
  - **Skill 2.B:** Verify remediation effectiveness through before-and-after testing.

### Learning Objectives & Essential Knowledge

| Objective ID | Learning Objective | Essential Knowledge Covered |
| :--- | :--- | :--- |
| **LO 5.5.A** | Apply input validation (allowlists) and output encoding to eliminate application vulnerabilities. | **EK 5.5.A.1:** Input allowlisting strictly defines acceptable characters, formats, and lengths. Output encoding converts special characters (`<`, `>`, `&`, `'`) into harmless HTML entities. |
| **LO 5.5.B** | Implement parameterized queries to prevent SQL injection. | **EK 5.5.B.1:** Prepared statements separate SQL query code from user-supplied data, ensuring input is never interpreted as executable syntax. |

---

## Core Concepts: Defense Against Application Exploits

### 1. Allowlisting vs. Blocklisting
- **Blocklisting (Bad):** Trying to filter out known bad words (`SELECT`, `<script>`, `DROP`). Attackers always find bypasses (e.g. `sElEcT`, `<<SCRIPT>script>`).
- **Allowlisting (Best):** Strictly defining what *is* allowed (e.g., a phone number field must ONLY contain digits `0-9` and be between 10-15 characters). Everything else is rejected!

### 2. Context-Aware Output Encoding
When displaying user comments on a webpage, replace dangerous characters with their HTML entity equivalents:
- `<` becomes `&lt;`
- `>` becomes `&gt;`
- `"` becomes `&quot;`

The browser renders the text safely on the screen without running it as JavaScript!

---

## Hands-on Lab Activity

Run the remediation lab:

```powershell
cd class_24_application_defenses
python secure_code_lab.py
```

### Student Activity: Code Remediation
Review the two demonstrations in the output:
1. Explain how a prepared statement prevents the malicious string `' OR '1'='1'` from executing SQL commands.
2. In the XSS demo, why does converting `<script>` to `&lt;script&gt;` prevent the script from stealing cookies?
3. Propose one additional browser defense (e.g., `HttpOnly` flag on cookies or Content Security Policy).

---

## Assessment: AP-Style Free Response Prompt

**Prompt:**  
A developer writes a user profile update form that takes a user's biography and writes it directly to the HTML page:  
`html_output = "<p>User Bio: " + user_bio + "</p>"`  
A user inputs: `<img src=x onerror="alert(document.cookie)">`

- **Part 1:** Identify the specific vulnerability and explain what occurs in the victim's browser when viewing this profile.
- **Part 2:** Provide the code-level remediation and explain why input length limits alone do not solve the vulnerability.

---

## Teacher Guidance & Answer Key

- **Part 1:** **Stored Cross-Site Scripting (XSS)**. The browser attempts to load an invalid image source `x`, fails, and immediately triggers the `onerror` JavaScript handler, executing arbitrary code that can exfiltrate session cookies to an attacker.
- **Part 2:** Apply **HTML Output Encoding** using a standard security library (e.g., `html.escape(user_bio)`) before embedding into the template. Input length limits restrict the size of the payload but do not neutralize malicious tags (a tiny XSS payload can be as short as 15 characters).

---

[⬅ Previous Class 23: Public & Private Keys](../class_23_public_private_keys/README.md) | [Next Class 25: Application & Data Events ➡](../class_25_application_data_events/README.md)
