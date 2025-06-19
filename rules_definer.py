import json
import os
import datetime
import time
from typing import List, Dict, Any, Optional
from drone_telemetry import DroneTelemetry,VideoFrame
from data_generator import Datasimulator
from security_events import SecurityAlert,SecurityEvent

class RuleEngine:
    def __init__(self):
        self.rules = [
            {
                "name" : "loitering_at_night",
                "conditions" : {
                    "event_type": "suspicious_activity",
                    "time_range": ["22:00","06:00"],
                    "objects": ["person"],
                    "actions": ["loitering"]
                },
                "alert_type": "security_threat",
                "severity" : "high",
                "message": "Person loitering at {location} during nighttime ({timestamp})"
            },
            {
                "name":"unknown_vehicle",
                "conditions":{
                    "event_type":"vehicle_detected",
                    "time_range":["all"],
                    "location":["Main Gate","Garage"]
                },
                "alert_type": "security_notice",
                "severity":"medium",
                "message": "{description}"
            },
            {
                "name": "running_person",
                "conditions":{
                    "event_type":"suspicious_activity",
                    "objects":["person"],
                    "actions": ["running"]
                },
                "alert_type":"security_notice",
                "severity":"medium",
                "message":"Person running detected at {location}"
            }
        ]
    def evaluate(self,event: SecurityEvent) -> Optional[SecurityAlert]:
        event_time = datetime.datetime.strptime(event.timestamp, "%Y-%m-%d %H:%M:%S").time()
        for rule in self.rules:
            match = True
            #check event type
            if rule["conditions"].get("event_type") and rule["conditions"]["event_type"] != event.event_type:
                match = False
                continue
            #check time ranges
            #check location if specified
            if rule["conditions"].get("location") and event.location not in rule["conditions"]["location"]:
                match = False
                continue
            
            #if all conditions match, generate an alert
            if match:
                alert_id = f"alert_{int(time.time())}_{hash(event.description)%10000}"
                #format the alert message
                message = rule["message"].format(
                    location = event.location,
                    timestamp = event.timestamp,
                    description = event.description
                )
                return SecurityAlert(
                    alert_id=alert_id,
                    timestamp=event.timestamp,
                    location=event.location,
                    alert_type= rule["alert_type"],
                    description=message,
                    severity=rule["severity"],
                    related_event_id=event.event_id
                )
        return None
            
            
