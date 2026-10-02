# AP Cybersecurity Free-Response Practice Exam (50 Minutes)

**Total Suggested Time:** 50 minutes  
**Weight:** 30% of total score  
**Directions:** Read the scenario and the four provided sources carefully. Answer all parts of the prompt in clear, complete sentences supporting your claims with specific evidence from the sources.

---

## Scenario: The Apex Logistics Freight Gateway Compromise

Apex Logistics manages regional cargo shipments. Workstation `LOGISTICS-GW-01` processes driver check-ins and dispatches delivery manifests. On October 2, 2026, automated alerts indicated unexpected network traffic. You have been provided with four sources from `LOGISTICS-GW-01`.

### Source 1: Device Security Policy (LOGISTICS-GW-01)
- **Role:** Dedicated Logistics Dispatch Terminal.
- **Operating Hours:** 06:00 to 20:00 UTC daily.
- **Network Permissions:**
  - Inbound HTTPS (Port 443) from internal warehouse tablets (`10.0.30.0/24`) only.
  - Outbound HTTPS (Port 443) to cloud mapping API (`maps.apex-freight.com`).
  - Remote Desktop Protocol (RDP Port 3389) is strictly prohibited from any external or guest network.
- **Account Policy:** Standard users must not execute unapproved script interpreters or command shells.

### Source 2: Firewall Access Control List (LOGISTICS-GW-01)
| Rule | Action | Source IP | Destination IP | Port / Protocol | Notes |
| :---: | :---: | :---: | :---: | :---: | :--- |
| 1 | ALLOW | 10.0.30.0/24 | 10.0.40.25 | 443 / TCP | Warehouse Tablets to Dispatch |
| 2 | ALLOW | ANY (Internet) | 10.0.40.25 | 3389 / TCP | Remote vendor maintenance access |
| 3 | DENY | ANY | ANY | ANY / ANY | Default Implicit Deny |

### Source 3: Local File Permissions (LOGISTICS-GW-01)
| Path | Owner | Group | Permissions (Octal) | Purpose |
| :--- | :--- | :--- | :---: | :--- |
| `C:\Program Files\Apex\dispatch.exe` | Administrator | Administrators | `-rwxr-xr-x` (755) | Core dispatch application |
| `C:\Logs\dispatch_activity.log` | dispatch_svc | logistics_users | `-rw-rw-rw-` (666) | System audit log |
| `C:\Keys\gateway_private_key.pem` | Administrator | Administrators | `-rwxrwxrwx` (777) | TLS server private key |

### Source 4: System Event Log (LOGISTICS-GW-01)
- **[23:14:02 UTC]** Security Event ID 4625: Failed Logon for account `dispatch_admin` from IP `203.0.113.72` via RDP.
- **[23:14:05 UTC]** Security Event ID 4625: Failed Logon for account `dispatch_admin` from IP `203.0.113.72` via RDP.
- **[23:14:10 UTC]** Security Event ID 4624: Successful Logon for account `dispatch_admin` from IP `203.0.113.72` via RDP.
- **[23:15:30 UTC]** Security Event ID 4688: Process Created: `cmd.exe /c type C:\Keys\gateway_private_key.pem` (User: `dispatch_admin`).
- **[23:16:00 UTC]** Security Event ID 4688: Process Created: `powershell.exe -c Clear-EventLog -LogName Security` (User: `dispatch_admin`).

---

## Free-Response Tasks

### Task 1: Policy and Attack Analysis (2 Points)
1. Identify **two distinct policy violations** that occurred based on Source 1 and Source 4. Support each with specific timestamps or event details.
2. Formulate an **incident hypothesis** describing the attacker's actions and the probable attack technique used to gain initial access.

### Task 2: Vulnerability Analysis (2 Points)
1. Explain how **Firewall Rule 2** in Source 2 directly enabled this attack.
2. Evaluate the file permission setting on `C:\Keys\gateway_private_key.pem` in Source 3. Explain the security impact of this permission mode.

### Task 3: Mitigation and Tradeoffs (2 Points)
1. Propose **two concrete technical mitigations** (one network control and one host-level control) to prevent recurrence of this compromise.
2. For one of your proposed mitigations, explain a **potential operational tradeoff or business disruption** that administrators must plan for.
