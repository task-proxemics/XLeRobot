# Real Robot Controller Implementation for XLeRobot

import asyncio
import base64
import json
import logging
import time
from typing import Optional, Dict, Any, Tuple

import cv2
import numpy as np
import zmq
import zmq.asyncio

from .base import RobotController


class RealRobotController(RobotController):

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize XLeRobot controller with ZeroMQ communication.

        Args:
            config: Configuration dictionary with keys:
                - robot_ip: IP address of the robot (default: localhost)
                - port_zmq_cmd: Command port (default: 5555)
                - port_zmq_observations: Observation port (default: 5556)
                - polling_timeout_ms: ZMQ polling timeout (default: 100)
                - connect_timeout_s: Connection timeout (default: 5)
                - robot_type: Type of robot (default: xlerobot)
        """
        super().__init__(config)

        # ZeroMQ Configuration
        self.robot_ip = config.get('robot_ip', 'localhost') if config else 'localhost'
        self.port_zmq_cmd = config.get('port_zmq_cmd', 5555) if config else 5555
        self.port_zmq_observations = config.get('port_zmq_observations', 5556) if config else 5556
        self.polling_timeout_ms = config.get('polling_timeout_ms', 100) if config else 100
        self.connect_timeout_s = config.get('connect_timeout_s', 5) if config else 5
        self.robot_type = config.get('robot_type', 'xlerobot') if config else 'xlerobot'

        # ZeroMQ components
        self.zmq_context = None
        self.zmq_cmd_socket = None
        self.zmq_observation_socket = None

        # State management
        self.last_observation_data = {}
        self.last_camera_frames = {}
        self.connection_established = False

        # XLeRobot state features
        self._state_features = [
            "left_arm_shoulder_pan.pos",
            "left_arm_shoulder_lift.pos",
            "left_arm_elbow_flex.pos",
            "left_arm_wrist_flex.pos",
            "left_arm_wrist_roll.pos",
            "left_arm_gripper.pos",
            "right_arm_shoulder_pan.pos",
            "right_arm_shoulder_lift.pos",
            "right_arm_elbow_flex.pos",
            "right_arm_wrist_flex.pos",
            "right_arm_wrist_roll.pos",
            "right_arm_gripper.pos",
            "head_motor_1.pos",
            "head_motor_2.pos",
            "x.vel",
            "y.vel",
            "theta.vel",
        ]

        self.controller_name = f"XLeRobot Controller ({self.robot_type})"
        print(f"{self.controller_name} initialized")
        print(f"   Target: {self.robot_ip}:{self.port_zmq_cmd}/{self.port_zmq_observations}")
    
    async def connect(self) -> bool:
        """
        Establish ZeroMQ connection to XLeRobot host.
        """
        if self.connected:
            print(f"{self.controller_name}: Already connected")
            return True

        try:
            print(f"{self.controller_name}: Connecting to robot...")
            print(f"   Command socket: {self.robot_ip}:{self.port_zmq_cmd}")
            print(f"   Observation socket: {self.robot_ip}:{self.port_zmq_observations}")

            # Initialize ZeroMQ context and sockets
            self.zmq_context = zmq.asyncio.Context()

            # Command socket (PUSH to robot)
            self.zmq_cmd_socket = self.zmq_context.socket(zmq.PUSH)
            cmd_address = f"tcp://{self.robot_ip}:{self.port_zmq_cmd}"
            self.zmq_cmd_socket.connect(cmd_address)
            self.zmq_cmd_socket.setsockopt(zmq.CONFLATE, 1)

            # Observation socket (PULL from robot)
            self.zmq_observation_socket = self.zmq_context.socket(zmq.PULL)
            obs_address = f"tcp://{self.robot_ip}:{self.port_zmq_observations}"
            self.zmq_observation_socket.connect(obs_address)
            self.zmq_observation_socket.setsockopt(zmq.CONFLATE, 1)

            # Test connection with timeout
            print(f"{self.controller_name}: Testing connection...")
            poller = zmq.asyncio.Poller()
            poller.register(self.zmq_observation_socket, zmq.POLLIN)

            # Wait for initial data to confirm connection
            start_time = time.time()
            while time.time() - start_time < self.connect_timeout_s:
                socks = await poller.poll(timeout=1000)  # 1 second timeout
                if socks:
                    # Receive test message to confirm connection
                    try:
                        test_msg = await self.zmq_observation_socket.recv_string(zmq.NOBLOCK)
                        self.connection_established = True
                        break
                    except zmq.Again:
                        pass
                await asyncio.sleep(0.1)

            if not self.connection_established:
                raise ConnectionError(f"Timeout waiting for robot connection after {self.connect_timeout_s}s")

            self.connected = True
            self.robot_state['status'] = 'connected'
            print(f"{self.controller_name}: Successfully connected!")
            return True

        except Exception as e:
            print(f"{self.controller_name}: Connection failed: {e}")
            await self._cleanup_sockets()
            return False
    
    async def disconnect(self) -> bool:
        """
        Close ZeroMQ connection to XLeRobot.
        """
        if not self.connected:
            return True

        print(f"{self.controller_name}: Disconnecting...")

        # Send stop command before disconnecting
        try:
            stop_action = {key: 0.0 for key in self._state_features}
            await self._send_action_internal(stop_action)
        except Exception as e:
            print(f"{self.controller_name}: Warning - failed to send stop command: {e}")

        await self._cleanup_sockets()

        self.connected = False
        self.connection_established = False
        self.robot_state['status'] = 'disconnected'

        print(f"{self.controller_name}: Disconnected")
        return True
    
    async def move(self, direction: str, speed: float = 1.0) -> Dict[str, Any]:
        """
        Control robot base movement using XLeRobot velocity commands.
        """
        if not self.connected:
            return {'status': 'error', 'message': 'Not connected to robot'}

        if not self.validate_direction(direction):
            return {'status': 'error', 'message': f'Invalid direction: {direction}'}

        speed = self.validate_speed(speed)

        try:
            # Convert web direction commands to XLeRobot velocity format
            action = self._web_direction_to_xlerobot_action(direction, speed)

            print(f"{self.controller_name}: Moving {direction} at speed {speed}")
            print(f"   XLeRobot action: x.vel={action.get('x.vel', 0):.2f}, "
                  f"y.vel={action.get('y.vel', 0):.2f}, theta.vel={action.get('theta.vel', 0):.2f}")

            # Send action to robot
            start_time = time.time()
            success = await self._send_action_internal(action)
            latency_ms = int((time.time() - start_time) * 1000)

            if success:
                # Update local state
                self._update_local_velocity_state(direction, speed)
                return {
                    'status': 'success',
                    'direction': direction,
                    'speed': speed,
                    'message': 'Command sent to XLeRobot',
                    'latency_ms': latency_ms
                }
            else:
                return {
                    'status': 'error',
                    'message': 'Failed to send command to robot',
                    'latency_ms': latency_ms
                }

        except Exception as e:
            print(f"{self.controller_name}: Move command failed: {e}")
            return {
                'status': 'error',
                'message': f'Move command failed: {str(e)}'
            }
    
    async def stop(self) -> Dict[str, Any]:
        """
        Emergency stop - send zero velocities to all motors.
        """
        if not self.connected:
            return {'status': 'error', 'message': 'Not connected to robot'}

        try:
            print(f"{self.controller_name}: EMERGENCY STOP")

            # Create stop action (all zeros)
            stop_action = {key: 0.0 for key in self._state_features}

            start_time = time.time()
            success = await self._send_action_internal(stop_action)
            latency_ms = int((time.time() - start_time) * 1000)

            if success:
                # Reset velocity state
                self.robot_state['velocity']['linear'] = {'x': 0.0, 'y': 0.0, 'z': 0.0}
                self.robot_state['velocity']['angular'] = {'x': 0.0, 'y': 0.0, 'z': 0.0}

                return {
                    'status': 'success',
                    'message': 'Emergency stop executed',
                    'latency_ms': latency_ms
                }
            else:
                return {
                    'status': 'error',
                    'message': 'Failed to execute emergency stop'
                }

        except Exception as e:
            print(f"{self.controller_name}: Emergency stop failed: {e}")
            return {
                'status': 'error',
                'message': f'Emergency stop failed: {str(e)}'
            }
    
    async def get_state(self) -> Dict[str, Any]:
        """
        Get current robot state from XLeRobot.
        """
        if not self.connected:
            return {
                'status': 'disconnected',
                'controller': self.controller_name,
                'robot_type': self.robot_type,
                'connection': {'type': 'zmq', 'connected': False}
            }

        try:
            # Get latest observation data
            await self._update_robot_state()

            # Build comprehensive state response
            state = self.robot_state.copy()
            state.update({
                'controller': self.controller_name,
                'robot_type': self.robot_type,
                'connection': {
                    'type': 'zmq',
                    'ip': self.robot_ip,
                    'cmd_port': self.port_zmq_cmd,
                    'obs_port': self.port_zmq_observations,
                    'connected': True
                },
                'joint_positions': self._extract_joint_positions(),
                'base_velocity': self._extract_base_velocity(),
                'last_update': time.time()
            })

            return state

        except Exception as e:
            print(f"{self.controller_name}: Failed to get state: {e}")
            return {
                'status': 'error',
                'controller': self.controller_name,
                'error': str(e)
            }
    
    async def get_camera_frame(self) -> Optional[np.ndarray]:
        """
        Get camera frame from XLeRobot cameras.
        """
        if not self.connected:
            return None

        try:
            # Update robot state to get latest camera data
            await self._update_robot_state()

            # Return the first available camera frame
            # XLeRobot typically has multiple cameras (head, hands)
            for camera_name, frame in self.last_camera_frames.items():
                if frame is not None:
                    return frame

            # If no frames available, return None
            print(f"{self.controller_name}: No camera frames available")
            return None

        except Exception as e:
            print(f"{self.controller_name}: Failed to get camera frame: {e}")
            return None
    
    async def get_camera_frame_base64(self) -> Optional[str]:
        """
        Get base64 encoded camera frame from XLeRobot.
        """
        if not self.connected:
            return None

        try:
            # Update robot state to get latest camera data
            await self._update_robot_state()

            # XLeRobot sends base64 encoded images directly
            # Return the first available base64 camera data
            observation_data = self.last_observation_data

            # Look for camera data in observation
            camera_names = ['head', 'left_wrist', 'right_wrist']  # Common XLeRobot cameras
            for cam_name in camera_names:
                if cam_name in observation_data:
                    base64_data = observation_data[cam_name]
                    if base64_data and isinstance(base64_data, str):
                        return base64_data

            # If we have a decoded frame, re-encode it
            frame = await self.get_camera_frame()
            if frame is not None:
                try:
                    encode_params = [cv2.IMWRITE_JPEG_QUALITY, 80]
                    success, buffer = cv2.imencode('.jpg', frame, encode_params)
                    if success:
                        return base64.b64encode(buffer).decode('utf-8')
                except Exception as encode_error:
                    print(f"{self.controller_name}: Failed to encode frame: {encode_error}")

            return None

        except Exception as e:
            print(f"{self.controller_name}: Failed to get base64 frame: {e}")
            return None
    
    async def set_arm_joint(self, arm: str, joint_index: int, angle: float) -> Dict[str, Any]:
        """
        Set arm joint angle on XLeRobot.
        """
        if not self.connected:
            return {'status': 'error', 'message': 'Not connected to robot'}

        if not self.validate_arm_parameters(arm, joint_index):
            return {'status': 'error', 'message': 'Invalid arm parameters'}

        try:
            print(f"{self.controller_name}: Setting {arm} arm joint {joint_index} to {angle:.2f} rad")

            # Create action with specific joint position
            action = {key: 0.0 for key in self._state_features}  # Start with zeros

            # Map arm and joint to XLeRobot joint name
            joint_name = self._get_xlerobot_joint_name(arm, joint_index)
            if joint_name:
                action[joint_name] = angle

                start_time = time.time()
                success = await self._send_action_internal(action)
                execution_time_ms = int((time.time() - start_time) * 1000)

                if success:
                    # Update local state
                    self.robot_state['arm_joints'][arm][joint_index] = angle

                    return {
                        'status': 'success',
                        'arm': arm,
                        'joint': joint_index,
                        'angle': angle,
                        'joint_name': joint_name,
                        'message': 'Joint command sent to XLeRobot',
                        'execution_time_ms': execution_time_ms
                    }
                else:
                    return {
                        'status': 'error',
                        'message': 'Failed to send joint command'
                    }
            else:
                return {
                    'status': 'error',
                    'message': f'Invalid joint mapping: {arm} joint {joint_index}'
                }

        except Exception as e:
            print(f"{self.controller_name}: Joint command failed: {e}")
            return {
                'status': 'error',
                'message': f'Joint command failed: {str(e)}'
            }

    async def reset_camera(self) -> Dict[str, Any]:
        """
        Reset camera position (XLeRobot head motors).
        """
        if not self.connected:
            return {'status': 'error', 'message': 'Not connected to robot'}

        try:
            # Reset head motors to neutral position
            action = {key: 0.0 for key in self._state_features}
            action['head_motor_1.pos'] = 0.0
            action['head_motor_2.pos'] = 0.0

            success = await self._send_action_internal(action)
            if success:
                return {'status': 'success', 'message': 'Camera reset to neutral position'}
            else:
                return {'status': 'error', 'message': 'Failed to reset camera'}

        except Exception as e:
            return {'status': 'error', 'message': f'Camera reset failed: {str(e)}'}

    async def set_camera_position(self, position: Tuple[float, float, float],
                                  target: Tuple[float, float, float] = None) -> Dict[str, Any]:
        """
        Set camera position using head motors.
        """
        if not self.connected:
            return {'status': 'error', 'message': 'Not connected to robot'}

        try:
            # Convert position to head motor angles
            # This is a simplified mapping - real implementation would use kinematics
            pan_angle = position[0]  # Use X for pan
            tilt_angle = position[1]  # Use Y for tilt

            action = {key: 0.0 for key in self._state_features}
            action['head_motor_1.pos'] = pan_angle
            action['head_motor_2.pos'] = tilt_angle

            success = await self._send_action_internal(action)
            if success:
                return {'status': 'success', 'message': 'Camera position set', 'position': position}
            else:
                return {'status': 'error', 'message': 'Failed to set camera position'}

        except Exception as e:
            return {'status': 'error', 'message': f'Set camera position failed: {str(e)}'}

    async def get_camera_info(self) -> Dict[str, Any]:
        """
        Get camera information from XLeRobot.
        """
        if not self.connected:
            return {'status': 'error', 'message': 'Not connected to robot'}

        try:
            camera_info = {
                'status': 'success',
                'cameras': {
                    'head': {'resolution': [640, 480], 'fps': 30, 'format': 'JPEG'},
                    'left_wrist': {'resolution': [640, 480], 'fps': 30, 'format': 'JPEG'},
                    'right_wrist': {'resolution': [640, 480], 'fps': 30, 'format': 'JPEG'}
                },
                'active_cameras': list(self.last_camera_frames.keys()),
                'head_position': {
                    'pan': self.last_observation_data.get('head_motor_1.pos', 0.0),
                    'tilt': self.last_observation_data.get('head_motor_2.pos', 0.0)
                }
            }
            return camera_info

        except Exception as e:
            return {'status': 'error', 'message': f'Get camera info failed: {str(e)}'}

    def get_capabilities(self) -> Dict[str, bool]:
        """
        Get XLeRobot controller capabilities.
        """
        capabilities = super().get_capabilities()
        capabilities.update({
            'simulation': False,
            'real_robot': True,
            'network_control': True,
            'zmq_communication': True,
            'dual_arm': True,
            'mobile_base': True,
            'head_control': True,
            'multi_camera': True,
            'battery_monitoring': True,
            'joint_control': True,
            'velocity_control': True,
            'implemented': True
        })
        return capabilities
    
    async def get_diagnostics(self) -> Dict[str, Any]:
        """
        Get XLeRobot diagnostics information.
        """
        try:
            if self.connected:
                await self._update_robot_state()

            diagnostics = {
                'controller': self.controller_name,
                'robot_type': self.robot_type,
                'connection_status': 'connected' if self.connected else 'disconnected',
                'zmq_connection': {
                    'established': self.connection_established,
                    'cmd_address': f"{self.robot_ip}:{self.port_zmq_cmd}",
                    'obs_address': f"{self.robot_ip}:{self.port_zmq_observations}"
                },
                'last_update': getattr(self, '_last_update_time', 0),
                'data_flow': {
                    'observations_received': len(self.last_observation_data) > 0,
                    'camera_frames': len(self.last_camera_frames),
                    'active_cameras': list(self.last_camera_frames.keys())
                }
            }

            # Add robot state if available
            if self.connected and self.last_observation_data:
                diagnostics.update({
                    'joint_positions': self._extract_joint_positions(),
                    'base_velocity': self._extract_base_velocity(),
                    'robot_status': 'operational'
                })
            else:
                diagnostics['robot_status'] = 'no_data'

            return diagnostics

        except Exception as e:
            return {
                'controller': self.controller_name,
                'robot_type': self.robot_type,
                'connection_status': 'error',
                'error': str(e)
            }
    
    async def calibrate(self) -> Dict[str, Any]:
        """
        XLeRobot calibration is handled by the host.
        This method provides calibration status.
        """
        if not self.connected:
            return {'status': 'error', 'message': 'Not connected to robot'}

        try:
            print(f"{self.controller_name}: Checking calibration status...")

            # XLeRobot calibration is done on the host side
            # We can check if we're receiving valid joint data
            await self._update_robot_state()

            if self.last_observation_data:
                joint_data_available = any(
                    key.endswith('.pos') for key in self.last_observation_data.keys()
                )

                if joint_data_available:
                    return {
                        'status': 'success',
                        'message': 'Robot appears to be calibrated (receiving joint data)',
                        'calibrated_components': [
                            'Joint Encoders',
                            'Motor Controllers',
                            'Base Wheels',
                            'Head Motors'
                        ]
                    }
                else:
                    return {
                        'status': 'warning',
                        'message': 'Connected but no joint data - check robot calibration'
                    }
            else:
                return {
                    'status': 'error',
                    'message': 'No data from robot - cannot verify calibration'
                }

        except Exception as e:
            return {
                'status': 'error',
                'message': f'Calibration check failed: {str(e)}'
            }

    # =================
    # HELPER METHODS
    # =================

    async def _cleanup_sockets(self):
        """
        Clean up ZeroMQ sockets and context.
        """
        try:
            if self.zmq_cmd_socket:
                self.zmq_cmd_socket.close()
                self.zmq_cmd_socket = None

            if self.zmq_observation_socket:
                self.zmq_observation_socket.close()
                self.zmq_observation_socket = None

            if self.zmq_context:
                self.zmq_context.term()
                self.zmq_context = None

        except Exception as e:
            print(f"{self.controller_name}: Warning - socket cleanup error: {e}")

    def _web_direction_to_xlerobot_action(self, direction: str, speed: float) -> Dict[str, float]:
        """
        Convert web direction commands to XLeRobot velocity format.
        """
        # Base action with all zeros
        action = {key: 0.0 for key in self._state_features}

        # XLeRobot speed scaling (m/s for linear, deg/s for angular)
        linear_speed = speed * 0.2  # Scale to reasonable m/s
        angular_speed = speed * 30.0  # Scale to reasonable deg/s

        # Map web directions to XLeRobot body frame velocities
        if direction == 'forward':
            action['x.vel'] = linear_speed
        elif direction == 'backward':
            action['x.vel'] = -linear_speed
        elif direction == 'left':
            action['y.vel'] = linear_speed
        elif direction == 'right':
            action['y.vel'] = -linear_speed
        elif direction == 'rotate_left':
            action['theta.vel'] = angular_speed
        elif direction == 'rotate_right':
            action['theta.vel'] = -angular_speed
        elif direction == 'stop':
            # All velocities already zero
            pass

        return action

    async def _send_action_internal(self, action: Dict[str, float]) -> bool:
        """
        Send action to XLeRobot via ZeroMQ.
        """
        try:
            if not self.zmq_cmd_socket:
                print(f"{self.controller_name}: Command socket not available")
                return False

            # Convert to JSON and send
            action_json = json.dumps(action)
            await self.zmq_cmd_socket.send_string(action_json)

            return True

        except Exception as e:
            print(f"{self.controller_name}: Failed to send action: {e}")
            return False

    async def _update_robot_state(self):
        """
        Update robot state from latest observation data.
        """
        try:
            if not self.zmq_observation_socket:
                return

            # Poll for new observation data
            poller = zmq.asyncio.Poller()
            poller.register(self.zmq_observation_socket, zmq.POLLIN)

            # Get latest message (non-blocking)
            socks = await poller.poll(timeout=self.polling_timeout_ms)

            if self.zmq_observation_socket in dict(socks):
                # Get the most recent message
                while True:
                    try:
                        obs_json = await self.zmq_observation_socket.recv_string(zmq.NOBLOCK)
                        # Parse the observation data
                        observation_data = json.loads(obs_json)
                        self.last_observation_data = observation_data
                        self._last_update_time = time.time()

                        # Extract and decode camera frames
                        self._extract_camera_frames(observation_data)

                        # Update robot state from observation
                        self._update_state_from_observation(observation_data)

                    except zmq.Again:
                        # No more messages
                        break
                    except json.JSONDecodeError as e:
                        print(f"{self.controller_name}: Failed to parse observation JSON: {e}")
                        break

        except Exception as e:
            print(f"{self.controller_name}: Failed to update robot state: {e}")

    def _extract_camera_frames(self, observation_data: Dict[str, Any]):
        """
        Extract and decode camera frames from observation data.
        """
        try:
            # Clear previous frames
            self.last_camera_frames = {}

            # Look for camera data (base64 encoded)
            camera_names = ['head', 'left_wrist', 'right_wrist']
            for cam_name in camera_names:
                if cam_name in observation_data:
                    base64_data = observation_data[cam_name]
                    if base64_data and isinstance(base64_data, str):
                        # Decode base64 to numpy array
                        frame = self._decode_base64_image(base64_data)
                        if frame is not None:
                            self.last_camera_frames[cam_name] = frame

        except Exception as e:
            print(f"{self.controller_name}: Failed to extract camera frames: {e}")

    def _decode_base64_image(self, base64_data: str) -> Optional[np.ndarray]:
        """
        Decode base64 image data to numpy array.
        """
        try:
            # Decode base64
            jpg_data = base64.b64decode(base64_data)
            # Convert to numpy array and decode JPEG
            np_arr = np.frombuffer(jpg_data, dtype=np.uint8)
            frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
            return frame

        except Exception as e:
            print(f"{self.controller_name}: Failed to decode base64 image: {e}")
            return None

    def _update_state_from_observation(self, observation_data: Dict[str, Any]):
        """
        Update internal robot state from observation data.
        """
        try:
            # Update joint positions
            joint_positions = self._extract_joint_positions_from_obs(observation_data)
            if joint_positions:
                for arm in ['left', 'right']:
                    if arm in joint_positions:
                        self.robot_state['arm_joints'][arm] = joint_positions[arm]

            # Update base velocity
            base_velocity = self._extract_base_velocity_from_obs(observation_data)
            if base_velocity:
                self.robot_state['velocity']['linear']['x'] = base_velocity.get('x', 0.0)
                self.robot_state['velocity']['linear']['y'] = base_velocity.get('y', 0.0)
                self.robot_state['velocity']['angular']['z'] = base_velocity.get('theta', 0.0)

            # Update status
            self.robot_state['status'] = 'connected'

        except Exception as e:
            print(f"{self.controller_name}: Failed to update state from observation: {e}")

    def _extract_joint_positions(self) -> Dict[str, Any]:
        """
        Extract joint positions from current observation data.
        """
        return self._extract_joint_positions_from_obs(self.last_observation_data)

    def _extract_joint_positions_from_obs(self, observation_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Extract joint positions from observation data.
        """
        try:
            joint_positions = {'left': [], 'right': [], 'head': []}

            # Left arm joints
            left_joints = [
                'left_arm_shoulder_pan.pos',
                'left_arm_shoulder_lift.pos',
                'left_arm_elbow_flex.pos',
                'left_arm_wrist_flex.pos',
                'left_arm_wrist_roll.pos',
                'left_arm_gripper.pos'
            ]
            joint_positions['left'] = [observation_data.get(joint, 0.0) for joint in left_joints]

            # Right arm joints
            right_joints = [
                'right_arm_shoulder_pan.pos',
                'right_arm_shoulder_lift.pos',
                'right_arm_elbow_flex.pos',
                'right_arm_wrist_flex.pos',
                'right_arm_wrist_roll.pos',
                'right_arm_gripper.pos'
            ]
            joint_positions['right'] = [observation_data.get(joint, 0.0) for joint in right_joints]

            # Head joints
            joint_positions['head'] = [
                observation_data.get('head_motor_1.pos', 0.0),
                observation_data.get('head_motor_2.pos', 0.0)
            ]

            return joint_positions

        except Exception as e:
            print(f"{self.controller_name}: Failed to extract joint positions: {e}")
            return {}

    def _extract_base_velocity(self) -> Dict[str, float]:
        """
        Extract base velocity from current observation data.
        """
        return self._extract_base_velocity_from_obs(self.last_observation_data)

    def _extract_base_velocity_from_obs(self, observation_data: Dict[str, Any]) -> Dict[str, float]:
        """
        Extract base velocity from observation data.
        """
        try:
            return {
                'x': observation_data.get('x.vel', 0.0),
                'y': observation_data.get('y.vel', 0.0),
                'theta': observation_data.get('theta.vel', 0.0)
            }
        except Exception as e:
            print(f"{self.controller_name}: Failed to extract base velocity: {e}")
            return {'x': 0.0, 'y': 0.0, 'theta': 0.0}

    def _get_xlerobot_joint_name(self, arm: str, joint_index: int) -> Optional[str]:
        """
        Map arm and joint index to XLeRobot joint name.
        """
        joint_mapping = {
            ('left', 0): 'left_arm_shoulder_pan.pos',
            ('left', 1): 'left_arm_shoulder_lift.pos',
            ('left', 2): 'left_arm_elbow_flex.pos',
            ('left', 3): 'left_arm_wrist_flex.pos',
            ('left', 4): 'left_arm_wrist_roll.pos',
            ('left', 5): 'left_arm_gripper.pos',
            ('right', 0): 'right_arm_shoulder_pan.pos',
            ('right', 1): 'right_arm_shoulder_lift.pos',
            ('right', 2): 'right_arm_elbow_flex.pos',
            ('right', 3): 'right_arm_wrist_flex.pos',
            ('right', 4): 'right_arm_wrist_roll.pos',
            ('right', 5): 'right_arm_gripper.pos',
        }
        return joint_mapping.get((arm, joint_index))

    def _update_local_velocity_state(self, direction: str, speed: float):
        """
        Update local velocity state for immediate feedback.
        """
        linear_speed = speed * 0.2
        angular_speed = speed * 30.0

        # Reset velocities
        self.robot_state['velocity']['linear'] = {'x': 0.0, 'y': 0.0, 'z': 0.0}
        self.robot_state['velocity']['angular'] = {'x': 0.0, 'y': 0.0, 'z': 0.0}

        # Set based on direction
        if direction == 'forward':
            self.robot_state['velocity']['linear']['x'] = linear_speed
        elif direction == 'backward':
            self.robot_state['velocity']['linear']['x'] = -linear_speed
        elif direction == 'left':
            self.robot_state['velocity']['linear']['y'] = linear_speed
        elif direction == 'right':
            self.robot_state['velocity']['linear']['y'] = -linear_speed
        elif direction == 'rotate_left':
            self.robot_state['velocity']['angular']['z'] = angular_speed
        elif direction == 'rotate_right':
            self.robot_state['velocity']['angular']['z'] = -angular_speed