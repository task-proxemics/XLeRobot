# To Run on the host
'''
PYTHONPATH=src python -m lerobot.robots.xlerobot.xlerobot_host --robot.id=my_xlerobot
'''

# To Run the teleop:
'''
PYTHONPATH=src python -m examples.xlerobot.teleoperate_joycon
'''

import time
import numpy as np
import math

from lerobot.robots.xlerobot import XLerobotConfig, XLerobot
from lerobot.utils.robot_utils import busy_wait
from lerobot.utils.visualization_utils import _init_rerun, log_rerun_data
from lerobot.model.SO101Robot import SO101Kinematics
from joyconrobotics import JoyconRobotics

LEFT_JOINT_MAP = {
    "shoulder_pan": "left_arm_shoulder_pan",
    "shoulder_lift": "left_arm_shoulder_lift",
    "elbow_flex": "left_arm_elbow_flex",
    "wrist_flex": "left_arm_wrist_flex",
    "wrist_roll": "left_arm_wrist_roll",
    "gripper": "left_arm_gripper",
}
RIGHT_JOINT_MAP = {
    "shoulder_pan": "right_arm_shoulder_pan",
    "shoulder_lift": "right_arm_shoulder_lift",
    "elbow_flex": "right_arm_elbow_flex",
    "wrist_flex": "right_arm_wrist_flex",
    "wrist_roll": "right_arm_wrist_roll",
    "gripper": "right_arm_gripper",
}

HEAD_MOTOR_MAP = {
    "head_motor_1": "head_motor_1",
    "head_motor_2": "head_motor_2",
}

