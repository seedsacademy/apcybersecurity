#!/usr/bin/env python3
"""Class 11: Enterprise Wireless Configuration & Policy Audit.

Run: python wireless_audit.py
"""
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

NETWORKS = [
    {
        "ssid": "District-Staff",
        "security": "WPA3-Enterprise (802.1X / EAP-TLS)",
        "authentication": "Individual school accounts + digital certificates via RADIUS server",
        "client_isolation": "Disabled (Allows printing and screen mirroring to classroom projectors)",
        "vlan": "VLAN 20 (Staff & Administrative Subnet)",
        "verdict": "STRONG: High security; no shared pre-shared key (PSK) to leak.",
    },
    {
        "ssid": "School-Guest",
        "security": "WPA2-PSK (Pre-Shared Key: 'WelcomePanthers2026!')",
        "authentication": "Single shared password for all visitors and students",
        "client_isolation": "DISABLED (CRITICAL FLAW!)",
        "vlan": "VLAN 10 (Same subnet as administrative printers!)",
        "verdict": "CRITICAL RISK: A guest can sniff and attack other guests or access administrative devices!",
    },
]


def main():
    print("=" * 70)
    print("  CLASS 11: ENTERPRISE WIRELESS SECURITY & POLICY AUDIT")
    print("=" * 70)

    for n in NETWORKS:
        print(f"\nSSID: {n['ssid']}")
        print(f"  Security Protocol : {n['security']}")
        print(f"  Authentication    : {n['authentication']}")
        print(f"  Client Isolation  : {n['client_isolation']}")
        print(f"  Assigned VLAN     : {n['vlan']}")
        print(f"  Security Verdict  : {n['verdict']}")
        print("-" * 70)

    print("\nRECOMMENDED GUEST NETWORK REVISIONS:")
    print("1. ENABLE Client Isolation so guest devices cannot communicate with each other.")
    print("2. Move Guest Wi-Fi to a dedicated isolated VLAN with outbound internet-only routing.")
    print("3. Implement a Captive Portal with terms-of-use and time-limited access tokens.")
    print("=" * 70)


if __name__ == "__main__":
    main()
