# Class 01: Recognize Social Engineering — The Human Firewall

[⬅ Back to Course Roadmap](../README.md) | [📄 Student Worksheet](student_worksheet.md) | [💻 Investigator Script](investigate.py) | [📁 Case Database](scenarios.json)

> [!NOTE]
> **Mission Briefing:** In cybersecurity, billions of dollars are spent on firewalls, encryption, and antivirus tools. Yet over **80% of data breaches start with a single human being tricked into clicking a link, opening a file, or handing over a password**. In this class, you step into the shoes of a cyber investigator to analyze the psychology of manipulation and learn how to defend the most vulnerable component of every computer network: the human mind.

---

## Course Alignment & AP Framework

- **Course:** AP Cybersecurity (College Board CED)
- **Unit 1:** Introduction to Security
- **CED Topic:** **1.1 Understanding Social Engineering**
- **Course Framework Skills:**
  - **Skill 1.A:** Identify security concepts, attack vectors, and threat actors.
  - **Skill 2.B:** Explain how human behavior and cognitive biases impact security.
  - **Skill 3.A:** Propose security controls and mitigations based on scenario evidence.

### Learning Objectives & Essential Knowledge

| Objective ID | Learning Objective | Essential Knowledge Covered |
| :--- | :--- | :--- |
| **LO 1.1.A** | Identify and categorize social engineering tactics in communication scenarios. | **EK 1.1.A.1:** Social engineering exploits human trust, helpfulness, fear, urgency, and obedience to authority to bypass technical controls. |
| **LO 1.1.B** | Analyze psychological triggers used to compel victims to take unauthorized actions. | **EK 1.1.B.1:** Attackers use cognitive biases (urgency, scarcity, authority, social proof, familiarity) to force fast, emotional decisions before critical thinking occurs. |
| **LO 1.1.C** | Describe the technical and organizational consequences of social engineering attacks and justify safe countermeasures. | **EK 1.1.C.1:** Consequences include credential theft, malware deployment, unauthorized access, and financial loss. Countermeasures include out-of-band verification, multi-factor authentication (MFA), and zero-trust verification policies. |

---

## Learning Goals

By the end of this class, students will be able to:
1. **Annotate** a suspicious message across different delivery channels (email, text, phone call, physical media) and highlight at least two technical red flags and two psychological triggers.
2. **Distinguish** between widespread untargeted attacks (phishing) and highly tailored attacks (spear phishing / pretexting).
3. **Differentiate** between a legitimate communication and a deceptive communication without false positives.
4. **Formulate** a safe out-of-band response and explain how technical controls (MFA, principle of least privilege) mitigate human error.

---

## Lesson Plan & Pacing (50-Minute Standard Period)

| Time | Phase | Teacher & Student Activities | Deliverable |
| :--- | :--- | :--- | :--- |
| **00–05 min** | **Retrieval Warm-up** | Quick-write on [student_worksheet.md](student_worksheet.md): Why attack a person instead of the math behind encryption? | Warm-up responses |
| **05–15 min** | **Direct Instruction** | Presentation on the **6 Psychological Levers** and attack delivery channels. Walk through the Worked Example together. | Guided notes |
| **15–40 min** | **Hands-on Case Lab** | Students run `python investigate.py` to examine 6 case files, uncover hidden forensic headers, and analyze evidence. | Case Matrix on Worksheet |
| **40–48 min** | **Assessment Practice** | Complete the AP-style Free Response prompt based on an organizational scenario. | AP-style FRQ response |
| **48–50 min** | **Debrief & Wrap-up** | Share-out: What is the "Golden Rule" when an unexpected message demands urgent action? | Exit ticket takeaway |

---

## Core Instruction: How Attackers Hack the Human Brain

Computers follow rules; humans follow emotions. Attackers rely on **cognitive shortcuts**—heuristics that humans use to make quick decisions. When an attacker triggers strong emotion, our rational brain takes a backseat.

### The 6 Master Psychological Levers

```text
               THE ATTACKER'S TOOLKIT
               
    [ Urgency ]       "Your account will be deleted in 60 minutes!"
    [ Authority ]     "This is Principal Martinez / District IT."
    [ Fear ]          "You will be fined or suspended if you don't respond."
    [ Familiarity ]   "Hey Maya, great job at the robotics meet on Saturday!"
    [ Greed / Bait ]  "Free $100 Gift Card / Leaked Exam Answers inside."
    [ Helpfulness ]   "I'm from Tech Support, let me fix your slow Wi-Fi."
```

