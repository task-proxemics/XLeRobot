<!-- THIS IS ALL GENERATED DOCUMENTATION via generate_robot_docs.py. DO NOT MODIFY THIS FILE DIRECTLY. -->

# Software

## Prepare LeRobot with XLeRobot files

Before getting started, copy all the codes of [XLeRobot config files](https://github.com/Vector-Wangel/XLeRobot/tree/main/software/src) to the corresponding place of lerobot.  

## Getting Started

1. **Choose Control Method**: Start with joint control (example 0) for basic testing, then progress to end-effector control (example 1)
2. **Advanced Features**: Try dual-arm control (example 2) or vision-based control (example 3) for more complex tasks
3. **Full System**: Use keyboard (example 4) or Xbox controller (example 5) teleoperation for complete robot control

All example scripts are located in the [`software/examples/`](https://github.com/Vector-Wangel/XLeRobot/tree/main/software/examples) directory and can be run directly after proper setup and calibration.

```{note}
For basic version of XLeRobot, you don't need a RasberryPi. Just use your laptop, and put it in the IKEA cart if you want to use the full system.
```

## XLeRobot Full System Control

### 5. Keyboard Teleoperation

Complete system control including dual arms, mobile base, and head motors. Run [4_xlerobot_teleop_keyboard.py](https://github.com/Vector-Wangel/XLeRobot/blob/main/software/examples/4_xlerobot_teleop_keyboard.py) for comprehensive keyboard-based teleoperation of the entire XLeRobot system with separate key mappings for left arm, right arm, base movement, and head control.

### 6. Xbox Controller Teleoperation  

Intuitive gamepad control for the full XLeRobot system. Run [5_xlerobot_teleop_xbox.py](https://github.com/Vector-Wangel/XLeRobot/blob/main/software/examples/5_xlerobot_teleop_xbox.py) for Xbox controller-based teleoperation with ergonomic stick and trigger mappings for natural human-robot interaction.


<video width="100%" controls>
  <source src="../_static/videos/Real_demos/xlerobot_025_001.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## SO100/SO101 Arm Control Examples

### 1. Keyboard Joint Control

The most basic control method using direct joint angle manipulation. Run `0_so100_keyboard_joint_control.py` for manual control of individual joint positions using keyboard inputs. This provides direct access to each joint's movement without inverse kinematics calculations.

### 2. Keyboard End-Effector Control

Advanced control using inverse kinematics to move the end-effector in Cartesian space. Run `1_so100_keyboard_ee_control.py` for intuitive control where keyboard inputs control the end-effector position (X, Y coordinates) rather than individual joints.

<video width="100%" controls>
  <source src="../_static/videos/Real_demos/keyboard_teleop.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

### 3. Dual-Arm Keyboard Control

Simultaneous control of two SO100 arms connected via different serial ports (/dev/ttyACM0 and /dev/ttyACM1). Run `2_dual_so100_keyboard_ee_control.py` for coordinated dual-arm manipulation with separate keyboard mappings for each arm.

### 4. Vision-based Object Following

YOLO-powered object detection and tracking system. Run `3_so100_yolo_ee_control.py` to enable the robot to automatically follow detected objects (such as bottles) using computer vision. This demo requires no training and combines real-time object detection with end-effector control.

<video width="100%" controls>
  <source src="../_static/videos/Real_demos/yolo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## (Optional, not fully tested) Leader-follower Control Based-on Lekiwi

```{note}
To test the single-arm version of XLeRobot with Lekiwi codes, you should detach the SO101 arm that doesn't share the same motor control board with the base, clamp it on your table and connect it to your PC to act as the leader arm.
```
```{note}
For mobile base version, you need a RasberryPi in advance.
```

Follow all of their [software instructions](https://github.com/huggingface/lerobot/blob/main/examples/11_use_lekiwi.md#b-install-software-on-pi) so you can:
-  [Install software on RasberryPi](https://github.com/huggingface/lerobot/blob/main/examples/11_use_lekiwi.md#b-install-software-on-pi) and setup SSH 
-  [Install LeRobot on PC](https://github.com/huggingface/lerobot/blob/main/examples/11_use_lekiwi.md#c-install-lerobot-on-laptop)
-  [Update config](https://github.com/huggingface/lerobot/blob/main/examples/11_use_lekiwi.md#update-config)
-  [Calibrate](https://github.com/huggingface/lerobot/blob/main/examples/11_use_lekiwi.md#e-calibration)



After these steps you should be able to teleoperate a basic single-arm version of XLeRobot [the same way Lekiwi does](https://github.com/huggingface/lerobot/blob/main/examples/11_use_lekiwi.md#f-teleoperate), to replicate this demo video:


<video width="100%" style="max-width: 100%;" controls>
  <source src="https://github.com/user-attachments/assets/98312e30-9a5d-41a1-a6ce-ef163c3abfd5" type="video/mp4">
  Your browser does not support the video tag.
</video>

<!-- ```{toctree}
:caption: Directory
:maxdepth: 1

anymal_c/index
allegro_hand_left/index
allegro_hand_right/index
allegro_hand_right_touch/index
dclaw/index
fetch/index
fixed_inspire_hand_left/index
fixed_inspire_hand_right/index
floating_inspire_hand_left/index
floating_inspire_hand_right/index
floating_panda_gripper/index
floating_robotiq_2f_85_gripper/index
googlerobot/index
humanoid/index
koch-v1.1/index
panda/index
panda_stick/index
panda_wristcam/index
so100/index
stompy/index
trifingerpro/index
ur_10e/index
unitree_g1/index
unitree_g1_simplified_legs/index
unitree_g1_simplified_upper_body/index
unitree_go2/index
unitree_h1/index
unitree_h1_simplified/index
widowx250s/index
widowxai/index
widowxai_wristcam/index
xarm6_nogripper/index
xarm6_robotiq/index
xarm6_robotiq_wristcam/index
xarm7_ability/index

``` -->
