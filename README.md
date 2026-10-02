# AP Cybersecurity Class Design

This repository is a workspace for developing separate lessons, hands-on activities, datasets, and assessments for AP Cybersecurity. The goal is to cover all required course topics and prepare students for the class and AP exam through practice and explanations supported by evidence.

## Course plan

The roadmap follows the five units in the [College Board Course and Exam Description (CED), effective Fall 2026](https://apcentral.collegeboard.org/media/pdf/ap-cybersecurity-course-and-exam-description.pdf). CED references identify official topics; the class titles, activities, and deliverables are our proposed lesson design.

Each row is a separate class topic to develop. A topic may take multiple meetings for instruction, practice, and assessment. This is a course roadmap, not a plan to complete the full course in 30 periods. Adjust pacing to the schedule and student needs.

**Existing lesson:** [Data Analysis: Trace Login and Firewall Events](sample_1/README.md). All other classes below are planned.

## Separate class topics

### Unit 1: Introduction to Security

| Class | Class topic | CED topic | Activity and student deliverable |
| --- | --- | --- | --- |
| 01 | Recognize social engineering | 1.1 | Annotate fictional messages; explain the tactic, consequence, and safe response. |
| 02 | Investigate suspicious logins | 1.2 | Compare login histories and recommend account protections. |
| 03 | Make decisions on public Wi-Fi | 1.3 | Evaluate a travel scenario and create a connection checklist. |
| 04 | Recognize AI-assisted deception | 1.4 | Evaluate an impersonation request and design independent verification. |
| 05 | Evaluate AI for defense | 1.5 | Check an AI-generated explanation against evidence and correct unsupported claims. |

### Unit 2: Securing Spaces

| Class | Class topic | CED topic | Activity and student deliverable |
| --- | --- | --- | --- |
| 06 | Build a security risk assessment | 2.1 | Inventory assets, explain confidentiality/integrity/availability needs, rank risks, and document responses. |
| 07 | Find physical weaknesses | 2.2 | Annotate a floor plan with entry routes, exposed equipment, and consequences. |
| 08 | Design layered physical protection | 2.3 | Revise a floor plan with controls and justify operational tradeoffs. |
| 09 | Investigate physical access events | 2.4 | Correlate synthetic badge, visitor, and alarm records into a timeline. |

### Unit 3: Securing Networks

| Class | Class topic | CED topic | Activity and student deliverable |
| --- | --- | --- | --- |
| 10 | Read a network and identify attack paths | 3.1 | Label addresses, ports, protocols, and services on a diagram; explain weaknesses. |
| 11 | Plan network policy and wireless protection | 3.2 | Review a guest-network configuration and propose policy and configuration changes. |
| 12 | Separate networks by purpose | 3.3 | Design student, staff, guest, and server segments with a required communication table. |
| 13 | Read and revise firewall rules | 3.4 | Predict traffic outcomes, repair an ordered ruleset, and explain edits. |
| 14 | Detect suspicious network activity | 3.5 | Compare baseline traffic with alerts; identify leads and possible false positives. |
| 15 | Analyze data with Python and pandas — existing | 1.2, 3.5, 4.4, 5.6 | Use [sample_1](sample_1/README.md) to summarize 2,000 synthetic events and build an investigation timeline. |

### Unit 4: Securing Devices

| Class | Class topic | CED topic | Activity and student deliverable |
| --- | --- | --- | --- |
| 16 | Assess device exposure | 4.1 | Review a workstation inventory and configuration; prioritize weaknesses and explain potential damage. |
| 17 | Design authentication and account controls | 4.2 | Compare authentication options and propose an account policy for several roles. |
| 18 | Harden a workstation | 4.3 | Apply a local-lab checklist and document changes, validation, and remaining risks. |
| 19 | Trace device activity | 4.4 | Correlate operating-system events, process activity, and alerts into an incident hypothesis. |

### Unit 5: Securing Applications and Data

| Class | Class topic | CED topic | Activity and student deliverable |
| --- | --- | --- | --- |
| 20 | Explain application attack paths | 5.1 | Analyze fictional input-handling examples involving injection, cross-site scripting, and buffer overflow. |
| 21 | Set data policy and file permissions | 5.2 | Classify sample files, assign role-based access, and justify permissions. |
| 22 | Protect stored data | 5.3 | Compare hashing and encryption; demonstrate integrity checking and symmetric encryption in a local lab. |
| 23 | Use public and private keys | 5.4 | Diagram a secure exchange and test with disposable keys; explain signatures and key protection. |
| 24 | Improve application defenses | 5.5 | Review an application configuration and input workflow; propose fixes and verification steps. |
| 25 | Investigate application and data events | 5.6 | Compare application logs and file-access records; identify suspicious sequences and missing context. |

### Integration and exam preparation

| Class | Class topic | Activity and student deliverable |
| --- | --- | --- |
| 26 | Team security assessment | Assign roles and assess a fictional organization across all five units; submit a risk register and mitigation plan. |
| 27 | Investigate one device using multiple sources | Combine a policy, firewall rules, permissions, and system/application logs; submit an investigation and hardening plan. |
| 28 | Multiple-choice practice | Complete mixed concept and evidence questions; explain answers and why alternatives fail. |
| 29 | Timed free-response practice | Complete a device investigation in 50 minutes and review using official sample scoring guidance. |
| 30 | Full practice exam and targeted review | Schedule full exam timing across suitable meetings; use errors to select topics for reteaching and another attempt. |

## Existing data analysis lesson

[Exercise 1: Trace Login and Firewall Events](sample_1/README.md) includes a dataset, generator, pandas analyzer, student tasks, and facilitator self-check.

Suggested teaching sequence:

1. **Read the evidence:** identify CSV fields, timestamp format, and missing context.
2. **Prepare and summarize:** load data, parse timestamps, sort events, and compare counts by event type, outcome, account, and source address.
3. **Investigate:** filter repeated failures and firewall denials; trace related activity chronologically.
4. **Explain:** cite event IDs and timestamps, consider a benign explanation, request more evidence, and recommend a mitigation with its tradeoff.

Students submit a short report with their queries or code and supporting results. Patterns are investigation leads; a successful login after failures does not establish compromise by itself.

Revisit this lesson with new questions as students learn device and application security. Dedicated lessons and a complete exam evidence packet are still needed.

## Standard design for each class

Each lesson should contain:

- **Alignment:** CED topic IDs, learning objectives, and essential knowledge statements covered.
- **Learning goal:** an action students should be able to perform and explain.
- **Preparation:** prerequisites, materials, setup, and duration.
- **Instruction:** a brief explanation and worked example.
- **Practice:** a scenario or lab with tasks and a student deliverable.
- **Assessment:** a concept check and an evidence-based explanation prompt.
- **Teacher notes:** answer guidance, misconceptions, and extensions.

A starting structure for a 50-minute meeting is 5 minutes of retrieval practice, 10 minutes of instruction, 25 minutes of activity, and 10 minutes of discussion and assessment. Split longer lessons across meetings.

Use a separate folder per new class, such as class_13_firewall_rules/, containing a README, activity files, and teacher guidance. Keep the existing data analysis lesson in sample_1/.

## Coverage and recurring skills

The roadmap includes every official topic ID: 1.1–1.5, 2.1–2.4, 3.1–3.5, 4.1–4.4, and 5.1–5.6. Before marking a lesson ready, map tasks and assessments to relevant CED learning objectives and essential knowledge. A topic title alone does not establish full coverage.

Track objectives as **planned**, **taught**, **practiced**, or **assessed**, with links to materials and student evidence. Review gaps after each unit and add instruction or practice as needed.

Students repeatedly analyze risk, select and implement mitigations, detect attacks from evidence, and collaborate. Include shared team objectives, assigned responsibilities, documented work, and verification of AI-assisted output. These skill categories come from the [official course framework](https://apcentral.collegeboard.org/courses/ap-cybersecurity).

Use synthetic data and authorized local labs. Record changes and verification results so students can explain what they did and why.

## Exam preparation targets

The [official exam information](https://apcentral.collegeboard.org/courses/ap-cybersecurity/exam) specifies a fully digital exam in Bluebook:

| Section | Format | Time | Score weight |
| --- | --- | --- | --- |
| Multiple choice | 60 questions | 80 minutes | 70% |
| Free response | 1 question | 50 minutes | 30% |

Free-response evidence includes firewall rules, system and application logs, file permissions, and a device policy for the same device. Students practice explaining policy, detecting attacks, revising rules and permissions, and recommending hardening changes. Class 27 combines these sources; the pandas lesson supplies only part of this preparation.

Include short exam-style prompts throughout the course, then use Classes 28–30 for timed practice and review.

## Official resources

- [AP Cybersecurity course page](https://apcentral.collegeboard.org/courses/ap-cybersecurity)
- [Course and Exam Description](https://apcentral.collegeboard.org/media/pdf/ap-cybersecurity-course-and-exam-description.pdf)
- [Exam information](https://apcentral.collegeboard.org/courses/ap-cybersecurity/exam)

Alignment and exam format checked October 2, 2026. Review subsequent College Board clarifications before finalizing lessons.