1. **Urgency & Time Pressure:** Creating a fake countdown or emergency. When people rush, they overlook obvious errors.
2. **Authority & Intimidation:** Posing as a boss, police officer, IT director, or government agent. People are conditioned to obey authority figures without questioning.
3. **Fear & Punishment:** Threatening legal action, grade drops, or public embarrassment.
4. **Familiarity & Liking:** Mentioning shared hobbies, school mascots, or real coworkers to create an illusion of trust.
5. **Scarcity & Greed (Baiting):** Offering exclusive rewards, prizes, or confidential gossip to tempt the victim.
6. **Helpfulness / Quid Pro Quo:** Offering a helpful service (e.g., "I'm calling to fix your computer") so the victim feels obligated to help in return.

---

### Social Engineering Attack Vectors

| Attack Vector | Channel | How it Operates |
| :--- | :--- | :--- |
| **Phishing** | Email (Mass) | Broad, generic email sent to thousands hoping a percentage click a fake link. |
| **Spear Phishing** | Email (Targeted) | Carefully researched attack targeting a specific person using personalized information (clubs, team names, projects). |
| **Whaling** | Email (Executive) | High-stakes spear phishing targeting CEOs, school superintendents, or CFOs to authorize massive wire transfers. |
| **Smishing** | SMS / Text Message | Text messages claiming a package delivery failed, a bank card was blocked, or an urgent boss request. |
| **Vishing** | Voice Call (Phone) | Live or AI-voiced phone calls impersonating IT support, credit card fraud departments, or family members in distress. |
| **Pretexting** | Any | Creating a fabricated backstory or scenario (the "pretext") to justify why the victim must disclose confidential data. |
| **Baiting** | Physical or Digital | Leaving an infected USB flash drive on a table or offering a free pirated game download containing a Trojan. |

---

## Worked Example: Annotating an Attack

Look at how an analyst deconstructs a deceptive message:

```text
From: "District IT Helpdesk" <support@district-he1pdesk.org>  <-- [RED FLAG 1: Typosquatting '1' for 'l']
To: student@lincolnhigh.edu
Date: October 2, 2026 08:14 UTC
Subject: ACCOUNT SUSPENDED IN 30 MINUTES                    <-- [LEVER: Extreme Urgency]

Dear User,                                                  <-- [RED FLAG 2: Generic Greeting]

Your school account was flagged for illegal activity.       <-- [LEVER: Fear & Authority]
To prevent your account and files from being erased,        <-- [LEVER: Threat of Permanent Loss]
log in immediately at:
http://lincoln-verify.secure-login-portal.net/auth          <-- [RED FLAG 3: External Unofficial URL]

Enter your current password and Student ID.                 <-- [OBJECTIVE: Credential Harvesting]

- District Tech Support
```

### The Safe Defense Protocol: Out-of-Band Verification
When you receive an unexpected message demanding urgent action or sensitive data:
1. **PAUSE:** Recognize the emotional trigger (urgency, panic, curiosity).
2. **DO NOT CLICK:** Never click links or open attachments in unsolicited messages.
3. **VERIFY OUT-OF-BAND:** Contact the sender using a **completely separate, verified communication channel** (e.g., walk up to the teacher, call the official main office phone number listed in the school handbook, or open your browser and manually type the known URL).

---

## Hands-on Lab: The Cyber Detective Case Files

Students investigate six active case files using the included terminal tool.

### Setup & Launch

```powershell
# 1. Navigate to the class directory
cd class_01_social_engineering

# 2. Run the investigation terminal
python investigate.py
```

### Student Workflow
1. Select a case file `[1–6]` to read the raw incoming communication.
2. Select `[1]` to run the **Forensic Header & Link Analysis** tool to reveal hidden sender data, lookalike domains, and concealed file extensions.
3. Select `[2]` to test your instincts with the **Mini Quiz**.
4. Record your evidence, psychological levers, technical consequences, and safe responses on the [Student Worksheet](student_worksheet.md).

---

## Concept Check & AP-Style Assessment

### Multiple-Choice Concept Checks

#### Question 1
An employee receives a text message: *"Your Amazon package #9482 could not be delivered due to an unpaid $1.50 customs fee. Update your card at http://track-pkg-fee.com within 2 hours or the package will be returned."* Which combination of attack vector and psychological lever is best demonstrated?
- (A) Spear phishing and familiarity
- (B) Smishing and urgency
- (C) Vishing and authority
- (D) Whaling and social proof

