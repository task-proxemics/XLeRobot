# XLeRobot Web Control Server

import os
import time
from collections import defaultdict
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import socketio
import uvicorn
import asyncio
from api.streaming import video_manager, webrtc_manager
from robot_interface.factory import get_or_create_controller, cleanup_controller
from config import load_config, get_robot_controller_config, print_config

# Load application configuration
app_config = load_config()
print_config()

# Create robot controller using factory with configuration
robot_controller = get_or_create_controller(
    controller_type=app_config.robot.controller_type,
    config=get_robot_controller_config()
)

# Client state tracking for rate limiting and throttling
client_states = defaultdict(lambda: {
    'last_command_time': 0,
    'is_moving': False,
    'current_direction': None,
    'movement_start_time': 0,
    'command_count': 0,
    'rate_limit_window': time.time(),
    'throttle_violations': 0,
    'last_throttle_time': 0
})

# Rate limiting and throttling configuration
RATE_LIMIT_CONFIG = {
    'max_commands_per_second': 20,  # Maximum 20 commands per second
    'min_command_interval': 0.05,  # Minimum 50ms between commands (throttling)
    'rate_limit_window': 1.0,      # 1 second window for rate limiting
    'throttle_penalty_duration': 2.0,  # 2 second penalty for throttle violations
    'max_throttle_violations': 3,   # Maximum violations before temporary ban
}

async def startup_event():
    # Initialize robot controller on startup
    print("Initializing robot controller...")
    if robot_controller:
        await robot_controller.connect()
        print(f"{robot_controller.get_controller_type()} initialized successfully")
    else:
        print("Robot controller initialization failed")

async def shutdown_event():
    # Cleanup resources on shutdown
    print("Shutting down robot controller...")
    if robot_controller:
        await robot_controller.disconnect()
    cleanup_controller()
    print("Robot controller shut down")

sio = socketio.AsyncServer(
    async_mode='asgi',
    cors_allowed_origins='*'
    logger=True,
    engineio_logger=True
)

app = FastAPI(title="XLeRobot Web Control API", version="0.1.0")

app.add_event_handler("startup", startup_event)
app.add_event_handler("shutdown", shutdown_event)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

socket_app = socketio.ASGIApp(sio, app)

@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "XLeRobot Web Control Server is running"}

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    controller_info = {}
    if robot_controller:
        controller_info = {
            'type': robot_controller.get_controller_type(),
            'connected': robot_controller.is_connected(),
            'capabilities': robot_controller.get_capabilities()
        }
    
    return {
        "status": "healthy", 
        "service": "XLeRobot Web Control",
        "controller": controller_info
    }

@app.get("/robot/info")
async def robot_info():
    """Robot controller info endpoint"""
    if not robot_controller:
        return {"error": "No robot controller available"}
    
    return {
        'controller_type': robot_controller.get_controller_type(),
        'connected': robot_controller.is_connected(),
        'capabilities': robot_controller.get_capabilities(),
        'state': await robot_controller.get_state() if robot_controller.is_connected() else None
    }

@app.get("/robot/controllers")
async def available_controllers():
    """Get available controllers"""
    from robot_interface.factory import RobotControllerFactory
    return RobotControllerFactory.get_available_controllers()

@app.post("/robot/camera/reset")
async def reset_camera():
    """Reset camera to default position"""
    if not robot_controller:
        return {"error": "No robot controller available"}

    try:
        result = await robot_controller.reset_camera()
        return result
    except Exception as e:
        return {"error": f"Camera reset failed: {str(e)}"}

@app.post("/robot/camera/position")
async def set_camera_position(request: dict):
    """Set camera position"""
    if not robot_controller:
        return {"error": "No robot controller available"}

    position = request.get('position')
    target = request.get('target')

    if not position:
        return {"error": "Position is required"}

    try:
        result = await robot_controller.set_camera_position(tuple(position), tuple(target) if target else None)
        return result
    except Exception as e:
        return {"error": f"Set camera position failed: {str(e)}"}

@app.get("/robot/camera/info")
async def get_camera_info():
    """Get camera info"""
    if not robot_controller:
        return {"error": "No robot controller available"}

    try:
        result = await robot_controller.get_camera_info()
        return result
    except Exception as e:
        return {"error": f"Get camera info failed: {str(e)}"}

# Rate limiting and throttling functions
def check_rate_limit(sid: str) -> bool:
    """Check if client is within rate limits"""
    current_time = time.time()
    client_state = client_states[sid]

    # Reset command count if window has passed
    if current_time - client_state['rate_limit_window'] >= RATE_LIMIT_CONFIG['rate_limit_window']:
        client_state['command_count'] = 0
        client_state['rate_limit_window'] = current_time

    # Check if client exceeds max commands per second
    if client_state['command_count'] >= RATE_LIMIT_CONFIG['max_commands_per_second']:
        return False

    return True

