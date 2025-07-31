<!-- THIS IS ALL GENERATED DOCUMENTATION via generate_robot_docs.py. DO NOT MODIFY THIS FILE DIRECTLY. -->

# 软件

## 开始使用

1. **选择控制方法**: 从关节控制(示例0)开始进行基本测试，然后进展到末端执行器控制(示例1)
2. **高级功能**: 尝试双臂控制(示例2)或基于视觉的控制(示例3)进行更复杂的任务
3. **完整系统**: 使用键盘(示例4)或Xbox控制器(示例5)遥操作进行完整的机器人控制

所有示例脚本都位于[`software/examples/`](https://github.com/Vector-Wangel/XLeRobot/tree/main/software/examples)目录中，在正确设置和校准后可以直接运行。

```{note}
对于XLeRobot的基础版本，您不需要树莓派。只需使用您的笔记本电脑，如果您想使用完整系统，可以将其放在宜家推车中。
```

## SO100/SO101手臂控制示例

### 1. 键盘关节控制

使用直接关节角度操作的最基本控制方法。运行`0_so100_keyboard_joint_control.py`使用键盘输入手动控制各个关节位置。这提供对每个关节运动的直接访问，无需逆运动学计算。

### 2. 键盘末端执行器控制

使用逆运动学在笛卡尔空间中移动末端执行器的高级控制。运行`1_so100_keyboard_ee_control.py`进行直观控制，其中键盘输入控制末端执行器位置(X、Y坐标)而不是单个关节。

<video width="100%" controls>
  <source src="../_static/videos/Real_demos/keyboard_teleop.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

### 3. 双臂键盘控制

通过不同串口(/dev/ttyACM0和/dev/ttyACM1)连接的两个SO100手臂的同时控制。运行`2_dual_so100_keyboard_ee_control.py`进行协调的双臂操作，每个手臂有单独的键盘映射。

### 4. 基于视觉的物体跟踪

YOLO驱动的物体检测和跟踪系统。运行`3_so100_yolo_ee_control.py`使机器人能够使用计算机视觉自动跟踪检测到的物体(如瓶子)。此演示无需训练，结合了实时物体检测和末端执行器控制。

<video width="100%" controls>
  <source src="../_static/videos/Real_demos/yolo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## XLeRobot完整系统控制

开始之前，将[XLeRobot配置文件](https://github.com/Vector-Wangel/XLeRobot/tree/main/software/src)的所有代码复制到lerobot的相应位置。

### 5. 键盘遥操作

包括双臂、移动底座和头部电机的完整系统控制。运行[4_xlerobot_teleop_keyboard.py](https://github.com/Vector-Wangel/XLeRobot/blob/main/software/examples/4_xlerobot_teleop_keyboard.py)进行基于键盘的整个XLeRobot系统综合遥操作，左臂、右臂、底座移动和头部控制有单独的按键映射。

### 6. Xbox控制器遥操作  

完整XLeRobot系统的直观游戏手柄控制。运行[5_xlerobot_teleop_xbox.py](https://github.com/Vector-Wangel/XLeRobot/blob/main/software/examples/5_xlerobot_teleop_xbox.py)进行基于Xbox控制器的遥操作，具有人体工学摇杆和扳机映射，实现自然的人机交互。

<video width="100%" controls>
  <source src="../_static/videos/Real_demos/xlerobot_025_001.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## 基于Lekiwi的主从控制

```{note}
要使用Lekiwi代码测试XLeRobot的单臂版本，您应该拆下与底座不共享同一电机控制板的SO101手臂，将其夹在桌子上并连接到PC作为主导手臂。
```
```{note}
对于移动底座版本，您需要提前准备一个树莓派。
```

按照他们的所有[软件说明](https://github.com/huggingface/lerobot/blob/main/examples/11_use_lekiwi.md#b-install-software-on-pi)，这样您就可以：
-  [在树莓派上安装软件](https://github.com/huggingface/lerobot/blob/main/examples/11_use_lekiwi.md#b-install-software-on-pi)并设置SSH 
-  [在PC上安装LeRobot](https://github.com/huggingface/lerobot/blob/main/examples/11_use_lekiwi.md#c-install-lerobot-on-laptop)
-  [更新配置](https://github.com/huggingface/lerobot/blob/main/examples/11_use_lekiwi.md#update-config)
-  [校准](https://github.com/huggingface/lerobot/blob/main/examples/11_use_lekiwi.md#e-calibration)

完成这些步骤后，您应该能够[像Lekiwi一样](https://github.com/huggingface/lerobot/blob/main/examples/11_use_lekiwi.md#f-teleoperate)遥操作XLeRobot的基础单臂版本，以复制此演示视频：

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
