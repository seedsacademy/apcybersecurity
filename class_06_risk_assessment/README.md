# Class 06: Build a Security Risk Assessment — The CIA Triad & Risk Register

[⬅ Back to Course Roadmap](../README.md) | [📁 Asset Database](assets.json) | [💻 Risk Matrix Script](risk_matrix.py)

> [!NOTE]
> **Mission Briefing:** Security teams cannot protect everything equally with an unlimited budget. To make smart decisions, defenders perform a **Risk Assessment** to inventory high-value assets, analyze the **CIA Triad** (Confidentiality, Integrity, Availability), and calculate:
> $$\text{Risk} = \text{Likelihood} \times \text{Impact}$$
> In this class, you will build and prioritize a formal organizational Risk Register!

---

## Course Alignment & AP Framework

- **Course:** AP Cybersecurity
- **Unit 2:** Securing Spaces
- **CED Topic:** **2.1 Security Risk Assessment & The CIA Triad**
- **Course Framework Skills:**
  - **Skill 1.A:** Identify asset sensitivity and evaluate CIA triad impacts.
  - **Skill 2.A:** Calculate quantitative and qualitative risk scores and propose treatments (Mitigate, Transfer, Accept, Avoid).

### Learning Objectives & Essential Knowledge

| Objective ID | Learning Objective | Essential Knowledge Covered |
| :--- | :--- | :--- |
| **LO 2.1.A** | Categorize organizational assets by their Confidentiality, Integrity, and Availability needs. | **EK 2.1.A.1:** Confidentiality prevents unauthorized disclosure; Integrity ensures data is accurate and untampered; Availability ensures systems are accessible when needed. |
| **LO 2.1.B** | Calculate risk as a function of likelihood and impact and prioritize mitigations. | **EK 2.1.B.1:** Risk = Likelihood × Impact. High-risk assets require prioritized countermeasures. |
| **LO 2.1.C** | Select appropriate risk response strategies (mitigate, transfer, accept, avoid). | **EK 2.1.C.1:** Organizations mitigate risk with controls, transfer risk via insurance, accept low-impact risks, or avoid risky activities altogether. |

---

## Core Concepts: The CIA Triad & Risk Formula

```text
               THE CIA TRIAD
               
           [ Confidentiality ]
                 /     \
                /       \
               /         \
    [ Integrity ] ------- [ Availability ]
```

- **Confidentiality:** Keeping secret information away from unauthorized eyes (e.g., student medical records, passwords).
- **Integrity:** Ensuring information is authentic and has not been altered or forged (e.g., student grades, financial balances).
- **Availability:** Ensuring critical systems are operational and accessible when people need them (e.g., emergency 911 dispatch, cloud classroom portal during exams).

### The 4 Risk Response Strategies
1. **Mitigate:** Apply security controls (firewalls, training, encryption) to lower likelihood or impact.
2. **Transfer:** Shift the financial loss to a third party (cybersecurity insurance, third-party cloud hosting SLAs).
3. **Accept:** Acknowledge the risk when the cost of defending it exceeds the value of the asset.
4. **Avoid:** Eliminate the activity entirely (e.g., deciding not to collect or store student Social Security numbers).

---

## Hands-on Lab Activity

Run the risk calculator:

```powershell
cd class_06_risk_assessment
python risk_matrix.py
```

### Student Activity: The School Risk Register
1. Review the assets in [assets.json](assets.json).
2. Rank the 4 assets from highest risk score to lowest risk score.
3. Propose a new asset (e.g., "District Bus GPS Tracking System") and assign its primary CIA pillar, a realistic threat, likelihood (1–5), impact (1–5), and treatment plan.

---

## Assessment: AP-Style Free Response Prompt

**Prompt:**  
A municipal water treatment facility manages an industrial control system (ICS) that regulates water chlorination levels. The system runs an outdated operating system that cannot be patched without taking the water plant offline for three weeks.

- **Part 1:** Identify which CIA pillar is most critically threatened if an attacker manipulates the chemical sensor data, and justify your answer.
- **Part 2:** Explain the difference between **Risk Mitigation** and **Risk Acceptance** in this scenario. Which strategy is legally and ethically required here?

---

## Teacher Guidance & Answer Key

- **Part 1:** **Integrity** (and Availability). If sensor data is altered, poisonous levels of chlorine could be introduced into the water supply without triggering alarms.
- **Part 2:** Acceptance means acknowledging the danger and doing nothing; mitigation means applying compensating controls (network isolation, air-gapping, manual valve overrides). In critical infrastructure affecting human health and life safety, **Risk Acceptance is unacceptable**—mitigation is legally and ethically mandated.

---

[⬅ Previous Class 05: AI Defense](../class_05_ai_defense/README.md) | [Next Class 07: Physical Weaknesses ➡](../class_07_physical_weaknesses/README.md)
