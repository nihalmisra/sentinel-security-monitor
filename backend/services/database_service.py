
from database import SessionLocal
from models import SecurityEvent, SecurityAlert


def save_analysis(events, alerts):

    db = SessionLocal()

    try:
        # Save security events
        for event in events:
            db_event = SecurityEvent(**event)
            db.add(db_event)

        # Save security alerts
        for alert in alerts:
            db_alert = SecurityAlert(**alert)
            db.add(db_alert)

        db.commit()

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()
