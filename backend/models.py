
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from database import Base


# Table 1: Security Events
class SecurityEvent(Base):
    __tablename__ = "security_events"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(String)
    hostname = Column(String)
    process_id = Column(String)
    event = Column(String)
    username = Column(String)
    ip_address = Column(String)


# Table 2: Security Alerts
class SecurityAlert(Base):
    __tablename__ = "security_alerts"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)
    ip_address = Column(String)
    failed_attempts = Column(Integer)
    severity = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
