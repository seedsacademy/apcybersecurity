# Class 17: Design Authentication and Account Controls — Least Privilege & RBAC

[⬅ Back to Course Roadmap](../README.md) | [💻 RBAC Designer Script](rbac_designer.py)

> [!NOTE]
> **Mission Briefing:** Why do malware infections spread so rapidly? In many organizations, users are granted "Local Administrator" rights simply because it's convenient for installing software. But when a user with admin rights clicks a malicious link, the malware inherits those exact same admin powers! In this class, you will implement the **Principle of Least Privilege (PoLP)** and design a **Role-Based Access Control (RBAC)** architecture.

---

## Course Alignment & AP Framework

- **Course:** AP Cybersecurity
- **Unit 4:** Securing Devices
- **CED Topic:** **4.2 Account Controls & Access Management**
- **Course Framework Skills:**
  - **Skill 2.A:** Design access control policies following the Principle of Least Privilege.
  - **Skill 2.B:** Formulate Role-Based Access Control (RBAC) matrices and separation-of-duties rules.

### Learning Objectives & Essential Knowledge

| Objective ID | Learning Objective | Essential Knowledge Covered |
| :--- | :--- | :--- |
| **LO 4.2.A** | Implement the Principle of Least Privilege across operating systems and account roles. | **EK 4.2.A.1:** Users and service processes should only receive the minimum permissions necessary to perform authorized duties. |
| **LO 4.2.B** | Construct Role-Based Access Control (RBAC) models and enforce separation of duties. | **EK 4.2.B.1:** RBAC assigns permissions to job roles, not individuals. High-risk administrative duties must be separated from daily user tasks. |

---

## Hands-on Lab Activity

Run the RBAC designer:

```powershell
cd class_17_account_controls
python rbac_designer.py
```

### Student Activity: Account Privilege Design
Review the 3 roles in the script output:
1. Why is it dangerous for a Network Administrator to use their Domain Admin account to browse the web or open daily emails?
2. What is "Separation of Duties", and why does it prevent internal fraud?
3. Propose a new role: "Substitute Teacher". What permissions should they have, and how should their account lifecycle be managed?

---

## Assessment: AP-Style Free Response Prompt

**Prompt:**  
To minimize help-desk calls, a school district's IT department makes all 500 teachers local administrators on their district laptops. A teacher visits an infected educational blog, and a malicious script silently disables the antivirus software, creates a hidden backdoor account, and begins copying school files.

- **Part 1:** Explain how the violation of the Principle of Least Privilege enabled this silent takeover.
- **Part 2:** Propose an account control policy that allows teachers to perform their educational duties while blocking unauthorized software and service alterations.

---

## Teacher Guidance & Answer Key

- **Part 1:** Because the teacher ran the web browser under a Local Administrator token, any code executed by the browser inherited full system-level permissions—allowing it to terminate security services and alter operating system registries without prompting for credentials.
- **Part 2:** Remove local administrator rights; reassign all teachers to **Standard User accounts**. Deploy a centralized self-service application catalog (or endpoint privilege management tool) where pre-approved educational tools can install without granting permanent administrative privileges.

---

[⬅ Previous Class 16: Device Exposure](../class_16_device_exposure/README.md) | [Next Class 18: Harden a Workstation ➡](../class_18_harden_workstation/README.md)
