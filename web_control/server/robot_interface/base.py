from abc import ABC, abstractmethod
from typing import Optional, Dict, Any, Tuple
import numpy as np


class RobotController(ABC):

    def __init__(self, config: Optional[Dict[str, Any]] = None):
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
        pass
    
    @abstractmethod
    async def disconnect(self) -> bool:
        pass
    
    @abstractmethod
    async def move(self, direction: str, speed: float = 1.0) -> Dict[str, Any]:
        pass
    
    @abstractmethod
    async def stop(self) -> Dict[str, Any]:
        pass
    
    @abstractmethod
    async def get_state(self) -> Dict[str, Any]:
        pass
    
    @abstractmethod
    async def get_camera_frame(self) -> Optional[np.ndarray]:
        pass
    
    @abstractmethod
    async def get_camera_frame_base64(self) -> Optional[str]:
        pass
    
    @abstractmethod
    async def set_arm_joint(self, arm: str, joint_index: int, angle: float) -> Dict[str, Any]:
        pass

    @abstractmethod
    async def reset_camera(self) -> Dict[str, Any]:
        pass

    @abstractmethod
    async def set_camera_position(self, position: Tuple[float, float, float], target: Tuple[float, float, float] = None) -> Dict[str, Any]:
        pass

    @abstractmethod
    async def get_camera_info(self) -> Dict[str, Any]:
        pass
    
    def is_connected(self) -> bool:
        return self.connected
    
    def get_controller_type(self) -> str:
        return self.__class__.__name__
    
    def get_capabilities(self) -> Dict[str, bool]:
        return {
            'movement': True,
            'camera': True,
            'camera_control': True,
            'arm_control': True,
            'telemetry': True,
            'simulation': False,
            'real_robot': False
        }
    
    async def emergency_stop(self) -> Dict[str, Any]:
        return await self.stop()
    
    async def reset(self) -> Dict[str, Any]:
        await self.stop()
        return {'status': 'reset', 'message': 'Robot reset to initial state'}
    
    def validate_direction(self, direction: str) -> bool:
        valid_directions = ['forward', 'backward', 'left', 'right', 
                          'rotate_left', 'rotate_right', 'stop']
        return direction in valid_directions
    
    def validate_speed(self, speed: float) -> float:
        return max(0.0, min(1.0, speed))
    
    def validate_arm_parameters(self, arm: str, joint_index: int) -> bool:
        return arm in ['left', 'right'] and 0 <= joint_index < 6