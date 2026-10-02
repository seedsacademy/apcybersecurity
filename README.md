# AP Cybersecurity Exam Preparation

This project is for developing lessons and practice materials to help students prepare for the AP Cybersecurity exam.

## Topic Map

The College Board course framework is organized into five units. Use the official [Course and Exam Description](https://apcentral.collegeboard.org/media/pdf/ap-cybersecurity-course-and-exam-description.pdf) for the required content and sequence. This topic map is a planning overview, not a replacement for the framework.

1. **Cybersecurity foundations**: assets, threats, vulnerabilities, risk, likelihood and impact, and defense in depth.
2. **Physical security**: protecting spaces, equipment, and devices from unauthorized access or damage.
3. **Network security**: network risks and attacks, monitoring, and controls such as firewall rules.
4. **Device and application security**: secure configurations, policies, file permissions, authentication, and hardening.
5. **Data security**: protecting information, managing access, and preserving confidentiality, integrity, and availability.
6. **Attacks and vulnerabilities**: how adversaries exploit weaknesses and how to recognize signs of compromise.
7. **Mitigation and detection**: choosing layered controls, monitoring systems, tracing events through logs, and classifying attacks.
8. **Security practice**: documenting risk and mitigations, collaborating on cybersecurity tasks, and using AI appropriately.

## Log Tracing and Analysis with pandas

Students will practice both producing useful logs and analyzing them. Use a local lab or synthetic events so no real account credentials, personal information, or production logs are exposed.

1. **Create events**: perform safe, controlled actions in a lab or generate sample events, such as successful and failed logins, file access, and firewall allow/deny decisions.
2. **Design the log format**: record consistent fields such as timestamp, event type, user or test account, source IP, action, and outcome. Export structured records as CSV or JSON.
3. **Load and prepare data**: use Python and `pandas` to read the files, parse timestamps, handle missing or inconsistent values, and sort events chronologically.
4. **Trace activity**: filter by account, address, time range, or event type; group related events; and build a timeline across system, application, and firewall logs.
5. **Investigate patterns**: look for repeated failed logins, unexpected access, unusual event sequences, or changes in activity. Compare observations with the lab scenario and identify alternative explanations.
6. **Report evidence**: explain which log entries support a conclusion, what remains uncertain, and which mitigation or additional evidence would help.

Students should treat patterns as leads for investigation, not proof by themselves. They should also consider log timestamps, time zones, missing records, and false positives.

## Exercises

Exercise materials, datasets, scripts, and dependencies are organized by folder. Start with [Exercise 1: Trace Login and Firewall Events](sample_1/README.md).

## Recurring Skills

Students apply these three skill categories throughout the course:

- **Analyze risk** to organizational assets.
- **Mitigate risk** with protective and deterrent controls.
- **Detect attacks** by monitoring systems and analyzing evidence.

Collaboration is also part of the course skills.

## Exam Snapshot

The AP Cybersecurity exam is fully digital and includes:

- **Multiple choice**: 60 questions, 80 minutes, 70% of the exam score.
- **Free response**: one question, 50 minutes, 30% of the exam score. Students work with evidence such as firewall rules, system and application logs, file permissions, and a device policy.

## Official Resources

- [AP Cybersecurity course page](https://apcentral.collegeboard.org/courses/ap-cybersecurity)
- [Course and Exam Description](https://apcentral.collegeboard.org/media/pdf/ap-cybersecurity-course-and-exam-description.pdf)
- [Exam information](https://apcentral.collegeboard.org/courses/ap-cybersecurity/exam)
