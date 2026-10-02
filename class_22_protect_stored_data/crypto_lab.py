#!/usr/bin/env python3
"""Class 22: Cryptographic Hashing vs. Symmetric Encryption Lab.

Run: python crypto_lab.py
"""
import hashlib
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def demo_hashing():
    print("--- 1. CRYPTOGRAPHIC HASHING (ONE-WAY INTEGRITY) ---")
    message = "Lincoln High AP Exam Grade: A+"
    hash1 = hashlib.sha256(message.encode()).hexdigest()
    print(f"Original Text : '{message}'")
    print(f"SHA-256 Hash  : {hash1}")

    # Avalanche effect: Change 1 single character
    tampered = "Lincoln High AP Exam Grade: A-"
    hash2 = hashlib.sha256(tampered.encode()).hexdigest()
    print(f"\nTampered Text : '{tampered}'")
    print(f"SHA-256 Hash  : {hash2}")
    print(f"[!] The Avalanche Effect: Notice how a 1-character difference completely changes the entire hash!")

    # Password salting demo
    password = "CorrectHorse123!"
    salt = os.urandom(8).hex()
    salted_hash = hashlib.sha256((salt + password).encode()).hexdigest()
    print(f"\nSalted Password Storage Demo:")
    print(f"  Password    : {password}")
    print(f"  Random Salt : {salt}")
    print(f"  Stored Hash : {salted_hash}")
    print("  Benefit: Defeats Rainbow Tables and pre-computed dictionary attack lists!")


def demo_encryption():
    print("\n--- 2. ENCRYPTION (TWO-WAY CONFIDENTIALITY) ---")
    print("Unlike a hash, encrypted ciphertext CAN be decrypted if you possess the secret key.")
    print("Symmetric Encryption (AES): Same secret key used to lock AND unlock.")
    print("Plaintext  --> [AES Encrypt with Secret Key] --> Ciphertext")
    print("Ciphertext --> [AES Decrypt with Secret Key] --> Plaintext")


def main():
    print("=" * 70)
    print("  CLASS 22: DATA PROTECTION - HASHING VS. ENCRYPTION")
    print("=" * 70)
    demo_hashing()
    demo_encryption()
    print("=" * 70)


if __name__ == "__main__":
    main()
