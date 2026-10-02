#!/usr/bin/env python3
"""Class 19: Operating System Process & Event Log Tracer.

Run: python trace_process_activity.py
"""
from pathlib import Path
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import pandas as pd

DATA_FILE = Path(__file__).with_name("os_events.csv")


def main():
    print("=" * 70)
    print("  CLASS 19: ENDPOINT PROCESS LINEAGE & ATTACK RECONSTRUCTION")
    print("=" * 70)

    df = pd.read_csv(DATA_FILE)
    print(f"\n[+] Loaded {len(df)} OS telemetry records.\n")

    print("--- 1. CHRONOLOGICAL PROCESS EXECUTION SEQUENCE ---")
    for _, row in df.iterrows():
        print(f"[{row['timestamp']}] Event {row['event_id']} ({row['event_name']})")
        print(f"  Parent Process : {row['parent_process']}")
        print(f"  Spawned Process: {row['process_name']} (User: {row['user']})")
        print(f"  Command Line   : {row['command_line']}")
        print("-" * 70)

    print("\n" + "=" * 70)
    print("DETECTED ATTACK CHAIN (Process Lineage):")
    print("outlook.exe (Email client) ")
    print("  --> winword.exe (User opens attached 'Invoice.docx')")
    print("        --> cmd.exe (Malicious macro executes hidden shell)")
    print("              --> powershell.exe (Downloads encoded payload with bypass)")
    print("                    --> New Service 'WindowsUpdateHelper' (PERSISTENCE ESTABLISHED!)")
    print("=" * 70)


if __name__ == "__main__":
    main()
