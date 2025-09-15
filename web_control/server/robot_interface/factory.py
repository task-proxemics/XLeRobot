# Robot Controller Factory

from typing import Optional, Dict, Any
from .base import RobotController

# Import controllers with exception handling
try:
    from .maniskill_controller import ManiSkillController
    MANISKILL_CONTROLLER_AVAILABLE = True
except ImportError as e:
    print(f"⚠️ ManiSkill controller not available: {e}")
    MANISKILL_CONTROLLER_AVAILABLE = False
    ManiSkillController = None

try:
    from .mujoco_controller import MuJoCoController
    MUJOCO_CONTROLLER_AVAILABLE = True
except ImportError as e:
    print(f"⚠️ MuJoCo controller not available: {e}")
    MUJOCO_CONTROLLER_AVAILABLE = False
    MuJoCoController = None

try:
    from .real_controller import RealRobotController
    REAL_CONTROLLER_AVAILABLE = True
except ImportError as e:
    print(f"⚠️ Real robot controller not available: {e}")
    REAL_CONTROLLER_AVAILABLE = False
    RealRobotController = None


class RobotControllerFactory:
    # Factory class for creating robot controllers
    
    # Available controller types (only include those that are available)
    @classmethod
    def _get_controller_types(cls) -> Dict[str, type]:
        # Get available controller types dynamically
        controller_types = {}

        if MANISKILL_CONTROLLER_AVAILABLE and ManiSkillController is not None:
            controller_types['maniskill'] = ManiSkillController

        if MUJOCO_CONTROLLER_AVAILABLE and MuJoCoController is not None:
            controller_types['mujoco'] = MuJoCoController

        if REAL_CONTROLLER_AVAILABLE and RealRobotController is not None:
            controller_types['real'] = RealRobotController
            controller_types['xlerobot'] = RealRobotController  # Alias

        return controller_types
    
    @classmethod
    def create_controller(cls, 
                         controller_type: str = 'mujoco',
                         config: Optional[Dict[str, Any]] = None) -> RobotController:
        # Create a robot controller instance
        controller_type = controller_type.lower()
        controller_types = cls._get_controller_types()

        if controller_type not in controller_types:
            available = ', '.join(controller_types.keys()) if controller_types else 'None'
            raise ValueError(
                f"Unsupported controller type: '{controller_type}'. "
                f"Available types: {available}"
            )

        controller_class = controller_types[controller_type]
        
        print(f"🏭 Creating {controller_type} controller...")
        
        # Create and return controller instance
        controller = controller_class(config)
        
        print(f"✅ {controller_type} controller created successfully")
        
        return controller
    
    @classmethod
    def get_available_controllers(cls) -> Dict[str, str]:
        # Get list of available controller types
        return {
            'mujoco': 'MuJoCo physics simulation (fully implemented)',
            'maniskill': 'ManiSkill robot learning platform (placeholder)',
            'real': 'Real robot hardware control (placeholder)',
            'xlerobot': 'XLeRobot hardware (alias for real)'
        }
    
    @classmethod
    def get_controller_info(cls, controller_type: str) -> Dict[str, Any]:
        # Get detailed information about a controller type
        controller_type = controller_type.lower()
        controller_types = cls._get_controller_types()

        if controller_type not in controller_types:
            return {'error': f'Unknown controller type: {controller_type}'}

        # Create temporary instance to get capabilities
        try:
            temp_controller = controller_types[controller_type]()
            capabilities = temp_controller.get_capabilities()
            controller_name = temp_controller.get_controller_type()
        except:
            capabilities = {}
            controller_name = controller_type
        
        info = {
            'type': controller_type,
            'class_name': controller_name,
            'capabilities': capabilities,
            'description': cls.get_available_controllers().get(controller_type, ''),
            'status': 'implemented' if capabilities.get('implemented', True) else 'placeholder'
        }
        
        # Add specific configuration requirements
        if controller_type == 'mujoco':
            info['config_options'] = {
                'mjcf_path': 'Path to MuJoCo model file',
                'enable_viewer': 'Enable GUI viewer window'
            }
        elif controller_type == 'maniskill':
            info['config_options'] = {
                'env_name': 'ManiSkill environment name',
                'robot_name': 'Robot model to use'
            }
        elif controller_type in ['real', 'xlerobot']:
            info['config_options'] = {
                'robot_ip': 'IP address of the robot',
                'robot_port': 'Communication port',
                'serial_port': 'Serial port for USB connection',
                'robot_type': 'Type of real robot'
            }
        
        return info


# Global controller instance management
_global_controller: Optional[RobotController] = None


def get_or_create_controller(controller_type: str = 'mujoco',
                            config: Optional[Dict[str, Any]] = None,
                            force_new: bool = False) -> RobotController:
    # Get existing controller or create a new one
    global _global_controller
    
    if force_new or _global_controller is None:
        # Cleanup existing controller if forcing new
        if _global_controller is not None and force_new:
            try:
                import asyncio
                asyncio.run(_global_controller.disconnect())
            except:
                pass
        
        # Create new controller
        _global_controller = RobotControllerFactory.create_controller(
            controller_type, config
        )
    
    return _global_controller


def get_current_controller() -> Optional[RobotController]:
    # Get the current global controller instance
    return _global_controller


def cleanup_controller():
    # Cleanup and disconnect the global controller
    global _global_controller
    
    if _global_controller is not None:
        try:
            import asyncio
            asyncio.run(_global_controller.disconnect())
        except:
            pass
        finally:
            _global_controller = None
            print("✅ Global controller cleaned up")