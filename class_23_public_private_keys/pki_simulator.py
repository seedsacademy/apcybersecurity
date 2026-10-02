#!/usr/bin/env python3
"""Class 23: Asymmetric Cryptography & Digital Signature Simulator.

Run: python pki_simulator.py
"""
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def main():
    print("=" * 70)
    print("  CLASS 23: ASYMMETRIC ENCRYPTION & DIGITAL SIGNATURES (PKI)")
    print("=" * 70)

    print("\n--- 1. CONFIDENTIALITY: ASYMMETRIC ENCRYPTION ---")
    print("Scenario: Alice wants to send a secret message to Bob.")
    print("  Step 1: Alice gets Bob's PUBLIC KEY (shared openly with the world).")
    print("  Step 2: Alice encrypts message: 'Meet me at the robotics lab.'")
    print("  Step 3: Ciphertext sent across public internet: '8f92b4c10a...'")
    print("  Step 4: ONLY Bob can decrypt this message using his secret PRIVATE KEY!")
    print("  [!] Even Alice cannot decrypt the ciphertext once it is encrypted!")

    print("\n--- 2. AUTHENTICITY & NON-REPUDIATION: DIGITAL SIGNATURES ---")
    print("Scenario: Principal Martinez publishes official school closing notice.")
    print("  Step 1: Principal creates document hash and encrypts it with HER PRIVATE KEY.")
    print("  Step 2: This encrypted hash is the DIGITAL SIGNATURE.")
    print("  Step 3: Any student or parent decrypts the signature using HER PUBLIC KEY.")
    print("  Result: Proves 100% that:")
    print("    1. The notice genuinely came from the Principal (Authenticity).")
    print("    2. Not a single word of the notice was altered (Integrity).")
    print("    3. The Principal cannot claim someone else wrote it (Non-repudiation).")
    print("=" * 70)


if __name__ == "__main__":
    main()
