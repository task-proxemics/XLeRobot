# 🦾 让您的机器人动起来！ 🦿

[![en](https://img.shields.io/badge/lang-en-red.svg)](Software.md)
[![中文](https://img.shields.io/badge/lang-中文-green.svg)](Software_CN.md)

> [!NOTE] 
> XLeRobot 的第一个预览版本还没有代码（将在一个月内推出），所以目前它 100% 依赖于 Lekiwi 的代码库。当新代码发布后，迁移过程将不超过 5 分钟。

## 完成 Lekiwi 上的所有必要步骤

按照他们的[软件说明](https://github.com/huggingface/lerobot/blob/main/examples/11_use_lekiwi.md#b-install-software-on-pi)操作，以便您可以：
-  [在树莓派上安装软件](https://github.com/huggingface/lerobot/blob/main/examples/11_use_lekiwi.md#b-install-software-on-pi)并设置 SSH 
-  [在 PC 上安装 LeRobot](https://github.com/huggingface/lerobot/blob/main/examples/11_use_lekiwi.md#c-install-lerobot-on-laptop)
-  [更新配置](https://github.com/huggingface/lerobot/blob/main/examples/11_use_lekiwi.md#update-config)（我们使用的是移动底座版本，而非有线版本）
-  [校准](https://github.com/huggingface/lerobot/blob/main/examples/11_use_lekiwi.md#e-calibration)


## 远程操作
> [!NOTE] 
> 要测试 XLeRobot 的基本单臂版本，您应该拆下与 Lekiwi 底座不共享同一电机控制板的 SO100 机械臂，将其固定在桌子上并连接到您的 PC，作为领导者机械臂使用。

如果您已经有一个领导者机械臂，也可以使用它。但仍建议拆下非 Lekiwi 的 SO100 机械臂。

> [!IMPORTANT]
> 直接使用跟随者机械臂硬件作为领导者机械臂可能不会很流畅。注意不要对其施加过大的扭矩或动态运动，因为电机齿轮没有被移除，而且我们之后仍需要这个机械臂作为跟随者机械臂。

完成这些步骤后，您应该能够[像 Lekiwi 一样](https://github.com/huggingface/lerobot/blob/main/examples/11_use_lekiwi.md#f-teleoperate)远程操作 XLeRobot 的基本单臂版本，以复现第一个演示视频。
