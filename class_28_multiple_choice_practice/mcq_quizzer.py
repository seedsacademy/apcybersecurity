#!/usr/bin/env python3
"""Class 28: AP Cybersecurity Multiple-Choice Practice Engine.

Run: python mcq_quizzer.py
"""
import json
from pathlib import Path
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

DATA_FILE = Path(__file__).with_name("questions.json")


def main():
    print("=" * 70)
    print("  CLASS 28: AP CYBERSECURITY MULTIPLE-CHOICE PRACTICE ENGINE")
    print("=" * 70)

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        questions = json.load(f)

    score = 0
    total = len(questions)

    for q in questions:
        print(f"\n[Question {q['id']} - {q['unit']}]")
        print(q["prompt"])
        print()
        for letter, text in q["options"].items():
            print(f"  ({letter}) {text}")
        
        # Display answer with full rationale
        print(f"\n--> Correct Answer: ({q['answer']})")
        print(f"    Rationale     : {q['rationale']}")
        print("-" * 70)

    print("\n" + "=" * 70)
    print("PRACTICE EXAM REVIEW COMPLETE: Review explanations for any incorrect concepts!")
    print("=" * 70)


if __name__ == "__main__":
    main()
