import json
import os
from typing import List, Any, Dict
from data_generator import Datasimulator
from drone_telemetry import *
from security_events import *
from ultralytics import YOLO
import cv2
#lets manipulate the ObjectDetector class and return the object:
class ObjectDetector:
    def __init__(self):
        self.model = YOLO('yolov8s.pt')
    def detect_objects(self,frame: VideoFrame) -> List[Dict]:
        cap = cv2.VideoCapture(0)
        ret,frame_1 = cap.read()
        names = {0: 'person', 1: 'bicycle', 2: 'car', 3: 'motorcycle', 4: 'airplane', 5: 'bus', 6: 'train', 7: 'truck', 8: 'boat', 9: 'traffic light', 10: 'fire hydrant', 11: 'stop sign', 12: 'parking meter', 13: 'bench', 14: 'bird', 15: 'cat', 16: 'dog', 17: 'horse', 18: 'sheep', 19: 'cow', 20: 'elephant', 21: 'bear', 22: 'zebra', 23: 'giraffe', 24: 'backpack', 25: 'umbrella', 26: 'handbag', 27: 'tie', 28: 'suitcase', 29: 'frisbee', 30: 'skis', 31: 'snowboard', 32: 'sports ball', 33: 'kite', 34: 'baseball bat', 35: 'baseball glove', 36: 'skateboard', 37: 'surfboard', 38: 'tennis racket', 39: 'bottle', 40: 'wine glass', 41: 'cup', 42: 'fork', 43: 'knife', 44: 'spoon', 45: 'bowl', 46: 'banana', 47: 'apple', 48: 'sandwich', 49: 'orange', 50: 'broccoli', 51: 'carrot', 52: 'hot dog', 53: 'pizza', 54: 'donut', 55: 'cake', 56: 'chair', 57: 'couch', 58: 'potted plant', 59: 'bed', 60: 'dining table', 61: 'toilet', 62: 'tv', 63: 'laptop', 64: 'mouse', 65: 'remote', 66: 'keyboard', 67: 'cell phone', 68: 'microwave', 69: 'oven', 70: 'toaster', 71: 'sink', 72: 'refrigerator', 73: 'book', 74: 'clock', 75: 'vase', 76: 'scissors', 77: 'teddy bear', 78: 'hair drier', 79: 'toothbrush'}
        outputs  = self.model(frame_1)
        output_classes = [names[int(x)] for x in outputs[0].boxes.cls]
        objects = []
        description = frame.description.lower()
        for output_class in output_classes:
            if output_class in description:
                objects.append({
                    #lets also add co-ordinates of object.
                    "object" : output_class,
                    "confidence":0.95
                })
        cap.release()
        # listed_objects = ["person","car","truck","dog","package"]
        # description = frame.description.lower()
        # for listed_object in listed_objects:
        #     if listed_object in description:
        #         objects.append({
        #             "object": listed_object,
        #             "confidence": 0.95
        #         })
        print(objects)
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
   