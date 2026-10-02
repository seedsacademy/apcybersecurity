# Class 18: Harden a Workstation — Baselines, BitLocker & Disabling Services

[⬅ Back to Course Roadmap](../README.md) | [💻 Hardening Checklist Script](hardening_checklist.py)

> [!NOTE]
> **Mission Briefing:** Default operating system installations are designed for ease of use, not security. They ship with unnecessary network services turned on, auto-run enabled for thumb drives, and unencrypted drives. **System Hardening** is the systematic process of closing open doors, turning on encryption, and configuring strict security policies. In this class, you will harden a workstation against the CIS Security Benchmarks!

---

## Course Alignment & AP Framework

- **Course:** AP Cybersecurity
- **Unit 4:** Securing Devices
- **CED Topic:** **4.3 Workstation Hardening & Configuration Baselines**
- **Course Framework Skills:**
  - **Skill 2.A:** Apply configuration baselines to harden operating systems.
  - **Skill 2.B:** Verify hardening controls and evaluate operational tradeoffs.

### Learning Objectives & Essential Knowledge

| Objective ID | Learning Objective | Essential Knowledge Covered |
| :--- | :--- | :--- |
| **LO 4.3.A** | Apply security baselines to reduce host attack surfaces. | **EK 4.3.A.1:** Hardening includes disabling unneeded ports and services, configuring host firewalls, disabling autorun, and enabling screen locks. |
| **LO 4.3.B** | Evaluate full disk encryption (FDE) and Trusted Platform Modules (TPM). | **EK 4.3.B.1:** Full-disk encryption (BitLocker, FileVault) protects data-at-rest against offline extraction from lost or stolen physical drives. |

---

## Hands-on Lab Activity

Run the hardening audit:

```powershell
cd class_18_harden_workstation
python hardening_checklist.py
```

### Student Activity: Hardening Analysis
Review the 5 hardening controls in the output:
1. Explain how **Full Disk Encryption (BitLocker)** protects data if a thief physically removes the SSD from a laptop and plugs it into another computer.
2. Why is disabling **USB Autorun** a vital defense against physical baiting attacks (Class 01)?
3. Name one operational tradeoff when IT blocks USB flash drives across a school campus.

---

## Assessment: AP-Style Free Response Prompt

**Prompt:**  
A district guidance counselor accidentally leaves a school laptop in a rideshare vehicle. The laptop's hard drive was unencrypted and had no screen timeout lock.

- **Part 1:** Identify the confidentiality risk to student privacy and explain how a person finding the laptop can access the files without knowing the counselor's Windows login password.
- **Part 2:** Explain how enabling **Full Disk Encryption (FDE)** and a **TPM-backed boot PIN** neutralizes this physical threat.

---

## Teacher Guidance & Answer Key

- **Part 1:** Without encryption, an attacker can boot the laptop from a portable Linux USB stick or remove the internal drive and mount it on another machine, reading all unencrypted documents and student files while bypassing the Windows login screen entirely.
- **Part 2:** Full-disk encryption scrambles the entire drive using AES-256. Without the cryptographic key held by the TPM chip and unlocked by the user's PIN/password, the physical drive appears as random unreadable noise (ciphertext).

---

[⬅ Previous Class 17: Account Controls](../class_17_account_controls/README.md) | [Next Class 19: Trace Device Activity ➡](../class_19_trace_device_activity/README.md)
