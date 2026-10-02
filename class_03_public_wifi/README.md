# Class 03: Make Decisions on Public Wi-Fi — Rogue APs & Encryption

[⬅ Back to Course Roadmap](../README.md) | [💻 Traffic Sniffer Simulator](traffic_sim.py)

> [!NOTE]
> **Mission Briefing:** Free public Wi-Fi is everywhere—airports, hotels, libraries, and coffee shops. But how do you know the network named `"Starbucks_Guest_Free"` is actually owned by the coffee shop? In this class, you will investigate wireless risks like **packet sniffing**, **Evil Twin hotspots**, and **Man-in-the-Middle (MitM)** attacks, and build a safe connection checklist.

---

## Course Alignment & AP Framework

- **Course:** AP Cybersecurity
- **Unit 1:** Introduction to Security
- **CED Topic:** **1.3 Public Wi-Fi and Wireless Risks**
- **Course Framework Skills:**
  - **Skill 1.C:** Explain wireless threats (eavesdropping, rogue access points, evil twin attacks).
  - **Skill 2.B:** Propose technical mitigations for mobile and remote access (VPN, HTTPS, disabling auto-connect).

### Learning Objectives & Essential Knowledge

| Objective ID | Learning Objective | Essential Knowledge Covered |
| :--- | :--- | :--- |
| **LO 1.3.A** | Explain how adversaries eavesdrop or intercept traffic on unencrypted and open wireless networks. | **EK 1.3.A.1:** Open Wi-Fi transmits radio frames without link-layer encryption, allowing anyone nearby to capture packets with a wireless sniffer. |
| **LO 1.3.B** | Analyze rogue access points (Evil Twins) and Man-in-the-Middle attacks. | **EK 1.3.B.1:** An Evil Twin broadcasts an identical SSID with a stronger signal to trick devices into connecting, intercepting all traffic. |
| **LO 1.3.C** | Justify defenses for remote and public network access. | **EK 1.3.C.1:** Virtual Private Networks (VPNs) create an encrypted tunnel for all device traffic; HTTPS secures application-layer data end-to-end. |

---

## Core Concepts: Wireless Dangers & Defenses

### 1. Packet Sniffing (Eavesdropping)
On an unencrypted (open) Wi-Fi network, radio signals fly through the air in all directions. Anyone with a $20 Wi-Fi adapter running software like Wireshark can capture every unencrypted frame transmitted by other users.

### 2. The "Evil Twin" Hotspot
An attacker sets up a portable Wi-Fi router broadcasting the exact same network name (SSID) as a legitimate business (e.g. `Airport_Free_WiFi`). Devices configured to "Auto-Connect" will connect to the attacker's router if its signal is slightly stronger. The attacker now controls the router and can view or redirect all web requests!

```text
       EVIL TWIN / MAN-IN-THE-MIDDLE ATTACK
       
  [ Student Laptop ] 
         |
         v (Wi-Fi)
  [ Hacker's Rogue Hotspot ] ---> Intercepts passwords, injects fake login pages
         |
         v (Internet)
  [ Real Website ]
```

### 3. Layers of Defense

| Defense | What It Protects | What It Does NOT Protect |
| :--- | :--- | :--- |
| **HTTPS (TLS)** | Encrypts data between your browser and the website (passwords, messages). | Does not hide the website domain name (SNI/DNS) or IP address from the Wi-Fi operator. |
| **VPN (Virtual Private Network)** | Encrypts **100% of network traffic** from your device to the VPN server, hiding everything from the local Wi-Fi provider. | Does not protect you if you voluntarily type your password into a phishing site. |
| **Cellular Hotspot** | Bypasses local Wi-Fi entirely; uses encrypted cellular carrier towers. | Consumes mobile data limits. |

---

## Hands-on Lab: Sniffing Simulation

Run the simulation script to compare what an attacker sees across different protocols:

```powershell
cd class_03_public_wifi
python traffic_sim.py
```

### Student Activity: The Traveler's Wi-Fi Connection Checklist
Imagine you are traveling with a school team to a national competition. Design a **5-step safety checklist** that every student must follow before connecting a school laptop to hotel Wi-Fi:
1. Turn off **"Auto-Connect to Open Networks"** in system settings.
2. Confirm the exact Wi-Fi SSID and password with the front desk (don't trust similar-sounding open names).
3. Verify that all browser connections show the padlock icon (**HTTPS**).
4. Connect to the school-approved **VPN tunnel** before accessing email or grades.
5. Avoid entering payment info or sensitive passwords over unverified networks.

---

## Assessment: AP-Style Free Response Prompt

**Scenario:**  
While waiting at an airport gate, Elena connects her laptop to an open network called `"Airport_Complimentary_WiFi"`. She logs into her school portal to submit a paper. Later that evening, an unauthorized login to her school cloud account originates from an IP address in another country.

- **Question 1:** Explain how an attacker at the airport could have obtained Elena's credentials even though she didn't open any emails or click on any suspicious links.
- **Question 2:** Propose two separate technical safeguards that Elena could have used to prevent this credential compromise.

---

## Teacher Guidance & Answer Key

- **Question 1:** The attacker operated an **Evil Twin (Rogue AP)** with a captive portal or performed a **Man-in-the-Middle (MitM) SSL stripping / DNS spoofing attack**, intercepting Elena's unencrypted HTTP traffic or tricking her browser into accepting a fake certificate.
- **Question 2:**
  1. Connecting through a trusted, encrypted **Virtual Private Network (VPN)**.
  2. Enforcing **Multi-Factor Authentication (MFA)** on the school portal, preventing account takeover even if the password was intercepted.

---

[⬅ Previous Class 02: Suspicious Logins](../class_02_suspicious_logins/README.md) | [Next Class 04: AI-Assisted Deception ➡](../class_04_ai_deception/README.md)
