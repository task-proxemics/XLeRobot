import os
from pathlib import Path
from typing import Dict, Any, Optional
from dataclasses import dataclass

try:
    from dotenv import load_dotenv

    env_path = Path('.env')
    if env_path.exists():
        load_dotenv(env_path)
        print(f"Loaded environment variables from {env_path.absolute()}")
    else:
        current_dir = Path(__file__).parent
        for parent in [current_dir, current_dir.parent, current_dir.parent.parent]:
            env_file = parent / '.env'
            if env_file.exists():
                load_dotenv(env_file)
                print(f"Loaded environment variables from {env_file.absolute()}")
                break
except ImportError:
    print("python-dotenv not installed. Environment variables will be read from system only.")

@dataclass
class RobotConfig:
    controller_type: str = "mujoco"
    use_mujoco_simulator: bool = True
    enable_viewer: bool = False
    mjcf_path: Optional[str] = None

@dataclass
class ServerConfig:
    host: str = "0.0.0.0"
    port: int = 8000
    reload: bool = True
    log_level: str = "info"

@dataclass
class VideoConfig:
    frame_width: int = 640
    frame_height: int = 480
    fps: int = 30
    quality: int = 80

@dataclass
class AppConfig:
    robot: RobotConfig
    server: ServerConfig
    video: VideoConfig

def load_config() -> AppConfig:

    robot_config = RobotConfig(
        controller_type=os.environ.get('ROBOT_CONTROLLER', 'mujoco'),
        use_mujoco_simulator=os.environ.get('USE_MUJOCO_SIMULATOR', 'true').lower() == 'true',
        enable_viewer=os.environ.get('ENABLE_VIEWER', 'false').lower() == 'true',
        mjcf_path=os.environ.get('MJCF_PATH', None)
    )

    server_config = ServerConfig(
        host=os.environ.get('SERVER_HOST', '0.0.0.0'),
        port=int(os.environ.get('SERVER_PORT', '8000')),
        reload=os.environ.get('SERVER_RELOAD', 'true').lower() == 'true',
        log_level=os.environ.get('LOG_LEVEL', 'info')
    )

    video_config = VideoConfig(
        frame_width=int(os.environ.get('VIDEO_WIDTH', '640')),
        frame_height=int(os.environ.get('VIDEO_HEIGHT', '480')),
        fps=int(os.environ.get('VIDEO_FPS', '30')),
        quality=int(os.environ.get('VIDEO_QUALITY', '80'))
    )

    return AppConfig(
        robot=robot_config,
        server=server_config,
        video=video_config
    )

def get_robot_controller_config() -> Dict[str, Any]:
    config = load_config()

    return {
        'enable_viewer': config.robot.enable_viewer,
        'use_mujoco_simulator': config.robot.use_mujoco_simulator,
        'mjcf_path': config.robot.mjcf_path,
        'frame_width': config.video.frame_width,
        'frame_height': config.video.frame_height,
        'fps': config.video.fps,
        'quality': config.video.quality
    }

app_config = load_config()

def print_config():
    config = load_config()
    print("XLeRobot Web Control Configuration:")
    print(f"Controller: {config.robot.controller_type}")
    print(f"MuJoCo Simulator: {'Enabled' if config.robot.use_mujoco_simulator else 'Disabled'}")
    print(f"Viewer: {'Enabled' if config.robot.enable_viewer else 'Disabled'}")
    print(f"Model Path: {config.robot.mjcf_path or 'Default (scene.xml)'}")
    print(f"Server: {config.server.host}:{config.server.port}")
    print(f"Video: {config.video.frame_width}x{config.video.frame_height} @ {config.video.fps}fps")

if __name__ == "__main__":
    print_config()