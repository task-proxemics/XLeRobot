import asyncio
import sys
import os
import numpy as np
import torch
import base64
import cv2
from typing import Optional, Dict, Any
from pathlib import Path
from .base import RobotController

sim_path = Path(__file__).parent.parent.parent.parent / "simulation" / "Maniskill"
if sim_path.exists():
    sys.path.insert(0, str(sim_path))

try:
    import gymnasium as gym
    import mani_skill.envs
    from mani_skill.envs.sapien_env import BaseEnv
    from agents.xlerobot import xlerobot_single
    MANISKILL_AVAILABLE = True
    print("ManiSkill imported successfully")
except ImportError as e:
    print(f"ManiSkill import error: {e}")
    MANISKILL_AVAILABLE = False


class ManiSkillController(RobotController):

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        super().__init__(config)
        self.controller_name = "ManiSkill Controller"
        self.env: Optional[BaseEnv] = None
        self.current_action = None
        self.episode_step = 0
        self.max_episode_steps = 200

        self.env_id = config.get('env_id', 'PushCube-v1') if config else 'PushCube-v1'
        self.obs_mode = config.get('obs_mode', 'sensor_data') if config else 'sensor_data'
        self.render_mode = config.get('render_mode', 'rgb_array') if config else 'rgb_array'
        self.enable_viewer = config.get('enable_viewer', False) if config else False

        self.continuous_control = {
            'enabled': False,
            'direction': None,
            'speed': 0.0,
            'accumulator': None,
            'last_update': 0.0,
            'decay_factor': 0.85,
            'update_strength': 0.3
        }

        print(f"{self.controller_name} initialized")
        print(f"   Environment: {self.env_id}")
        print(f"   Observation mode: {self.obs_mode}")
        print(f"   Continuous control: enabled")

    async def connect(self) -> bool:
        if not MANISKILL_AVAILABLE:
            print(f"{self.controller_name}: ManiSkill not available")
            return False

        try:
            print(f"{self.controller_name}: Creating ManiSkill environment...")

            env_kwargs = {
                'obs_mode': self.obs_mode,
                'robot_uids': 'xlerobot_single',
                'render_mode': self.render_mode,
                'num_envs': 1,
                'sim_backend': 'auto',
            }

            if self.enable_viewer:
                env_kwargs['render_mode'] = 'human'

            self.env = gym.make(self.env_id, **env_kwargs)

            self.obs, _ = self.env.reset(seed=2024)


            if self.env.action_space is not None:
                self.current_action = np.zeros(self.env.action_space.shape[0])
            else:
                self.current_action = np.zeros(10)

            self.continuous_control['accumulator'] = np.zeros_like(self.current_action)

            self.connected = True
            self.robot_state['status'] = 'connected'
            self.episode_step = 0

            print(f"{self.controller_name}: Connected to ManiSkill")
            print(f"   Action space: {self.env.action_space}")
            print(f"   Observation space: {self.env.observation_space}")

            if "sensor_data" in self.obs:
                cameras = list(self.obs["sensor_data"].keys())
                print(f"   Available cameras: {cameras}")

            return True

        except Exception as e:
            print(f"{self.controller_name}: Connection failed - {e}")
            import traceback
            traceback.print_exc()
            self.connected = False
            return False

    async def disconnect(self) -> bool:
        try:
            if self.env is not None:
                self.env.close()
                self.env = None

            self.connected = False
            self.robot_state['status'] = 'disconnected'
            print(f"{self.controller_name}: Disconnected")
            return True

        except Exception as e:
            print(f"{self.controller_name}: Disconnect error - {e}")
            return False

    async def move(self, direction: str, speed: float = 1.0) -> Dict[str, Any]:
        if not self.connected or self.env is None:
            return {'status': 'error', 'message': 'Not connected to ManiSkill'}

        if not self.validate_direction(direction):
            return {'status': 'error', 'message': f'Invalid direction: {direction}'}

        speed = self.validate_speed(speed)

        import time
        current_time = time.time()

        if direction == 'stop':
            self.continuous_control['enabled'] = False
            self.continuous_control['direction'] = None
            self.continuous_control['speed'] = 0.0
            self.continuous_control['accumulator'] *= 0.5
        else:
            self.continuous_control['enabled'] = True
            self.continuous_control['direction'] = direction
            self.continuous_control['speed'] = speed
            self.continuous_control['last_update'] = current_time

        self._update_action_accumulator(direction, speed)

        self.current_action = self.continuous_control['accumulator'].copy()

        try:
            self.obs, reward, terminated, truncated, info = self.env.step(self.current_action)
            self.episode_step += 1

            if terminated or truncated or self.episode_step >= self.max_episode_steps:
                print(f"{self.controller_name}: Episode ended, resetting...")
                await self._reset_environment()

            self._update_state_from_obs()

            return {
                'status': 'success',
                'direction': direction,
                'speed': speed,
                'continuous_mode': self.continuous_control['enabled'],
                'episode_step': self.episode_step,
                'reward': float(reward) if reward is not None else 0.0,
                'action_magnitude': float(np.linalg.norm(self.current_action))
            }

        except Exception as e:
            print(f"{self.controller_name}: Move error - {e}")
            return {'status': 'error', 'message': str(e)}

    async def stop(self) -> Dict[str, Any]:
        # Stop all movements
        return await self.move('stop', 0)

    async def get_state(self) -> Dict[str, Any]:
        state = self.robot_state.copy()
        state['controller'] = self.controller_name
        state['simulation_engine'] = 'ManiSkill3'
        state['physics_engine'] = 'SAPIEN'
        state['environment'] = self.env_id
        state['episode_step'] = self.episode_step
        state['max_episode_steps'] = self.max_episode_steps

        if self.current_action is not None:
            state['current_action'] = self.current_action.tolist()

        return state

    async def get_camera_frame(self) -> Optional[np.ndarray]:
        if not self.connected or self.env is None or self.obs is None:
            return None

        try:
            if "sensor_data" in self.obs:
                if "fetch_head" in self.obs["sensor_data"]:
                    camera_data = self.obs["sensor_data"]["fetch_head"]

                    # Get Color/RGB data
                    rgb_data = None
                    if "Color" in camera_data:
                        rgb_data = camera_data["Color"]
                    elif "rgb" in camera_data:
                        rgb_data = camera_data["rgb"]

                    if rgb_data is not None:
                        # Convert tensor to numpy
                        if hasattr(rgb_data, 'cpu'):
                            rgb_array = rgb_data.cpu().numpy()
                        elif hasattr(rgb_data, 'numpy'):
                            rgb_array = rgb_data.numpy()
                        else:
                            rgb_array = np.array(rgb_data)

                        # Handle batch dimension
                        if rgb_array.ndim == 4:
                            rgb_array = rgb_array[0]  # Take first batch

                        # Remove alpha channel if present (RGBA -> RGB)
                        if rgb_array.shape[-1] == 4:
                            rgb_array = rgb_array[..., :3]

                        # Ensure uint8 type
                        if rgb_array.dtype != np.uint8:
                            if rgb_array.max() <= 1.0:
                                rgb_array = (rgb_array * 255).astype(np.uint8)
                            else:
                                rgb_array = rgb_array.astype(np.uint8)

                        return rgb_array
                else:
                    # List available cameras for debugging
                    available_cameras = list(self.obs["sensor_data"].keys())
                    print(f"fetch_head not found. Available cameras: {available_cameras}")

                    # Try to use first available camera as fallback
                    if available_cameras:
                        first_camera = available_cameras[0]
                        print(f"   Using fallback camera: {first_camera}")
                        camera_data = self.obs["sensor_data"][first_camera]

                        # Similar processing as above
                        rgb_data = camera_data.get("Color") or camera_data.get("rgb")
                        if rgb_data is not None:
                            if hasattr(rgb_data, 'cpu'):
                                rgb_array = rgb_data.cpu().numpy()
                            elif hasattr(rgb_data, 'numpy'):
                                rgb_array = rgb_data.numpy()
                            else:
                                rgb_array = np.array(rgb_data)

                            if rgb_array.ndim == 4:
                                rgb_array = rgb_array[0]
                            if rgb_array.shape[-1] == 4:
                                rgb_array = rgb_array[..., :3]
                            if rgb_array.dtype != np.uint8:
                                if rgb_array.max() <= 1.0:
                                    rgb_array = (rgb_array * 255).astype(np.uint8)
                                else:
                                    rgb_array = rgb_array.astype(np.uint8)
                            return rgb_array

            # Fallback: try to render directly
            try:
                render_images = self.env.render()
                if render_images is not None:
                    if isinstance(render_images, dict) and 'fetch_head' in render_images:
                        rgb_array = render_images['fetch_head']
                    elif isinstance(render_images, np.ndarray):
                        rgb_array = render_images
                    else:
                        return None

                    # Ensure correct format
                    if hasattr(rgb_array, 'cpu'):
                        rgb_array = rgb_array.cpu().numpy()
                    elif hasattr(rgb_array, 'numpy'):
                        rgb_array = rgb_array.numpy()

                    if rgb_array.ndim == 4:
                        rgb_array = rgb_array[0]
                    if rgb_array.shape[-1] == 4:
                        rgb_array = rgb_array[..., :3]
                    if rgb_array.dtype != np.uint8:
                        if rgb_array.max() <= 1.0:
                            rgb_array = (rgb_array * 255).astype(np.uint8)
                        else:
                            rgb_array = rgb_array.astype(np.uint8)

                    return rgb_array
            except:
                pass

            return None

        except Exception as e:
            print(f"{self.controller_name}: Camera frame error - {e}")
            return None

    async def get_camera_frame_base64(self) -> Optional[str]:
        # Get base64 encoded camera frame
        frame = await self.get_camera_frame()
        if frame is not None:
            try:
                # Encode frame as JPEG
                success, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
                if success:
                    return base64.b64encode(buffer).decode('utf-8')
            except Exception as e:
                print(f"{self.controller_name}: Encoding error - {e}")
        return None

    async def set_arm_joint(self, arm: str, joint_index: int, angle: float) -> Dict[str, Any]:
        # Set arm joint angle
        if not self.connected or self.env is None:
            return {'status': 'error', 'message': 'Not connected'}

        if not self.validate_arm_parameters(arm, joint_index):
            return {'status': 'error', 'message': 'Invalid arm parameters'}

        # Map to action space
        # For XLeRobot single arm, joints are typically indexed from 2-7
        action_index = 2 + joint_index
        if action_index < len(self.current_action):
            # Use delta control
            current_angle = self.robot_state['arm_joints'][arm][joint_index]
            delta = angle - current_angle
            self.current_action[action_index] = np.clip(delta * 0.1, -0.1, 0.1)

            # Execute action
            self.obs, _, _, _, _ = self.env.step(self.current_action)
            self.episode_step += 1

            # Update state
            self.robot_state['arm_joints'][arm][joint_index] = angle
            self._update_state_from_obs()

        return {
            'status': 'success',
            'arm': arm,
            'joint': joint_index,
            'angle': angle
        }

    async def reset_camera(self) -> Dict[str, Any]:
        """
        Reset camera to default view position.
        Reset camera to default view position.
        """
        return {
            'status': 'success',
            'message': 'Camera reset not implemented in ManiSkill controller',
            'position': [2.0, 2.0, 2.0],
            'target': [0.0, 0.0, 0.0]
        }

    async def set_camera_position(self, position: tuple, target: tuple = None) -> Dict[str, Any]:
        """
        Set camera position and target.
        Set camera position and target.
        """
        return {
            'status': 'success',
            'message': 'Camera control not implemented in ManiSkill controller',
            'position': list(position),
            'target': list(target) if target else [0.0, 0.0, 0.0]
        }

    async def get_camera_info(self) -> Dict[str, Any]:
        """
        Get current camera information.
        Get current camera information.
        """
        return {
            'position': [2.0, 2.0, 2.0],
            'target': [0.0, 0.0, 0.0],
            'camera_id': 0,
            'frame_size': {'width': 640, 'height': 480},
            'default_position': [2.0, 2.0, 2.0],
            'default_target': [0.0, 0.0, 0.0],
            'message': 'Camera info from ManiSkill controller (limited support)'
        }

    def get_capabilities(self) -> Dict[str, bool]:
        # Get controller capabilities
        capabilities = super().get_capabilities()
        capabilities.update({
            'simulation': True,
            'real_robot': False,
            'maniskill': True,
            'sapien_physics': True,
            'implemented': True,
            'camera_streaming': True,
            'xlerobot': True
        })
        return capabilities

    def _update_state_from_obs(self):
        # Update robot state from observation
        if self.obs is None:
            return

        # Update state if we have state_dict observation
        if isinstance(self.obs, dict):
            if "agent" in self.obs:
                agent_obs = self.obs["agent"]
                if "qpos" in agent_obs:
                    # Update joint positions
                    qpos = agent_obs["qpos"]
                    if hasattr(qpos, 'cpu'):
                        qpos = qpos.cpu().numpy()
                    elif hasattr(qpos, 'numpy'):
                        qpos = qpos.numpy()

                    # Update base position (first 3 values typically)
                    if len(qpos) >= 3:
                        self.robot_state['position']['x'] = float(qpos[0])
                        self.robot_state['position']['y'] = float(qpos[1])
                        self.robot_state['rotation']['yaw'] = float(qpos[2])

                if "qvel" in agent_obs:
                    # Update velocities
                    qvel = agent_obs["qvel"]
                    if hasattr(qvel, 'cpu'):
                        qvel = qvel.cpu().numpy()
                    elif hasattr(qvel, 'numpy'):
                        qvel = qvel.numpy()

                    if len(qvel) >= 3:
                        self.robot_state['velocity']['linear']['x'] = float(qvel[0])
                        self.robot_state['velocity']['linear']['y'] = float(qvel[1])
                        self.robot_state['velocity']['angular']['z'] = float(qvel[2])

    def _update_action_accumulator(self, direction: str, speed: float):
        if self.continuous_control['accumulator'] is None:
            return

        # Apply decay to existing actions
        self.continuous_control['accumulator'] *= self.continuous_control['decay_factor']

        # Add new action component
        update_strength = self.continuous_control['update_strength'] * speed

        if direction == 'forward':
            self.continuous_control['accumulator'][0] += update_strength
        elif direction == 'backward':
            self.continuous_control['accumulator'][0] -= update_strength
        elif direction == 'left':
            self.continuous_control['accumulator'][1] += update_strength
        elif direction == 'right':
            self.continuous_control['accumulator'][1] -= update_strength
        elif direction == 'rotate_left':
            self.continuous_control['accumulator'][1] += update_strength
        elif direction == 'rotate_right':
            self.continuous_control['accumulator'][1] -= update_strength
        elif direction == 'stop':
            # More aggressive decay for stop
            self.continuous_control['accumulator'] *= 0.3

        # Clamp actions to valid range
        self.continuous_control['accumulator'] = np.clip(
            self.continuous_control['accumulator'], -1.0, 1.0
        )

    async def _reset_environment(self):
        """Reset environment and clear continuous control state"""
        self.obs, _ = self.env.reset()
        self.episode_step = 0
        self.current_action = np.zeros_like(self.current_action)

        # Reset continuous control state
        self.continuous_control['enabled'] = False
        self.continuous_control['direction'] = None
        self.continuous_control['speed'] = 0.0
        if self.continuous_control['accumulator'] is not None:
            self.continuous_control['accumulator'] = np.zeros_like(self.continuous_control['accumulator'])

    async def reset(self) -> Dict[str, Any]:
        # Reset robot to initial state
        if self.env is not None:
            await self._reset_environment()
            self._update_state_from_obs()
            return {'status': 'reset', 'message': 'Environment reset, continuous control disabled'}
        return {'status': 'error', 'message': 'No environment to reset'}