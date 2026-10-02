# Class 14: Detect Suspicious Network Activity — Scans, Floods & Tunneling

[⬅ Back to Course Roadmap](../README.md) | [💻 Anomaly Detector Script](detect_anomalies.py)

> [!NOTE]
> **Mission Briefing:** Attackers rarely attack blind; they map the network first using **Port Scans**, probe for open doors, and exfiltrate stolen files disguised as innocent DNS queries. In this class, you will analyze network traffic flow records (NetFlow), detect reconnaissance scans, identify DNS tunneling, and separate real threats from benign network spikes.

---

## Course Alignment & AP Framework

- **Course:** AP Cybersecurity
- **Unit 3:** Securing Networks
- **CED Topic:** **3.5 Network Traffic Analysis & Anomaly Detection**
- **Course Framework Skills:**
  - **Skill 3.A:** Detect network reconnaissance (vertical/horizontal port scans) from traffic logs.
  - **Skill 3.B:** Differentiate between genuine attacks and false-positive baseline spikes.

### Learning Objectives & Essential Knowledge

| Objective ID | Learning Objective | Essential Knowledge Covered |
| :--- | :--- | :--- |
| **LO 3.5.A** | Identify indicators of network scanning, denial of service, and covert channels. | **EK 3.5.A.1:** Vertical scans probe many ports on one host; horizontal scans probe one port across many hosts. DNS tunneling encodes exfiltrated data inside DNS queries. |
| **LO 3.5.B** | Evaluate network traffic against established operational baselines. | **EK 3.5.B.1:** High bandwidth usage is not automatically malicious; analysts must verify whether scheduled backups or software updates explain the spike. |

---

## Hands-on Lab Activity

Run the anomaly detector:

```powershell
cd class_14_network_anomalies
python detect_anomalies.py
```

### Student Activity: Log Analysis
1. In the script output, which ports on `10.0.10.5` responded as `OPEN` to the scanner `203.0.113.99`?
2. What makes the queries from `10.0.30.99` look like DNS tunneling rather than ordinary web browsing?
3. Propose one Intrusion Prevention System (IPS) rule to automatically block aggressive port scans.

---

## Assessment: AP-Style Free Response Prompt

**Prompt:**  
During the 2:00 AM maintenance window, an automated network alarm alerts the on-duty analyst of a massive 500% spike in outbound network traffic from the accounting file server to an external IP address.

- **Part 1:** What two hypotheses should the analyst formulate (one malicious and one benign)?
- **Part 2:** What specific telemetry sources or log fields should the analyst inspect to determine which hypothesis is correct?

---

## Teacher Guidance & Answer Key

- **Part 1:**
  - *Malicious hypothesis:* Active data exfiltration (a compromised account or ransomware actor dumping the accounting database to an attacker server).
  - *Benign hypothesis:* Scheduled automated offsite cloud backup or operating system image synchronization during the scheduled maintenance window.
- **Part 2:**
  - Check the **destination IP and domain**: Is it an authorized enterprise cloud backup provider (e.g., AWS S3, Azure) or an unknown suspicious overseas IP?
  - Check **process and user logs**: Was the transfer initiated by the backup service account or by an interactive command shell (`cmd.exe`, `powershell.exe`)?

---

[⬅ Previous Class 13: Firewall Rules](../class_13_firewall_rules/README.md) | [Next Class 15: Python & pandas Analysis ➡](../sample_1/README.md)
