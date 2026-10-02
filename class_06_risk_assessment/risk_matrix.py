#!/usr/bin/env python3
"""Class 06: Risk Matrix & Assessment Calculator.

Run: python risk_matrix.py
"""
import json
from pathlib import Path
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

DATA_FILE = Path(__file__).with_name("assets.json")


def calculate_risk_level(score):
    if score >= 16:
        return "CRITICAL"
    elif score >= 10:
        return "HIGH"
    elif score >= 5:
        return "MEDIUM"
    return "LOW"


def main():
    print("=" * 70)
    print("  CLASS 06: CYBERSECURITY RISK REGISTER & MATRIX TERMINAL")
    print("=" * 70)

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        assets = json.load(f)

    print(f"\n[+] Loaded {len(assets)} organizational assets for risk evaluation.\n")
    print(f"{'Asset Name':<30} {'Likelihood':<12} {'Impact':<10} {'Risk Score':<12} {'Level'}")
    print("-" * 70)

    for a in assets:
        score = a["likelihood"] * a["impact"]
        level = calculate_risk_level(score)
        print(f"{a['name']:<30} {a['likelihood']:<12} {a['impact']:<10} {score:<12} {level}")

    print("\n" + "=" * 70)
    print("DETAILED ASSET PROFILES & RISK TREATMENTS:")
    print("=" * 70)

    for a in assets:
        score = a["likelihood"] * a["impact"]
        print(f"\nID: {a['id']} - {a['name']}")
        print(f"  Description    : {a['description']}")
        print(f"  Primary CIA    : {a['cia_primary']}")
        print(f"  Threat Scenario: {a['threat']}")
        print(f"  Risk Evaluation: Likelihood={a['likelihood']}/5, Impact={a['impact']}/5 -> Score={score} ({calculate_risk_level(score)})")
        print(f"  Treatment Plan : {a['treatment']}")


if __name__ == "__main__":
    main()
