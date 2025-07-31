# 🖨️ 3D打印

## 🤔 打印前准备 🤔

> 我们假设你有使用消费级3D打印机(BambuLab、Prusa等)的基本经验。这意味着你知道如何正确地使用PLA耗材3D打印STL文件，并熟悉重新定向零件、添加支撑、调整填充率和修改打印速度，以在材料强度、效率和模型细节质量之间达到理想的平衡。
> 
- 更详细的信息，你可以查看[Lekiwi](https://github.com/SIGRobotics-UIUC/LeKiwi/blob/main/3DPrinting.md)和[SO100手臂](https://github.com/TheRobotStudio/SO-ARM100#printing-the-parts)的3D打印说明。
- XLeRobot演示视频和图片中显示的所有3D打印零件都是用**BambuLab A1使用BambuLab PLA哑光黑色**打印的。
- 你也可以使用具有更好机械性能的耗材，如**PETG HF、PLA CF**等，以增强手臂的强度。

示例对比：

![image](https://github.com/user-attachments/assets/3d0eeb80-1fc6-47cb-bd15-bc2f023030f4)

## ⏫ XLeRobot额外零件 ⏫

如果你已经有2个SO100手臂和1个Lekiwi底座，你只需要为XLeRobot硬件版本0.1.0额外打印3个零件。

(请同时查看下面的从零开始构建部分，因为零件清单略有不同)

### [手臂底座](https://www.notion.so/vectorwang/3D_Models/3D_models_for_printing/XLeRobot_special/SO_5DOF_ARM100_Assemblybases.stl)

- 底座设计为向外旋转15度，扩展两侧的工作空间区域，同时实现两个手臂之间的平滑协作。
- <img src="https://github.com/user-attachments/assets/f612c9d8-fca2-406e-ab25-d015ea5e62c4" width="500" />
- 如果你想保持简单，也可以使用[原始正向底座](https://www.notion.so/vectorwang/3D_Models/3D_models_for_printing/XLeRobot_special/XLe_arm_bases_0degrees_rotated.stl)。
- 
    
    ![image](https://github.com/user-attachments/assets/eb77aad3-4df3-45c1-93c2-1c2e278512b5)
    
- 设计采用中空中心以节省耗材。你可以插入使用过的Bambulab耗材纸质线轴以增加结构支撑。
- <img src="https://github.com/user-attachments/assets/384c5cb1-849c-43e5-a5e5-8f31d39712f8" width="300" />

### [Lekiwi底座连接器](https://www.notion.so/vectorwang/3D_Models/3D_models_for_printing/XLeRobot_special/BaseConnector.stl)

- 这个组件将Lekiwi底座的顶板连接到宜家推车底部。这是Lekiwi底座电机支架的增强版本，重新设计以获得更好的稳定性。
- <img src="https://github.com/user-attachments/assets/07752338-1c1b-49ca-81b2-ccac9699b498" width="300" />

```{note}
如果你使用的不是正宗的宜家推车，你可以在切片软件中调整z轴比例(同时保持xy轴比例)，以确保Lekiwi底座和推车轮子之间的压力分布均匀。
```

### [更薄的Lekiwi底座顶板](https://www.notion.so/vectorwang/3D_Models/3D_models_for_printing/XLeRobot_special/base_plate_layer2_thinner.stl)

- 这是标准Lekiwi底座顶板的更薄版本，用于将连接器固定到宜家推车底部。
- <img src="https://github.com/user-attachments/assets/17d63ccf-469c-4811-860f-e55ffdee396b" width="400" />
- 虽然当前Lekiwi底座和推车之间的连接是稳定的，但即将推出的第二版将简化在推车金属网格底部的安装。

## 🌿 从零开始打印 🌿

如果你还没有打印任何SO100手臂或Lekiwi底座，请按照它们的说明([Lekiwi](https://github.com/SIGRobotics-UIUC/LeKiwi/blob/main/3DPrinting.md)和[SO100手臂](https://github.com/TheRobotStudio/SO-ARM100#printing-the-parts))以及下面的建议进行。

### 🦾 2x SO100手臂

```{note}
截至2025年4月28日，SO101手臂已发布，对跟随手臂模型进行了修改。这些变化包括简化的零件和改进的线缆管理，同时保持与XLeRobot的兼容性。我强烈建议大家构建SO101而不是SO100，因为组装速度更快！
```
- 在当前硬件版本中，你只需要打印两个[跟随手臂](https://www.notion.so/vectorwang/3D_Models/3D_models_for_printing/SO100/Prusa_Follower_SO101.stl)。[主导手臂](https://github.com/TheRobotStudio/SO-ARM100/tree/main/stl_files_for_3dprinting/Leader)只有在你计划用主从关节控制同时操作双臂时才需要。打印前，请在切片软件中重新排列此stl文件的布局，以获得最佳打印体验。
- <img src="https://github.com/user-attachments/assets/a5a49a95-e75e-4ea1-879c-0a0ec22f07a7" width="800" />
- 手腕相机(MF)支架及其[安装指南](https://github.com/TheRobotStudio/SO-ARM100/tree/main/Optional/Wrist_Cam_Mount_32x32_UVC_Module)可以帮助优化数据收集效率。
- <img src="https://github.com/user-attachments/assets/8f74f9f4-321c-4689-acbe-6d7280922bfe" width="400" />

### 🧑‍🦼‍➡️ Lekiwi底座

- 对于Lekiwi底座，你需要打印：[顶板](https://www.notion.so/vectorwang/3D_Models/3D_models_for_printing/Lekiwi/base_plate_layer1.stl)和[底板](https://www.notion.so/vectorwang/3D_Models/3D_models_for_printing/Lekiwi/base_plate_layer2.stl)、三个[电机支架](https://www.notion.so/vectorwang/3D_Models/3D_models_for_printing/Lekiwi/drive_motor_mount_v2.stl)和三个[轮子-舵机轮毂](https://www.notion.so/vectorwang/3D_Models/3D_models_for_printing/Lekiwi/servo_wheel_hub.stl)。XLeRobot不需要任何其他零件。
- <img src="https://github.com/user-attachments/assets/7c35c7cc-ab69-4cf6-bfa9-0e4b3b983e22" width="800" />