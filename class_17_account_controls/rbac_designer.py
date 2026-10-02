#!/usr/bin/env python3
"""Class 17: Role-Based Access Control (RBAC) & Least Privilege Designer.

Run: python rbac_designer.py
"""
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROLES = [
    {
        "role": "High School Student",
        "workstation_privilege": "Standard User (Cannot install software, cannot modify system registry)",
        "network_access": "Student Wi-Fi & Internet only",
        "file_permissions": "Personal home folder (Read/Write), Class Handouts (Read Only)",
        "polp_justification": "Prevents unauthorized software/malware installation and lateral tampering.",
    },
    {
        "role": "Classroom Teacher",
        "workstation_privilege": "Standard User with UAC elevation prompt for approved educational software",
        "network_access": "Staff VLAN + Internet + Grading Portal (HTTPS Port 443)",
        "file_permissions": "Curriculum shares (Read/Write), Student grade submission folder (Read/Write)",
        "polp_justification": "Protects grading integrity; prevents day-to-day web surfing with administrative privileges.",
    },
    {
        "role": "Network Administrator",
        "workstation_privilege": "Dedicated Privileged Access Workstation (PAW); separate unprivileged account for daily email",
        "network_access": "Restricted Management VLAN (SSH, RDP, Switch consoles)",
        "file_permissions": "Domain Controller and System configuration files",
        "polp_justification": "Separation of Duties: Admins must NEVER browse the web or check personal email using domain admin credentials.",
    },
]


def main():
    print("=" * 70)
    print("  CLASS 17: ROLE-BASED ACCESS CONTROL (RBAC) & LEAST PRIVILEGE")
    print("=" * 70)

    for r in ROLES:
        print(f"\n[ROLE]: {r['role']}")
        print(f"  Device Privilege : {r['workstation_privilege']}")
        print(f"  Network Scope    : {r['network_access']}")
        print(f"  File Permissions : {r['file_permissions']}")
        print(f"  Security Rationale: {r['polp_justification']}")
        print("-" * 70)


if __name__ == "__main__":
    main()
