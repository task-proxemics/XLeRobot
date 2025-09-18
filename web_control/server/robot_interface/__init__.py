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

# Import controllers with exception handling to avoid dependency issues
try:
    from .mujoco_controller import MuJoCoController
except ImportError:
    MuJoCoController = None

try:
    from .maniskill_controller import ManiSkillController
except ImportError:
    ManiSkillController = None

try:
    from .real_controller import RealRobotController
except ImportError:
    RealRobotController = None

# For backward compatibility
from .factory import get_or_create_controller as get_or_create_robot_controller

# Dynamic __all__ list based on available controllers
__all__ = [
    'RobotController',
    'RobotControllerFactory',
    'get_or_create_controller',
    'get_or_create_robot_controller',
    'get_current_controller',
    'cleanup_controller'
]

# Add available controllers to __all__
if MuJoCoController is not None:
    __all__.append('MuJoCoController')
if ManiSkillController is not None:
    __all__.append('ManiSkillController')
if RealRobotController is not None:
    __all__.append('RealRobotController')

print("Robot interface module loaded with optional dependencies")