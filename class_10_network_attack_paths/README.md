# Class 10: Read a Network and Identify Attack Paths — Topology & Ports

[⬅ Back to Course Roadmap](../README.md) | [💻 Network Mapper Script](network_mapper.py)

> [!NOTE]
> **Mission Briefing:** Before an attacker hacks a system or a defender builds a firewall, both must understand the **Network Map**. In this class, you will learn to read network topology diagrams, identify IP addressing schemes (public vs. private RFC 1918), inspect ports and protocols (TCP vs. UDP), and trace how an attacker moves laterally through a network to reach high-value targets.

---

## Course Alignment & AP Framework

- **Course:** AP Cybersecurity
- **Unit 3:** Securing Networks
- **CED Topic:** **3.1 Network Fundamentals & Attack Paths**
- **Course Framework Skills:**
  - **Skill 1.B:** Read network diagrams containing hosts, routers, switches, and firewalls.
  - **Skill 3.A:** Trace attack paths and identify unauthorized network entry points.

### Learning Objectives & Essential Knowledge

| Objective ID | Learning Objective | Essential Knowledge Covered |
| :--- | :--- | :--- |
| **LO 3.1.A** | Read and label network components: IP addresses, subnets, ports, protocols, and services. | **EK 3.1.A.1:** Public IPs route across the internet; private IPs (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) are internal. Common ports: HTTP (80), HTTPS (443), SSH (22), DNS (53), RDP (3389). |
| **LO 3.1.B** | Identify potential attack paths from public external zones to internal private assets. | **EK 3.1.B.1:** Adversaries enter through exposed perimeter services and pivot laterally to reach internal databases. |

---

## Core Concepts: Network Addressing & Common Ports

### 1. Public vs. Private IP Addresses
- **Public IP:** Globally routable on the public internet (assigned by ISP).
- **Private IP (RFC 1918):** Used inside homes, schools, and offices; cannot route directly to the internet without Network Address Translation (NAT):
  - `10.0.0.0` – `10.255.255.255`
  - `172.16.0.0` – `172.31.255.255`
  - `192.168.0.0` – `192.168.255.255`

### 2. Common Ports & Protocols
| Port | Protocol | Common Service | Risk if Exposed to Internet |
| :--- | :--- | :--- | :--- |
| **22** | TCP | SSH (Secure Shell) | Brute-force remote command execution. |
| **53** | UDP/TCP | DNS (Domain Name System) | DNS amplification DDoS, DNS poisoning. |
| **80** | TCP | HTTP (Unencrypted Web) | Eavesdropping, credential sniffing. |
| **443** | TCP | HTTPS (Encrypted Web) | Standard web traffic; vulnerable to web app exploits. |
| **3389** | TCP | RDP (Remote Desktop) | Ransomware deployment, brute force. |

---

## Hands-on Lab Activity

Run the topology mapper:

```powershell
cd class_10_network_attack_paths
python network_mapper.py
```

### Student Activity: Diagram Annotation
1. Label the boundary between the public WAN and the internal LAN.
2. Trace the attack path shown in the script: why is exposing port 3306 (MySQL Database) directly to the web server a major risk?
3. Propose one network control that would stop lateral movement between the DMZ web server and the internal database.

---

## Assessment: AP-Style Free Response Prompt

**Prompt:**  
A regional hospital maintains an internal database at IP `10.0.4.15` storing patient medical charts. An external web portal at IP `203.0.113.80` allows patients to book appointments. The hospital's router was mistakenly configured to forward port 3389 (RDP) from the public internet directly to the internal medical database server.

- **Part 1:** Explain why exposing port 3389 on a database server to the public internet represents a critical vulnerability.
- **Part 2:** Trace the steps an external attacker could take to exploit this misconfiguration, compromise patient privacy, and deploy ransomware.

---

## Teacher Guidance & Answer Key

- **Part 1:** Port 3389 runs Microsoft Remote Desktop Protocol (RDP), giving anyone with valid credentials (or an unpatched RDP exploit like BlueKeep) full graphical administrative control of the server over the internet.
- **Part 2:**
  1. The attacker port scans the hospital's public IP range and discovers port 3389 open.
  2. The attacker uses password spraying or credential stuffing against administrator accounts to gain RDP access.
  3. Once logged in, the attacker dumps patient database records (Confidentiality breach) and executes ransomware to encrypt the system (Availability breach).

---

[⬅ Previous Class 09: Physical Access](../class_09_physical_access_events/README.md) | [Next Class 11: Wireless Protection ➡](../class_11_wireless_protection/README.md)
