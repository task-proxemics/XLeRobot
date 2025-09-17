# MuJoCo Robot Controller Implementation

import os
import sys
import time
import threading
import numpy as np
import base64
import traceback
from typing import Optional, Dict, Any

# Add MuJoCo simulation path
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../simulation/mujoco'))

from .base import RobotController

# Try to import MuJoCo and related modules
try:
    import mujoco
    import cv2
    MUJOCO_AVAILABLE = True
    print("MuJoCo modules loaded for controller")
except ImportError as e:
    print(f"MuJoCo not available: {e}")
    MUJOCO_AVAILABLE = False



class MuJoCoController(RobotController):
    # MuJoCo simulation robot controller
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        # Initialize MuJoCo controller
        super().__init__(config)
        
        # Configuration
        self.mjcf_path = config.get('mjcf_path') if config else None
        self.enable_viewer = config.get('enable_viewer', False) if config else False
        self.model = None
        self.data = None
        self.renderer = None
        
        # Simulation thread
        self.sim_thread = None
        self.running = False
        self.sim_lock = threading.Lock()
        
        # Control parameters
        self.abs_vel = np.array([1.0, 1.0, 1.0])
        self.chassis_ref_vel = np.zeros(3)
        self.qCmd = None
        self.qdCmd = None
        self.qFb = None
        self.qdFb = None
        self.kp = 1.0
        
        # Camera parameters
        self.frame_width = 640
        self.frame_height = 480
        self.camera_id = -1  # Use free camera since no cameras defined in model

        # Default camera settings for free camera (matching the original MuJoCo implementation)
        self.default_camera_distance = 3.0
        self.default_camera_azimuth = 90.0
        self.default_camera_elevation = -30.0
        self.default_camera_lookat = np.array([0.0, 0.0, 0.0])

        # Current camera settings
        self.current_camera_distance = self.default_camera_distance
        self.current_camera_azimuth = self.default_camera_azimuth
        self.current_camera_elevation = self.default_camera_elevation
        self.current_camera_lookat = self.default_camera_lookat.copy()

        # MuJoCo camera object (will be initialized in connect)
        self.camera = None
    
    async def connect(self) -> bool:
        """
        Connect to MuJoCo simulation.
        Connect to MuJoCo simulation.
        """
        # Use basic MuJoCo
        if MUJOCO_AVAILABLE:
            try:
                # Find model file
                if not self.mjcf_path:
                    base_dir = os.path.dirname(os.path.abspath(__file__))
                    self.mjcf_path = os.path.join(base_dir, '../../../simulation/mujoco/scene.xml')
                
                if os.path.exists(self.mjcf_path):
                    print(f"Loading MuJoCo model: {self.mjcf_path}")
                    self.model = mujoco.MjModel.from_xml_path(self.mjcf_path)
                    self.data = mujoco.MjData(self.model)
                    mujoco.mj_forward(self.model, self.data)
                    
                    # Initialize control arrays
                    self.qCmd = np.zeros(self.model.nu)
                    self.qdCmd = np.zeros(self.model.nu)
                    self.qFb = np.zeros(self.model.nu)
                    self.qdFb = np.zeros(self.model.nu)
                    
                    # Initialize renderer with proper dimensions
                    self.renderer = mujoco.Renderer(self.model, height=self.frame_height, width=self.frame_width)

                    # Initialize MuJoCo camera object (like in the original implementation)
                    self.camera = mujoco.MjvCamera()
                    mujoco.mjv_defaultCamera(self.camera)
                    self.camera.type = mujoco.mjtCamera.mjCAMERA_TRACKING  # Track the robot
                    self.camera.trackbodyid = self.model.body("chassis").id  # Track chassis body
                    self.camera.distance = self.default_camera_distance
                    self.camera.azimuth = self.default_camera_azimuth
                    self.camera.elevation = self.default_camera_elevation
                    self.camera.lookat[:] = self.default_camera_lookat

                    # Start simulation thread
                    self.running = True
                    self.sim_thread = threading.Thread(target=self._simulation_loop)
                    self.sim_thread.daemon = True
                    self.sim_thread.start()
                    
                    self.connected = True
                    print("Connected via basic MuJoCo")
                    return True
                else:
                    print(f"Model file not found: {self.mjcf_path}")
            except Exception as e:
                print(f"MuJoCo initialization failed: {e}")
        
        # Mock mode
        self.connected = True
        print("Running in mock mode (no MuJoCo)")
        return True
    
    async def disconnect(self) -> bool:
        """
        Disconnect from MuJoCo simulation.
        Disconnect from MuJoCo simulation.
        """
        # Stop simulation thread
        if self.running:
            self.running = False
            if self.sim_thread:
                self.sim_thread.join(timeout=2.0)
        
        # Cleanup renderer
        if self.renderer:
            try:
                self.renderer.close()
            except:
                pass
            self.renderer = None
        
        self.connected = False
        print("Disconnected from MuJoCo")
        return True
    
    async def move(self, direction: str, speed: float = 1.0) -> Dict[str, Any]:
        """
        Control robot movement.
        Control robot movement.
        """
        if not self.connected:
            return {'status': 'error', 'message': 'Not connected'}
        
        # Validate input
        if not self.validate_direction(direction):
            return {'status': 'error', 'message': f'Invalid direction: {direction}'}
        
        speed = self.validate_speed(speed)
        
        # Use basic control
        with self.sim_lock:
            self.chassis_ref_vel = np.zeros(3)
            
            if direction == 'forward':
                self.chassis_ref_vel[0] = self.abs_vel[0] * speed
            elif direction == 'backward':
                self.chassis_ref_vel[0] = -self.abs_vel[0] * speed
            elif direction == 'left':
                self.chassis_ref_vel[1] = self.abs_vel[1] * speed
            elif direction == 'right':
                self.chassis_ref_vel[1] = -self.abs_vel[1] * speed
            elif direction == 'rotate_left':
                self.chassis_ref_vel[2] = self.abs_vel[2] * speed
            elif direction == 'rotate_right':
                self.chassis_ref_vel[2] = -self.abs_vel[2] * speed
            elif direction == 'stop':
                self.chassis_ref_vel = np.zeros(3)
            
            print(f"Move: direction={direction}, speed={speed}, ref_vel={self.chassis_ref_vel}")
            return {'status': 'success', 'direction': direction, 'speed': speed}
    
    async def stop(self) -> Dict[str, Any]:
        """
        Stop all movements.
        Stop all movement.
        """
        return await self.move('stop', 0)
    
    async def get_state(self) -> Dict[str, Any]:
        """
        Get current robot state.
        Get current robot status.
        """
        # Use basic state
        if self.data:
            with self.sim_lock:
                self.robot_state['position']['x'] = float(self.data.qpos[0]) if len(self.data.qpos) > 0 else 0
                self.robot_state['position']['y'] = float(self.data.qpos[1]) if len(self.data.qpos) > 1 else 0
                self.robot_state['position']['z'] = float(self.data.qpos[2]) if len(self.data.qpos) > 2 else 0
                
                if len(self.qdFb) >= 3:
                    self.robot_state['velocity']['linear']['x'] = float(self.qdFb[0])
                    self.robot_state['velocity']['linear']['y'] = float(self.qdFb[1])
                    self.robot_state['velocity']['linear']['z'] = float(self.qdFb[2])
                
                self.robot_state['status'] = 'running' if self.running else 'stopped'
        
        return self.robot_state
    
    async def get_camera_frame(self) -> Optional[np.ndarray]:
        """
        Get camera frame.
        Get camera frame.
        """
        # Use renderer with MuJoCo camera object
        if MUJOCO_AVAILABLE and self.renderer and self.data and self.camera:
            try:
                with self.sim_lock:
                    # Update scene with our camera object
                    self.renderer.update_scene(self.data, camera=self.camera)
                    pixels = self.renderer.render()

                    # Apply vertical flip (MuJoCo convention)
                    if pixels is not None:
                        pixels = np.flipud(pixels)

                    return pixels
            except Exception as e:
                print(f"Camera frame error: {e}")

        # Mock mode - return test pattern
        test_frame = np.random.randint(0, 255, (self.frame_height, self.frame_width, 3), dtype=np.uint8)
        return test_frame
    
    async def get_camera_frame_base64(self) -> Optional[str]:
        """
        Get base64 encoded camera frame.
        Get Base64 encoded camera frame.
        """
        # Get frame and encode
        frame = await self.get_camera_frame()
        if frame is not None:
            try:
                # Convert to JPEG
                success, buffer = cv2.imencode('.jpg', frame)
                if success:
                    return base64.b64encode(buffer).decode('utf-8')
            except Exception as e:
                print(f"Base64 encoding error: {e}")
        
        return None
    
    async def set_arm_joint(self, arm: str, joint_index: int, angle: float) -> Dict[str, Any]:
        """
        Set arm joint angle.
        Set robot arm joint angles.
        """
        if not self.validate_arm_parameters(arm, joint_index):
            return {'status': 'error', 'message': 'Invalid arm parameters'}
        
        self.robot_state['arm_joints'][arm][joint_index] = angle

        return {
            'status': 'success',
            'arm': arm,
            'joint': joint_index,
            'angle': angle,
            'message': 'Arm control not yet implemented in MuJoCo'
        }
    
    def _simulation_loop(self):
        """
        Simulation main loop.
        Main simulation loop.
        """
        if not self.model or not self.data:
            return
        
        time_step = self.model.opt.timestep
        
        while self.running:
            with self.sim_lock:
                # Update feedback
                self.qFb = self.data.qpos
                self.qdFb = self.data.qvel
                
                # Update control
                self._update_control()
                
                # Step simulation
                mujoco.mj_step(self.model, self.data)
            
            time.sleep(time_step)
    
    def _update_control(self):
        """
        Update robot control.
        Update robot control.
        """
        if not self.model or len(self.qFb) < 3:
            return
        
        # Get yaw angle
        yaw = self.qFb[2] if len(self.qFb) > 2 else 0
        
        # Rotation matrix
        rotmz = np.array([
            [np.cos(yaw), np.sin(yaw), 0],
            [-np.sin(yaw), np.cos(yaw), 0],
            [0, 0, 1]
        ])
        
        # Get chassis velocity
        chassis_vel = rotmz @ self.qdFb[0:3] if len(self.qdFb) >= 3 else np.zeros(3)
        
        # PID control
        k_p = 10
        k_p_rot = 100
        
        # Calculate velocity command
        self.qdCmd[0] = (self.chassis_ref_vel[0] * np.cos(yaw) + 
                        self.chassis_ref_vel[1] * np.cos(yaw + 1.5708) + 
                        k_p * (self.chassis_ref_vel[0] - chassis_vel[0]) * np.cos(yaw) + 
                        k_p * (self.chassis_ref_vel[1] - chassis_vel[1]) * np.cos(yaw + 1.5708))
        
        self.qdCmd[1] = (self.chassis_ref_vel[0] * np.sin(yaw) + 
                        self.chassis_ref_vel[1] * np.sin(yaw + 1.5708) + 
                        k_p * (self.chassis_ref_vel[0] - chassis_vel[0]) * np.sin(yaw) + 
                        k_p * (self.chassis_ref_vel[1] - chassis_vel[1]) * np.sin(yaw + 1.5708))
        
        self.qdCmd[2] = self.chassis_ref_vel[2] + k_p_rot * (self.chassis_ref_vel[2] - chassis_vel[2])
        
        # Apply control
        self.qdCmd[0:3] = self.kp * self.qdCmd[0:3]
        if len(self.data.ctrl) >= 3:
            self.data.ctrl[:3] = self.qdCmd[:3]
    
    async def reset_camera(self) -> Dict[str, Any]:
        """
        Reset camera to default view position.
        Reset camera to default view position.
        """
        try:
            # Reset camera settings to defaults
            self.current_camera_distance = self.default_camera_distance
            self.current_camera_azimuth = self.default_camera_azimuth
            self.current_camera_elevation = self.default_camera_elevation
            self.current_camera_lookat = self.default_camera_lookat.copy()

            # Apply to MuJoCo camera object if available
            if MUJOCO_AVAILABLE and self.camera:
                with self.sim_lock:
                    # Reset camera parameters using MuJoCo camera object
                    self.camera.type = mujoco.mjtCamera.mjCAMERA_TRACKING  # Ensure tracking mode
                    self.camera.trackbodyid = self.model.body("chassis").id  # Track chassis body
                    self.camera.distance = self.default_camera_distance
                    self.camera.azimuth = self.default_camera_azimuth
                    self.camera.elevation = self.default_camera_elevation
                    self.camera.lookat[:] = self.default_camera_lookat

            return {
                'status': 'success',
                'message': 'Camera reset to default position',
                'distance': self.current_camera_distance,
                'azimuth': self.current_camera_azimuth,
                'elevation': self.current_camera_elevation,
                'lookat': self.current_camera_lookat.tolist()
            }
        except Exception as e:
            return {
                'status': 'error',
                'message': f'Failed to reset camera: {str(e)}'
            }

    async def set_camera_position(self, position: tuple, target: tuple = None) -> Dict[str, Any]:
        """
        Set camera position and target.
        Set camera position and target.
        """
        try:
            # Convert to numpy arrays
            new_position = np.array(position)
            new_target = np.array(target) if target else self.current_camera_target.copy()

            # Update current camera settings
            self.current_camera_position = new_position
            self.current_camera_target = new_target

            # Apply to renderer if available
            if MUJOCO_AVAILABLE and self.renderer:
                with self.sim_lock:
                    # Set camera parameters for free camera
                    self.renderer.camera.lookat[:] = self.current_camera_target
                    self.renderer.camera.distance = np.linalg.norm(self.current_camera_position - self.current_camera_target)

                    # Calculate azimuth and elevation
                    diff = self.current_camera_position - self.current_camera_target
                    distance = np.linalg.norm(diff)
                    if distance > 0:
                        self.renderer.camera.azimuth = np.degrees(np.arctan2(diff[1], diff[0]))
                        self.renderer.camera.elevation = np.degrees(np.arcsin(diff[2] / distance))

            return {
                'status': 'success',
                'message': 'Camera position updated',
                'position': self.current_camera_position.tolist(),
                'target': self.current_camera_target.tolist()
            }
        except Exception as e:
            return {
                'status': 'error',
                'message': f'Failed to set camera position: {str(e)}'
            }

    async def get_camera_info(self) -> Dict[str, Any]:
        """
        Get current camera information.
        Get current camera information.
        """
        camera_info = {
            'position': self.current_camera_position.tolist(),
            'target': self.current_camera_target.tolist(),
            'camera_id': self.camera_id,
            'frame_size': {'width': self.frame_width, 'height': self.frame_height},
            'default_position': self.default_camera_position.tolist(),
            'default_target': self.default_camera_target.tolist()
        }

        # Add renderer-specific info if available
        if MUJOCO_AVAILABLE and self.renderer:
            try:
                with self.sim_lock:
                    camera_info.update({
                        'distance': float(self.renderer.camera.distance),
                        'azimuth': float(self.renderer.camera.azimuth),
                        'elevation': float(self.renderer.camera.elevation),
                        'lookat': self.renderer.camera.lookat.tolist()
                    })
            except Exception as e:
                camera_info['renderer_error'] = str(e)

        return camera_info

    def get_capabilities(self) -> Dict[str, bool]:
        """
        Get controller capabilities.
        Get controller capabilities.
        """
        capabilities = super().get_capabilities()
        capabilities.update({
            'simulation': True,
            'real_robot': False,
            'mujoco': MUJOCO_AVAILABLE
        })
        return capabilities