#!/usr/bin/env python3
"""Cyber Detective: Social Engineering Case Investigator.

Class 01: Recognize Social Engineering (CED Topic 1.1)

Run interactively:
    python investigate.py

Or view a specific case:
    python investigate.py --case CASE-101
    python investigate.py --all
"""

import argparse
import json
from pathlib import Path
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

DATA_FILE = Path(__file__).with_name("scenarios.json")


def load_cases():
    if not DATA_FILE.is_file():
        print(f"Error: Could not find evidence database at {DATA_FILE}")
        sys.exit(1)
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def print_banner():
    banner = r"""
========================================================================
   ____ ____   _   ____    ____  _____ _____ _____ ____ _____ _____     
  / ___/ ___| / \ / ___|  |  _ \| ____|_   _| ____/ ___|_   _| ____|    
 | |   \___ \/ _ \\___ \  | | | |  _|   | | |  _|| |     | | |  _|      
 | |___ ___) / ___ \___) | | |_| | |___  | | | |__| |___  | | | |___     
  \____|____/_/   \_\____/  |____/|_____| |_| |_____\____| |_| |_____|    
      SOC INCIDENT INVESTIGATION TERMINAL - CLASS 01: CED 1.1           
========================================================================
    """
    print(banner)


def display_case(case, reveal_evidence=False):
    title = case.get('title', '').replace('\u2014', '-').replace('\u2013', '-')
    print(f"\n{'='*70}")
    print(f"CASE FILE: {case['id']} - {title}")
    print(f"{'='*70}")
    print(f"Channel     : {case['channel']}")
    print(f"Display Name: {case['sender_display']}")
    print(f"Recipient   : {case['recipient']}")
    print(f"Timestamp   : {case['timestamp']}")
    if case.get("subject"):
        print(f"Subject     : {case['subject'].replace('\u2014', '-')}")
    print(f"{'-'*70}")
    print("MESSAGE CONTENT:")
    for line in case["body"].split("\n"):
        print(f"  | {line}")
    print(f"{'-'*70}")

    if reveal_evidence:
        print("\n[+] FORENSIC INSPECTION (Deep Dive):")
        print(f"  * Actual Sender / Technical Origin: {case['actual_sender']}")
        print("  * Red Flags Detected:")
        for rf in case["red_flags"]:
            print(f"     [!] {rf}")
        print("  * Psychological Levers Used:")
        for pt in case["psychological_triggers"]:
            print(f"     [+] {pt}")
        print(f"  * Attack Classification: {case['attack_type']}")
        print(f"  * Potential Consequence: {case['potential_consequence']}")
        print(f"  * Recommended Safe Response:\n     --> {case['safe_response']}")
    else:
        print("\n[Tip: Use the Forensic Tool in interactive mode to inspect headers and reveal hidden clues!]")


def interactive_mode(cases):
    case_map = {c["id"]: c for c in cases}
    print_banner()
    print("Welcome, Agent! Select a case file to investigate:")

    while True:
        print("\n--- ACTIVE CASE FILES ---")
        for i, c in enumerate(cases, 1):
            print(f"  [{i}] {c['id']}: {c['title']} ({c['channel']})")
        print("  [A] Inspect All Cases")
        print("  [Q] Exit Investigation Terminal")

        choice = input("\nEnter case number [1-6], 'A', or 'Q': ").strip().upper()
        if choice == "Q":
            print("\nExiting terminal. Stay safe online, Detective!\n")
            break
        elif choice == "A":
            for c in cases:
                display_case(c, reveal_evidence=True)
            continue

        selected_case = None
        if choice.isdigit() and 1 <= int(choice) <= len(cases):
            selected_case = cases[int(choice) - 1]
        elif choice in case_map:
            selected_case = case_map[choice]

        if not selected_case:
            print("Invalid selection. Please choose an available case.")
            continue

        # Case interaction loop
        display_case(selected_case, reveal_evidence=False)
        while True:
            print(f"\nOptions for {selected_case['id']}:")
            print("  [1] [Forensics] Run Forensic Header & Link Analysis (Reveal hidden clues)")
            print("  [2] [Quiz] Quiz Yourself: Identify Tactics & Safe Response")
            print("  [3] [Back] Return to Case List")

            sub_choice = input("Select an option [1-3]: ").strip()
            if sub_choice == "1":
                display_case(selected_case, reveal_evidence=True)
            elif sub_choice == "2":
                run_mini_quiz(selected_case)
            elif sub_choice == "3":
                break
            else:
                print("Please enter 1, 2, or 3.")


def run_mini_quiz(case):
    print(f"\n--- POP QUIZ: CASE {case['id']} ---")
    print("1. Is this message malicious or benign?")
    print("   [A] Legitimate / Benign")
    print("   [B] Malicious Social Engineering Attack")
    ans1 = input("Your answer (A or B): ").strip().upper()
    is_malicious_expected = "B" if case["attack_type"] != "Legitimate (Benign)" else "A"

    if ans1 == is_malicious_expected:
        print("   -> CORRECT! Excellent judgment.")
    else:
        print(f"   -> Careful! Expected answer was [{is_malicious_expected}].")

    print("\n2. Name one psychological trick or red flag you spotted in this case:")
    tactic = input("   Your observation: ").strip()
    if tactic:
        print(f"   -> Good eye! You noted: '{tactic}'")
        print("   -> Known Case Triggers:", ", ".join(case["psychological_triggers"]))

    print("\n3. What is the safest response a student or staff member should take?")
    resp = input("   Your recommended response: ").strip()
    if resp:
        print(f"   -> Recorded: '{resp}'")
        print(f"   -> SOC Best Practice: {case['safe_response']}")
    print("\n--- Quiz Complete! ---\n")


def main():
    parser = argparse.ArgumentParser(description="Investigate social engineering case files.")
    parser.add_argument("--case", type=str, help="Case ID to inspect (e.g. CASE-101)")
    parser.add_argument("--all", action="store_true", help="Display all cases with forensic details")
    args = parser.parse_args()

    cases = load_cases()

    if args.all:
        print_banner()
        for c in cases:
            display_case(c, reveal_evidence=True)
    elif args.case:
        matched = [c for c in cases if c["id"].upper() == args.case.upper()]
        if not matched:
            print(f"Error: No case found with ID '{args.case}'. Available: {[c['id'] for c in cases]}")
            sys.exit(1)
        display_case(matched[0], reveal_evidence=True)
    else:
        interactive_mode(cases)


if __name__ == "__main__":
    main()