class FixedAxesJoyconRobotics(JoyconRobotics):
    def __init__(self, device, **kwargs):
        super().__init__(device, **kwargs)
        
        # Set different center values for left and right Joy-Cons
        if self.joycon.is_right():
            self.joycon_stick_v_0 = 1900
            self.joycon_stick_h_0 = 2100
        else:  # left Joy-Con
            self.joycon_stick_v_0 = 2300
            self.joycon_stick_h_0 = 2000
    
    def common_update(self):
        # 修改后的更新逻辑：摇杆只控制固定轴向
        speed_scale = 0.0011
        
        # 垂直摇杆：控制X轴和Z轴（前后）
        joycon_stick_v = self.joycon.get_stick_right_vertical() if self.joycon.is_right() else self.joycon.get_stick_left_vertical()
        joycon_stick_v_threshold = 300
        joycon_stick_v_range = 1000
        if joycon_stick_v > joycon_stick_v_threshold + self.joycon_stick_v_0:
            self.position[0] += speed_scale * (joycon_stick_v - self.joycon_stick_v_0) / joycon_stick_v_range *self.dof_speed[0] * self.direction_reverse[0] * self.direction_vector[0]
            self.position[2] += speed_scale * (joycon_stick_v - self.joycon_stick_v_0) / joycon_stick_v_range *self.dof_speed[1] * self.direction_reverse[1] * self.direction_vector[2]
        elif joycon_stick_v < self.joycon_stick_v_0 - joycon_stick_v_threshold:
            self.position[0] += speed_scale * (joycon_stick_v - self.joycon_stick_v_0) / joycon_stick_v_range *self.dof_speed[0] * self.direction_reverse[0] * self.direction_vector[0]
            self.position[2] += speed_scale * (joycon_stick_v - self.joycon_stick_v_0) / joycon_stick_v_range *self.dof_speed[1] * self.direction_reverse[1] * self.direction_vector[2]
        
        # 水平摇杆：只控制Y轴（左右）  
        joycon_stick_h = self.joycon.get_stick_right_horizontal() if self.joycon.is_right() else self.joycon.get_stick_left_horizontal()
        joycon_stick_h_threshold = 300
        joycon_stick_h_range = 1000
        if joycon_stick_h > joycon_stick_h_threshold + self.joycon_stick_h_0:
            self.position[1] += speed_scale * (joycon_stick_h - self.joycon_stick_h_0) / joycon_stick_h_range * self.dof_speed[1] * self.direction_reverse[1]
        elif joycon_stick_h < self.joycon_stick_h_0 - joycon_stick_h_threshold:
            self.position[1] += speed_scale * (joycon_stick_h - self.joycon_stick_h_0) / joycon_stick_h_range * self.dof_speed[1] * self.direction_reverse[1]
        
        # Z轴按钮控制
        joycon_button_up = self.joycon.get_button_r() if self.joycon.is_right() else self.joycon.get_button_l()
        if joycon_button_up == 1:
            self.position[2] += speed_scale * self.dof_speed[2] * self.direction_reverse[2]
        
        joycon_button_down = self.joycon.get_button_r_stick() if self.joycon.is_right() else self.joycon.get_button_l_stick()
        if joycon_button_down == 1:
            self.position[2] -= speed_scale * self.dof_speed[2] * self.direction_reverse[2]
        
        # Home按钮重置逻辑（简化版）
        joycon_button_home = self.joycon.get_button_home() if self.joycon.is_right() else self.joycon.get_button_capture()
        if joycon_button_home == 1:
            self.position = self.offset_position_m.copy()
        
        # 夹爪控制逻辑（复制原来的）
        for event_type, status in self.button.events():
            if (self.joycon.is_right() and event_type == 'plus' and status == 1) or (self.joycon.is_left() and event_type == 'minus' and status == 1):
                self.reset_button = 1
                self.reset_joycon()
            elif self.joycon.is_right() and event_type == 'a':
                self.next_episode_button = status
            elif self.joycon.is_right() and event_type == 'y':
                self.restart_episode_button = status
            elif ((self.joycon.is_right() and event_type == 'zr') or (self.joycon.is_left() and event_type == 'zl')) and not self.change_down_to_gripper:
                self.gripper_toggle_button = status
            elif ((self.joycon.is_right() and event_type == 'stick_r_btn') or (self.joycon.is_left() and event_type == 'stick_l_btn')) and self.change_down_to_gripper:
                self.gripper_toggle_button = status
            else: 
                self.reset_button = 0
            
        if self.gripper_toggle_button == 1 :
            if self.gripper_state == self.gripper_open:
                self.gripper_state = self.gripper_close
            else:
                self.gripper_state = self.gripper_open
            self.gripper_toggle_button = 0

        # 按钮控制状态
        if self.joycon.is_right():
            if self.next_episode_button == 1:
                self.button_control = 1
            elif self.restart_episode_button == 1:
                self.button_control = -1
            elif self.reset_button == 1:
                self.button_control = 8
            else:
                self.button_control = 0
        
        return self.position, self.gripper_state, self.button_control
    
