# 🖨️ 3D打印你的东西! 🖨️

[![en](https://img.shields.io/badge/lang-en-red.svg)](BOM.md)
[![中文](https://img.shields.io/badge/lang-中文-green.svg)](BOM_CN.md)

## 🤔 打印前准备 🤔

> [!NOTE] 
> 我们假设您具有消费级3D打印机（BambuLab、Prusa等）的基本使用经验。这意味着您知道如何使用PLA耗材正确地3D打印STL文件，并且熟悉重新定向零件、添加支撑、调整填充率以及修改打印速度，以达到您所需的材料强度、效率和模型细节质量的平衡。

- 有关更详细的信息，您可以查看[Lekiwi](https://github.com/SIGRobotics-UIUC/LeKiwi/blob/main/3DPrinting.md)和[SO100机械臂](https://github.com/TheRobotStudio/SO-ARM100#printing-the-parts)的3D打印说明。

- XLeRobot演示视频和图片中展示的所有3D打印部件都是使用**BambuLab A1和BambuLab PLA哑光黑色**耗材打印的。
- 您也可以使用具有更好机械性能的耗材，如**PETG HF、PLA CF**等，以增强机械臂的强度。

一个对比示例：![image](https://github.com/user-attachments/assets/3d0eeb80-1fc6-47cb-bd15-bc2f023030f4)


## ⏫ XLeRobot的额外部件 ⏫

如果您已经拥有2个SO100机械臂和1个Lekiwi底座，您只需要为XLeRobot硬件版本0.1.0额外打印3个部件。

（请同时查看下面的"从零开始构建"部分，因为部件列表略有不同）


### [机械臂底座](3D_Models/3D_models_for_printing/XLeRobot_special/SO_5DOF_ARM100_Assemblybases.stl)

- 底座设计为向外旋转15度，扩大两侧的工作空间区域，同时使两个机械臂能够顺畅协作。
- <img src="https://github.com/user-attachments/assets/f612c9d8-fca2-406e-ab25-d015ea5e62c4" width="500" />
- 如果你不想初始化麻烦的话，也有[正面向前的底座](3D_Models/3D_models_for_printing/XLeRobot_special/XLe_arm_bases_0degrees_rotated.stl)
- ![image](https://github.com/user-attachments/assets/eb77aad3-4df3-45c1-93c2-1c2e278512b5)
- 设计具有空心结构以节省耗材。您可以插入用过的Bambulab耗材纸板卷轴以增加结构支撑。
- <img src="https://github.com/user-attachments/assets/384c5cb1-849c-43e5-a5e5-8f31d39712f8" width="300" />


### [Lekiwi底座支撑件](3D_Models/3D_models_for_printing/XLeRobot_special/base_connector.stl)

- 这个组件将Lekiwi底座的顶板连接到IKEA推车底部。它是Lekiwi底座电机支架的增强版，重新设计以提供更好的稳定性。
- <img src="https://github.com/user-attachments/assets/2702b0b2-18ce-471b-bc65-015d9d8b456e" width="300" />


> [!NOTE] 
> 如果您使用的**不是正品IKEA推车**，您可以在切片软件中调整z轴比例（同时保持xy轴比例不变），以确保Lekiwi底座和推车轮子之间的压力分布均匀。

### [更薄的Lekiwi底座顶板](3D_Models/3D_models_for_printing/XLeRobot_special/base_plate_layer2_thinner.stl)

- 这是标准Lekiwi底座顶板的更薄版本，用于将连接器固定到IKEA推车底部。
- <img src="https://github.com/user-attachments/assets/17d63ccf-469c-4811-860f-e55ffdee396b" width="400" />
- 虽然当前Lekiwi底座和推车之间的连接已经稳定，但即将推出的第二版将简化在推车金属网格底部的安装。

## 🌿 从零开始打印 🌿

如果您尚未打印任何SO100机械臂或Lekiwi底座，请按照它们的说明（[Lekiwi](https://github.com/SIGRobotics-UIUC/LeKiwi/blob/main/3DPrinting.md)和[SO100机械臂](https://github.com/TheRobotStudio/SO-ARM100#printing-the-parts)）以及下面的建议进行操作。
### 🦾 2个SO100机械臂 
> [!NOTE]
> 截至2025年4月28日，SO101机械臂已发布，对跟随者机械臂模型进行了修改。这些变更包括简化的零件和改进的线缆管理，同时保持与XLeRobot的兼容性。

- 在当前硬件版本中，您只需要打印两个[跟随者机械臂](3D_Models/3D_models_for_printing/SO100)。只有当您计划使用领导者-跟随者关节控制操作双臂时，才需要[领导者机械臂](https://github.com/TheRobotStudio/SO-ARM100/tree/main/stl_files_for_3dprinting/Leader)。
- <img src="https://github.com/user-attachments/assets/d1a5870e-ab96-4c57-a949-1e5daf84bbb3" width="800" />

- SO100的腕部摄像头(MF)支架及其[安装指南](https://github.com/TheRobotStudio/SO-ARM100/tree/main/Optional/Wrist_Cam_Mount_32x32_UVC_Module)可以帮助优化数据收集效率。
- <img src="https://github.com/user-attachments/assets/8f74f9f4-321c-4689-acbe-6d7280922bfe" width="400" />

### 🧑‍🦼‍➡️ Lekiwi底座 
- 对于Lekiwi底座，您需要打印：[顶板](3D_Models/3D_models_for_printing/Lekiwi/base_plate_layer1.stl)和[底板](3D_Models/3D_models_for_printing/Lekiwi/base_plate_layer2.stl)，三个[电机支架](3D_Models/3D_models_for_printing/Lekiwi/drive_motor_mount_v2.stl)，以及三个[轮-舵机连接器](3D_Models/3D_models_for_printing/Lekiwi/servo_wheel_hub.stl)。XLeRobot不需要任何其他部件。
- <img src="https://github.com/user-attachments/assets/7c35c7cc-ab69-4cf6-bfa9-0e4b3b983e22" width="800" />

### 现在让我们[⚒️ 开始组装！ ⚒️](Assembly.md)
