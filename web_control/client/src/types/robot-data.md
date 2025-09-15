# XLeRobot Socket.IO API Documentation

This document describes the Socket.IO events that the XLeRobot web client expects to receive real robot data.

## Client Events (Outgoing)

These events are sent by the client to the server:

### Connection Events
- `ping` - Ping test message
  ```json
  { "timestamp": 1234567890, "message": "ping from client" }
  ```

### Control Events  
- `move_command` - Robot movement control
  ```json
  { "direction": "forward|backward|left|right|stop", "speed": 1.0 }
  ```

### Video Stream Events
- `start_video_stream` - Start video streaming
- `stop_video_stream` - Stop video streaming

## Server Events (Incoming)

These events should be sent by the server to provide real robot data:

### Connection Events
- `connection_established` - Server connection confirmation
  ```json
  { "message": "XLeRobot server connected" }
  ```
- `pong` - Response to ping
  ```json
  { "timestamp": 1234567890, "message": "pong from server" }
  ```
- `command_received` - Confirmation of received command
  ```json
  { "type": "move", "direction": "forward", "timestamp": 1234567890 }
  ```

### Video Stream Events
- `video_stream_started` - Video stream started successfully
  ```json
  { "status": "started", "timestamp": 1234567890 }
  ```
- `video_stream_stopped` - Video stream stopped
  ```json
  { "status": "stopped", "timestamp": 1234567890 }
  ```
- `video_stream_error` - Video stream error
  ```json
  { "error": "Camera not available", "code": "CAMERA_ERROR" }
  ```
- `video_frame` - Real-time video frame data
  ```json
  {
    "timestamp": 1234567890,
    "frame": "base64_encoded_jpeg_data",  // Option 1: Base64 image
    "url": "http://server/image.jpg",     // Option 2: Image URL
    "width": 640,
    "height": 480
  }
  ```

### Robot Telemetry Events
- `telemetry_update` - Real robot sensor data
  ```json
  {
    "timestamp": 1234567890,
    "battery": "85%",           // Battery level (string with %)
    "temperature": "42.5°C",    // Temperature reading  
    "speed": "1.25 m/s",       // Current movement speed
    "voltage": "11.8V"         // System voltage
  }
  ```

### Network Performance Events
- `network_metrics` - Network performance data
  ```json
  {
    "timestamp": 1234567890,
    "latency": 45,        // Round-trip time in milliseconds (number)
    "fps": 30,           // Video frame rate (number)
    "packetLoss": 0.1    // Packet loss percentage (number)
  }
  ```

### Robot Arm Events  
- `arm_position_update` - Robot arm joint positions
  ```json
  {
    "timestamp": 1234567890,
    "angles": [0, 45, -30, 90],           // Joint angles in degrees (array of numbers)
    "positions": ["base", "shoulder", "elbow", "wrist"]  // Joint names (array of strings)
  }
  ```

## Data Display Behavior

When real data is not available (null values), the interface displays:
- **"Not Available"** for text fields (battery, temp, voltage, speed)
- **"N/A"** for numeric fields (latency, fps)
- **null values** for array data (arm angles)

## Implementation Notes

1. All timestamp fields should use Unix timestamp (milliseconds)
2. The video_frame event supports both base64 encoded images and URLs
3. Telemetry data should be sent at regular intervals (recommended: 1-2 seconds)
4. Network metrics should be calculated and sent periodically 
5. Video frames should be sent at the target FPS rate (typically 30 FPS)
6. All data fields are optional - missing fields will show "Not Available" or "N/A"

## Example Server Implementation (Python)

```python
import socketio

sio = socketio.Server()

# Send telemetry data every 2 seconds
@sio.event
def send_telemetry():
    sio.emit('telemetry_update', {
        'timestamp': int(time.time() * 1000),
        'battery': '87%',
        'temperature': '38.2°C', 
        'speed': '0.85 m/s',
        'voltage': '12.1V'
    })

# Send network metrics
@sio.event  
def send_network_metrics():
    sio.emit('network_metrics', {
        'timestamp': int(time.time() * 1000),
        'latency': 42,
        'fps': 30,
        'packetLoss': 0.05
    })

# Send arm positions
@sio.event
def send_arm_positions():
    sio.emit('arm_position_update', {
        'timestamp': int(time.time() * 1000),
        'angles': [15, 45, -20, 90],
        'positions': ['base', 'shoulder', 'elbow', 'wrist']
    })
```