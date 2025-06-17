# Drone Security Analyst Agent

## Overview
The Drone Security Analyst Agent is a prototype system designed to process telemetry data and video feed from a docked drone monitoring a fixed property. The agent analyzes the data in real-time to detect security events, generate alerts, and provide a searchable database of detected objects and activities.

## Features
- Processing of simulated drone telemetry data and video frames
- Object detection and identification from video content
- Event analysis and contextual logging
- Real-time security alerts based on predefined rules
- Frame-by-frame video indexing and search capabilities

## Value to Property Owners
The Drone Security Analyst Agent enhances property security through:
1. **Automated 24/7 Monitoring**: Continuously monitors the property without human intervention
2. **Intelligent Threat Detection**: Identifies suspicious activities and objects in real-time
3. **Searchable Security History**: Maintains a queryable database of all detected events

## Key Requirements
1. Real-time processing of video and telemetry data
2. Accurate object detection and classification
3. Context-aware security event analysis
4. Customizable alert rules based on time, location, and detected objects

## Architecture
The system follows a modular architecture:

1. **Data Ingestion Layer**: Processes incoming video frames and telemetry data
2. **Processing Layer**: Detects objects, analyzes events, and builds context
3. **Alert System**: Evaluates events against security rules and generates alerts
4. **Storage & Indexing**: Maintains a searchable database of frames, events, and alerts
5. **Query Interface**: Provides search capabilities for historical data

## Setup and Installation

### Prerequisites
- Python 3.8+
- SQLite3

### Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/drone-security-analyst.git
   cd drone-security-analyst
   ```

2. (Optional) Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Run the Demo
```
python main.py --demo
```

### Run a Simulation
```
python main.py --simulate 20  # Process 20 simulated frames
```

### Run Interactive Query Mode
```
python main.py --query
```

### Run Tests
```
python test_drone_security.py
```

## Example Output

### Event Logging
```
Event logged: Blue Ford F150 spotted at Garage.
```

### Alert Generation
```
ALERT: Person loitering at Main Gate during nighttime (2025-03-19 00:01:00) (Severity: high)
```

### Frame Searching
```
Query: Show all truck events
- Frame 101: Blue Ford F150 at Garage (Time: 2025-03-19 12:00:00)
- Frame 103: Blue Ford F150 at Main Gate (Time: 2025-03-19 14:30:00)
```

## Design Decisions

### Simulated Data
For the prototype, we're using text descriptions to simulate video frames instead of actual video processing. This allows us to focus on the architecture and functionality without requiring complex computer vision components.

### Database Choice
SQLite was chosen for its simplicity and zero-configuration nature, making it ideal for a prototype. In a production environment, a more robust database like PostgreSQL would be more appropriate.

### Modular Architecture
The system is designed with separate components (object detection, event analysis, rule engine, indexing) to allow for easy extension and replacement of individual modules.

## Future Enhancements
- Implement actual video processing using computer vision libraries
- Add machine learning for more accurate object detection and classification
- Develop a web interface for configuration and monitoring
- Implement real-time notifications via email or SMS
- Add support for multiple drones and integration with other security systems

## AI Tool Assistance
This project was developed with the assistance of AI tools to expedite the development process:

- **Architecture Design**: Used AI to help formulate the system architecture and component interactions
- **Code Generation**: Leveraged AI to generate initial code structure and basic functionality
- **Testing Strategy**: AI assisted in creating comprehensive test cases to validate system functionality

## License
This project is proprietary and confidential. Not for distribution.
