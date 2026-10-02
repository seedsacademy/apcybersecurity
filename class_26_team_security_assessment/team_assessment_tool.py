#!/usr/bin/env python3
"""Class 26: Team Security Assessment & Multi-Domain Audit Simulator.

Run: python team_assessment_tool.py
"""
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

TEAM_ROLES = [
    {
        "role": "Role 1: Physical Security Analyst (Unit 2)",
        "focus": "Inspect facility entry points, server room access, badge logs, and environmental controls.",
        "key_finding": "Rear loading dock frequently propped open; server room lacks biometric verification.",
    },
    {
        "role": "Role 2: Network Infrastructure Architect (Unit 3)",
        "focus": "Review IP subnets, VLAN segmentation, Wi-Fi encryption, and perimeter firewall ACLs.",
        "key_finding": "Guest Wi-Fi on same broadcast domain as administrative printers; firewall allows port 3389 inbound.",
    },
    {
        "role": "Role 3: Endpoint Defense Engineer (Unit 4)",
        "focus": "Audit workstation OS versions, local administrator privileges, and process execution logs.",
        "key_finding": "Users possess local administrator rights; USB mass storage autorun enabled on clinical PCs.",
    },
    {
        "role": "Role 4: Application & Data Specialist (Unit 5)",
        "focus": "Evaluate web portal code, SQL injection defenses, file permissions, and data-at-rest encryption.",
        "key_finding": "Patient search parameter concatenates raw input into SQL queries; sensitive records stored unencrypted.",
    },
]


def main():
    print("=" * 70)
    print("  CLASS 26: CAPSTONE TEAM SECURITY ASSESSMENT - APEX HEALTH")
    print("=" * 70)

    print("\nTEAM ROLE ASSIGNMENTS & INITIAL AUDIT FINDINGS:\n")
    for r in TEAM_ROLES:
        print(f"[{r['role']}]")
        print(f"  Audit Focus  : {r['focus']}")
        print(f"  Discovered Red Flag: [!] {r['key_finding']}\n")

    print("=" * 70)
    print("EXECUTIVE DELIVERABLE: Synthesize findings into a unified Risk Register")
    print("and prioritize the Top 3 Immediate Remediations with cost/tradeoff analysis!")
    print("=" * 70)


if __name__ == "__main__":
    main()
