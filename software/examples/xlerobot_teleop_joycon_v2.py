# To Run on the host
'''
PYTHONPATH=src python -m lerobot.robots.xlerobot.xlerobot_host --robot.id=my_xlerobot
'''

# To Run the teleop:
'''
cd XLeRobot/lerobot
PYTHONPATH=src python examples/xlerobot_teleop_joycon_v2.py
'''

import time
import numpy as np
import math
from joyconrobotics import JoyconRobotics

from lerobot.robots.xlerobot import XLerobotConfig, XLerobot
from lerobot.utils.robot_utils import busy_wait

# 继承JoyconRobotics类来修改控制逻辑 - 基于6_so100_joycon_ee_control.py
class FixedAxesJoyconRobotics(JoyconRobotics):
    def common_update(self):
        # 修改后的更新逻辑：摇杆只控制固定轴向
        speed_scale = 0.0008
        
        # 垂直摇杆：控制X轴和Z轴（前后）
        joycon_stick_v = self.joycon.get_stick_right_vertical() if self.joycon.is_right() else self.joycon.get_stick_left_vertical()
        joycon_stick_v_0 = 1900
        joycon_stick_v_threshold = 300
        joycon_stick_v_range = 1000
        if joycon_stick_v > joycon_stick_v_threshold + joycon_stick_v_0:
            self.position[0] += speed_scale * (joycon_stick_v - joycon_stick_v_0) / joycon_stick_v_range *self.dof_speed[0] * self.direction_reverse[0] * self.direction_vector[0]
            self.position[2] += speed_scale * (joycon_stick_v - joycon_stick_v_0) / joycon_stick_v_range *self.dof_speed[1] * self.direction_reverse[1] * self.direction_vector[2]
        elif joycon_stick_v < joycon_stick_v_0 - joycon_stick_v_threshold:
            self.position[0] += speed_scale * (joycon_stick_v - joycon_stick_v_0) / joycon_stick_v_range *self.dof_speed[0] * self.direction_reverse[0] * self.direction_vector[0]
            self.position[2] += speed_scale * (joycon_stick_v - joycon_stick_v_0) / joycon_stick_v_range *self.dof_speed[1] * self.direction_reverse[1] * self.direction_vector[2]
        
        # 水平摇杆：只控制Y轴（左右）  
        joycon_stick_h = self.joycon.get_stick_right_horizontal() if self.joycon.is_right() else self.joycon.get_stick_left_horizontal()
        joycon_stick_h_0 = 2100
        joycon_stick_h_threshold = 300
        joycon_stick_h_range = 1000
        if joycon_stick_h > joycon_stick_h_threshold + joycon_stick_h_0:
            self.position[1] += speed_scale * (joycon_stick_h - joycon_stick_h_0) / joycon_stick_h_range * self.dof_speed[1] * self.direction_reverse[1]
        elif joycon_stick_h < joycon_stick_h_0 - joycon_stick_h_threshold:
            self.position[1] += speed_scale * (joycon_stick_h - joycon_stick_h_0) / joycon_stick_h_range * self.dof_speed[1] * self.direction_reverse[1]
        
        # Z轴按钮控制
        joycon_button_up = self.joycon.get_button_r() if self.joycon.is_right() else self.joycon.get_button_l()
        if joycon_button_up == 1:
            self.position[2] += speed_scale * self.dof_speed[2] * self.direction_reverse[2]
        
        joycon_button_down = self.joycon.get_button_r_stick() if self.joycon.is_right() else self.joycon.get_button_l_stick()
        if joycon_button_down == 1:
            self.position[2] -= speed_scale * self.dof_speed[2] * self.direction_reverse[2]

        # 移除X/B按钮对手臂position的影响，这些按钮专用于底盘控制
        # joycon_button_xup = self.joycon.get_button_x() if self.joycon.is_right() else self.joycon.get_button_up()
        # joycon_button_xback = self.joycon.get_button_b() if self.joycon.is_right() else self.joycon.get_button_down()
        # if joycon_button_xup == 1:
        #     self.position[0] += 0.001 * self.dof_speed[0]
        # elif joycon_button_xback == 1:
        #     self.position[0] -= 0.001 * self.dof_speed[0]
        
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

