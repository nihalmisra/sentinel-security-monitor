
from collections import defaultdict

def detect_bruteforce(events, threshold=5):

    failed_attempts = defaultdict(int)

    for event in events:
        if event["event"] == "Failed password":
            ip = event["ip_address"]
            failed_attempts[ip] += 1

    alerts = []

    for ip, count in failed_attempts.items():
        if count >= threshold:
            alerts.append({
                "type": "Brute Force Attempt",
                "ip_address": ip,
                "failed_attempts": count,
                "severity": "HIGH"
            })

    return alerts
