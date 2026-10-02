# Class 07: Find Physical Weaknesses — Perimeter Breaches & Environmental Risks

[⬅ Back to Course Roadmap](../README.md) | [💻 Floor Plan Audit Tool](floorplan_audit.py)

> [!NOTE]
> **Mission Briefing:** All the firewalls and encryption in the world cannot protect a server if an intruder walks into the building and unplugs the hard drive! Physical security protects physical hardware, cabling, and human spaces from unauthorized access, theft, tampering, and environmental disasters. In this class, you will audit a building floor plan and hunt down physical security weaknesses.

---

## Course Alignment & AP Framework

- **Course:** AP Cybersecurity
- **Unit 2:** Securing Spaces
- **CED Topic:** **2.2 Physical Security Vulnerabilities**
- **Course Framework Skills:**
  - **Skill 1.C:** Identify physical access vulnerabilities in facilities and floor plans.
  - **Skill 3.A:** Annotate attack paths across physical perimeters and access zones.

### Learning Objectives & Essential Knowledge

| Objective ID | Learning Objective | Essential Knowledge Covered |
| :--- | :--- | :--- |
| **LO 2.2.A** | Identify physical vulnerabilities that allow unauthorized access to facilities and hardware. | **EK 2.2.A.1:** Weaknesses include tailgating/piggybacking, unmonitored emergency exits, propped doors, shared physical keys, and camera blind spots. |
| **LO 2.2.B** | Describe physical reconnaissance tactics like dumpster diving and shoulder surfing. | **EK 2.2.B.1:** Attackers search trash for sensitive documents (dumpster diving) or observe PINs/credentials over victims' shoulders. |

---

## Core Concepts: Physical Attack Methods

### 1. Tailgating vs. Piggybacking
- **Tailgating:** An unauthorized person slips through an open door behind an authorized worker without their knowledge.
- **Piggybacking:** An unauthorized person convinces an authorized worker to hold the door open for them (exploiting social politeness).

### 2. Propped Doors & Blind Spots
Even high-tech badge access systems fail when employees prop doors open with garbage cans or wooden wedges for convenience (e.g., loading deliveries or taking breaks).

### 3. Dumpster Diving
Attackers recover discarded hard drives, employee directories, invoices, and password sticky notes from company trash bins that were not properly shredded or destroyed.

---

## Hands-on Lab Activity

Run the audit script:

```powershell
cd class_07_physical_weaknesses
python floorplan_audit.py
```

### Student Activity: Floor Plan Vulnerability Map
Review the 4 facility zones in the script output. For each zone:
1. Explain how an intruder could exploit the identified vulnerability during a school day.
2. What physical or procedural control would eliminate the weakness?

---

## Assessment: AP-Style Free Response Prompt

**Prompt:**  
A hospital research laboratory houses medical prototypes and confidential clinical trial records. The entrance uses a card-swipe door lock, but during lunch hours, a researcher often uses a heavy doorstop to keep the door open so colleagues can carry cafeteria trays without swiping badges.

- **Part 1:** Identify the primary physical vulnerability created by this habit and describe one realistic attack scenario.
- **Part 2:** Recommend both a **technical control** and a **policy control** to permanently eliminate this risk.

---

## Teacher Guidance & Answer Key

- **Part 1:** Unmonitored unauthorized entry / bypass of access control. An intruder posing as a visitor, delivery courier, or patient can enter the lab unhindered and copy data onto a flash drive or plant a rogue hardware device.
- **Part 2:**
  - **Technical control:** Install a **door-prop alarm sensor** that sounds an audible alert and notifies security if the door is held open for longer than 30 seconds; install an automatic door closer.
  - **Policy control:** Implement and enforce a **clean-desk and physical security policy** prohibiting door propping, backed by security audits and staff accountability.

---

[⬅ Previous Class 06: Risk Assessment](../class_06_risk_assessment/README.md) | [Next Class 08: Layered Physical Protection ➡](../class_08_physical_protection/README.md)
