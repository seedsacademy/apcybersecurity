# AP Cybersecurity Free-Response Scoring Guidelines

**Total Possible Points:** 6 Points  
*(Scored on a 0–6 holistic AP scale with 1 point awarded per specific criteria).*

---

## Task 1: Policy and Attack Analysis (2 Points Maximum)

### Point 1: Policy Violations
- **Criteria:** The response correctly identifies two distinct policy violations supported by specific evidence from Source 1 and Source 4.
- **Acceptable Evidence:**
  - Login occurred at 23:14 UTC, which is outside the approved operating window of 06:00 to 20:00 UTC.
  - Inbound RDP connection was established from external IP `203.0.113.72`, violating the strict prohibition on external RDP.
  - Command shell execution (`cmd.exe` / `powershell.exe`) violates the prohibition on standard script/shell interpreters.

### Point 2: Incident Hypothesis & Initial Access
- **Criteria:** The response formulates a plausible incident hypothesis supported by log telemetry and correctly identifies the initial access technique.
- **Acceptable Evidence:**
  - Identifies **brute-force password guessing** or **credential stuffing** against the RDP port (citing Event 4625 failures followed immediately by Event 4624 success).
  - Describes the post-exploitation actions: the attacker read the TLS private key (`gateway_private_key.pem`) and attempted to cover their tracks by clearing Windows security event logs (`Clear-EventLog`).

---

## Task 2: Vulnerability Analysis (2 Points Maximum)

### Point 3: Firewall Misconfiguration
- **Criteria:** Explains that Firewall Rule 2 exposed port 3389 (RDP) to `ANY (Internet)` without restriction, allowing the external attacker to establish a direct connection to the dispatch gateway from the public internet.

### Point 4: File Permission Flaw
- **Criteria:** Explains that file mode `777` (`-rwxrwxrwx`) makes the private key world-readable and world-writable by any account or process on the system.
- **Impact Explanation:** Stolen private keys allow the attacker to decrypt past and future TLS communications, perform Man-in-the-Middle attacks, and forge trusted gateway communications.

---

## Task 3: Mitigation and Tradeoffs (2 Points Maximum)

### Point 5: Concrete Mitigations
- **Criteria:** Proposes two distinct technical remediations (one network-level and one host-level).
- **Acceptable Network Mitigations:** Delete Firewall Rule 2; place RDP behind an encrypted VPN requiring Multi-Factor Authentication; restrict management to internal administrative IPs only.
- **Acceptable Host Mitigations:** Correct private key permissions to mode `600` or `400` restricted exclusively to the `Administrator` account; enforce account lockout policies or MFA on RDP; restrict PowerShell script execution.

### Point 6: Operational Tradeoff
- **Criteria:** Accurately describes an operational impact or user friction resulting from the proposed mitigation.
- **Acceptable Tradeoffs:**
  - If external RDP is blocked, legitimate remote vendors and technicians cannot perform emergency after-hours support without logging into a VPN.
  - Enforcing strict account lockouts may cause denial-of-service if an attacker deliberately sprays passwords to lock out legitimate dispatch operators during working hours.
