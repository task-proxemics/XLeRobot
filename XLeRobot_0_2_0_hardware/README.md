# XLeRobot Changelog

## Version 0.2.0 - Hardware Update Release

### [Download the 3D print file HERE](XLeRobot_0_2_0.3mf)

<img width="522" alt="95f4276408c903c8755f2c198c01202" src="https://github.com/user-attachments/assets/d270ee9e-a5cb-4dba-8a71-160fcaab983e" />

![image](https://github.com/user-attachments/assets/d17127c8-9025-4fab-bf48-c53a1c36e826)


### 📋 Updated Bill of Materials (BOM)
The total cost of XLeRobot 0.2.0 is less than 1000$

The BOM is essentially the same as [XLeRobot 0.1.0](https://github.com/Vector-Wangel/XLeRobot/blob/main/BOM.md), with the following additional components:
- [RealSense D415 depth camera](https://a.co/d/hzuPDe6)
- [Anker USB hub](https://a.co/d/6tJW8lN)
- [Hand cameras](https://github.com/TheRobotStudio/SO-ARM100/tree/main/Optional/Wrist_Cam_Mount_32x32_UVC_Module)
- 2 additional motors (same specifications as arm motors)


### 🔧 Hardware Updates

#### Bottom Base
- **Improved base plate layout**: All screws can now be installed smoothly without interference
- **Added branding**: XLeRobot (Zima) watermark and designer name have been added to the base plate

![image](https://github.com/user-attachments/assets/d3dc8614-ee42-4856-bd88-b1e6b3aacb76)




#### Top Base
- **Standardized arm spacing**: Two arm bases are now connected to ensure consistent spacing
![image](https://github.com/user-attachments/assets/4aed916e-5930-451c-ac72-795d2cb22601)

- **Clamp mounting system**: Retained clamp-based attachment for easier installation and modular design
- **Integrated cable management**: Added protective shell for Raspberry Pi with organized cable routing
![image](https://github.com/user-attachments/assets/fff88e18-08ef-4165-bb0b-32affb557a99)

- **Hollow neck design**: Space-efficient design that saves filament while accommodating USB hub
![image](https://github.com/user-attachments/assets/95a7e585-e625-440e-90f9-5199c092aff7)

- **2-DOF head rotation**: Direct modification based on SO101 base design
![image](https://github.com/user-attachments/assets/6de3d78d-392d-4d82-b19d-0e11d1f6bb0f)

- **Modular architecture**: Even if head functionality isn't immediately needed, you can print and assemble everything below the neck first
<img width="868" alt="1749615226961" src="https://github.com/user-attachments/assets/d5685698-5f49-407e-a12a-5adc6dbc658a" />

### 🔨 Assembly Instructions

#### Hardware Requirements
- Continue using M3 hex screws as in previous versions
- Bottom base assembly process remains the same as [version 0.1.0](https://github.com/Vector-Wangel/XLeRobot/blob/main/Assembly.md#%EF%B8%8F-install-the-lekiwi-base-)

#### Top Base Assembly
Follow the assembly sequence shown in the diagram below (easier when filpped over):
![image](https://github.com/user-attachments/assets/1640d830-b7e9-474b-810d-070097fec59e)
![image](https://github.com/user-attachments/assets/885034a4-61f8-4d61-ab43-b88788b6058b)



**Important**: Complete all wiring and install the Raspberry Pi in its case before clamping the top base to the IKEA cart.

![97716d359d26b2e24cdf0db03f6628a](https://github.com/user-attachments/assets/b0ee286e-bec0-4a70-95ee-2cf108ae4ab6)

### 📸 Final Assembly

![image](https://github.com/user-attachments/assets/8703d472-0ab5-4e17-a9c8-eac8d3a001c1)


### ⚠️ Current Limitations
Due to ongoing LeRobot system updates, we are currently working on control integration with the new system version. Complete end-effector control code and corresponding simulation will be released this month.

**Temporary Workaround**: You can continue using Lekiwi's code base. For now, implement head control and base movement control separately (either disable base motors or disable head motors during operation).

### 🚀 Coming Soon
- Full control algorithm release
- End-effector control code
- Simulation environment
- Integration with updated LeRobot system
