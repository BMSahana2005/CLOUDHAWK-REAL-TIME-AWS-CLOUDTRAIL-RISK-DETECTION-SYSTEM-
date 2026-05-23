# CLOUDHAWK REAL-TIME AWS CLOUDTRAIL RISK DETECTION SYSTEM

## Overview

CloudHawk Enhanced is a cloud security monitoring and threat detection platform developed using Python, Flask, AWS CloudTrail, and Amazon S3. The project acts as a lightweight SIEM-like solution that continuously monitors AWS infrastructure activities by collecting and analyzing CloudTrail logs stored in S3 buckets.

The system uses a rule-based detection engine to identify suspicious and security-critical activities such as:

* S3 bucket deletion
* IAM privilege escalation
* CloudTrail tampering
* Security group modifications
* Unauthorized access attempts

The platform classifies events into multiple severity levels including:

* Critical
* High
* Medium
* Low

It also generates human-readable security narratives for easier incident investigation and analysis.

A real-time Flask dashboard provides centralized visibility into AWS cloud activities, enabling efficient threat monitoring, security auditing, and incident response.

This project demonstrates practical implementation of:

* Cloud Security Monitoring
* AWS Log Analysis
* Threat Detection Engineering
* SOC Monitoring Concepts
* DevSecOps Practices

---

# Features

* Real-time AWS CloudTrail log monitoring
* Rule-based threat detection engine
* Severity-based alert classification
* Human-readable incident narratives
* Flask-based monitoring dashboard
* AWS S3 integration for log collection
* Security event analysis and auditing
* Lightweight SIEM-inspired architecture

---

# Technologies Used

| Technology     | Purpose                      |
| -------------- | ---------------------------- |
| Python         | Core backend logic           |
| Flask          | Web dashboard and API        |
| AWS CloudTrail | Cloud activity logging       |
| Amazon S3      | Log storage                  |
| HTML/CSS       | Frontend dashboard           |
| JSON           | Log data storage and parsing |

---

# Project Structure

```bash
cloudhawk/
│
├── app.py                  # Main Flask application
├── aws_fetch.py            # Fetches AWS CloudTrail logs from S3
├── model.py                # Threat detection and analysis engine
├── requirements.txt        # Project dependencies
│
├── data/
│   └── logs.json           # Sample CloudTrail logs
│
├── templates/
│   └── index.html          # Dashboard frontend
│
└── __pycache__/            # Python cache files
```

---

# Installation

## Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/cloudhawk-enhanced.git
cd cloudhawk-enhanced
```

---

## Step 2: Create Virtual Environment

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

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

```bash
python app.py
```

After running the application, open:

```bash
http://127.0.0.1:5000
```

---

# Detection Capabilities

The system can detect multiple suspicious AWS activities including:

| Threat Type                 | Severity |
| --------------------------- | -------- |
| S3 Bucket Deletion          | Critical |
| IAM Policy Changes          | High     |
| CloudTrail Disabled         | Critical |
| Security Group Modification | Medium   |
| Unauthorized Login Attempts | High     |

---

# Sample Workflow

1. AWS CloudTrail generates activity logs.
2. Logs are stored inside Amazon S3.
3. CloudHawk Enhanced fetches logs periodically.
4. The detection engine analyzes suspicious events.
5. Alerts are categorized by severity.
6. Results are displayed on the Flask dashboard.

---

#Future Improvements

* Machine Learning-based anomaly detection
* Real-time alerts using Email/SMS notifications
* Multi-cloud support for Azure and GCP

---

# Learning Outcomes

This project helped in understanding:

* AWS Cloud Security
* CloudTrail log monitoring
* Threat detection engineering
* Flask web development
* Security Operations Center (SOC) workflows
* DevSecOps concepts

---

# Requirements

Install all dependencies using:

```bash
pip install -r requirements.txt
```

Main libraries used:

```txt
Flask
boto3
```

---

# GitHub Upload Steps

## Initialize Git

```bash
git init
```

## Add Files

```bash
git add .
```

## Commit Files

```bash
git commit -m "Initial commit - CloudHawk Enhanced"
```

## Create GitHub Repository

1. Open GitHub
2. Click on "New Repository"
3. Repository Name: `cloudhawk-enhanced`
4. Click "Create Repository"

---

## Connect Local Project to GitHub

```bash
git remote add origin https://github.com/your-username/cloudhawk-enhanced.git
```

---

## Push Project to GitHub

```bash
git branch -M main
git push -u origin main
```

---

# Suggested .gitignore

Create a `.gitignore` file and add:

```gitignore
venv/
__pycache__/
*.pyc
.env
```

---

# Author

Developed as a cloud security and threat detection project using AWS services and Python.

---

# License

This project is developed for educational and learning purposes.
