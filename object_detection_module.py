import json
import os
from typing import List, Any, Dict
from data_generator import Datasimulator
from drone_telemetry import *
from security_events import *
class ObjectDetector:
    def detect_objects(self,frame: VideoFrame) -> List[Dict]:
        objects = []
        listed_objects = ["person","car","truck","dog","package"]
        description = frame.description.lower()
        for listed_object in listed_objects:
            if listed_object in description:
                objects.append({
                    "object": listed_object,
                    "confidence": 0.95
                })
        return objects

class EventAnalyzer:
    def analyze(self,frame: VideoFrame, telemetry: DroneTelemetry, detected_objects: List[Dict])->Optional[SecurityEvent]:
        timestamp = telemetry.timestamp
        location = telemetry.location
        event_id = f"event_{int(time.time())}_{hash(frame.description)%10000}"
        event_type = None
        objects_list = [obj.get("object") for obj in detected_objects]
        description = ""
        severity = "low"

        for obj in detected_objects:
            event_type = f"{obj["object"]} detected"
            description = f"{obj["object"]} spotted at {location}"
            severity = "Medium" #this should be decided by agent
        
        if event_type:
            return SecurityEvent(event_id=event_id,timestamp=timestamp,location=location,event_type=event_type,objects=objects_list,description=description,severity=severity)
        return None
   