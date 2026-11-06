
from services.detection_engine import detect_bruteforce

events = []

for i in range(7):
    events.append({
        "event": "Failed password",
        "ip_address": "192.168.1.20"
    })

events.append({
    "event": "Accepted password",
    "ip_address": "192.168.1.20"
})

alerts = detect_bruteforce(events)

for alert in alerts:
    print(alert)
