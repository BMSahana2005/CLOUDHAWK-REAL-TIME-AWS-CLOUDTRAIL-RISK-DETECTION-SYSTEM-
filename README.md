# ☁️ CloudHawk
### Real-Time AWS Cloud Security Monitoring & Threat Detection

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)
![AWS](https://img.shields.io/badge/AWS-CloudTrail-orange?logo=amazonaws)
![Amazon S3](https://img.shields.io/badge/Amazon-S3-red?logo=amazons3)
![License](https://img.shields.io/badge/License-Educational-green)

CloudHawk is a lightweight cloud security monitoring system that continuously analyzes **AWS CloudTrail** logs to identify suspicious cloud activities in near real time. Built using **Python**, **Flask**, **Boto3**, and **Amazon S3**, the system converts raw AWS audit logs into actionable security insights through a centralized web dashboard.

The project demonstrates practical cloud security monitoring by detecting critical events such as unauthorized IAM user creation, privilege escalation, CloudTrail tampering, and resource termination using a rule-based detection engine.

---

# 📌 Features

- Real-time AWS CloudTrail log monitoring
- Automated log retrieval from Amazon S3
- Rule-based threat detection
- Threat severity classification
- Live Flask monitoring dashboard
- Detailed event logging
- Continuous background monitoring
- Lightweight and scalable architecture

---

# 🏗️ System Architecture

```
                AWS Cloud Environment
                         │
                         ▼
                 AWS CloudTrail Logs
                         │
                         ▼
                    Amazon S3 Bucket
                         │
                         ▼
                  Boto3 Log Collector
                         │
                         ▼
               Log Processing Engine
                         │
                         ▼
             Rule-Based Threat Detection
                         │
                         ▼
               Flask Web Dashboard
                         │
                         ▼
                    Security Analyst
```

---

# 🚀 Technologies Used

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| Web Framework | Flask |
| Cloud Platform | AWS |
| Cloud Logging | AWS CloudTrail |
| Cloud Storage | Amazon S3 |
| AWS SDK | Boto3 |
| Frontend | HTML5, CSS3 |
| Data Format | JSON |
| Detection Engine | Rule-Based Security Analysis |
| Background Processing | Python Multithreading |

---

# 📂 Project Structure

```bash
CloudHawk/
│
├── app.py                     # Main Flask application
├── aws_fetch.py               # Retrieves CloudTrail logs
├── detector.py                # Rule-based detection engine
├── requirements.txt
│
├── data/
│   └── logs.json
│
├── templates/
│   └── index.html
│
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/cloudhawk.git

cd cloudhawk
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

# 🔍 Threat Detection Capabilities

CloudHawk continuously monitors CloudTrail logs and detects events including:

| Threat | Description |
|---------|-------------|
| IAM User Creation | Detects unauthorized IAM account creation |
| Privilege Escalation | Identifies suspicious permission changes |
| CloudTrail Tampering | Detects attempts to disable logging |
| Resource Termination | Monitors deletion of critical AWS resources |
| Security Group Changes | Detects potentially risky firewall modifications |
| Root Account Activity | Flags sensitive root user operations |

---

# 🔄 Workflow

1. AWS CloudTrail records cloud activities.
2. Logs are stored in Amazon S3.
3. CloudHawk periodically retrieves the latest logs.
4. Log files are decompressed and parsed.
5. Rule-based detection analyzes security events.
6. Threats are classified by severity.
7. Results are displayed on the web dashboard.
8. Monitoring repeats automatically every five minutes.

---

# 📸 Dashboard

Add screenshots here after deployment.

```
dashboard-home.png

threat-analysis.png

event-logs.png
```

---

# 🌟 Key Highlights

- Near real-time cloud monitoring
- Automated threat analysis
- Lightweight architecture
- Continuous background monitoring
- Easy-to-use security dashboard
- AWS native integration
- Scalable monitoring solution

---

# 📚 Learning Outcomes

This project helped strengthen practical knowledge of:

- AWS Cloud Security
- AWS CloudTrail
- Amazon S3
- Python Automation
- Flask Web Development
- Cloud Log Analysis
- Threat Detection Engineering
- Security Monitoring
- DevSecOps Fundamentals

---

# 🔮 Future Enhancements

- Email and SMS alert integration
- Slack and Microsoft Teams notifications
- Support for Azure and Google Cloud
- Advanced threat scoring
- Interactive analytics dashboard
- Containerized deployment using Docker
- Kubernetes deployment
- SIEM integration

---

# 📦 Requirements

```txt
Python 3.10+

Flask

boto3
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🤝 Contributing

Contributions, issues, and feature requests are welcome.

Feel free to fork the repository and submit pull requests.

---

# 👨‍💻 Author

**Your Name**

Bachelor of Technology (Computer Science & Engineering – Cybersecurity)

Cloud Security • DevSecOps • Python • AWS

---

# 📄 License

This project is developed for educational and learning purposes.
