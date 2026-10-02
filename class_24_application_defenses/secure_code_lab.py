#!/usr/bin/env python3
"""Class 24: Application Defense - Code Vulnerability Remediation.

Run: python secure_code_lab.py
"""
import html
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def demo_sqli_defense():
    print("--- 1. DEFENDING AGAINST SQL INJECTION ---")
    raw_input = "admin' --"
    print(f"Malicious Input: {raw_input}")

    print("\n[VULNERABLE CODE - String Concatenation]:")
    vulnerable_sql = f"SELECT * FROM users WHERE username = '{raw_input}'"
    print(f"  Resulting SQL Query: {vulnerable_sql}")
    print("  [!] Single quote breaks syntax, comment '--' deletes password check!")

    print("\n[SECURE CODE - Parameterized Query / Prepared Statement]:")
    print("  Code: cursor.execute('SELECT * FROM users WHERE username = %s', (raw_input,))")
    print("  [+] The database treats the entire input as a single literal string.")


def demo_xss_defense():
    print("\n--- 2. DEFENDING AGAINST CROSS-SITE SCRIPTING (XSS) ---")
    user_comment = "<script>alert('Hacked!');</script>"
    print(f"Malicious Input: {user_comment}")

    print("\n[VULNERABLE CODE - Unencoded HTML Reflection]:")
    print(f"  Browser renders: <div>{user_comment}</div>  --> SCRIPT EXECUTES!")

    print("\n[SECURE CODE - Context-Aware HTML Entity Encoding]:")
    sanitized = html.escape(user_comment)
    print(f"  Browser renders: <div>{sanitized}</div>")
    print("  [+] Special characters converted to &lt;script&gt; -- harmless text on screen!")


def main():
    print("=" * 70)
    print("  CLASS 24: SECURE CODING & APPLICATION DEFENSE REMEDIATION")
    print("=" * 70)
    demo_sqli_defense()
    demo_xss_defense()
    print("=" * 70)


if __name__ == "__main__":
    main()