*Answer:* **(B)**. The communication is via SMS (smishing) and uses an artificial 2-hour deadline to create urgency.

#### Question 2
Why is spear phishing significantly more effective than traditional mass phishing?
- (A) Spear phishing emails bypass all mathematical spam filters automatically.
- (B) Spear phishing attacks target the hardware BIOS instead of operating systems.
- (C) Attackers conduct reconnaissance to incorporate realistic personal details that build false trust.
- (D) Spear phishing requires physical access to the victim's keyboard.

*Answer:* **(C)**. Spear phishing leverages tailored information gathered from social media or public school websites to make the pretext appear genuine.

---

### Free-Response Practice Prompt (Scoring Guide)

**Scenario:** Marcus, an accountant at a community medical clinic, receives an urgent email from `security-support@quick-alert-patch.com` directing him to download and run `Update_HIPAA_Patch.exe` before 5:00 PM to avoid a regulatory fine.

| Score Point | Scoring Criteria | Sample High-Scoring Response |
| :---: | :--- | :--- |
| **Part 1 (1 pt)** | Correctly identifies the attack type and psychological levers with scenario evidence. | *"The attack is **phishing (pretexting)** using **authority** (posing as security compliance) and **fear/urgency** (threat of a $10,000 regulatory fine and a 5:00 PM deadline)."* |
| **Part 2 (1 pt)** | Explains the specific technical harm of running the executable. | *"Running an `.exe` file from an untrusted external sender executes malicious code on Marcus's machine, potentially installing ransomware or a backdoor that gives the attacker direct access to confidential patient records."* |
| **Part 3 (1 pt)** | Proposes an organizational policy or technical control mitigating the risk. | *"The clinic should enforce a **software execution restriction policy / application allowlisting** so standard users cannot run unapproved `.exe` files, along with **mandatory out-of-band verification** requiring IT approval before any system update."* |

---

## Teacher & Facilitator Guidance

### Complete Case Key (for [scenarios.json](scenarios.json))

- **CASE-101 (Panicked Password Reset):** Phishing email. Sender `admin@district-he1pdesk.org` uses typosquatting (`1` for `l`). Goal: credential theft. Safe response: report to school IT; visit portal directly.
- **CASE-102 (Principal's Gift Cards):** Smishing / Impersonation. Classic business email compromise (BEC) adapted to school. Safe response: call main office or ask principal face-to-face.
- **CASE-103 (Robotics Team Invoice):** Spear phishing. Uses real club details. Attachment has double extension `.pdf.exe`. Goal: malware installation. Safe response: verify order with advisor; do not run file.
- **CASE-104 (Help Desk Vishing Call):** Vishing & MFA bypass. Caller asks for 6-digit phone code. Goal: bypass multi-factor authentication to hijack session. Safe response: never give MFA codes over the phone; hang up and call verified IT extension.
- **CASE-105 (Golden USB):** Baiting / Physical attack. Curiosity lever. Risk: Rubber Ducky keystroke injection or script execution. Safe response: hand directly to IT without plugging into any computer.
- **CASE-106 (Library Book Notice):** **Legitimate / Control Case.** Proper `@lincolnhigh.edu` domain, HTTPS portal link, personal student and barcode match, zero threats or password requests.

### Common Student Misconceptions

1. *"Only gullible or foolish people fall for social engineering."*  
   **Correction:** Modern spear phishing and vishing attacks are engineered by professional criminal groups who research their targets. Even top cybersecurity executives and tech companies have been compromised by well-crafted pretexting.
2. *"Antivirus software protects me from all phishing attacks."*  
   **Correction:** If an attacker tricks a user into typing their password into a fake Google or Microsoft login form, no malware was downloaded—antivirus software has nothing to block!
3. *"If the Caller ID says 'School District', it must be real."*  
   **Correction:** Caller ID numbers and display names are easily spoofed using cheap Voice-over-IP (VoIP) software.

### Extension Activities

- **The Phishing Audit:** Have students draft a mock phishing simulation email for their school and write a reflection on which psychological levers they chose and why.
- **The Parent Security Briefing:** Students take home the out-of-band verification checklist and interview a parent or guardian about a suspicious call or text they recently received.
- **AI-Assisted Pretexting Preview (Prep for Class 04):** Discuss how generative AI tools make it trivial for attackers to generate grammatically flawless spear phishing messages in seconds.

---

[⬅ Return to Course Roadmap](../README.md) | [Next Class 02: Investigate Suspicious Logins ➡](../README.md)