class SimpleTeleopArm:
    def __init__(self, joint_map, initial_obs, kinematics, prefix="right", kp=1):
        self.joint_map = joint_map
        self.prefix = prefix
        self.kp = kp
        self.kinematics = kinematics
        
        # 初始关节位置
        self.joint_positions = {
            "shoulder_pan": initial_obs[f"{prefix}_arm_shoulder_pan.pos"],
            "shoulder_lift": initial_obs[f"{prefix}_arm_shoulder_lift.pos"],
            "elbow_flex": initial_obs[f"{prefix}_arm_elbow_flex.pos"],
            "wrist_flex": initial_obs[f"{prefix}_arm_wrist_flex.pos"],
            "wrist_roll": initial_obs[f"{prefix}_arm_wrist_roll.pos"],
            "gripper": initial_obs[f"{prefix}_arm_gripper.pos"],
        }
        
        # 设置初始 x/y 为固定值
        self.current_x = 0.1629
        self.current_y = 0.1131
        self.pitch = 0.0
        
        # 设置步长
        self.degree_step = 2
        self.xy_step = 0.005
        
        # P控制目标位置，设为零位
        self.target_positions = {
            "shoulder_pan": 0.0,
            "shoulder_lift": 0.0,
            "elbow_flex": 0.0,
            "wrist_flex": 0.0,
            "wrist_roll": 0.0,
            "gripper": 0.0,
        }
        self.zero_pos = {
            'shoulder_pan': 0.0,
            'shoulder_lift': 0.0,
            'elbow_flex': 0.0,
            'wrist_flex': 0.0,
            'wrist_roll': 0.0,
            'gripper': 0.0
        }

    def move_to_zero_position(self, robot):
        print(f"[{self.prefix}] Moving to Zero Position: {self.zero_pos} ......")
        self.target_positions = self.zero_pos.copy()
        
        # 重置运动学变量到初始状态
        self.current_x = 0.1629
        self.current_y = 0.1131
        self.pitch = 0.0
        
        # 明确设置 wrist_flex
        self.target_positions["wrist_flex"] = 0.0
        
        action = self.p_control_action(robot)
        robot.send_action(action)

    def handle_joycon_input(self, joycon_pose, gripper_state):
        """处理Joy-Con输入，更新手臂控制 - 基于6_so100_joycon_ee_control.py"""
        x, y, z, roll_, pitch_, yaw = joycon_pose
        
        # 计算pitch控制 - 与6_so100_joycon_ee_control.py一致
        pitch = -pitch_ * 60 + 20
        
        # 设置坐标 - 与6_so100_joycon_ee_control.py一致  
        current_x = 0.1629 + x
        current_y = 0.1131 + z
        
        # 计算roll - 与6_so100_joycon_ee_control.py一致
        roll = roll_ * 50
        
        print(f"[{self.prefix}] pitch: {pitch}")
        
        # 添加y值控制shoulder_pan关节 - 与6_so100_joycon_ee_control.py一致
        y_scale = 300.0  # 缩放因子，可以根据需要调整
        self.target_positions["shoulder_pan"] = y * y_scale
        
        # 使用反向运动学计算关节角度 - 与6_so100_joycon_ee_control.py一致
        try:
            joint2_target, joint3_target = self.kinematics.inverse_kinematics(current_x, current_y)
            self.target_positions["shoulder_lift"] = joint2_target
            self.target_positions["elbow_flex"] = joint3_target
        except Exception as e:
            print(f"[{self.prefix}] IK failed: {e}")
        
        # 设置wrist_flex - 与6_so100_joycon_ee_control.py一致
        self.target_positions["wrist_flex"] = -self.target_positions["shoulder_lift"] - self.target_positions["elbow_flex"] + pitch
        
        # 设置wrist_roll - 与6_so100_joycon_ee_control.py一致
        self.target_positions["wrist_roll"] = roll
        
        # 夹爪控制 - 与6_so100_joycon_ee_control.py一致
        if gripper_state == 1:
            self.target_positions["gripper"] = 60
        else:
            self.target_positions["gripper"] = 0

    def p_control_action(self, robot):
        obs = robot.get_observation()
        current = {j: obs[f"{self.prefix}_arm_{j}.pos"] for j in self.joint_map}
        action = {}
        for j in self.target_positions:
            error = self.target_positions[j] - current[j]
            control = self.kp * error
            action[f"{self.joint_map[j]}.pos"] = current[j] + control
        return action

def get_joycon_base_action(joycon, robot):
    """
    从Joy-Con获取底盘控制指令
    X: 前进, B: 后退, Y: 左转, A: 右转
    """
    # 获取按钮状态
    button_x = joycon.joycon.get_button_x()  # 前进
    button_b = joycon.joycon.get_button_b()  # 后退  
    button_y = joycon.joycon.get_button_y()  # 左转
    button_a = joycon.joycon.get_button_a()  # 右转
    
    # 构建按键集合（模拟键盘输入）
    pressed_keys = set()
    
    if button_x == 1:
        pressed_keys.add('k')  # 前进
        print("[BASE] 前进")
    if button_b == 1:
        pressed_keys.add('i')  # 后退
        print("[BASE] 后退")
    if button_y == 1:
        pressed_keys.add('u')  # 左转
        print("[BASE] 左转")
    if button_a == 1:
        pressed_keys.add('o')  # 右转
        print("[BASE] 右转")
    
    # 转换为numpy数组并获取底盘动作
    keyboard_keys = np.array(list(pressed_keys))
    base_action = robot._from_keyboard_to_base_action(keyboard_keys) or {}
    
    return base_action

