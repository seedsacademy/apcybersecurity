# Class 25: Investigate Application and Data Events — Web Logs & Exfiltration

[⬅ Back to Course Roadmap](../README.md) | [📁 Log File: web_access.log](web_access.log) | [💻 Log Parser Script](investigate_app_events.py)

> [!NOTE]
> **Mission Briefing:** Web servers record every single click, search query, and file request in access logs. When a hacker attempts to inject SQL commands or steal database tables, their payloads are logged in plain view alongside HTTP status codes and response byte sizes. In this class, you will parse web server access logs to uncover an active web application attack and verify data theft!

---

## Course Alignment & AP Framework

- **Course:** AP Cybersecurity
- **Unit 5:** Securing Applications and Data
- **CED Topic:** **5.6 Application Telemetry & Data Exfiltration Analysis**
- **Course Framework Skills:**
  - **Skill 3.A:** Parse HTTP server logs (Common Log Format) and extract request URIs, status codes, and payload sizes.
  - **Skill 3.B:** Correlate application errors (500 Internal Server Error) and oversized responses (200 OK with high byte count) to confirm exploitation.

### Learning Objectives & Essential Knowledge

| Objective ID | Learning Objective | Essential Knowledge Covered |
| :--- | :--- | :--- |
| **LO 5.6.A** | Interpret HTTP status codes and URI parameters in application access logs. | **EK 5.6.A.1:** Status codes: 200 (Success), 401/403 (Unauthorized/Forbidden), 404 (Not Found), 500 (Internal Server Error). SQLi indicators include encoded characters (`%27` for `'`), `UNION`, and `OR 1=1`. |
| **LO 5.6.B** | Detect data exfiltration through response size anomalies. | **EK 5.6.B.1:** A sudden surge in HTTP response bytes for a search query indicates bulk database record dumping. |

---

## Hands-on Lab Activity

Run the web log parser:

```powershell
cd class_25_application_data_events
python investigate_app_events.py
```

### Student Activity: Log Sleuthing
Inspect [web_access.log](web_access.log) and answer:
1. What automated attack tool did IP `198.51.100.42` use? (Check the `User-Agent` field).
2. What happened at 15:01:22 when the attacker sent `%27%20OR%201=1%20--`? Why did the server return a `500` status code?
3. At 15:01:45, the server returned status `200` with `95,400` bytes. What evidence proves that database exfiltration occurred?

---

## Assessment: AP-Style Free Response Prompt

**Prompt:**  
A security analyst reviews web access logs for an e-commerce website and spots 200 rapid requests within 30 seconds to `/product.php?id=...` returning HTTP status 200. The response size jumped from a normal 2,500 bytes to 450,000 bytes.

- **Part 1:** Identify the attack technique and explain what the dramatic change in response size indicates.
- **Part 2:** Propose an immediate incident response action and an architectural mitigation to prevent recurrence.

---

## Teacher Guidance & Answer Key

- **Part 1:** **Automated SQL Injection (SQLi) data exfiltration**. The jump from 2.5 KB to 450 KB demonstrates that the query bypassed individual product retrieval and dumped the entire customer or product table in a single bulk response.
- **Part 2:**
  - *Immediate action:* Temporarily block the offending source IP at the perimeter firewall / WAF, revoke compromised sessions, and take the vulnerable PHP script offline for emergency patching.
  - *Architectural mitigation:* Implement **parameterized database queries** and deploy a **Web Application Firewall (WAF)** configured with SQLi detection rulesets.

---

[⬅ Previous Class 24: Application Defenses](../class_24_application_defenses/README.md) | [Integration Start: Class 26: Team Security Assessment ➡](../class_26_team_security_assessment/README.md)
