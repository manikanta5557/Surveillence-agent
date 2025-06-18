import json
import time
import datetime
from typing import Dict, List, Any, Optional
import sqlite3
import os
from drone_telemetry import VideoFrame,DroneTelemetry

class Datasimulator:
    def __init__(self):
        self.locations = ["Main Gate","Garage","Backyard","Perimeter","Front Door"]
        self.objects = ["person","car","truck","dog","package"]
    def generate_video_frames(self, num_frames:int) -> List[VideoFrame]:
        frames = []
        for i in range(num_frames):
            timestamp = datetime.datetime.now() + datetime.timedelta(minutes=i)
            timestamp_str = timestamp.strftime("%Y-%m-%d %H:%M:%S")
            location  = self.locations[i%len(self.locations)]
            #lets say for every 3rd frame we detect an object
            object = self.objects[i%len(self.locations)]
            description = f"Frame {i}: {object} is at {location}"
            frames.append(VideoFrame(i,timestamp_str,description))
        return frames
    def generate_telemetry_data(self,num_records:int)-> List[DroneTelemetry]:
        telemetry_records = []
        for i in range(num_records):
            timestamp = datetime.datetime.now() + datetime.timedelta(minutes=i)
            timestamp_str = timestamp.strftime("%Y-%m-%d %H:%M:%S")

            location = self.locations[i%len(self.locations)]
            altitude = 10.0 + (i%5) 
            speed = 15.0 + (i%5)
            battery = 100 - (i%20)
            telemetry_records.append(DroneTelemetry(timestamp_str,location,altitude,speed,battery))
        return telemetry_records
