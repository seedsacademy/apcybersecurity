#!/usr/bin/env python3
"""Class 07: Physical Security & Floor Plan Audit Tool.

Run: python floorplan_audit.py
"""
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ZONES = [
    {
        "zone": "Main Lobby & Reception",
        "controls": "Single receptionist, badge turnstiles",
        "vulnerability": "Tailgating: Visitors slip in behind authorized staff holding the door open during the morning rush.",
        "risk_level": "HIGH",
        "recommended_fix": "Install optical turnstiles that sound an alert on double-entry without a badge swipe.",
    },
    {
        "zone": "Cafeteria Delivery Loading Dock",
        "controls": "Roll-up garage door, delivery clipboard",
        "vulnerability": "Unmonitored Entry: Door frequently propped open with a wooden wedge for ventilation by kitchen staff.",
        "risk_level": "CRITICAL",
        "recommended_fix": "Install door-prop alarm sensors that alert campus security after 60 seconds of continuous opening.",
    },
    {
        "zone": "Second Floor Server Closet",
        "controls": "Standard brass key lock",
        "vulnerability": "Shared Master Key: Janitorial and IT staff share the same key; no electronic audit log of entry.",
        "risk_level": "HIGH",
        "recommended_fix": "Upgrade to electronic badge reader with multi-factor biometric/PIN entry and dedicated CCTV camera.",
    },
    {
        "zone": "Outdoor Waste Disposal & Dumpsters",
        "controls": "Chain-link enclosure (unlocked)",
        "vulnerability": "Dumpster Diving: Printed student test sheets and administrative notes discarded without shredding.",
        "risk_level": "MEDIUM",
        "recommended_fix": "Enforce locked secure shredding bins inside offices before outdoor disposal.",
    },
]


def main():
    print("=" * 70)
    print("  CLASS 07: PHYSICAL SECURITY AUDIT & WEAKNESS INSPECTION")
    print("=" * 70)

    for z in ZONES:
        print(f"\n[ZONE]: {z['zone']}")
        print(f"  Existing Controls: {z['controls']}")
        print(f"  Vulnerability    : [!] {z['vulnerability']}")
        print(f"  Risk Level       : {z['risk_level']}")
        print(f"  Remediation      : --> {z['recommended_fix']}")
        print("-" * 70)


if __name__ == "__main__":
    main()
