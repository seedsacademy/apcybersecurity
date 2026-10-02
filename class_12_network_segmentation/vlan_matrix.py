#!/usr/bin/env python3
"""Class 12: Network Segmentation & VLAN Communication Matrix.

Run: python vlan_matrix.py
"""
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SEGMENTS = [
    {"vlan_id": 10, "name": "Public / DMZ", "subnet": "10.0.10.0/24", "purpose": "External-facing services (Web, DNS, Email Gateway)"},
    {"vlan_id": 20, "name": "Staff / Faculty", "subnet": "10.0.20.0/24", "purpose": "Teacher workstations, grading portals, administrative printers"},
    {"vlan_id": 30, "name": "Student Lab & BYOD", "subnet": "10.0.30.0/24", "purpose": "Student laptops, computer science lab workstations"},
    {"vlan_id": 40, "name": "Secure Server Core", "subnet": "10.0.40.0/24", "purpose": "Domain Controller, Student Information System (SIS) DB"},
    {"vlan_id": 50, "name": "IoT & Facilities", "subnet": "10.0.50.0/24", "purpose": "Security cameras, smart HVAC thermostats, door badge controllers"},
]

MATRIX = [
    ("Student (VLAN 30)", "Internet (WAN)", "ALLOWED (Web filtering enforced)"),
    ("Student (VLAN 30)", "Secure Core (VLAN 40)", "BLOCKED (Direct access prohibited)"),
    ("Student (VLAN 30)", "IoT / Facilities (VLAN 50)", "BLOCKED (Isolate HVAC and badge doors)"),
    ("Staff (VLAN 20)", "Secure Core (VLAN 40)", "ALLOWED (Port 443 HTTPS only for grading app)"),
    ("IoT (VLAN 50)", "Internet (WAN)", "BLOCKED (Prevent smart devices calling home to botnets)"),
]


def main():
    print("=" * 70)
    print("  CLASS 12: NETWORK SEGMENTATION & VLAN TRAFFIC CONTROL")
    print("=" * 70)

    print("\n[+] DEFINED NETWORK SEGMENTS (VLANs):\n")
    for s in SEGMENTS:
        print(f"VLAN {s['vlan_id']:<3} | {s['name']:<20} | {s['subnet']:<14} | {s['purpose']}")

    print("\n" + "-" * 70)
    print("INTER-VLAN ACCESS CONTROL POLICY (Required Communication Table):")
    print("-" * 70)
    for src, dst, rule in MATRIX:
        print(f"From: {src:<25} --> To: {dst:<25} | Rule: {rule}")
    print("=" * 70)


if __name__ == "__main__":
    main()
