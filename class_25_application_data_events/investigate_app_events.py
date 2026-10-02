#!/usr/bin/env python3
"""Class 25: Web Application & Data Access Log Analyzer.

Run: python investigate_app_events.py
"""
from pathlib import Path
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

LOG_FILE = Path(__file__).with_name("web_access.log")


def main():
    print("=" * 70)
    print("  CLASS 25: WEB APPLICATION & DATA ACCESS FORENSIC PARSER")
    print("=" * 70)

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    print(f"\n[+] Loaded {len(lines)} web application access records:\n")

    pattern = re.compile(r'(\S+) - - \[(.*?)\] "(.*?)" (\d{3}) (\d+) "(.*?)" "(.*?)"')

    for line in lines:
        match = pattern.match(line.strip())
        if match:
            ip, ts, req, status, size, ref, ua = match.groups()
            print(f"[{ts}] Status: {status} | Size: {size:>6} bytes | IP: {ip}")
            print(f"  Request   : {req}")
            print(f"  User Agent: {ua}")
            
            # Anomaly checks
            if "UNION" in req or "OR 1=1" in req or "%27" in req:
                print("  [!] ALERT: SQL Injection attack pattern detected in URL parameter!")
            if int(size) > 50000:
                print("  [!] ALERT: Abnormally large response payload (Suspected Data Exfiltration)!")
            print("-" * 70)


if __name__ == "__main__":
    main()
