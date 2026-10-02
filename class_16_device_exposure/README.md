# Class 16: Assess Device Exposure — Endpoints, Patches & Services

[⬅ Back to Course Roadmap](../README.md) | [💻 Device Audit Script](device_audit.py)

> [!NOTE]
> **Mission Briefing:** Every laptop, desktop, server, and tablet connected to a network is an **endpoint**. If a single endpoint runs outdated software, leaves unnecessary network ports open, or grants users permanent administrator privileges, an attacker can use it as a launching pad to compromise the entire domain. In this class, you will audit device configurations and prioritize security fixes.

---

## Course Alignment & AP Framework

- **Course:** AP Cybersecurity
- **Unit 4:** Securing Devices
- **CED Topic:** **4.1 Device Attack Surface & Vulnerability Assessment**
- **Course Framework Skills:**
  - **Skill 1.A:** Identify endpoint exposures: unpatched operating systems, legacy protocols, unneeded services.
  - **Skill 2.A:** Prioritize vulnerabilities and propose endpoint remediation plans.

### Learning Objectives & Essential Knowledge

| Objective ID | Learning Objective | Essential Knowledge Covered |
| :--- | :--- | :--- |
| **LO 4.1.A** | Audit device inventories and configurations to discover security weaknesses. | **EK 4.1.A.1:** Unnecessary running services, unpatched software (CVEs), and default configurations expand the attack surface. |
| **LO 4.1.B** | Analyze legacy protocols that introduce severe vulnerabilities. | **EK 4.1.B.1:** Legacy protocols (Telnet, SMBv1) lack modern encryption and security features, exposing devices to credential sniffing and automated worm propagation. |

---

## Hands-on Lab Activity

Run the audit tool:

```powershell
cd class_16_device_exposure
python device_audit.py
```

### Student Activity: Prioritizing Fixes
Review `LIBRARY-KIOSK-04` in the script output:
1. Why is automatic login with Local Administrator rights considered an extreme hazard on a public library terminal?
2. Explain the danger of running SMBv1 on a local network.
3. Write an action checklist for the IT department to bring this kiosk to a secure baseline.

---

## Assessment: AP-Style Free Response Prompt

**Prompt:**  
A university department maintains 50 research lab PCs. To make remote support easier, the lab assistant installed an unencrypted VNC remote-control server on all PCs listening on port 5900 with a shared default password of `"admin"`. Operating system updates have been disabled for two years so tests are not interrupted.

- **Part 1:** Identify three distinct vulnerabilities on these workstations and explain how an attacker on the campus Wi-Fi could exploit them.
- **Part 2:** Propose a centralized management control (e.g., Mobile Device Management / Group Policy) to enforce baseline security without disrupting lab research.

---

## Teacher Guidance & Answer Key

- **Part 1:**
  1. Default password `"admin"` on port 5900 allows anyone on the network to take full graphical control.
  2. Unencrypted VNC transmits mouse, keystrokes, and screen captures in plaintext across the local network.
  3. Two years of unpatched OS updates leaves known high-severity remote code execution exploits unmitigated.
- **Part 2:** Deploy centralized **Group Policy Objects (GPO)** or **MDM**:
  - Enforce scheduled automated patch windows during overnight hours.
  - Disable legacy VNC and replace it with secure, encrypted SSH or enterprise remote desktop requiring MFA and individual credentials.

---

[⬅ Previous Class 15: Data Analysis](../sample_1/README.md) | [Next Class 17: Account Controls ➡](../class_17_account_controls/README.md)
