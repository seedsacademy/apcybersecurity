#!/usr/bin/env python3
"""Class 03: Public Wi-Fi & Packet Sniffing Simulation.

Run: python traffic_sim.py
"""
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def main():
    print("=" * 65)
    print("  CLASS 03: PUBLIC WI-FI PACKET SNIFFING SIMULATION")
    print("=" * 65)

    packets = [
        {
            "protocol": "HTTP (Unencrypted)",
            "src": "192.168.1.105 (Student Laptop)",
            "dest": "93.184.216.34 (cafe-menu-orders.com:80)",
            "raw_payload": "POST /login HTTP/1.1\nHost: cafe-menu-orders.com\nuser=alex&pass=SecretP@ssw0rd!&card=4111-2222-3333-4444",
            "sniffed_result": "CRITICAL RISK: Plaintext password & credit card captured by nearby sniffer!",
        },
        {
            "protocol": "HTTPS / TLS 1.3 (Encrypted)",
            "src": "192.168.1.105 (Student Laptop)",
            "dest": "140.82.112.4 (github.com:443)",
            "raw_payload": "b'\\x17\\x03\\x03\\x00\\xa5\\x9b\\x12\\x8f\\xcd\\xfe... [Encrypted Application Data]'",
            "sniffed_result": "SAFE: Sniffer sees destination IP and port, but payload contents are unreadable ciphertext.",
        },
        {
            "protocol": "VPN Tunnel (WireGuard/IPsec)",
            "src": "192.168.1.105 (Student Laptop)",
            "dest": "198.51.100.5 (School VPN Gateway:51820)",
            "raw_payload": "b'\\x04\\x00\\x00\\x00\\x7a\\x3c... [Entire packet inside encrypted tunnel]'",
            "sniffed_result": "MAXIMUM PRIVACY: Local Wi-Fi sniffer cannot see the real destination websites or DNS lookups.",
        },
    ]

    for p in packets:
        print(f"\n[Packet Type]: {p['protocol']}")
        print(f"  Source      : {p['src']}")
        print(f"  Destination : {p['dest']}")
        print(f"  Raw Payload :")
        for line in p["raw_payload"].split("\n"):
            print(f"    | {line}")
        print(f"  Verdict     : {p['sniffed_result']}")
        print("-" * 65)


if __name__ == "__main__":
    main()