def check_throttle(sid: str) -> bool:
    """Check if client is throttling commands too fast"""
    current_time = time.time()
    client_state = client_states[sid]

    # Check if client is in penalty period
    if (client_state['throttle_violations'] >= RATE_LIMIT_CONFIG['max_throttle_violations'] and
        current_time - client_state['last_throttle_time'] < RATE_LIMIT_CONFIG['throttle_penalty_duration']):
        return False

    # Reset violations if penalty period has passed
    if current_time - client_state['last_throttle_time'] >= RATE_LIMIT_CONFIG['throttle_penalty_duration']:
        client_state['throttle_violations'] = 0

    # Check minimum interval between commands
    if current_time - client_state['last_command_time'] < RATE_LIMIT_CONFIG['min_command_interval']:
        client_state['throttle_violations'] += 1
        client_state['last_throttle_time'] = current_time
        return False

    return True

def update_client_state(sid: str, direction: str, continuous: bool = False):
    """Update client state after successful command"""
    current_time = time.time()
    client_state = client_states[sid]

    client_state['last_command_time'] = current_time
    client_state['command_count'] += 1

    if direction == 'stop':
        client_state['is_moving'] = False
        client_state['current_direction'] = None
    else:
        if not client_state['is_moving']:
            client_state['movement_start_time'] = current_time
        client_state['is_moving'] = True
        client_state['current_direction'] = direction

@sio.event
async def connect(sid, environ, auth):
    """Client connection event"""
    print(f"Client connected: {sid}")
    # Initialize client state
    client_states[sid] = {
        'last_command_time': 0,
        'is_moving': False,
        'current_direction': None,
        'movement_start_time': 0,
        'command_count': 0,
        'rate_limit_window': time.time(),
        'throttle_violations': 0,
        'last_throttle_time': 0
    }
    await sio.emit('connection_established', {'message': 'Connected to XLeRobot control server'}, to=sid)

@sio.event
async def disconnect(sid):
    """Client disconnect event"""
    print(f"Client disconnected: {sid}")

    if sid in video_manager.stream_tasks:
        task = video_manager.stream_tasks[sid]
        if not task.cancelled():
            task.cancel()
            print(f"Cancelled video stream task for disconnected client {sid}")
        del video_manager.stream_tasks[sid]

    if sid in client_states:
        del client_states[sid]
        print(f"Cleaned up state for client {sid}")

@sio.event
async def ping(sid, data):
    """Ping-pong test event"""
    print(f"Received ping from {sid}: {data}")
    await sio.emit('pong', {'message': 'pong', 'timestamp': data.get('timestamp')}, to=sid)

@sio.event
async def move_command(sid, data):
    """Movement command handler with rate limiting and throttling"""
    direction = data.get('direction')
    speed = data.get('speed', 1.0)
    continuous = data.get('continuous', False)
    timestamp = data.get('timestamp', time.time() * 1000)

    current_time = time.time()

    # Check rate limiting
    if not check_rate_limit(sid):
        await sio.emit('command_received', {
            'type': 'move',
            'status': 'rate_limited',
            'message': f'Rate limit exceeded: maximum {RATE_LIMIT_CONFIG["max_commands_per_second"]} commands per second',
            'max_rate': RATE_LIMIT_CONFIG['max_commands_per_second'],
            'client_timestamp': timestamp,
            'server_timestamp': current_time * 1000
        }, to=sid)
        return

    # Check throttling
    if not check_throttle(sid):
        client_state = client_states[sid]
        await sio.emit('command_received', {
            'type': 'move',
            'status': 'throttled',
            'message': f'Command throttled: minimum {RATE_LIMIT_CONFIG["min_command_interval"]*1000:.0f}ms interval required',
            'min_interval': RATE_LIMIT_CONFIG['min_command_interval'] * 1000,
            'violations': client_state['throttle_violations'],
            'penalty_remaining': max(0, RATE_LIMIT_CONFIG['throttle_penalty_duration'] - (current_time - client_state['last_throttle_time'])) if client_state['throttle_violations'] >= RATE_LIMIT_CONFIG['max_throttle_violations'] else 0,
            'client_timestamp': timestamp,
            'server_timestamp': current_time * 1000
        }, to=sid)
        return

    if not robot_controller:
        await sio.emit('command_received', {
            'type': 'move',
            'status': 'error',
            'message': 'Robot controller not available',
            'client_timestamp': timestamp,
            'server_timestamp': current_time * 1000
        }, to=sid)
        return

    # Log command with rate limiting info
    client_state = client_states[sid]
    print(f"[{sid[:8]}] Move command: {direction} (speed={speed:.1f}) - continuous={continuous} - count={client_state['command_count']+1}/{RATE_LIMIT_CONFIG['max_commands_per_second']}")

    # Execute robot command
    try:
        result = await robot_controller.move(direction, speed)

        # Update client state after successful command
        update_client_state(sid, direction, continuous)

        # Get current robot state
        robot_state = await robot_controller.get_state()

        # Calculate latency
        latency = (current_time * 1000) - timestamp if timestamp else 0

        # Send success response with detailed metrics
        await sio.emit('command_received', {
            'type': 'move',
            'direction': direction,
            'speed': speed,
            'continuous': continuous,
            'status': result.get('status', 'executed'),
            'robot_state': robot_state,
            'metrics': {
                'latency': latency,
                'commands_in_window': client_state['command_count'],
                'max_commands': RATE_LIMIT_CONFIG['max_commands_per_second'],
                'throttle_violations': client_state['throttle_violations']
            },
            'client_timestamp': timestamp,
            'server_timestamp': current_time * 1000
        }, to=sid)

    except Exception as e:
        await sio.emit('command_received', {
            'type': 'move',
            'status': 'error',
            'message': f'Command execution failed: {str(e)}',
            'client_timestamp': timestamp,
            'server_timestamp': current_time * 1000
        }, to=sid)

