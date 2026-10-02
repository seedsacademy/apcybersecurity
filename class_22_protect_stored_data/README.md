# Class 22: Protect Stored Data — Hashing vs. Encryption

[⬅ Back to Course Roadmap](../README.md) | [💻 Cryptography Lab Script](crypto_lab.py)

> [!NOTE]
> **Mission Briefing:** Students often confuse **Hashing** and **Encryption**, but they solve completely different cybersecurity problems! Hashing is a **one-way fingerprint** used to verify that data has not been modified (Integrity). Encryption is a **reversible scramble** using a secret key used to keep data hidden from unauthorized eyes (Confidentiality). In this class, you will explore both and see the "Avalanche Effect" in action!

---

## Course Alignment & AP Framework

- **Course:** AP Cybersecurity
- **Unit 5:** Securing Applications and Data
- **CED Topic:** **5.3 Protecting Data at Rest: Hashing & Symmetric Encryption**
- **Course Framework Skills:**
  - **Skill 1.B:** Differentiate between cryptographic hashing and encryption.
  - **Skill 2.A:** Select appropriate cryptographic tools to protect confidentiality and integrity.

### Learning Objectives & Essential Knowledge

| Objective ID | Learning Objective | Essential Knowledge Covered |
| :--- | :--- | :--- |
| **LO 5.3.A** | Compare cryptographic hash functions (SHA-256) and symmetric encryption (AES). | **EK 5.3.A.1:** Hashing is deterministic, fixed-length, and non-reversible (one-way). Encryption is two-way and reversible with a cryptographic key. |
| **LO 5.3.B** | Explain the necessity of password salting. | **EK 5.3.B.1:** Adding unique random salts to passwords prior to hashing prevents attackers from using precomputed rainbow tables or finding identical passwords across users. |

---

## Core Concepts: Hashing vs. Encryption

| Feature | Cryptographic Hashing | Symmetric Encryption |
| :--- | :--- | :--- |
| **Primary Goal** | **Integrity** (detect tampering) | **Confidentiality** (hide data) |
| **Reversibility** | **One-way only** (cannot be decrypted) | **Two-way** (can be decrypted with key) |
| **Input / Output** | Any length input $\rightarrow$ **Fixed length** output (e.g. 256 bits) | Output length matches input size |
| **Key Required?** | No key needed (deterministic mathematical digest) | Secret cryptographic key required |
| **Common Uses** | Password storage, file download checksums, digital forensics | Hard drive encryption (BitLocker), database column encryption |

---

## Hands-on Lab Activity

Run the crypto lab:

```powershell
cd class_22_protect_stored_data
python crypto_lab.py
```

### Student Activity: Cryptographic Principles
1. What happened to the SHA-256 hash when we changed a single letter from `A+` to `A-`? What is this property called?
2. Why should web applications never store user passwords in plain text or reversible encryption?
3. What is a **cryptographic salt**, and why does it defeat precomputed "rainbow tables"?

---

## Assessment: AP-Style Free Response Prompt

**Prompt:**  
A software developer builds a hospital patient intake app. To store user passwords, the developer encrypts them using AES-256 with the secret key hardcoded into the Python source code.

- **Part 1:** Explain why storing passwords using reversible encryption (even AES-256) is a severe security design flaw compared to salted cryptographic hashing.
- **Part 2:** Explain the additional risk created by hardcoding the cryptographic key inside the application source code.

---

## Teacher Guidance & Answer Key

- **Part 1:** Encryption is reversible. If an attacker breaches the application server or obtains the key, they can decrypt and expose every patient's plaintext password. Passwords must be stored using a **one-way salted hash function (e.g., Argon2, bcrypt, or salted PBKDF2/SHA-256)** so they cannot be mathematically reversed.
- **Part 2:** Hardcoded keys are static and exposed to anyone who reads the source code (developers, contractors, or attackers using decompilation/repository leaks). Once leaked, all past and future encrypted records are instantly compromised with zero key rotation capability.

---

[⬅ Previous Class 21: File Permissions](../class_21_file_permissions/README.md) | [Next Class 23: Public & Private Keys ➡](../class_23_public_private_keys/README.md)
