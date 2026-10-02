# Class 26: Team Security Assessment — Multi-Domain Audit

[⬅ Back to Course Roadmap](../README.md) | [💻 Team Assessment Tool](team_assessment_tool.py)

> [!NOTE]
> **Mission Briefing:** Real cybersecurity is a team sport! In this capstone integration exercise, student teams take on specialized defender roles to perform a 360-degree security audit of a simulated healthcare organization ("Apex Health") spanning all five units of the AP Cybersecurity curriculum.

---

## Course Alignment & AP Framework

- **Course:** AP Cybersecurity
- **Course Framework Skills:**
  - **Skill 1.A:** Identify multi-domain security vulnerabilities across physical, network, device, and application layers.
  - **Skill 2.A:** Synthesize risks into an executive Risk Register and prioritize remediation actions.
  - **Skill 4.A:** Collaborate effectively in specialized technical roles and justify resource tradeoffs.

---

## Team Roles & Responsibilities

| Role | Domain Focus | Units Covered | Key Investigation Deliverable |
| :--- | :--- | :--- | :--- |
| **Physical Security Analyst** | Facilities, badge access, server rooms, environmental controls | Unit 2 | Floor plan audit, tailgating vulnerabilities, mantrap and badge policy |
| **Network Architect** | Network diagrams, VLANs, Wi-Fi policies, firewall rule logic | Unit 3 | Subnet redesign, guest isolation, firewall ACL corrections |
| **Endpoint Engineer** | Workstation baselines, least privilege, process monitoring | Unit 4 | Local admin removal, BitLocker verification, OS hardening checklist |
| **Data & App Specialist** | Web portals, SQLi/XSS, file permissions, encryption | Unit 5 | Input validation fixes, POSIX permission adjustments, AES encryption |
| **Chief Risk Officer (Lead)** | Executive synthesis, CIA impact scoring, cost tradeoffs | Unit 1 | Master Risk Register and 90-Day Remediation Roadmap |

---

## Hands-on Lab Activity

Run the team briefing:

```powershell
cd class_26_team_security_assessment
python team_assessment_tool.py
```

### Student Team Deliverable
Each team submits a 2-page **Executive Risk Register & Remediation Plan**:
1. Top 5 highest-risk vulnerabilities scored by Likelihood × Impact.
2. Proposed technical and policy remediations.
3. Realistic operational and financial tradeoffs for each recommendation.

---

[⬅ Previous Class 25: Application Events](../class_25_application_data_events/README.md) | [Next Class 27: Multi-Source Investigation ➡](../class_27_multi_source_device_investigation/README.md)
