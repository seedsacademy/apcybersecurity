#!/usr/bin/env python3
"""Class 08: Layered Physical Defense (Defense in Depth).

Run: python defense_in_depth.py
"""
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RINGS = [
    {
        "ring": "Ring 1: Outer Property Perimeter",
        "objective": "Deter and delay unauthorized vehicles and trespassers before reaching the facility.",
        "controls": ["Perimeter fencing with razor wire", "Vehicle crash bollards", "License plate reader cameras", "Perimeter lighting"],
        "tradeoff": "High installation cost; creates an imposing, less welcoming public appearance.",
    },
    {
        "ring": "Ring 2: Building Exterior & Entrance",
        "objective": "Channel visitors through a single monitored entry point.",
        "controls": ["Reinforced exterior doors", "Security guard / Reception desk", "Visitor sign-in with government ID", "CCTV at all entrances"],
        "tradeoff": "Slows down entry during peak morning arrival hours.",
    },
    {
        "ring": "Ring 3: Interior Workspaces",
        "objective": "Restrict movement between departments based on need-to-know.",
        "controls": ["Electronic RFID badge readers", "Clean desk policy", "Automatic locking office doors", "Security cameras in hallways"],
        "tradeoff": "Staff must carry badges at all times; lost badges require rapid deactivation.",
    },
    {
        "ring": "Ring 4: Core Data Center / Server Room",
        "objective": "Provide maximum protection for critical compute and storage infrastructure.",
        "controls": ["Security vestibule / Mantrap (interlocking double doors)", "Biometric palm/fingerprint scanner", "Server rack keyed locks", "Clean-agent gaseous fire suppression (FM-200)"],
        "tradeoff": "Expensive maintenance; restricts emergency access to small authorized IT group.",
    },
]


def main():
    print("=" * 70)
    print("  CLASS 08: CONCENTRIC RINGS OF PHYSICAL DEFENSE")
    print("=" * 70)

    for r in RINGS:
        print(f"\n[+] {r['ring']}")
        print(f"    Objective: {r['objective']}")
        print("    Controls Deployed:")
        for c in r["controls"]:
            print(f"      - {c}")
        print(f"    Operational Tradeoff: {r['tradeoff']}")
        print("-" * 70)


if __name__ == "__main__":
    main()
