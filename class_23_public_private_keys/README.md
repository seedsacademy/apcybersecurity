# Class 23: Use Public and Private Keys — Asymmetric Cryptography & PKI

[⬅ Back to Course Roadmap](../README.md) | [💻 PKI Simulator Script](pki_simulator.py)

> [!NOTE]
> **Mission Briefing:** How can two people on opposite sides of the world who have never met send secret messages across the public internet without sharing a secret password first? The answer is **Asymmetric Cryptography** (Public-Key Cryptography)! By using a mathematically paired **Public Key** (which you share with the world) and **Private Key** (which you guard with your life), the modern internet makes secure online banking, HTTPS browsing, and **Digital Signatures** possible!

---

## Course Alignment & AP Framework

- **Course:** AP Cybersecurity
- **Unit 5:** Securing Applications and Data
- **CED Topic:** **5.4 Asymmetric Cryptography & Digital Signatures**
- **Course Framework Skills:**
  - **Skill 1.B:** Differentiate between symmetric and asymmetric cryptographic algorithms.
  - **Skill 2.A:** Explain how Public Key Infrastructure (PKI) guarantees confidentiality, authenticity, and non-repudiation.

### Learning Objectives & Essential Knowledge

| Objective ID | Learning Objective | Essential Knowledge Covered |
| :--- | :--- | :--- |
| **LO 5.4.A** | Explain how public and private key pairs enable secure communication and digital signatures. | **EK 5.4.A.1:** Public keys encrypt data; corresponding private keys decrypt it. Senders sign hashes with private keys; recipients verify signatures with public keys. |
| **LO 5.4.B** | Describe the role of Certificate Authorities (CAs) in establishing trust. | **EK 5.4.B.1:** CAs digitally sign public key certificates to verify that a domain name (e.g. google.com) genuinely belongs to the verified entity. |

---

## The Golden Rules of Asymmetric Keys

```text
               THE TWO MODES OF ASYMMETRIC CRYPTO
               
  1. For SECRECY (Confidentiality):
     Encrypt with RECIPIENT'S PUBLIC KEY  ===> Decrypt with RECIPIENT'S PRIVATE KEY
     
  2. For AUTHENTICITY (Digital Signature):
     Sign with SENDER'S PRIVATE KEY       ===> Verify with SENDER'S PUBLIC KEY
```

- **Non-Repudiation:** Because only the sender possesses their private key, they cannot later deny authoring a signed message.

---

## Hands-on Lab Activity

Run the PKI simulator:

```powershell
cd class_23_public_private_keys
python pki_simulator.py
```

### Student Activity: Cryptographic Key Exchange
1. If Taylor wants to send an encrypted file to Jordan, which key does Taylor use to encrypt? Which key does Jordan use to decrypt?
2. If Jordan wants to prove that an email genuinely came from them, which key does Jordan use to create the digital signature?
3. What catastrophic failure occurs if someone steals a user's private key?

---

## Assessment: AP-Style Free Response Prompt

**Prompt:**  
A municipal voting commission announces a system where citizens can submit ballots online. The system encrypts each ballot using the Voting Commission's Public Key and attaches a Digital Signature created with the voter's Private Key.

- **Part 1:** Explain how encrypting the ballot with the Commission's Public Key protects voter privacy.
- **Part 2:** Explain how the voter's Digital Signature guarantees ballot authenticity and non-repudiation while preventing election fraud.

---

## Teacher Guidance & Answer Key

- **Part 1:** Encrypting with the Commission's Public Key ensures confidentiality: only the election commission (the sole possessor of the private decryption key) can read the ballot. No eavesdropper or intermediate ISP can see how the citizen voted.
- **Part 2:** Signing with the voter's private key provides authenticity and integrity: any alteration of the ballot invalidates the signature, and only a registered voter holding that private key could generate the valid signature, ensuring the voter cannot claim an imposter cast the vote (non-repudiation).

---

[⬅ Previous Class 22: Protect Stored Data](../class_22_protect_stored_data/README.md) | [Next Class 24: Application Defenses ➡](../class_24_application_defenses/README.md)
