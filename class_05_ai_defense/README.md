# Class 05: Evaluate AI for Defense — Verification & Hallucinations

[⬅ Back to Course Roadmap](../README.md) | [💻 AI Verification Lab Script](ai_verification_lab.py)

> [!NOTE]
> **Mission Briefing:** Security teams receive millions of alerts every day. To keep up, organizations use Artificial Intelligence (AI) to summarize logs and spot anomalies. However, AI models can **hallucinate**, misinterpret baseline traffic, and invent facts that do not exist in the evidence. In this class, you will audit an AI-generated incident report against raw log data, identify false claims, and practice human-in-the-loop verification.

---

## Course Alignment & AP Framework

- **Course:** AP Cybersecurity
- **Unit 1:** Introduction to Security
- **CED Topic:** **1.5 Evaluating AI for Defense**
- **Course Framework Skills:**
  - **Skill 4.A:** Collaborate with and critically evaluate AI-assisted outputs.
  - **Skill 3.B:** Correlate technical evidence to support or refute security hypotheses.

### Learning Objectives & Essential Knowledge

| Objective ID | Learning Objective | Essential Knowledge Covered |
| :--- | :--- | :--- |
| **LO 1.5.A** | Explain how machine learning and AI assist defenders in threat detection and incident triage. | **EK 1.5.A.1:** AI algorithms process telemetry across millions of endpoints, clustering related alerts and detecting behavioral anomalies faster than human analysts. |
| **LO 1.5.B** | Evaluate the risks and failure modes of AI tools in security operations. | **EK 1.5.B.1:** AI models may generate hallucinations, suffer from high false-positive rates, or be manipulated by adversarial data poisoning. |
| **LO 1.5.C** | Justify the necessity of human verification (human-in-the-loop) in security response. | **EK 1.5.C.1:** Automated actions based on unverified AI summaries can cause accidental business disruption or overlook real compromises. |

---

## Core Concepts: The Strengths and Traps of Defensive AI

### What AI Does Exceptionally Well
- **High-Speed Filtering:** Sifting through 100,000 firewall events per second to discard known benign traffic.
- **Pattern Clustering:** Grouping 50 related alerts across 10 machines into a single incident timeline.
- **Baseline Modeling:** Learning what a "normal" Tuesday afternoon looks like across a company's network.

### The Traps: Why AI Cannot Replace Human Defenders
1. **Hallucination:** Large Language Models predict likely text, not guaranteed truth. An AI may confidently cite a file name, IP address, or attack technique that never appeared in the raw log.
2. **False Positives:** Flagging legitimate administrative tasks (like a scheduled server backup) as malicious ransomware.
3. **False Negatives:** Missing subtle, low-and-slow human attacks that blend into normal traffic.
4. **Data Poisoning:** An adversary deliberately feeding misleading log data to confuse the AI model over time.

```text
               THE HUMAN-IN-THE-LOOP DEFENSE MODEL
               
  [ Raw Logs & Alerts ] 
         |
         v
  [ AI Assistant ]  -----> Triage, summarize, highlight leads
         |
         v
  [ Human Analyst ] -----> FACT-CHECK against raw evidence,
                           make final containment decisions!
```

---

## Hands-on Lab Activity

Run the verification lab:

```powershell
cd class_05_ai_defense
python ai_verification_lab.py
```

### Student Activity: The AI Audit Challenge
Compare the raw log data and the AI summary in the script output:
1. List 3 specific claims made by the AI that are completely contradicted or unsupported by the raw firewall log.
2. What catastrophic business consequence would have occurred if the company blindly followed the AI's recommendation?
3. Rewrite the incident report in 2 sentences, describing *only* the facts supported by the raw evidence.

---

## Assessment: AP-Style Free Response Prompt

**Prompt:**  
A hospital SOC deploys an automated AI incident responder. The tool is programmed to immediately isolate any device from the network if its AI risk score exceeds 85/100. During a shift, the AI flags a surgical workstation because it downloaded an unusually large 4GB firmware patch, scoring it 92/100 and cutting its network connection during an operation.

- **Part 1:** Identify the failure mode of the AI system in this scenario (e.g., false positive, lack of operational context).
- **Part 2:** Explain the real-world operational impact of this unverified automated action.
- **Part 3:** Recommend a governance change or operational workflow to prevent this failure while still benefiting from AI monitoring.

---

## Teacher Guidance & Answer Key

- **Part 1:** The AI committed a **false positive** due to a lack of contextual awareness—it evaluated data volume without recognizing scheduled hospital maintenance or device role.
- **Part 2:** Severe life-safety impact: disconnecting critical operating room equipment during patient care.
- **Part 3:** Require **Human-in-the-Loop approval** before isolating life-critical systems, or configure role-based exemption policies for medical devices requiring human confirmation before disruptive containment.

---

[⬅ Previous Class 04: AI Deception](../class_04_ai_deception/README.md) | [Unit 2 Start: Class 06: Risk Assessment ➡](../class_06_risk_assessment/README.md)
