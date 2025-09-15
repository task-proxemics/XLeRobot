# XLeRobot Web Control

## Overview

XLeRobot Web Control provides a unified interface for controlling different types of robots:
- **Simulator**: Support video streaming from robots in simulators (ManiSkill / MuJoCo)
- **Real Hardware (On Progress)**: Direct control of physical robots via network/serial communication

## Quick Start

### Prerequisites
- Python 3.11
- Node 22


### 1. Server Setup

```bash
cd server
pip install -r requirements.txt
```

Create a `.env` file with your configuration:
```env
# Example

ROBOT_CONTROLLER=mujoco
SERVER_HOST=0.0.0.0
SERVER_PORT=8000
VIDEO_WIDTH=640
VIDEO_HEIGHT=480
```

Start the server:
```bash
python main.py
```

### 2. Client Setup

```bash
cd client
npm install
npm run dev
```

### 3. Access the Interface

Open your browser to `http://localhost:5173` and start controlling your robot.

## Configuration

### Robot Controller Selection

Configure your robot type in `.env`:

```env
# For MuJoCo Simulation
ROBOT_CONTROLLER=mujoco
USE_MUJOCO_SIMULATOR=true
MJCF_PATH=/path/to/your/model.xml

# For Real Robot
ROBOT_CONTROLLER=real
ROBOT_IP=192.168.1.100
ROBOT_PORT=8080

# For ManiSkill Environment
ROBOT_CONTROLLER=maniskill
MANISKILL_ENV=PickCube-v1
```

### Advanced Settings

```env
# Server Configuration
LOG_LEVEL=info
ENABLE_CORS=true
MAX_CONNECTIONS=10

# Video Settings
VIDEO_FPS=30
VIDEO_QUALITY=80
ENABLE_RECORDING=true

# Safety Settings
MOVEMENT_TIMEOUT=5.0
MAX_SPEED=2.0
ENABLE_SAFETY_LIMITS=true
```

### Adding New Robot Controllers

1. Create a new controller class in `server/robot_interface/`:

```python
from .base import RobotController

class YourRobotController(RobotController):
    async def connect(self) -> bool:
        # Implement connection logic
        pass

    async def move(self, direction: str, speed: float):
        # Implement movement commands
        pass

    async def get_camera_frame(self):
        # Implement camera access
        pass
```

2. Register it in the factory (`factory.py`):

```python
AVAILABLE_CONTROLLERS['your_robot'] = YourRobotController
```

3. Update configuration options in `config.py`

### API Extension

Add new WebSocket events in `main.py`:

```python
@sio.event
async def your_custom_command(sid, data):
    # Handle custom robot commands
    result = await controller.your_method(data)
    await sio.emit('response', result, to=sid)
```

### WebSocket Events & API References

**Robot Control**:
- `move_command`: Send movement commands
- `stop_command`: Emergency stop
- `get_robot_state`: Request current status

**Video Streaming**:
- `start_video_stream`: Begin video feed
- `stop_video_stream`: End video feed
- `video_frame`: Receive video frames

**Camera Control**:
- `reset_camera`: Reset to default position
- `set_camera_position`: Adjust camera angle

### REST Endpoints

- `GET /health`: System status check
- `GET /robot/info`: Robot controller information
- `GET /robot/controllers`: Available controller types
- `POST /robot/camera/reset`: Reset camera position
