#!/usr/bin/env python3
"""Class 04: AI-Assisted Deception Analyzer.

Run: python evaluate_deception.py
"""
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


SAMPLES = [
    {
        "id": "AI-CLONE-01",
        "medium": "Audio Voicemail / Voice Clone",
        "alleged_source": "Superintendent Dr. Vance",
        "content": "'Hello Marcus, this is Dr. Vance. I am in an urgent budget hearing with the county council and my cell connection is spotty. We need to wire $15,000 for emergency stadium generator repairs before the storm hits tonight. Please authorize account transfer #9021 immediately. Call me back only if there is an error.'",
        "ai_indicators": [
            "Voice matches Dr. Vance's cadence, but slight metallic resonance / unnatural breath pacing",
            "Urgent financial demand bypassing the 2-signature board policy",
            "Discouraging callbacks ('Call me back only if there is an error') to prevent live conversational scrutiny",
        ],
        "verification_protocol": "Hang up. Call Dr. Vance on his pre-registered direct office phone or verify in person with the district finance officer.",
    },
    {
        "id": "AI-SPEAR-02",
        "medium": "Generative AI Spear Phishing Email",
        "alleged_source": "District Science Fair Coordinator",
        "content": "'Dear Maya,\nI thoroughly enjoyed your presentation on microcontroller-based autonomous navigation at the tri-county STEM symposium. Because your project achieved a 98% efficiency rating, you qualify for our expedited $2,500 research grant. Please open the attached form to submit your tax ID and direct deposit details.'",
        "ai_indicators": [
            "Flawless grammar and academic tone (unlike traditional broken-English phishing)",
            "Automated reconnaissance: scraped project title and scores from public school newspaper article",
            "Lures student into revealing sensitive PII (Social Security / Tax ID and bank routing numbers)",
        ],
        "verification_protocol": "Check official district science department website; verify grant legitimacy with school science department chair.",
    },
]


def main():
    print("=" * 65)
    print("  CLASS 04: AI-ASSISTED DECEPTION & IMPERSONATION LAB")
    print("=" * 65)

    for s in SAMPLES:
        print(f"\n[CASE {s['id']}]: {s['medium']}")
        print(f"Alleged Sender: {s['alleged_source']}")
        print(f"Message Transcript:\n  {s['content']}")
        print("\nAI Markers & Red Flags:")
        for ind in s["ai_indicators"]:
            print(f"  [!] {ind}")
        print(f"\nRequired Out-of-Band Verification:\n  --> {s['verification_protocol']}")
        print("-" * 65)


if __name__ == "__main__":
    main()
