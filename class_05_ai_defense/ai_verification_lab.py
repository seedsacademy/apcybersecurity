#!/usr/bin/env python3
"""Class 05: Evaluating AI for Defense - Hallucination & Fact-Checking Lab.

Run: python ai_verification_lab.py
"""
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


RAW_LOG_DATA = """
[LOG EXCERPT - FIREWALL ALERT #4092]
Timestamp           : 2026-10-02 14:22:10 UTC
Source IP           : 198.51.100.82
Destination IP      : 10.0.0.15 (Internal Web Server)
Destination Port    : 443 (HTTPS)
Action              : ALLOWED
Packets Transferred : 14
Bytes Sent          : 1,420 bytes
Bytes Received      : 8,900 bytes
TCP Flags           : SYN, ACK, PSH, FIN (Clean TCP handshake and closure)
Associated User     : None recorded
Status              : Standard web page request
"""

AI_GENERATED_SUMMARY = """
[AI DEFENDER SUMMARY - COPILOT v3]
"ALERT SEVERITY: CRITICAL!
The network firewall detected an ongoing distributed denial-of-service (DDoS) attack from Russia.
The attacker successfully exploited a remote code execution vulnerability in the Apache web server
and exfiltrated 50 Gigabytes of student records. Recommendation: Immediately wipe the server and shut down
all school operations."
"""


def main():
    print("=" * 70)
    print("  CLASS 05: AI DEFENSE EVALUATION & FACT-CHECKING LAB")
    print("=" * 70)

    print("\n1. THE GROUND TRUTH (Actual Raw Log Evidence):")
    print(RAW_LOG_DATA.strip())

    print("\n" + "-" * 70)
    print("2. THE UNVERIFIED AI COPILOT REPORT:")
    print(AI_GENERATED_SUMMARY.strip())

    print("\n" + "-" * 70)
    print("3. DETECTIVE AUDIT: SPOTTING AI HALLUCINATIONS:")
    hallucinations = [
        ("Claim: 'Ongoing DDoS attack'", "Truth: Only 1 single connection (14 packets) was recorded."),
        ("Claim: 'From Russia'", "Truth: IP 198.51.100.82 has no geographic attribution in the log."),
        ("Claim: 'Remote code execution exploited'", "Truth: Normal TCP handshake and clean closure recorded."),
        ("Claim: 'Exfiltrated 50 Gigabytes of data'", "Truth: Only 8,900 bytes (8.9 KB) were received."),
        ("Recommendation: 'Wipe server / shut down school'", "Truth: Catastrophic overreaction caused by hallucination!"),
    ]

    for claim, truth in hallucinations:
        print(f"  [X] AI Hallucination : {claim}")
        print(f"      Ground Reality   : {truth}\n")

    print("=" * 70)
    print("TAKEAWAY: AI tools are powerful assistants, but human analysts must ALWAYS")
    print("verify AI claims against raw telemetry before making security decisions!")
    print("=" * 70)


if __name__ == "__main__":
    main()
