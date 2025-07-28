<!-- THIS IS ALL GENERATED DOCUMENTATION via generate_robot_docs.py. DO NOT MODIFY THIS FILE DIRECTLY. -->
# Get Started

```{note}
We are currently actively working on codes (will rollout within a month), so currently it 100% rely on the Lekiwi codebase.
```

## Leader-follower Control: Lekiwi

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


