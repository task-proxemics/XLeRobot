<!-- THIS IS ALL GENERATED DOCUMENTATION via generate_robot_docs.py. DO NOT MODIFY THIS FILE DIRECTLY. -->

# Software

## Leader-follower Control: Based-on Lekiwi

Follow all of their [software instructions](https://github.com/huggingface/lerobot/blob/main/examples/11_use_lekiwi.md#b-install-software-on-pi) so you can:
-  [Install software on RasberryPi](https://github.com/huggingface/lerobot/blob/main/examples/11_use_lekiwi.md#b-install-software-on-pi) and setup SSH 
-  [Install LeRobot on PC](https://github.com/huggingface/lerobot/blob/main/examples/11_use_lekiwi.md#c-install-lerobot-on-laptop)
-  [Update config](https://github.com/huggingface/lerobot/blob/main/examples/11_use_lekiwi.md#update-config) (we are the mobile base version, not wired version)
-  [Calibrate](https://github.com/huggingface/lerobot/blob/main/examples/11_use_lekiwi.md#e-calibration)

```{note}
To test the basic single-arm version of XLeRobot, you should detach the SO100 arm that doesn't share the same motor control board with the Lekiwi base, clamp it on your table and connect it to your PC to act as the leader arm.
```

After these steps you should be able to teleoperate a basic single-arm version of XLeRobot [the same way Lekiwi does](https://github.com/huggingface/lerobot/blob/main/examples/11_use_lekiwi.md#f-teleoperate), to replicate this demo video:


<video width="100%" style="max-width: 100%;" controls>
  <source src="https://github.com/user-attachments/assets/98312e30-9a5d-41a1-a6ce-ef163c3abfd5" type="video/mp4">
  Your browser does not support the video tag.
</video>

## Keyboard End-Effector Control

After installing lerobot, directly put [this script](https://github.com/Vector-Wangel/XLeRobot/blob/main/software/simple_so100_keyboard_ee_control.py) into /example and run. Then you can play with keyboard EE control smoothly:

<video width="100%" controls>
  <source src="../_static/videos/Real_demos/keyboard_teleop.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


## Vision-based Object Following

We used YOLO to identify the object (such as a bottle) and track its position. Then we use preivous EE control to make the robot follow the object. This demo need no training at all.

Directly put [this script](https://github.com/Vector-Wangel/XLeRobot/blob/main/software/simple_so100_yolo_ee_control.py) into /example and run.

<video width="100%" controls>
  <source src="../_static/videos/Real_demos/yolo.mp4" type="video/mp4">
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
