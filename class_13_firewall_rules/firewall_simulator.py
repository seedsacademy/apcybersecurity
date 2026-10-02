#!/usr/bin/env python3
"""Class 13: Packet Filtering Firewall Simulator.

Run: python firewall_simulator.py
"""
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Ordered ruleset: First Match Wins!
RULESET = [
    {"rule_num": 10, "action": "ALLOW", "src": "10.0.20.0/24 (Staff)", "dst": "10.0.40.50 (Grading DB)", "port": 443, "proto": "TCP"},
    {"rule_num": 20, "action": "DENY",  "src": "ANY", "dst": "10.0.40.0/24 (Server Core)", "port": "ANY", "proto": "ANY"},
    {"rule_num": 30, "action": "ALLOW", "src": "10.0.30.0/24 (Students)", "dst": "ANY (Internet)", "port": 80, "proto": "TCP"},
    {"rule_num": 40, "action": "ALLOW", "src": "10.0.30.0/24 (Students)", "dst": "ANY (Internet)", "port": 443, "proto": "TCP"},
    {"rule_num": 99, "action": "DENY",  "src": "ANY", "dst": "ANY", "port": "ANY", "proto": "ANY", "note": "Implicit Deny"},
]

PACKETS = [
    {"desc": "Teacher accesses grading app", "src": "10.0.20.15", "dst": "10.0.40.50", "port": 443, "proto": "TCP"},
    {"desc": "Student tries direct database connection", "src": "10.0.30.45", "dst": "10.0.40.50", "port": 443, "proto": "TCP"},
    {"desc": "Student searches Wikipedia over HTTPS", "src": "10.0.30.88", "dst": "198.35.26.96", "port": 443, "proto": "TCP"},
    {"desc": "Inbound internet hacker attempts SSH to Server", "src": "203.0.113.7", "dst": "10.0.40.10", "port": 22, "proto": "TCP"},
]


def test_packet(packet):
    for r in RULESET:
        # Check rule match
        src_match = (r["src"].startswith("ANY") or 
                     (r["src"].startswith("10.0.20") and packet["src"].startswith("10.0.20")) or
                     (r["src"].startswith("10.0.30") and packet["src"].startswith("10.0.30")))
        
        dst_match = (r["dst"].startswith("ANY") or
                     (r["dst"].startswith("10.0.40.50") and packet["dst"] == "10.0.40.50") or
                     (r["dst"].startswith("10.0.40") and packet["dst"].startswith("10.0.40")))
        
        port_match = (r["port"] == "ANY" or r["port"] == packet["port"])
        proto_match = (r["proto"] == "ANY" or r["proto"] == packet["proto"])

        if src_match and dst_match and port_match and proto_match:
            return r["rule_num"], r["action"]
    return 99, "DENY"


def main():
    print("=" * 70)
    print("  CLASS 13: STATEFUL FIREWALL RULE ENGINE & PACKET EVALUATOR")
    print("=" * 70)

    print("\nCURRENT ACTIVE ORDERED RULESET (Top-to-Bottom Evaluation):\n")
    for r in RULESET:
        print(f"Rule {r['rule_num']:<3} | Action: {r['action']:<5} | Src: {r['src']:<22} | Dst: {r['dst']:<22} | Port: {str(r['port']):<5} | Proto: {r['proto']}")

    print("\n" + "-" * 70)
    print("TESTING INCOMING PACKETS:\n")
    for p in PACKETS:
        rule_hit, decision = test_packet(p)
        print(f"Packet: {p['desc']}")
        print(f"  {p['src']} --> {p['dst']}:{p['port']} ({p['proto']})")
        print(f"  Result : Matched Rule {rule_hit} ==> [{decision}]\n")
    print("=" * 70)


if __name__ == "__main__":
    main()
