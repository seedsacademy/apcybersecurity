# Class 27: Investigate One Device Using Multiple Sources — AP FRQ Mastery

[⬅ Back to Course Roadmap](../README.md) | [💻 Multi-Source Correlator Script](multi_source_correlator.py)

> [!NOTE]
> **Mission Briefing:** On Section II of the AP Cybersecurity exam, you will encounter the **Device Security Analysis Free-Response Question** (50 minutes, 30% of your total exam score). The exam provides **four authentic sources for a single device**: a device policy, firewall rules, file permissions, and system logs. Your task: synthesize all four sources to detect the attack, explain policy violations, and write a complete hardening plan.

---

## Course Alignment & AP Framework

- **Course:** AP Cybersecurity
- **Exam Target:** **Section II: Free-Response Question (Device Security Analysis)**
- **Course Framework Skills:**
  - **Skill 1.C:** Analyze security policies, firewall rules, and file permissions.
  - **Skill 3.B:** Correlate disparate log sources with policy baselines to identify compromises.
  - **Skill 2.A:** Propose concrete hardening revisions across network, host, and application layers.

---

## The 4 Evidence Sources Explained

```text
               THE AP FREE-RESPONSE 4-SOURCE MODEL
               
       [ Source 1: Device Policy ]     <-- Tells you what WAS SUPPOSED to happen
       [ Source 2: Firewall Rules ]    <-- Network layer: What ports were open?
       [ Source 3: File Permissions ]  <-- Host layer: Who had read/write access?
       [ Source 4: System Logs ]       <-- Telemetry: What ACTUALLY happened?
```

---

## Hands-on Lab Activity

Run the correlator:

```powershell
cd class_27_multi_source_device_investigation
python multi_source_correlator.py
```

### Student Activity: The 4-Source Analysis Matrix
1. **Identify the Policy Violation:** Compare the timestamp and protocol in Source 4 against Source 1. What two specific policy rules were broken?
2. **Identify the Firewall Vulnerability:** Which firewall rule in Source 2 permitted the adversary to reach the server? How should this rule be rewritten?
3. **Identify the Permission Defect:** Why was the service account `backup_svc` able to read `/var/data/patients/records_2026.db`? What should the file mode be?
4. **Identify the Attack Technique:** Trace the commands in Source 4: what utility did the attacker use to exfiltrate patient records?

---

## Full AP-Style Scoring Rubric

| Part | Points | Criteria for Full Credit |
| :---: | :---: | :--- |
| **A (Policy)** | 1 pt | Cites connection at 23:45 UTC (outside 07:00-19:00 window) and use of SSH (strictly prohibited). |
| **B (Firewall)** | 1 pt | Identifies Rule 2 as overly permissive; revises rule to restrict SSH to IT management IP or deletes rule. |
| **C (Permissions)** | 1 pt | Identifies mode 666 as world-readable; corrects to mode 640 or 600 restricted to `dr_smith` / `clinical_staff`. |
| **D (Hardening)** | 1 pt | Recommends disabling password-based SSH in favor of public-key authentication, enforcing MFA, and removing netcat. |

---

[⬅ Previous Class 26: Team Assessment](../class_26_team_security_assessment/README.md) | [Next Class 28: Multiple Choice Practice ➡](../class_28_multiple_choice_practice/README.md)