def get_joycon_speed_control(joycon):
    """
    从Joy-Con获取速度控制
    +按钮: 切换速度档位
    """
    global current_base_speed_level
    if 'current_base_speed_level' not in globals():
        current_base_speed_level = 1  # 默认速度等级（低速）
    
    # 检测+按钮按下事件
    for event_type, status in joycon.button.events():
        if event_type == 'plus' and status == 1:
            # +按钮按下 - 切换速度
            current_base_speed_level = 2 if current_base_speed_level == 1 else 1
            speed_name = "高速" if current_base_speed_level == 2 else "低速"
            print(f"[BASE] 速度切换到 {speed_name} (等级 {current_base_speed_level})")
    
    # 映射速度等级到倍数
    speed_multiplier = float(current_base_speed_level)
    
    return speed_multiplier


def main():
    FPS = 30
    robot_config = XLerobotConfig()
    robot = XLerobot(robot_config)
    try:
        robot.connect()
        print(f"[MAIN] Successfully connected to robot")
    except Exception as e:
        print(f"[MAIN] Failed to connect to robot: {e}")
        print(robot_config)
        print(robot)
        return

    _init_rerun(session_name="xlerobot_teleop_joycon")

    # 初始化右Joy-Con控制器 - 基于6_so100_joycon_ee_control.py
    print("[MAIN] 初始化右Joy-Con控制器...")
    joycon_right = FixedAxesJoyconRobotics(
        "right",
        dof_speed=[2, 2, 2, 1, 1, 1]
    )
    print(f"[MAIN] 右Joy-Con控制器已连接")
    print("[MAIN] 初始化左Joy-Con控制器...")
    joycon_left = FixedAxesJoyconRobotics(
        "left",
        dof_speed=[2, 2, 2, 1, 1, 1]
    )
    print(f"[MAIN] 左Joy-Con控制器已连接")

    # Init the arm and head instances
    obs = robot.get_observation()
    kin_left = SO101Kinematics()
    kin_right = SO101Kinematics()
    left_arm = SimpleTeleopArm(LEFT_JOINT_MAP, obs, kin_left, prefix="left")
    right_arm = SimpleTeleopArm(RIGHT_JOINT_MAP, obs, kin_right, prefix="right")
    # head_control = SimpleHeadControl(obs)

    # Move both arms and head to zero position at start
    left_arm.move_to_zero_position(robot)
    right_arm.move_to_zero_position(robot)

    try:
        while True:
            pose_right, gripper_right, control_button_right = joycon_right.get_control()
            print(f"pose_right: {pose_right}, gripper_right: {gripper_right}, control_button_right: {control_button_right}")
            pose_left, gripper_left, control_button_left = joycon_left.get_control()
            print(f"pose_left: {pose_left}, gripper_left: {gripper_left}, control_button_left: {control_button_left}")

            if control_button_right == 8:  # reset button
                print("[MAIN] Reset to zero position!")
                right_arm.move_to_zero_position(robot)
                left_arm.move_to_zero_position(robot)
                continue

            right_arm.handle_joycon_input(pose_right, gripper_right)
            right_action = right_arm.p_control_action(robot)
            left_arm.handle_joycon_input(pose_left, gripper_left)
            left_action = left_arm.p_control_action(robot)

            base_action = get_joycon_base_action(joycon_right, robot)
            speed_multiplier = get_joycon_speed_control(joycon_right)
            
            if base_action:
                for key in base_action:
                    if 'vel' in key or 'velocity' in key:  
                        base_action[key] *= speed_multiplier 

            # Merge all actions
            action = {**left_action, **right_action, **{}, **base_action}
            robot.send_action(action)

            obs = robot.get_observation()
            log_rerun_data(obs, action)
    finally:
        joycon_right.disconnect()
        joycon_left.disconnect()
        robot.disconnect()
        print("Teleoperation ended.")

if __name__ == "__main__":
    main()