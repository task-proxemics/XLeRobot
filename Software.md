# 🦾 Get Your Robot Moving! 🦿
> [!NOTE] 
> The first preview verison of XLeRobot doesn't have codes yet (will rollout within a month), so currently it 100% rely on the Lekiwi codebase. When the new code comes out, it will take less than 5 minutes to migrate over.

## Finish everything required on Lekiwi

Follow all of their [software instructions](https://github.com/huggingface/lerobot/blob/main/examples/11_use_lekiwi.md#b-install-software-on-pi) so you can:
-  [Install software on RasberryPi](https://github.com/huggingface/lerobot/blob/main/examples/11_use_lekiwi.md#b-install-software-on-pi) and setup SSH 
-  [Install LeRobot on PC](https://github.com/huggingface/lerobot/blob/main/examples/11_use_lekiwi.md#c-install-lerobot-on-laptop)
-  [Update config](https://github.com/huggingface/lerobot/blob/main/examples/11_use_lekiwi.md#update-config) (we are the mobile base version, not wired version)
-  [Calibrate](https://github.com/huggingface/lerobot/blob/main/examples/11_use_lekiwi.md#e-calibration)


## Teleoperate
> [!NOTE] 
> To test the basic single-arm version of XLeRobot, you should detach the SO100 arm that doesn't share the same motor control board with the Lekiwi base, clamp it on your table and connect it to your PC to act as the leader arm.

If you already have a leader arm, you can also use it. But still suggest to take off the non-lekiwi SO100 arm.

> [!IMPORTANT]
> Directly use follow arm hardware as leader arm may not be very smooth. Be careful not to enforce too large torque of dynamic motion to it since the motor gear is not removed and we still need this arm to be our follower arm later

After these steps you should be able to teleoperate a basic single-arm version of XLeRobot [the same way Lekiwi does](https://github.com/huggingface/lerobot/blob/main/examples/11_use_lekiwi.md#f-teleoperate), to replicate the first demo video.
