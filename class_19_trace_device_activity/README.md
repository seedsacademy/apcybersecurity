# Class 19: Trace Device Activity — Process Trees & Incident Hypotheses

[⬅ Back to Course Roadmap](../README.md) | [📁 Log File: os_events.csv](os_events.csv) | [💻 Process Tracer Script](trace_process_activity.py)

> [!NOTE]
> **Mission Briefing:** When a hacker breaks into a computer, they leave digital fingerprints inside the operating system: processes spawned, command-line arguments executed, and services installed for persistence. By inspecting **Process Trees** (which program launched which child program), cyber detectives can reconstruct an attack from an innocent email click all the way to root compromise. In this class, you will trace a real process attack chain!

---

## Course Alignment & AP Framework

- **Course:** AP Cybersecurity
- **Unit 4:** Securing Devices
- **CED Topic:** **4.4 Device Telemetry & Process Tree Analysis**
- **Course Framework Skills:**
  - **Skill 3.A:** Trace process lineage (parent-child relationships) and detect anomalous execution patterns.
  - **Skill 3.B:** Formulate and validate an incident hypothesis supported by system event IDs.

### Learning Objectives & Essential Knowledge

| Objective ID | Learning Objective | Essential Knowledge Covered |
| :--- | :--- | :--- |
| **LO 4.4.A** | Correlate operating system telemetry (process creation, service installation, logons). | **EK 4.4.A.1:** Common Windows Event IDs: 4624 (Successful Logon), 4688 (Process Creation with Command Line), 7045 (New Service Installed). |
| **LO 4.4.B** | Identify abnormal process relationships and persistence mechanisms. | **EK 4.4.B.1:** Productivity applications (Word, Excel) spawning command shells (`cmd.exe`, `powershell.exe`) indicate macro execution or document weaponization. |

---

## Hands-on Lab Activity

Run the process tracer:

```powershell
cd class_19_trace_device_activity
python trace_process_activity.py
```

### Student Activity: Process Lineage Investigation
Review [os_events.csv](os_events.csv) and answer:
1. What was the exact parent process that launched `cmd.exe`? Is that normal behavior for a document reader?
2. What suspicious flags were passed to `powershell.exe`? Why did the attacker use Base64 encoding?
3. How did the attacker establish **persistence** on the computer so their malware restarts automatically when the PC reboots?

---

## Assessment: AP-Style Free Response Prompt

**Prompt:**  
An endpoint detection system flags Event ID 4688 on an accountant's workstation:  
`Parent Process: C:\Program Files\Adobe\Acrobat Reader DC\AcroRd32.exe`  
`Process Created: C:\Windows\System32\powershell.exe -WindowStyle Hidden -ExecutionPolicy Bypass -Command "Invoke-WebRequest ..."`

- **Part 1:** Formulate an incident hypothesis explaining what user action triggered this alert and why this process relationship is an extreme red flag.
- **Part 2:** Propose two immediate containment actions the security analyst must take to prevent the infection from spreading across the network.

---

## Teacher Guidance & Answer Key

- **Part 1:**
  - *Hypothesis:* The user opened a weaponized, malicious PDF document inside Adobe Acrobat that exploited an embedded script or vulnerability to spawn PowerShell silently in the background.
  - *Red flag:* PDF viewers should never launch administrative command shells; `-WindowStyle Hidden` and `-ExecutionPolicy Bypass` are explicit indicators of evasive malicious execution.
- **Part 2:**
  1. **Network Isolation:** Immediately isolate the infected workstation from the network (cutting Wi-Fi/Ethernet or via Endpoint Detection & Response agent quarantine) to block command-and-control communication and lateral movement.
  2. **Process Termination & Credential Revocation:** Kill the malicious PowerShell process, revoke the user's active session tokens, and initiate a password reset.

---

[⬅ Previous Class 18: Workstation Hardening](../class_18_harden_workstation/README.md) | [Unit 5 Start: Class 20: Application Attack Paths ➡](../class_20_application_attacks/README.md)
