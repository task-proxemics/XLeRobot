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
    print("✅ MuJoCo modules loaded for controller")
except ImportError as e:
    print(f"⚠️ MuJoCo not available: {e}")
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
        self.camera_id = 0
    
    async def connect(self) -> bool:
        """
        Connect to MuJoCo simulation.
        连接到MuJoCo仿真。
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
                    
                    # Initialize renderer
                    self.renderer = mujoco.Renderer(self.model)
                    
                    # Start simulation thread
                    self.running = True
                    self.sim_thread = threading.Thread(target=self._simulation_loop)
                    self.sim_thread.daemon = True
                    self.sim_thread.start()
                    
                    self.connected = True
                    print("✅ Connected via basic MuJoCo")
                    return True
                else:
                    print(f"❌ Model file not found: {self.mjcf_path}")
            except Exception as e:
                print(f"❌ MuJoCo initialization failed: {e}")
        
        # Mock mode
        self.connected = True
        print("⚠️ Running in mock mode (no MuJoCo)")
        return True
    
    async def disconnect(self) -> bool:
        """
        Disconnect from MuJoCo simulation.
        断开MuJoCo仿真连接。
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
        print("✅ Disconnected from MuJoCo")
        return True
    
    async def move(self, direction: str, speed: float = 1.0) -> Dict[str, Any]:
        """
        Control robot movement.
        控制机器人移动。
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
        停止所有运动。
        """
        return await self.move('stop', 0)
    
    async def get_state(self) -> Dict[str, Any]:
        """
        Get current robot state.
        获取机器人当前状态。
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
        获取摄像头画面。
        """
        # Use basic renderer
        if MUJOCO_AVAILABLE and self.renderer and self.data:
            try:
                with self.sim_lock:
                    self.renderer.update_scene(self.data, camera=self.camera_id)
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
        获取Base64编码的摄像头画面。
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
        设置机械臂关节角度。
        """
        if not self.validate_arm_parameters(arm, joint_index):
            return {'status': 'error', 'message': 'Invalid arm parameters'}
        
        # Update internal state
        self.robot_state['arm_joints'][arm][joint_index] = angle
        
        # TODO: Implement actual joint control when arm model is available
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
        仿真主循环。
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
        更新机器人控制。
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
    
    def get_capabilities(self) -> Dict[str, bool]:
        """
        Get controller capabilities.
        获取控制器能力。
        """
        capabilities = super().get_capabilities()
        capabilities.update({
            'simulation': True,
            'real_robot': False,
            'mujoco': MUJOCO_AVAILABLE
        })
        return capabilities