# XLeRobot Web Control Configuration Guide

## Table of Contents
1. [Tailscale Network Configuration](#tailscale-network-configuration)
2. [Server Configuration](#server-configuration)
3. [Client Configuration](#client-configuration)
4. [Controller-Specific Requirements](#controller-specific-requirements)

## Tailscale Network Configuration

### Prerequisites
Tailscale is required for connecting devices across different networks (e.g., robot on one WiFi, control computer on another).

### Server Machine Setup

1. Install Tailscale:
```bash
# Linux/Ubuntu
curl -fsSL https://tailscale.com/install.sh | sh

# macOS
brew install tailscale
```

2. Start Tailscale and authenticate:
```bash
sudo tailscale up
```

3. Get the server's Tailscale IP:
```bash
tailscale ip -4
# Example output: 100.116.148.99
```

4. Ensure the server port is accessible:
```bash
# Check firewall status
sudo ufw status

# If needed, allow port 8000
sudo ufw allow 8000
```

### Client Machine Setup

1. Install Tailscale on the client machine following the same installation steps

2. Authenticate and join the same Tailscale network:
```bash
sudo tailscale up
```

3. Verify connection to server:
```bash
ping <server-tailscale-ip>
# Example: ping 100.116.148.99
```

## Server Configuration

### Environment Variables

Create a `.env` file in the `web_control/server/` directory:

```bash
# Robot Controller Selection
# Options: mujoco, maniskill, real
ROBOT_CONTROLLER=mujoco

# Server Network Configuration
SERVER_HOST=0.0.0.0  # Listen on all interfaces
SERVER_PORT=8000
SERVER_RELOAD=true
LOG_LEVEL=info

# MuJoCo Configuration
USE_MUJOCO_SIMULATOR=true
ENABLE_VIEWER=false  # Set to true for GUI window
MJCF_PATH=  # Leave empty for default scene.xml

# Video Stream Configuration
VIDEO_WIDTH=640
VIDEO_HEIGHT=480
VIDEO_FPS=30
VIDEO_QUALITY=80  # JPEG quality (1-100)
```

### Installation Requirements

#### Base Requirements
```bash
pip install fastapi uvicorn python-socketio opencv-python numpy python-dotenv
```

#### Controller-Specific Dependencies

**For MuJoCo:**
```bash
pip install mujoco
# MuJoCo will be automatically downloaded on first use
```

**For ManiSkill:**
```bash
pip install mani-skill gymnasium torch
```

**For Real Robot:**
```bash
pip install pyserial  # For USB/serial connection
pip install requests  # For HTTP API connection
```

### Running the Server

```bash
cd web_control/server
python main.py
```

The server will start on `http://0.0.0.0:8000`

## Client Configuration

### Environment Variables

Create a `.env` file in the `web_control/client/` directory:

```bash
# Server Connection
VITE_SERVER_HOST=localhost  # For local development
VITE_SERVER_PORT=8000
VITE_SERVER_PROTOCOL=http

# For Tailscale connection, use the server's Tailscale IP:
# VITE_SERVER_HOST=100.116.148.99
```

### Installation

```bash
cd web_control/client
npm install
```

### Running the Client

Development mode:
```bash
npm run dev
# Access at http://localhost:5173
```

Production build:
```bash
npm run build
npm run preview
```

## Controller-Specific Requirements

### MuJoCo Controller

**Environment Variables:**
```bash
ROBOT_CONTROLLER=mujoco
USE_MUJOCO_SIMULATOR=true
ENABLE_VIEWER=false  # true for GUI window
MJCF_PATH=/path/to/model.xml  # Optional custom model
```

**Required Files:**
- Default model: `simulation/mujoco/scene.xml`
- Custom models can be specified via MJCF_PATH

**System Requirements:**
- Python 3.8+
- OpenGL support for rendering
- CPU with SSE4.2 support

### ManiSkill Controller

**Environment Variables:**
```bash
ROBOT_CONTROLLER=maniskill
# Additional ManiSkill-specific configs
ENV_ID=PushCube-v1  # ManiSkill environment
OBS_MODE=sensor_data
RENDER_MODE=rgb_array
```

**Required Files:**
- Place ManiSkill agents in: `simulation/Maniskill/agents/`
- Ensure `xlerobot_single.py` exists for robot control

**System Requirements:**
- Python 3.8+
- CUDA-capable GPU (optional but recommended)
- 8GB+ RAM

### Real Robot Controller (XLeRobot)

**Environment Variables:**
```bash
ROBOT_CONTROLLER=real
# XLeRobot ZeroMQ connection settings
ROBOT_IP=localhost
PORT_ZMQ_CMD=5555
PORT_ZMQ_OBSERVATIONS=5556
POLLING_TIMEOUT_MS=100
CONNECT_TIMEOUT_S=5
ROBOT_TYPE=xlerobot
```

**Deployment Options:**

1. **PC Deployment (Remote Control):**
   ```bash
   # Run web_control on your PC, control remote robot
   ROBOT_IP=192.168.1.100  # Robot's IP address
   SERVER_HOST=localhost   # Accept local connections only
   ```
   - Robot runs: `python xlerobot_host.py`
   - PC runs: `python main.py`
   - Access: http://localhost:8000

2. **Robot Deployment (On-board Control):**
   ```bash
   # Run web_control on the robot itself
   ROBOT_IP=localhost      # Connect to local xlerobot_host
   SERVER_HOST=0.0.0.0     # Accept remote connections
   ```
   - Robot runs: `python xlerobot_host.py` and `python main.py`
   - Access from PC: http://robot-ip:8000

**Connection Requirements:**

1. **Prerequisites:**
   - XLeRobot hardware with xlerobot_host.py running
   - Network connectivity (local network or Tailscale)
   - Python dependencies: `zmq`, `asyncio`

2. **Network Setup:**
   - Local Network: Use robot's local IP
   - Tailscale: Use robot's Tailscale IP
   - Same Machine: Use localhost

3. **Port Configuration:**
   - Port 5555: Command channel (web_control → robot)
   - Port 5556: Data channel (robot → web_control)
   - Port 8000: Web interface (default)

**Robot Hardware Communication:**
   - **Control Protocol**: ZeroMQ PUSH/PULL sockets
   - **Command Format**: JSON with joint positions and velocities
   - **Data Flow**: Real-time robot state and camera feeds
   - **Safety**: Watchdog timeout and emergency stop

## Troubleshooting

### Connection Issues

1. **Client cannot connect to server:**
   - Verify server is running: `curl http://<server-ip>:8000`
   - Check firewall settings
   - Ensure correct IP in client .env file

2. **Tailscale connection problems:**
   - Verify both devices are authenticated: `tailscale status`
   - Check if devices can ping each other
   - Restart Tailscale service: `sudo tailscale down && sudo tailscale up`

3. **Video stream not working:**
   - Check VIDEO_QUALITY setting (lower values for better network performance)
   - Verify OpenCV is installed: `python -c "import cv2"`
   - Check browser console for WebSocket errors

### Controller Issues

1. **MuJoCo fails to initialize:**
   - Verify MuJoCo is installed: `python -c "import mujoco"`
   - Check MJCF_PATH points to valid model file
   - Ensure OpenGL is available for rendering

2. **ManiSkill environment errors:**
   - Verify gymnasium is installed: `pip install gymnasium`
   - Check ENV_ID is valid ManiSkill environment
   - Ensure CUDA drivers are installed (if using GPU)

3. **XLeRobot not responding:**
   - Verify xlerobot_host.py is running on robot
   - Check ZeroMQ port connectivity: `telnet robot-ip 5555`
   - Test robot calibration and motor connections
   - Check network connectivity between web_control and robot
   - Verify robot is not in emergency stop state

4. **ZeroMQ communication issues:**
   - Check firewall allows ports 5555 and 5556
   - Verify ZeroMQ library is installed: `pip install pyzmq`
   - Test connection timeout settings
   - Check for network latency issues

## Performance Optimization

### Network Optimization
- Reduce VIDEO_QUALITY for lower bandwidth usage
- Lower VIDEO_FPS for smoother control on slow networks
- Use wired connection when possible

### Server Optimization
- Set ENABLE_VIEWER=false to reduce CPU usage
- Adjust VIDEO_WIDTH/VIDEO_HEIGHT for performance
- Use SERVER_RELOAD=false in production

### Client Optimization
- Use production build for better performance
- Close unnecessary browser tabs
- Use Chrome/Edge for best WebSocket performance