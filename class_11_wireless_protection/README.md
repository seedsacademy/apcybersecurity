# Class 11: Plan Network Policy and Wireless Protection — Enterprise Wi-Fi & Isolation

[⬅ Back to Course Roadmap](../README.md) | [💻 Wireless Audit Script](wireless_audit.py)

> [!NOTE]
> **Mission Briefing:** Setting up Wi-Fi at home with a simple pre-shared password is easy. But on an enterprise campus with 2,000 students, staff, and visitors, sharing a single password leads to instant credential leaks. In this class, you will evaluate **WPA3-Enterprise (802.1X)**, configure **Client Isolation**, debunk wireless security myths (MAC filtering, hidden SSIDs), and design a robust guest network policy.

---

## Course Alignment & AP Framework

- **Course:** AP Cybersecurity
- **Unit 3:** Securing Networks
- **CED Topic:** **3.2 Wireless Security & Network Policy**
- **Course Framework Skills:**
  - **Skill 2.A:** Select appropriate wireless encryption standards and authentication modes.
  - **Skill 2.B:** Formulate wireless access policies and guest isolation rules.

### Learning Objectives & Essential Knowledge

| Objective ID | Learning Objective | Essential Knowledge Covered |
| :--- | :--- | :--- |
| **LO 3.2.A** | Compare wireless encryption and authentication protocols (WPA2 vs. WPA3, Personal vs. Enterprise). | **EK 3.2.A.1:** WPA3 uses Simultaneous Authentication of Equals (SAE) to eliminate offline dictionary attacks. Enterprise mode (802.1X) uses individual user credentials authenticated against a RADIUS server. |
| **LO 3.2.B** | Evaluate network controls for guest and BYOD wireless environments. | **EK 3.2.B.1:** Client Isolation prevents connected wireless devices from communicating with one another. Security through obscurity (hidden SSIDs, MAC filtering) does not stop attackers. |

---

## Core Concepts: Personal vs. Enterprise Wireless

### 1. WPA Personal vs. WPA Enterprise
- **WPA Personal (PSK):** Every device uses the same shared password. If one student shares the password on social media, the entire network is exposed!
- **WPA Enterprise (802.1X):** Every person logs in with their own unique school username and password (or digital certificate). A central **RADIUS server** checks credentials. When an employee leaves, their account is disabled immediately without changing everyone else's Wi-Fi!

### 2. Client Isolation
By default, devices on the same Wi-Fi network can ping and connect to each other. On a guest or public Wi-Fi network, **Client Isolation** must be turned on so no visitor can scan, hack, or spread malware to other guests' laptops!

### 3. Debunking Wi-Fi Security Myths
- **Myth 1: "Hiding your SSID makes you invisible."**  
  *Reality:* Attackers with basic packet sniffers see the network name the moment any legitimate client connects.
- **Myth 2: "MAC address filtering is unbreakable."**  
  *Reality:* MAC addresses travel in plain unencrypted text over the radio. An attacker can sniff an authorized MAC address and spoof it in 10 seconds.

---

## Hands-on Lab Activity

Run the audit tool:

```powershell
cd class_11_wireless_protection
python wireless_audit.py
```

### Student Activity: Policy Review
Review the `School-Guest` network profile in the script:
1. Explain how a visitor with malicious intent could compromise an administrative network printer if Client Isolation is disabled.
2. Outline 3 specific configuration changes needed to make the guest network secure.

---

## Assessment: AP-Style Free Response Prompt

**Prompt:**  
A high school allows students to bring their own personal laptops (BYOD) and connect to a single wireless network named `"School_Open"` that uses WPA2-Personal with the password written on classroom whiteboards. A student uses network scanning software on their laptop and discovers unencrypted administrative file shares and grade entry portals.

- **Part 1:** Identify two critical architectural vulnerabilities in this wireless setup.
- **Part 2:** Propose an enterprise-grade redesign specifying encryption standards, network segmentation, and client isolation rules.

---

## Teacher Guidance & Answer Key

- **Part 1:**
  1. Use of a shared pre-shared key (PSK) written publicly on whiteboards, allowing anyone within radio range to join or capture handshakes.
  2. Lack of network segmentation and client isolation: personal student devices sit on the same broadcast domain as administrative school assets.
- **Part 2:**
  - Transition staff and students to **WPA3-Enterprise (802.1X)** with individual credentials authenticated via RADIUS.
  - Separate BYOD and guest traffic onto a dedicated, isolated VLAN with **Client Isolation enabled** and firewall rules blocking all traffic to internal administrative servers.

---

[⬅ Previous Class 10: Network Attack Paths](../class_10_network_attack_paths/README.md) | [Next Class 12: Network Segmentation ➡](../class_12_network_segmentation/README.md)
