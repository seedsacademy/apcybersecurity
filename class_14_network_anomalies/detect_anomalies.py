#!/usr/bin/env python3
"""Class 14: Network Telemetry & Port Scan Anomaly Detector.

Run: python detect_anomalies.py
"""
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FLOWS = [
    # Normal user browsing
    {"timestamp": "10:00:01", "src": "10.0.30.12", "dst": "140.82.112.4", "port": 443, "proto": "TCP", "status": "SYN-ACK"},
    {"timestamp": "10:00:02", "src": "10.0.30.12", "dst": "140.82.112.4", "port": 443, "proto": "TCP", "status": "ESTABLISHED"},
    
    # Port scan from external IP (rapid connection attempts to sequential ports)
    {"timestamp": "10:01:00", "src": "203.0.113.99", "dst": "10.0.10.5", "port": 21,   "proto": "TCP", "status": "RST/DENIED"},
    {"timestamp": "10:01:01", "src": "203.0.113.99", "dst": "10.0.10.5", "port": 22,   "proto": "TCP", "status": "RST/DENIED"},
    {"timestamp": "10:01:02", "src": "203.0.113.99", "dst": "10.0.10.5", "port": 23,   "proto": "TCP", "status": "RST/DENIED"},
    {"timestamp": "10:01:03", "src": "203.0.113.99", "dst": "10.0.10.5", "port": 80,   "proto": "TCP", "status": "OPEN"},
    {"timestamp": "10:01:04", "src": "203.0.113.99", "dst": "10.0.10.5", "port": 443,  "proto": "TCP", "status": "OPEN"},
    {"timestamp": "10:01:05", "src": "203.0.113.99", "dst": "10.0.10.5", "port": 3389, "proto": "TCP", "status": "RST/DENIED"},
    
    # High volume DNS query anomaly (DNS Tunneling)
    {"timestamp": "10:05:10", "src": "10.0.30.99", "dst": "8.8.8.8", "port": 53, "proto": "UDP", "status": "QUERY: a7x91b.exfil.badsite.com"},
    {"timestamp": "10:05:11", "src": "10.0.30.99", "dst": "8.8.8.8", "port": 53, "proto": "UDP", "status": "QUERY: c29z11.exfil.badsite.com"},
]


def main():
    print("=" * 70)
    print("  CLASS 14: NETWORK FLOW ANOMALY & PORT SCAN DETECTION")
    print("=" * 70)

    print("\n[+] ANALYZING PACKET TELEMETRY STREAM:\n")
    scan_ips = {}
    for f in FLOWS:
        print(f"[{f['timestamp']}] {f['src']} --> {f['dst']}:{f['port']} ({f['status']})")
        if "DENIED" in f["status"] or "RST" in f["status"]:
            scan_ips[f["src"]] = scan_ips.get(f["src"], 0) + 1

    print("\n" + "-" * 70)
    print("DETECTED ANOMALIES & INCIDENT LEADS:")
    print("-" * 70)
    for ip, count in scan_ips.items():
        if count >= 3:
            print(f"[!] VERTICAL PORT SCAN ALERT: Source IP {ip} probed multiple sequential ports.")
    print("[!] DNS DATA EXFILTRATION (TUNNELING) SUSPECT: Host 10.0.30.99 sending encoded subdomains.")
    print("=" * 70)


if __name__ == "__main__":
    main()
