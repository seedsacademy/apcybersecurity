#!/usr/bin/env python3
"""Class 30: AP Cybersecurity Composite Score & Grade Calculator.

Run: python score_calculator.py
"""
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def compute_ap_score(mcq_correct, frq_points):
    # Weightings: MCQ = 70%, FRQ = 30%
    mcq_weighted = (mcq_correct / 60.0) * 70.0
    frq_weighted = (frq_points / 6.0) * 30.0
    composite = round(mcq_weighted + frq_weighted, 1)

    # Standard AP 5-point composite scale approximation
    if composite >= 75:
        ap_grade = 5
    elif composite >= 62:
        ap_grade = 4
    elif composite >= 50:
        ap_grade = 3
    elif composite >= 38:
        ap_grade = 2
    else:
        ap_grade = 1

    return composite, ap_grade


def main():
    print("=" * 70)
    print("  CLASS 30: AP CYBERSECURITY COMPOSITE SCORE CALCULATOR")
    print("=" * 70)

    # Example student scores
    samples = [
        ("High Scoring (Target)", 52, 5),
        ("Passing Baseline", 36, 4),
        ("Review Needed", 25, 2),
    ]

    for label, mcq, frq in samples:
        comp, grade = compute_ap_score(mcq, frq)
        print(f"\nStudent Profile : {label}")
        print(f"  Section I MCQ : {mcq}/60 correct ({round((mcq/60)*70, 1)} / 70 pts)")
        print(f"  Section II FRQ: {frq}/6 points   ({round((frq/6)*30, 1)} / 30 pts)")
        print(f"  Total Composite: {comp}/100.0")
        print(f"  Projected AP Score: [{grade}]")
        print("-" * 70)


if __name__ == "__main__":
    main()
