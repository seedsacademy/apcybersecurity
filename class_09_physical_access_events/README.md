# Class 09: Investigate Physical Access Events — Correlating Badges & Alarms

[⬅ Back to Course Roadmap](../README.md) | [📁 Telemetry Log: badge_events.csv](badge_events.csv) | [💻 Physical Correlator](investigate_physical.py)

> [!NOTE]
> **Mission Briefing:** Digital forensics does not stop at keyboard logs. When a physical facility is breached, investigators must correlate electronic badge swipes, door contact sensors, and motion detectors into a precise timeline to discover how an intruder moved through the building. In this class, you will analyze physical access logs to reconstruct a real intrusion!

---

## Course Alignment & AP Framework

- **Course:** AP Cybersecurity
- **Unit 2:** Securing Spaces
- **CED Topic:** **2.4 Physical Access Telemetry & Incident Correlation**
- **Course Framework Skills:**
  - **Skill 3.A:** Parse and chronologically sort physical telemetry (swipes, sensors, alarms).
  - **Skill 3.B:** Correlate physical records with digital timestamps to support or refute an incident hypothesis.

### Learning Objectives & Essential Knowledge

| Objective ID | Learning Objective | Essential Knowledge Covered |
| :--- | :--- | :--- |
| **LO 2.4.A** | Correlate physical badge records, motion detectors, and door alarms into an incident timeline. | **EK 2.4.A.1:** Physical telemetry logs capture timestamps, door IDs, badge credentials, and alarm states (e.g., Door Forced Open, Door Held Open). |
| **LO 2.4.B** | Reconstruct an adversary's physical movements and distinguish authorized actions from breaches. | **EK 2.4.B.1:** Anomalies include access denied spikes, out-of-hours swipes, and impossible travel times between badge readers. |

---

## Hands-on Lab Activity

Run the correlator:

```powershell
cd class_09_physical_access_events
python investigate_physical.py
```

### Student Activity: Reconstructing the Server Room Breach
Inspect [badge_events.csv](badge_events.csv) and answer:
1. Whose badge was used right before the break-in? Did that badge have permission to enter the server room?
2. What evidence proves that a physical human actually entered the server room, rather than the door sensor merely glitching?
3. How did the intruder exit the facility? Why didn't they badge out at the main lobby?

---

## Assessment: AP-Style Free Response Prompt

**Prompt:**  
At 10:14 PM, a university security operations center receives an alert that the root administrator password was entered on the physical console of the campus domain controller. Badge logs show that professor Dr. Harris badged into the engineering lab at 10:12 PM. However, security camera footage confirms Dr. Harris was attending a conference 200 miles away.

- **Part 1:** Explain the most probable physical security breakdown that enabled this unauthorized console access.
- **Part 2:** Propose two controls (one physical and one technical) that would prevent this attack even if an employee's physical badge is stolen.

---

## Teacher Guidance & Answer Key

- **Part 1:** The attacker acquired or cloned Dr. Harris's physical access badge (stolen badge / badge cloning) and used it to enter the lab.
- **Part 2:**
  - **Physical control:** Require **Two-Factor Physical Authentication** (e.g., badge swipe PLUS a personal PIN or biometric fingerprint reader) to enter high-security server rooms.
  - **Technical control:** Require **Multi-Factor Authentication (MFA)** on the domain controller console, and configure screen auto-lock timeouts and CCTV facial recognition alerts at sensitive doorways.

---

[⬅ Previous Class 08: Layered Protection](../class_08_physical_protection/README.md) | [Unit 3 Start: Class 10: Network Attack Paths ➡](../class_10_network_attack_paths/README.md)
