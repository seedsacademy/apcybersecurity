#!/usr/bin/env python3
"""Class 10: Network Attack Path Mapper & Port/Protocol Inspector.

Run: python network_mapper.py
"""
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

TOPOLOGY = [
    {
        "device": "Perimeter Router & Gateway",
        "ip": "203.0.113.1 (Public WAN) / 10.0.0.1 (Internal LAN)",
        "open_ports": ["22/TCP (SSH - restricted to admin subnet)", "443/TCP (VPN Gateway)"],
        "exposure": "Internet-facing; hardened with ACLs",
    },
    {
        "device": "District Public Web Server (DMZ)",
        "ip": "10.0.10.5",
        "open_ports": ["80/TCP (HTTP - redirects to 443)", "443/TCP (HTTPS)"],
        "exposure": "Publicly accessible; isolated in DMZ VLAN 10",
    },
    {
        "device": "Internal Student Records Database",
        "ip": "10.0.20.50",
        "open_ports": ["3306/TCP (MySQL)"],
        "exposure": "HIGH RISK if reachable from DMZ or Student Wi-Fi! Must be restricted to Internal App Server.",
    },
    {
        "device": "Classroom Teacher Workstations",
        "ip": "10.0.30.100 - 10.0.30.250",
        "open_ports": ["445/TCP (SMB File Sharing)", "3389/TCP (RDP Remote Desktop)"],
        "exposure": "Internal only; vulnerable to lateral movement if student devices share subnet.",
    },
]


def main():
    print("=" * 70)
    print("  CLASS 10: NETWORK TOPOLOGY & ATTACK PATH MAPPER")
    print("=" * 70)

    print("\n[+] MAPPING NETWORK NODES & EXPOSED SERVICES:\n")
    for node in TOPOLOGY:
        print(f"Device     : {node['device']}")
        print(f"IP Address : {node['ip']}")
        print(f"Open Ports : {', '.join(node['open_ports'])}")
        print(f"Risk Profile: {node['exposure']}")
        print("-" * 70)

    print("\nIDENTIFIED ATTACK PATH:")
    print("Internet (Attacker) --> [Port 443] DMZ Web Server (10.0.10.5)")
    print("                     --> [Vulnerability in Web App]")
    print("                     --> Lateral Movement across unsegmented link")
    print("                     --> [Port 3306] Internal DB Server (10.0.20.50) [DATA EXFILTRATION!]")
    print("=" * 70)


if __name__ == "__main__":
    main()
