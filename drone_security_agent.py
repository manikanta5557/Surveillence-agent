import json
import os
import datetime
import time
from typing import Any, Optional, List, Dict
from drone_telemetry import DroneTelemetry, VideoFrame
from data_generator import Datasimulator 
from object_detection_module import ObjectDetector, EventAnalyzer
from rules_definer import RuleEngine
from security_events import SecurityAlert, SecurityEvent

class DroneSecurityAgent:
    def __init__(self):
        self.simulator = Datasimulator()
        self.object_detector = ObjectDetector()
        self.event_analyzer = EventAnalyzer()
        self.rule_engine = RuleEngine()
    
    def process_frame(self,frame: VideoFrame, telemetry: DroneTelemetry):
        detected_objects = self.object_detector.detect_objects(frame)
        event = self.event_analyzer.analyze(frame, telemetry, detected_objects)
        if event:
            alert = self.rule_engine.evaluate(event)
            print(f"Event logged: {event.description}")
            if alert:
                print(f"ALERT: {alert.description} (Severity: {alert.severity})")
    def run_simulation(self,num_frames:int):
        print("Start Drone Security Analyst simulation")
        video_frames = self.simulator.generate_video_frames(num_frames)
        telemetry_data = self.simulator.generate_telemetry_data(num_frames)
        for i in range(num_frames):
            print(f"\nProcessing frame {i+1}/{num_frames}")
            self.process_frame(video_frames[i],telemetry_data[i])
            time.sleep(0.5)
        print("\nSimulation complete!")
    

if __name__ == "__main__":
    agent = DroneSecurityAgent()
    agent.run_simulation(20)
