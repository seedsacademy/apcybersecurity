# Class 21: Set Data Policy and File Permissions — POSIX & Data Classification

[⬅ Back to Course Roadmap](../README.md) | [💻 File Permissions Auditor](permissions_auditor.py)

> [!NOTE]
> **Mission Briefing:** In an operating system, every file has an owner, a group, and permission bits that decide: **Who can Read (r), Write (w), or Execute (x)?** If an administrator accidentally gives a sensitive grade file `777` permissions (world-writable), any student or malware on the machine can modify or delete it. In this class, you will audit file permission structures and enforce strict data access policies!

---

## Course Alignment & AP Framework

- **Course:** AP Cybersecurity
- **Unit 5:** Securing Applications and Data
- **CED Topic:** **5.2 Data Classification & File Permissions**
- **Course Framework Skills:**
  - **Skill 2.A:** Calculate and audit file permission modes (octal and symbolic representation).
  - **Skill 2.B:** Formulate data handling policies aligned with sensitivity levels.

### Learning Objectives & Essential Knowledge

| Objective ID | Learning Objective | Essential Knowledge Covered |
| :--- | :--- | :--- |
| **LO 5.2.A** | Calculate and assign file permission bits across Owner, Group, and Others. | **EK 5.2.A.1:** Read (4), Write (2), Execute (1). Octal permissions: 755 (rwxr-xr-x), 644 (rw-r--r--), 600 (rw-------). |
| **LO 5.2.B** | Classify organizational data into tiers (Public, Internal, Confidential, Restricted). | **EK 5.2.B.1:** Confidential and restricted files must never be world-readable (`chmod o-r`) or world-writable (`chmod o-w`). |

---

## Core Concepts: POSIX Permission Bits

```text
               ANATOMY OF A FILE PERMISSION
               
      -   [ r w x ]   [ r - x ]   [ r - - ]
      |     Owner       Group      Others (World)
      |    (User)
   File Type
   (- = file, d = directory)
   
   Values: Read (r) = 4, Write (w) = 2, Execute (x) = 1
   Owner  : 4 + 2 + 1 = 7
   Group  : 4 + 0 + 1 = 5
   Others : 4 + 0 + 0 = 4   ===> Octal Mode: 754
```

---

## Hands-on Lab Activity

Run the auditor:

```powershell
cd class_21_file_permissions
python permissions_auditor.py
```

### Student Activity: Permission Math
1. Calculate the numeric octal mode for a file with permissions `-rw-r-----`.
2. Why is granting `777` (`rwxrwxrwx`) considered the single worst permission setting in cybersecurity?
3. What command would an admin use to remove all write permissions for "others" from `fall_2026.csv`?

---

## Assessment: AP-Style Free Response Prompt

**Prompt:**  
A software developer creates an automated script that stores API access keys and database passwords in a configuration file named `/opt/app/config.json`. The file permissions are set to `-rw-rw-rw-` (mode 666).

- **Part 1:** Identify the security vulnerability created by mode 666 and describe what a non-administrative user on the server can do.
- **Part 2:** Recommend the exact corrected POSIX permission mode and justify your choice using the Principle of Least Privilege.

---

## Teacher Guidance & Answer Key

- **Part 1:** Mode 666 grants Read and Write access to **everyone (Owner, Group, and Others/World)**. Any low-privileged guest, student, or unprivileged web process running on the host can read the plain API keys and database passwords, or overwrite/delete the configuration file.
- **Part 2:** Set the permission to **mode 600 (`-rw-------`)** or **mode 400 (`-r--------`)** with ownership assigned exclusively to the dedicated service account that runs the application. Only that service account can read the secrets; all other accounts and users are strictly blocked.

---

[⬅ Previous Class 20: Application Attacks](../class_20_application_attacks/README.md) | [Next Class 22: Protect Stored Data ➡](../class_22_protect_stored_data/README.md)
