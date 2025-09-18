# XLeRobot Web Control

A web-based control interface for XLeRobot supporting multiple simulation and real robot environments.

## Quick Start

1. **Choose your controller type and configure environment:**
   ```bash
   cd web_control/server
   cp .env.example .env
   # Edit .env file with your controller settings
   ```

2. **Install dependencies and start server:**
   ```bash
   pip install -r requirements.txt
   python main.py
   ```

3. **Start client interface:**
   ```bash
   cd ../client
   npm install
   npm run dev
   ```

4. **Access the interface:** http://localhost:5173

## Controller Types

### 1. MuJoCo Simulation Controller

**Best for:** Physics simulation, algorithm development, safe testing

**Configuration (.env):**
```bash
ROBOT_CONTROLLER=mujoco
USE_MUJOCO_SIMULATOR=true
ENABLE_VIEWER=false
MJCF_PATH=
```

**Dependencies:**
```bash
pip install mujoco
```

**Features:**
- Physics-based simulation
- Fast iteration and testing
- No hardware required
- 3D visualization optional
- Custom model support

**Usage:**
- Ideal for developing control algorithms
- Safe environment for testing dangerous movements
- Physics accuracy for dynamics research

---

### 2. ManiSkill Environment Controller

**Best for:** AI training, reinforcement learning, skill development

**Configuration (.env):**
```bash
ROBOT_CONTROLLER=maniskill
```

**Dependencies:**
```bash
pip install mani-skill gymnasium torch
```

**Features:**
- AI training environments
- Task-specific scenarios
- GPU acceleration support
- Standardized observation/action spaces
- Integration with ML frameworks

**Usage:**
- Train RL agents on robot tasks
- Evaluate learned policies
- Benchmark robot learning algorithms
- Sim-to-real transfer research

---

### 3. Real Robot Controller (XLeRobot)

**Best for:** Real-world deployment, physical robot control

**Configuration (.env):**

*Option A - Control Remote Robot:*
```bash
ROBOT_CONTROLLER=real
ROBOT_IP=192.168.1.100
PORT_ZMQ_CMD=5555
PORT_ZMQ_OBSERVATIONS=5556
SERVER_HOST=localhost
```

*Option B - Run on Robot:*
```bash
ROBOT_CONTROLLER=real
ROBOT_IP=localhost
PORT_ZMQ_CMD=5555
PORT_ZMQ_OBSERVATIONS=5556
SERVER_HOST=0.0.0.0
```

**Dependencies:**
```bash
pip install pyzmq
```

**Prerequisites:**
- XLeRobot hardware with xlerobot_host.py running
- Network connection (local or Tailscale)
- ZeroMQ communication ports available

**Features:**
- Real-time robot control
- Dual-arm manipulation (12 DoF)
- Mobile base control (3 DoF)
- Head control (2 DoF)
- Multi-camera video streams
- Real-time telemetry
- Emergency stop functionality

**Deployment Architectures:**

1. **Remote Control Setup:**
   ```
   [Your PC] → web_control → [Robot] xlerobot_host.py
   ```
   - Run web_control on your computer
   - Control robot over network/Tailscale
   - Good for development and remote operation

2. **On-Robot Setup:**
   ```
   [Robot] xlerobot_host.py + web_control ← [Your PC] browser
   ```
   - Run web_control directly on robot
   - Access via web browser from any device
   - Good for production deployment

**Usage:**
- Physical task execution
- Real-world testing
- Human-robot interaction
- Production deployments

## Network Configuration

### Local Network
- Ensure all devices on same network
- Use device IP addresses in configuration

### Tailscale (Recommended for remote access)

1. **Install Tailscale on both devices:**
   ```bash
   curl -fsSL https://tailscale.com/install.sh | sh
   sudo tailscale up
   ```

2. **Get device IPs:**
   ```bash
   tailscale ip -4
   ```

3. **Configure firewall:**
   ```bash
   sudo ufw allow 8000  # Web interface
   sudo ufw allow 5555  # Robot commands
   sudo ufw allow 5556  # Robot data
   ```

## Client Configuration

Create `web_control/client/.env`:
```bash
VITE_SERVER_HOST=localhost
VITE_SERVER_PORT=8000
VITE_SERVER_PROTOCOL=http
```

For remote access, use server's IP:
```bash
VITE_SERVER_HOST=192.168.1.100
```

## Troubleshooting

### Controller-Specific Issues

**MuJoCo:**
- Verify installation: `python -c "import mujoco"`
- Check OpenGL support for rendering
- Validate MJCF model files

**ManiSkill:**
- Install gymnasium: `pip install gymnasium`
- Check CUDA for GPU acceleration
- Verify environment IDs

**Real Robot:**
- Ensure xlerobot_host.py is running on robot
- Test ZeroMQ connectivity: `telnet robot-ip 5555`
- Check robot calibration and hardware status
- Verify network connectivity and ports

### General Issues

**Connection Problems:**
- Check firewall settings
- Verify IP addresses and ports
- Test network connectivity with ping

**Performance Issues:**
- Reduce VIDEO_QUALITY for better network performance
- Lower VIDEO_FPS on slow connections
- Use production build for client

**Video Stream Issues:**
- Verify OpenCV installation: `python -c "import cv2"`
- Check browser WebSocket support
- Test with different browsers

## Development

### Adding New Controllers
1. Create controller class in `robot_interface/`
2. Implement base controller interface
3. Add configuration options to `config.py`
4. Update factory pattern in `factory.py`

### Configuration Options
All settings can be configured via environment variables or `.env` files. See `.env.example` for complete options list.