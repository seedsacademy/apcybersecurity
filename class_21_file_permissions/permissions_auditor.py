#!/usr/bin/env python3
"""Class 21: File Permissions & Data Classification Auditor.

Run: python permissions_auditor.py
"""
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FILES = [
    {
        "file": "/etc/shadow (System password hashes)",
        "owner": "root", "group": "shadow",
        "current_perm": "-rw-r--r-- (644)",
        "flaw": "CRITICAL FLAW: World-readable! Any standard student or guest account can copy and crack password hashes.",
        "secure_perm": "-rw-r----- (640) or -r-------- (400)",
    },
    {
        "file": "/var/www/html/grades/fall_2026.csv",
        "owner": "registrar", "group": "faculty",
        "current_perm": "-rwxrwxrwx (777)",
        "flaw": "CRITICAL FLAW: World-writable and executable! Anyone can view, alter, or delete student grades.",
        "secure_perm": "-rw-rw---- (660)",
    },
    {
        "file": "/usr/local/bin/python3",
        "owner": "root", "group": "root",
        "current_perm": "-rwxr-xr-x (755)",
        "flaw": "None. Normal standard executable: owner can modify, everyone can execute.",
        "secure_perm": "-rwxr-xr-x (755)",
    },
]


def main():
    print("=" * 70)
    print("  CLASS 21: POSIX FILE PERMISSION & DATA CLASSIFICATION AUDITOR")
    print("=" * 70)

    for f in FILES:
        print(f"\nTarget File        : {f['file']}")
        print(f"Ownership          : Owner={f['owner']}, Group={f['group']}")
        print(f"Current Permission : {f['current_perm']}")
        print(f"Vulnerability Audit: [!] {f['flaw']}")
        print(f"Remediation (chmod): --> Set to {f['secure_perm']}")
        print("-" * 70)


if __name__ == "__main__":
    main()
