import json
import time
import datetime
from typing import Dict, List, Any, Optional
import sqlite3
import os

class Datasimulator:
    def __init__(self):
        self.locations = ["Main Gate","Garage","Backyard","Perimeter","Front Door"]
        self.objects = ["person","car","truck","dog","package"]
    