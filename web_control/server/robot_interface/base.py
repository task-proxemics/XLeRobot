# Abstract base class for robot controllers

from abc import ABC, abstractmethod
from typing import Optional, Dict, Any, Tuple
import numpy as np


class RobotController(ABC):
    # Abstract base class for robot controllers
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        # Initialize the robot controller
        self.config = config or {}
        self.connected = False
        self.robot_state = {
            'position': {'x': 0.0, 'y': 0.0, 'z': 0.0},
            'rotation': {'roll': 0.0, 'pitch': 0.0, 'yaw': 0.0},
            'velocity': {
                'linear': {'x': 0.0, 'y': 0.0, 'z': 0.0},
                'angular': {'x': 0.0, 'y': 0.0, 'z': 0.0}
            },
            'arm_joints': {
                'left': [0.0] * 6,
                'right': [0.0] * 6
            },
            'status': 'disconnected',
            'battery': 100.0,
            'temperature': 25.0
        }
    
    @abstractmethod
    async def connect(self) -> bool:
        # Connect to the robot
        pass
    
    @abstractmethod
    async def disconnect(self) -> bool:
        # Disconnect from the robot
        pass
    
    @abstractmethod
    async def move(self, direction: str, speed: float = 1.0) -> Dict[str, Any]:
        # Control robot movement
        pass
    
    @abstractmethod
    async def stop(self) -> Dict[str, Any]:
        # Stop all robot movements
        pass
    
    @abstractmethod
    async def get_state(self) -> Dict[str, Any]:
        # Get current robot state
        pass
    
    @abstractmethod
    async def get_camera_frame(self) -> Optional[np.ndarray]:
        # Get camera frame as numpy array
        pass
    
    @abstractmethod
    async def get_camera_frame_base64(self) -> Optional[str]:
        # Get camera frame as base64 encoded string
        pass
    
    @abstractmethod
    async def set_arm_joint(self, arm: str, joint_index: int, angle: float) -> Dict[str, Any]:
        # Set arm joint angle
        pass
    
    # Common utility methods that can be overridden if needed
    
    def is_connected(self) -> bool:
        # Check if robot is connected
        return self.connected
    
    def get_controller_type(self) -> str:
        # Get the type of controller
        return self.__class__.__name__
    
    def get_capabilities(self) -> Dict[str, bool]:
        # Get controller capabilities
        return {
            'movement': True,
            'camera': True,
            'arm_control': True,
            'telemetry': True,
            'simulation': False,  # Override in simulation controllers
            'real_robot': False   # Override in real robot controller
        }
    
    async def emergency_stop(self) -> Dict[str, Any]:
        # Emergency stop
        return await self.stop()
    
    async def reset(self) -> Dict[str, Any]:
        # Reset robot to initial state
        # Default implementation - can be overridden
        await self.stop()
        return {'status': 'reset', 'message': 'Robot reset to initial state'}
    
    def validate_direction(self, direction: str) -> bool:
        # Validate movement direction
        valid_directions = ['forward', 'backward', 'left', 'right', 
                          'rotate_left', 'rotate_right', 'stop']
        return direction in valid_directions
    
    def validate_speed(self, speed: float) -> float:
        # Validate and clamp speed value
        return max(0.0, min(1.0, speed))
    
    def validate_arm_parameters(self, arm: str, joint_index: int) -> bool:
        # Validate arm control parameters
        return arm in ['left', 'right'] and 0 <= joint_index < 6