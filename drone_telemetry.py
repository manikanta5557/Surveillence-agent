import json
import time
import datetime
from typing import Dict, Any, List, Optional
import sqlite3
import os


class DroneTelemetry:
    def __init__(self, timestamp: str, location:str, altitude: float, speed: float, battery: float):
        self.timestamp = timestamp
        self.location = location
        self.altitude = altitude
        self.speed = speed
        self.battery = battery
    def to_dict(self) -> Dict:
        return {
            "timestamp": self.timestamp,
            "location": self.location,
            "altitude": self.altitude,
            "speed": self.speed,
            "battery": self.battery
        }
    @classmethod
    def from_dict(cls,data: Dict)-> 'DroneTelemetry':
        return cls(
            timestamp = data["timestamp"],
            location = data["location"],
            altitude = data["altitude"],
            speed = data["speed"],
            battery = data["battery"]
        )

class VideoFrame:
    def __init__(self,frame_id:int,timestamp:str,description:str):
        self.frame_id = frame_id
        self.timestamp = timestamp
        self.description = description
    def to_dict(self):
        return {
            "frame_id": self.frame_id,
            "timestamp": self.timestamp,
            "description": self.description
        }
    @classmethod
    def from_dict(cls,data:Dict) -> 'VideoFrame':
        return cls(
            frame_id = data["frame_id"],
            timestamp = data["timestamp"],
            description = data["description"]
        )
    