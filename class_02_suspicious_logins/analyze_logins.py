#!/usr/bin/env python3
"""Class 02: Investigate Suspicious Logins.

Run: python analyze_logins.py
"""
from pathlib import Path
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import pandas as pd

CSV_PATH = Path(__file__).with_name("logins.csv")


def main():
    print("=" * 65)
    print("  CLASS 02: AUTHENTICATION & LOGIN INVESTIGATION TERMINAL")
    print("=" * 65)

    df = pd.read_csv(CSV_PATH)
    print(f"\n[+] Loaded {len(df)} login records from logins.csv\n")

    print("--- 1. OVERALL OUTCOME SUMMARY ---")
    print(df["outcome"].value_counts().to_string())

    print("\n--- 2. DETECTING BRUTE FORCE (Single target, rapid repeated attempts) ---")
    brute = df.groupby(["src_ip", "username"]).filter(lambda g: len(g) >= 4)
    print(brute[["timestamp", "src_ip", "username", "outcome", "notes"]].to_string(index=False))

    print("\n--- 3. DETECTING PASSWORD SPRAYING (Single IP, many distinct accounts) ---")
    spray = df.groupby("src_ip").filter(lambda g: g["username"].nunique() >= 4)
    print(spray[["timestamp", "src_ip", "username", "user_agent", "outcome"]].to_string(index=False))

    print("\n--- 4. MULTI-FACTOR AUTHENTICATION (MFA) EVENTS ---")
    mfa_events = df[df["notes"].str.contains("mfa", case=False, na=False)]
    print(mfa_events[["timestamp", "username", "src_ip", "outcome", "notes"]].to_string(index=False))
    print("\n" + "=" * 65)


if __name__ == "__main__":
    main()
