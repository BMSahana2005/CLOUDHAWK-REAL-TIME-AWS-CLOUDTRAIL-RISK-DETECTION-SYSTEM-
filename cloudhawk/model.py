from aws_fetch import fetch_logs
from datetime import datetime, timedelta


def run_pipeline():
    logs = fetch_logs()
    results = []

    for record in logs:
        event = record.get("eventName")
        event_time = record.get("eventTime")

        if not event or not event_time:
            continue

        # 🔥 FILTER ONLY LAST 15 MINUTES
        try:
            event_dt = datetime.strptime(event_time, "%Y-%m-%dT%H:%M:%SZ")
            if event_dt < datetime.utcnow() - timedelta(minutes=15):
                continue
        except:
            continue

        user = record.get("userIdentity", {}).get("userName") \
            or record.get("userIdentity", {}).get("type", "Unknown")
        ip = record.get("sourceIPAddress", "N/A")
        region = record.get("awsRegion", "N/A")

        # 🔥 DETECTION RULES
        if event == "RunInstances":
            risk = "HIGH"
            label = "EC2 Instance Created"

        elif event == "TerminateInstances":
            risk = "CRITICAL"
            label = "EC2 Instance Terminated"

        elif event == "StopInstances":
            risk = "MEDIUM"
            label = "EC2 Instance Stopped"

        elif event == "StartInstances":
            risk = "MEDIUM"
            label = "EC2 Instance Started"

        elif event == "DeleteBucket":
            risk = "CRITICAL"
            label = "S3 Bucket Deleted"

        elif event == "CreateBucket":
            risk = "HIGH"
            label = "S3 Bucket Created"

        elif event == "StopLogging":
            risk = "CRITICAL"
            label = "CloudTrail Logging Stopped"

        elif event == "DeleteTrail":
            risk = "CRITICAL"
            label = "CloudTrail Deleted"

        elif event == "CreateUser":
            risk = "HIGH"
            label = "IAM User Created"

        elif event == "AttachUserPolicy":
            risk = "HIGH"
            label = "Privilege Escalation"

        elif event == "AuthorizeSecurityGroupIngress":
            risk = "HIGH"
            label = "Security Group Rule Changed"

        else:
            continue

        results.append({
            "event": event,
            "label": label,
            "user": user,
            "ip": ip,
            "time": event_time,
            "region": region,
            "risk": risk
        })

    print(f"🚨 Alerts detected: {len(results)}")
    return results