@sio.event
async def start_video_stream(sid):
    """Start video streaming"""
    print(f"Client {sid} requested start video stream")
    
    if sid in video_manager.stream_tasks:
        task = video_manager.stream_tasks[sid]
        if not task.cancelled():
            task.cancel()
        del video_manager.stream_tasks[sid]
    
    result = await video_manager.start_stream()
    await sio.emit('stream_status', result, to=sid)
    
    task = asyncio.create_task(video_manager.stream_frames(sio, sid))
    video_manager.stream_tasks[sid] = task

@sio.event
async def stop_video_stream(sid):
    """Stop video streaming"""
    print(f"Client {sid} requested stop video stream")
    result = await video_manager.stop_stream(sid)
    await sio.emit('stream_status', result, to=sid)

@sio.event
async def webrtc_offer(sid, data):
    """Handle WebRTC offer"""
    print(f"Received WebRTC offer from {sid}")
    answer = await webrtc_manager.handle_offer(data, sid)
    await sio.emit('webrtc_answer', answer, to=sid)

@sio.event
async def webrtc_ice_candidate(sid, data):
    """Handle ICE candidate"""
    await webrtc_manager.handle_ice_candidate(data, sid)

@sio.event
async def reset_camera(sid):
    """Reset camera event handler"""
    print(f"Client {sid} requested camera reset")

    if not robot_controller:
        await sio.emit('camera_action_result', {
            'action': 'reset',
            'status': 'error',
            'message': 'Robot controller not available'
        }, to=sid)
        return

    try:
        result = await robot_controller.reset_camera()
        await sio.emit('camera_action_result', {
            'action': 'reset',
            **result
        }, to=sid)
        print(f"Camera reset result: {result['status']}")
    except Exception as e:
        await sio.emit('camera_action_result', {
            'action': 'reset',
            'status': 'error',
            'message': f'Camera reset failed: {str(e)}'
        }, to=sid)

@sio.event
async def set_camera_position(sid, data):
    """Set camera position event handler"""
    print(f"Client {sid} requested set camera position")

    if not robot_controller:
        await sio.emit('camera_action_result', {
            'action': 'set_position',
            'status': 'error',
            'message': 'Robot controller not available'
        }, to=sid)
        return

    position = data.get('position')
    target = data.get('target')

    if not position:
        await sio.emit('camera_action_result', {
            'action': 'set_position',
            'status': 'error',
            'message': 'Position is required'
        }, to=sid)
        return

    try:
        result = await robot_controller.set_camera_position(tuple(position), tuple(target) if target else None)
        await sio.emit('camera_action_result', {
            'action': 'set_position',
            **result
        }, to=sid)
        print(f"Camera position set result: {result['status']}")
    except Exception as e:
        await sio.emit('camera_action_result', {
            'action': 'set_position',
            'status': 'error',
            'message': f'Set camera position failed: {str(e)}'
        }, to=sid)

@sio.event
async def get_camera_info(sid):
    """Get camera info event handler"""
    print(f"Client {sid} requested camera info")

    if not robot_controller:
        await sio.emit('camera_info_result', {
            'status': 'error',
            'message': 'Robot controller not available'
        }, to=sid)
        return

    try:
        result = await robot_controller.get_camera_info()
        await sio.emit('camera_info_result', {
            'status': 'success',
            'camera_info': result
        }, to=sid)
    except Exception as e:
        await sio.emit('camera_info_result', {
            'status': 'error',
            'message': f'Get camera info failed: {str(e)}'
        }, to=sid)

if __name__ == "__main__":
    uvicorn.run(
        "main:socket_app"
        host=app_config.server.host,
        port=app_config.server.port,
        reload=app_config.server.reload,
        log_level=app_config.server.log_level
    )