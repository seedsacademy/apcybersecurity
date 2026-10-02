# Class 08: Design Layered Physical Protection — Defense in Depth

[⬅ Back to Course Roadmap](../README.md) | [💻 Layered Defense Simulator](defense_in_depth.py)

> [!NOTE]
> **Mission Briefing:** In cybersecurity, no single lock or guard can stop every intruder. Instead, security architects use **Defense in Depth** (also called concentric rings of security). If an intruder slips past the front gate, the lobby receptionist catches them; if they slip past the lobby, the locked server room stops them. In this class, you will design a multi-tiered physical defense strategy and evaluate operational tradeoffs.

---

## Course Alignment & AP Framework

- **Course:** AP Cybersecurity
- **Unit 2:** Securing Spaces
- **CED Topic:** **2.3 Layered Physical Protection & Controls**
- **Course Framework Skills:**
  - **Skill 2.A:** Design layered security architectures using physical controls.
  - **Skill 2.B:** Justify operational tradeoffs (cost, convenience, emergency evacuation safety).

### Learning Objectives & Essential Knowledge

| Objective ID | Learning Objective | Essential Knowledge Covered |
| :--- | :--- | :--- |
| **LO 2.3.A** | Design layered physical security controls following concentric rings of defense. | **EK 2.3.A.1:** Layers progress from outer perimeter (fences, bollards) to building exterior (guards, visitor badges) to interior zones (RFID doors) to secure rooms (mantraps, biometrics). |
| **LO 2.3.B** | Evaluate environmental and physical controls for data centers. | **EK 2.3.B.1:** Controls include HVAC climate management, UPS battery backups, and clean-agent fire suppression (FM-200) instead of water sprinklers. |
| **LO 2.3.C** | Analyze operational tradeoffs and human safety requirements. | **EK 2.3.C.1:** Life safety always takes priority over security (e.g., fail-safe doors that unlock automatically during a fire alarm). |

---

## Core Concepts: Concentric Rings of Protection

```text
               CONCENTRIC RINGS OF PHYSICAL DEFENSE
               
       +---------------------------------------------+
       | Ring 1: Property Perimeter (Fences, Bollards)|
       |   +-------------------------------------+   |
       |   | Ring 2: Building Entry (Guards, ID) |   |
       |   |   +-----------------------------+   |   |
       |   |   | Ring 3: Workspaces (Badges) |   |   |
       |   |   |   +---------------------+   |   |   |
       |   |   |   | Ring 4: Server Room |   |   |   |
       |   |   |   | (Mantrap, Biometrics|   |   |   |
       |   |   |   +---------------------+   |   |   |
       |   |   +-----------------------------+   |   |
       |   +-------------------------------------+   |
       +---------------------------------------------+
```

### Specialized Physical Controls
1. **Mantrap / Security Vestibule:** A small room with two interlocking doors where the second door cannot open until the first door closes and the occupant verifies their identity. Stops tailgating completely!
2. **Vehicle Crash Bollards:** Heavy concrete or steel posts anchored into the ground to prevent vehicles from ramming into building entrances.
3. **Clean-Agent Fire Suppression:** Water sprinklers ruin servers and electronics. Clean agents (like FM-200 or Novec 1230) extinguish fires by removing heat without spraying liquids or leaving chemical residue.

> [!IMPORTANT]
> **Life Safety Always Wins:** During a building fire or earthquake, electronic security doors MUST operate in a **fail-safe** mode (unlocking automatically so people can evacuate safely), never fail-secure (locking people inside).

---

## Hands-on Lab Activity

Run the simulation:

```powershell
cd class_08_physical_protection
python defense_in_depth.py
```

### Student Activity: The Data Center Blueprint
Review the 4 rings of defense in the output:
1. Explain how a **mantrap / security vestibule** mathematically eliminates the risk of tailgating.
2. What happens if a water sprinkler goes off inside a server room compared to clean-agent gaseous suppression?
3. Name one operational tradeoff for each ring (e.g., cost, employee wait times, emergency access delays).

---

## Assessment: AP-Style Free Response Prompt

**Prompt:**  
A financial investment bank is designing a new downtown headquarters. The architects propose replacing all interior badge readers with automated facial recognition turnstiles and locking all fire exit stairwell doors so intruders cannot escape with stolen laptops.

- **Part 1:** Evaluate the physical security benefits and privacy/usability drawbacks of biometric turnstiles.
- **Part 2:** Explain the critical safety and regulatory flaw in locking the fire exit stairwells, and describe the required standard behavior during an emergency.

---

## Teacher Guidance & Answer Key

- **Part 1:**
  - *Benefits:* Prevents badge sharing, tailgating, and lost card replacement costs.
  - *Drawbacks:* High capital cost, potential biometric privacy concerns from staff, and slower throughput during high-volume arrival times.
- **Part 2:**
  - *Safety flaw:* Locking fire exit doors violates fire safety codes and endangers human lives by trapping occupants during a fire or evacuation.
  - *Required behavior:* Emergency exits must always be **fail-safe** (automatically unlocking or opening via emergency crash bars from the inside regardless of power state). Life safety strictly overrides property security.

---

[⬅ Previous Class 07: Physical Weaknesses](../class_07_physical_weaknesses/README.md) | [Next Class 09: Physical Access Events ➡](../class_09_physical_access_events/README.md)
