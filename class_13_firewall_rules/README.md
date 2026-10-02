# Class 13: Read and Revise Firewall Rules — Rule Ordering & Logic

[⬅ Back to Course Roadmap](../README.md) | [💻 Firewall Rule Simulator](firewall_simulator.py)

> [!NOTE]
> **Mission Briefing:** A firewall is the gatekeeper of a network, examining packets and deciding whether to ALLOW or DENY them. But firewalls have a strict rule: **First Match Wins**. If an administrator places a generic `DENY ALL` rule at line 10, no rule placed at line 20 will ever be reached! In this class, you will evaluate ordered firewall rules, fix broken configurations, and prevent security bypasses.

---

## Course Alignment & AP Framework

- **Course:** AP Cybersecurity
- **Unit 3:** Securing Networks
- **CED Topic:** **3.4 Firewall Rule Logic and Ordering**
- **Course Framework Skills:**
  - **Skill 2.A:** Read, analyze, and repair ordered packet-filtering and stateful firewall rules.
  - **Skill 3.A:** Predict packet transmission outcomes based on source/dest IP, port, and protocol.

### Learning Objectives & Essential Knowledge

| Objective ID | Learning Objective | Essential Knowledge Covered |
| :--- | :--- | :--- |
| **LO 3.4.A** | Read and trace ordered firewall access control lists (ACLs). | **EK 3.4.A.1:** Firewalls evaluate rules sequentially from top to bottom. The first rule matching a packet determines the action; remaining rules are ignored. |
| **LO 3.4.B** | Revise a flawed ruleset to permit legitimate operations while blocking unauthorized traffic. | **EK 3.4.B.1:** The default rule at the end of an ACL should be an explicit or implicit DENY ALL (zero-trust default). Specific allow rules must precede general deny rules. |

---

## Hands-on Lab Activity

Run the firewall simulator:

```powershell
cd class_13_firewall_rules
python firewall_simulator.py
```

### Student Activity: Fixing a Rule Order Bug
Suppose a junior technician accidentally swapped Rule 10 and Rule 20:
- Rule 10: `DENY ANY to 10.0.40.0/24 (Server Core)`
- Rule 20: `ALLOW Staff (10.0.20.0/24) to 10.0.40.50 Port 443`

1. Trace what happens when a teacher tries to open the grading portal. Which rule matches first?
2. Why is rule ordering critical to network availability?

---

## Assessment: AP-Style Free Response Prompt

**Prompt:**  
An organization's web server at IP `10.0.10.5` hosts both a public website on port 443 and an administrative management console on port 8443. The firewall administrator configured the following inbound rules:

| Rule # | Action | Source IP | Destination IP | Port | Protocol |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | ALLOW | ANY | 10.0.10.5 | 443, 8443 | TCP |
| 2 | DENY | ANY (Internet) | 10.0.10.5 | 8443 | TCP |
| 3 | ALLOW | 10.0.20.0/24 (IT Admin) | 10.0.10.5 | 8443 | TCP |
| 4 | DENY | ANY | ANY | ANY | ANY |

- **Part 1:** Identify the fatal rule order mistake that exposes the administrative console on port 8443 to the entire public internet.
- **Part 2:** Rewrite the corrected, secure rule order.

---

## Teacher Guidance & Answer Key

- **Part 1:** Rule 1 permits ANY source to access port 8443. Because firewalls evaluate rules from top to bottom on a **first-match-wins** basis, internet traffic hitting port 8443 matches Rule 1 and is ALLOWED. Rules 2 and 3 are never evaluated for port 8443!
- **Part 2:** Corrected Rule Order:
  1. `ALLOW 10.0.20.0/24 to 10.0.10.5 Port 8443 TCP` (Permit IT admins first)
  2. `DENY ANY to 10.0.10.5 Port 8443 TCP` (Block everyone else from port 8443)
  3. `ALLOW ANY to 10.0.10.5 Port 443 TCP` (Permit public website)
  4. `DENY ANY to ANY Port ANY` (Implicit deny)

---

[⬅ Previous Class 12: Network Segmentation](../class_12_network_segmentation/README.md) | [Next Class 14: Network Anomalies ➡](../class_14_network_anomalies/README.md)
