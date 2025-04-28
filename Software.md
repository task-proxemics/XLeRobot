## Install Lerobot 

- Skip it if you have pip installed Lerobot on your PC in the Assembly section. 

- If not, follow this [installation guide](https://github.com/huggingface/lerobot/blob/main/examples/10_use_so100.md#b-install-lerobot)

## Finish everything required on Lekiwi

- The first preview verison of XLeRobot doesn't have codes yet (will rollout within a month), so it 100% rely on the Lekiwi codebase.
- Follow all of their [software instructions](https://github.com/huggingface/lerobot/blob/main/examples/11_use_lekiwi.md#b-install-software-on-pi) so you can:
  -  [Install software on RasberryPi[(https://github.com/huggingface/lerobot/blob/main/examples/11_use_lekiwi.md#b-install-software-on-pi) and setup SSH (which could be a little difficult for a computer newbie, but the instructions of Lekiwi have some great tutorials)
  -  [Install LeRobot on PC](https://github.com/huggingface/lerobot/blob/main/examples/11_use_lekiwi.md#c-install-lerobot-on-laptop)
  -  [Update config](https://github.com/huggingface/lerobot/blob/main/examples/11_use_lekiwi.md#update-config)(we are the mobile base version, not wired version)
  -  [Calibrate](https://github.com/huggingface/lerobot/blob/main/examples/11_use_lekiwi.md#e-calibration)


## Teleoperate
> [!NOTE] 
> To test the basic single-arm version of XLeRobot, you should detach the SO100 arm that doesn't share the same motor control board with the Lekiwi base, clamp it on your table and connect it to your PC to act as the leader arm.

> [!IMPORTANT]
> Be careful not to enforce too large torque of dynamic motion to it since the motor gear is not removed and we still need this arm to be our follower arm later

After these steps you should be able to run a basic single-arm version of teleoperating XLeRobot [the same way Lekiwi does]([https://github.com/huggingface/lerobot/blob/main/examples/11_use_lekiwi.md#e-calibration](https://github.com/huggingface/lerobot/blob/main/examples/11_use_lekiwi.md#f-teleoperate)), to replicate the first demo video.
