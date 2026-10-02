# Class 12: Separate Networks by Purpose — VLANs & Subnetting

[⬅ Back to Course Roadmap](../README.md) | [💻 VLAN Matrix Script](vlan_matrix.py)

> [!NOTE]
> **Mission Briefing:** On a flat, unsegmented network, if an attacker compromises a single smart lightbulb or student laptop, they can immediately reach the school grade database and police dispatch servers. **Network Segmentation** divides a large network into isolated zones (VLANs and subnets) so traffic between zones is strictly inspected. In this class, you will design a multi-segment campus network and write a Required Communication Table.

---

## Course Alignment & AP Framework

- **Course:** AP Cybersecurity
- **Unit 3:** Securing Networks
- **CED Topic:** **3.3 Network Segmentation & Purpose-Driven Zones**
- **Course Framework Skills:**
  - **Skill 2.A:** Design segmented network architectures (VLANs, DMZ, internal subnets).
  - **Skill 2.B:** Construct a Required Communication Matrix defining allowed inter-VLAN flows.

### Learning Objectives & Essential Knowledge

| Objective ID | Learning Objective | Essential Knowledge Covered |
| :--- | :--- | :--- |
| **LO 3.3.A** | Design network segments (VLANs and subnets) aligned with organizational roles and device trust levels. | **EK 3.3.A.1:** Segmentation isolates sensitive data and prevents lateral movement. Dedicated zones include DMZ, staff, student/BYOD, server core, and IoT. |
| **LO 3.3.B** | Construct inter-zone traffic rules based on the principle of least privilege. | **EK 3.3.B.1:** Inter-VLAN routing is blocked by default; only explicitly required communication paths and ports are permitted. |

---

## Hands-on Lab Activity

Run the segmentation script:

```powershell
cd class_12_network_segmentation
python vlan_matrix.py
```

### Student Activity: Inter-VLAN Rule Design
Review the 5 VLANs in the script:
1. Why should IoT devices (cameras, thermostats) be blocked from initiating outbound connections to the internet?
2. A biology teacher wants students to connect directly to the classroom lab microscope server. Which two VLANs are involved, and what specific firewall rule should be added?

---

## Assessment: AP-Style Free Response Prompt

**Prompt:**  
A manufacturing company operates industrial assembly robots and administrative office computers on a single unsegmented subnet (`192.168.1.0/24`). An office worker opens a phishing email, and ransomware encrypts the office PCs and spreads across the network to lock the robotic assembly line controllers.

- **Part 1:** Explain how the lack of network segmentation facilitated this catastrophic failure.
- **Part 2:** Propose an architectural redesign separating operational technology (OT) from corporate information technology (IT), and specify the traffic restriction between them.

---

## Teacher Guidance & Answer Key

- **Part 1:** On a flat network, there are no internal firewall boundaries (zero East-West inspection). Once the workstation was compromised, the ransomware scanned and infected the robots across the same broadcast domain unimpeded.
- **Part 2:** Place robots in a dedicated **Industrial / OT VLAN** separated by an internal firewall from the corporate IT VLAN. Enforce an **explicit deny** rule on all corporate-to-OT traffic, allowing only authenticated engineering management consoles over a restricted port (e.g., via a jump box or VPN).

---

[⬅ Previous Class 11: Wireless Protection](../class_11_wireless_protection/README.md) | [Next Class 13: Firewall Rules ➡](../class_13_firewall_rules/README.md)
