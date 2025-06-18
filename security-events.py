import json
import os
import time
import datetime
from typing import Dict, List, Any, Optional
import sqlite3

class SecurityEvent:
    def __init__(self,event_id:str,timestamp:str,location:str,event_type:str,objects: List[str],description: str, severity: str):
        self.event_id = event_id
        self.timestamp = timestamp
        self.location = location
        self.event_type = event_type
        self.objects = objects
        self.description = description
        self.severity = severity
    
    def to_dict(self) -> Dict:
        return {
            "event_id":self.event_id,
            "timestamp":self.timestamp,
            "location":self.location,
            "event_type":self.event_type,
            "objects":self.objects,
            "description":self.description,
            "severity" : self.severity
        }
    @classmethod
    def from_dict(cls,data: Dict) -> 'SecurityEvent':
        return cls(
            event_id = data["event_id"],
            timestamp = data["timestamp"],
            location = data["location"],
            event_type = data["event_type"],
            objects = data["objects"],
            description = data["description"],
            severity = data["severity"]
        )

class SecurityAlert:
    def __init__(self,alert_id:str,timestamp:str,location:str,alert_type:str,description: str, severity: str,related_event_id: str):
        self.alert_id = alert_id
        self.timestamp = timestamp
        self.location = location
        self.alert_type = alert_type
        self.description = description
        self.severity = severity
        self.related_event_id = related_event_id
    
    def to_dict(self) -> Dict:
        return {
            "alert_id":self.alert_id,
            "timestamp":self.timestamp,
            "location":self.location,
            "alert_type":self.alert_type,
            "description":self.description,
            "severity" : self.severity,
            "related_event_id": self.related_event_id
        }
    @classmethod
    def from_dict(cls,data: Dict) -> 'SecurityAlert':
        return cls(
            alert_id = data["alert_id"],
            timestamp = data["timestamp"],
            location = data["location"],
            alert_type = data["alert_type"],
            description = data["description"],
            severity = data["severity"],
            related_event_id = data["releated_event_id"]
        )

