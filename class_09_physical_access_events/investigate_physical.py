#!/usr/bin/env python3
"""Class 09: Physical Access Log Correlator & Incident Timeline.

Run: python investigate_physical.py
"""
from pathlib import Path
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import pandas as pd

DATA_FILE = Path(__file__).with_name("badge_events.csv")


def main():
    print("=" * 70)
    print("  CLASS 09: PHYSICAL ACCESS TELEMETRY & ALARM CORRELATOR")
    print("=" * 70)

    df = pd.read_csv(DATA_FILE)
    print(f"\n[+] Loaded {len(df)} physical telemetry events.\n")

    print("--- 1. CHRONOLOGICAL PHYSICAL ACCESS TIMELINE ---")
    print(df.to_string(index=False))

    print("\n--- 2. CRITICAL ANOMALIES & ALARMS ---")
    alarms = df[df["status"].isin(["DENIED", "CRITICAL_ALARM", "ALERT"])]
    print(alarms[["timestamp", "door_id", "event_type", "status"]].to_string(index=False))

    print("\n" + "=" * 70)
    print("INCIDENT HYPOTHESIS SUMMARY:")
    print("1. 21:05 - Custodian badge B-1042 enters Main Lobby and Floor 2.")
    print("2. 21:15 - Badge B-1042 attempts entry to Server Room twice and is DENIED.")
    print("3. 21:18 - Server room door is forcibly pried open (DOOR_FORCED_ALARM).")
    print("4. 21:18 - Interior motion sensor confirms physical intruder inside server room.")
    print("5. 21:22 - Intruder flees through rear emergency fire exit door.")
    print("=" * 70)


if __name__ == "__main__":
    main()