# 反向运动学函数 - 基于6_so100_joycon_ee_control.py
def inverse_kinematics(x, y, l1=0.1159, l2=0.1350):
    """
    Calculate inverse kinematics for a 2-link robotic arm, considering joint offsets

    Parameters:
        x: End effector x coordinate
        y: End effector y coordinate
        l1: Upper arm length (default 0.1159 m)
        l2: Lower arm length (default 0.1350 m)

    Returns:
        joint2, joint3: Joint angles in radians as defined in the URDF file
    """
    # Calculate joint2 and joint3 offsets in theta1 and theta2
    theta1_offset = math.atan2(0.028, 0.11257)  # theta1 offset when joint2=0
    theta2_offset = math.atan2(0.0052, 0.1349) + theta1_offset  # theta2 offset when joint3=0

    # Calculate distance from origin to target point
    r = math.sqrt(x**2 + y**2)
    r_max = l1 + l2  # Maximum reachable distance

    # If target point is beyond maximum workspace, scale it to the boundary
    if r > r_max:
        scale_factor = r_max / r
        x *= scale_factor
        y *= scale_factor
        r = r_max

    # If target point is less than minimum workspace (|l1-l2|), scale it
    r_min = abs(l1 - l2)
    if r < r_min and r > 0:
        scale_factor = r_min / r
        x *= scale_factor
        y *= scale_factor
        r = r_min

    # Use law of cosines to calculate theta2
    cos_theta2 = -(r**2 - l1**2 - l2**2) / (2 * l1 * l2)

    # Calculate theta2 (elbow angle)
    theta2 = math.pi - math.acos(cos_theta2)

    # Calculate theta1 (shoulder angle)
    beta = math.atan2(y, x)
    gamma = math.atan2(l2 * math.sin(theta2), l1 + l2 * math.cos(theta2))
    theta1 = beta + gamma

    # Convert theta1 and theta2 to joint2 and joint3 angles
    joint2 = theta1 + theta1_offset
    joint3 = theta2 + theta2_offset

    # Ensure angles are within URDF limits
    joint2 = max(-0.1, min(3.45, joint2))
    joint3 = max(-0.2, min(math.pi, joint3))

    # Convert from radians to degrees
    joint2_deg = math.degrees(joint2)
    joint3_deg = math.degrees(joint3)

    joint2_deg = 90 - joint2_deg
    joint3_deg = joint3_deg - 90

    return joint2_deg, joint3_deg

# 右手臂关节映射
RIGHT_JOINT_MAP = {
    "shoulder_pan": "right_arm_shoulder_pan",
    "shoulder_lift": "right_arm_shoulder_lift",
    "elbow_flex": "right_arm_elbow_flex",
    "wrist_flex": "right_arm_wrist_flex",
    "wrist_roll": "right_arm_wrist_roll",
    "gripper": "right_arm_gripper",
}

class SimpleTeleopArm:
    def __init__(self, joint_map, initial_obs, prefix="right", kp=1):
        self.joint_map = joint_map
        self.prefix = prefix
        self.kp = kp
        
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
            joint2_target, joint3_target = inverse_kinematics(current_x, current_y)
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

    # 初始化右Joy-Con控制器 - 基于6_so100_joycon_ee_control.py
    print("[MAIN] 初始化右Joy-Con控制器...")
    joycon_right = FixedAxesJoyconRobotics(
        "right",
        dof_speed=[2, 2, 2, 1, 1, 1]
    )
    print(f"[MAIN] 右Joy-Con控制器已连接")

    # 初始化右手臂控制
    obs = robot.get_observation()
    right_arm = SimpleTeleopArm(RIGHT_JOINT_MAP, obs, prefix="right")

    # 移动右手臂到零位
    print("[MAIN] 移动右手臂到零位...")
    right_arm.move_to_zero_position(robot)
    
    print("[MAIN] Joy-Con控制说明 (基于6_so100_joycon_ee_control.py):")
    print("手臂控制 (仅通过摇杆和姿态):")
    print("  垂直摇杆: 控制右手臂X轴和Z轴位置")
    print("  水平摇杆: 控制右手臂Y轴位置") 
    print("  R按钮: 手臂Z轴上升")
    print("  摇杆按钮: 手臂Z轴下降")
    print("  Joy-Con姿态: 控制shoulder_pan, pitch, roll")
    print("  ZR按钮: 切换夹爪")
    print("底盘控制 (专用按钮):")
    print("  X按钮: 底盘前进")
    print("  B按钮: 底盘后退")
    print("  Y按钮: 底盘左转")
    print("  A按钮: 底盘右转")
    print("  +按钮: 切换底盘速度档位")
    print("其他:")
    print("  Home按钮: 重置右手臂到零位")
    print("注意: X/B/Y/A按钮现在只控制底盘，不影响手臂运动")
    print()

    try:
        while True:
            # 获取Joy-Con控制数据
            pose_right, gripper_right, control_button_right = joycon_right.get_control()
            
            # 检查重置按钮
            if control_button_right == 8:  # reset button
                print("[MAIN] 重置右手臂到零位!")
                right_arm.move_to_zero_position(robot)
                continue

            # 处理右手臂控制
            right_arm.handle_joycon_input(pose_right, gripper_right)
            right_action = right_arm.p_control_action(robot)

            # 获取底盘控制和速度控制
            base_action = get_joycon_base_action(joycon_right, robot)
            speed_multiplier = get_joycon_speed_control(joycon_right)
            
            # 应用速度倍数到底盘动作
            if base_action:
                for key in base_action:
                    if 'vel' in key or 'velocity' in key:  # 应用到速度指令
                        base_action[key] *= speed_multiplier * 1.2

            # 合并所有动作
            action = {**right_action, **base_action}
            robot.send_action(action)

            # 获取观测数据
            obs = robot.get_observation()
            
            # 控制循环频率
            time.sleep(1.0 / FPS)
            
    except KeyboardInterrupt:
        print("\n[MAIN] 收到中断信号，正在停止...")
    finally:
        joycon_right.disconnect()
        robot.disconnect()
        print("[MAIN] 遥控结束。")

if __name__ == "__main__":
    main() 