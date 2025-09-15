"""
Robot Interface Module

This module provides a unified interface for controlling different types of robots.
"""

from .base import RobotController
from .factory import (
    RobotControllerFactory,
    get_or_create_controller,
    get_current_controller,
    cleanup_controller
)
from .mujoco_controller import MuJoCoController
from .maniskill_controller import ManiSkillController
from .real_controller import RealRobotController

# For backward compatibility
from .factory import get_or_create_controller as get_or_create_robot_controller

__all__ = [
    'RobotController',
    'RobotControllerFactory',
    'MuJoCoController',
    'ManiSkillController', 
    'RealRobotController',
    'get_or_create_controller',
    'get_or_create_robot_controller',
    'get_current_controller',
    'cleanup_controller'
]

print("Robot interface module loaded with new architecture")