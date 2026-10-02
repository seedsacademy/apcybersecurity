#!/usr/bin/env python3
"""Class 16: Endpoint Device Exposure & Vulnerability Audit.

Run: python device_audit.py
"""
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

DEVICES = [
    {
        "hostname": "LIBRARY-KIOSK-04",
        "os": "Windows 10 (Version 1909 - End of Life)",
        "unnecessary_services": ["Telnet Server (Port 23 unencrypted)", "SMBv1 (Vulnerable to EternalBlue)"],
        "account_privilege": "Autologin with Local Administrator rights",
        "patch_status": "Missing 18 critical security patches",
        "risk_level": "CRITICAL",
    },
    {
        "hostname": "NURSE-STATION-PC",
        "os": "Windows 11 Enterprise (Fully patched)",
        "unnecessary_services": ["None (Hardened baseline)"],
        "account_privilege": "Standard User (Local admin stripped)",
        "patch_status": "Up to date",
        "risk_level": "LOW",
    },
]


def main():
    print("=" * 70)
    print("  CLASS 16: ENDPOINT EXPOSURE & ATTACK SURFACE AUDIT")
    print("=" * 70)

    for d in DEVICES:
        print(f"\nDevice Name       : {d['hostname']}")
        print(f"Operating System  : {d['os']}")
        print(f"Exposed Services  : {', '.join(d['unnecessary_services'])}")
        print(f"User Privilege    : {d['account_privilege']}")
        print(f"Patch Status      : {d['patch_status']}")
        print(f"Evaluated Risk    : [{d['risk_level']}]")
        print("-" * 70)


if __name__ == "__main__":
    main()
