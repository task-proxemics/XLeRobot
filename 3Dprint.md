# 3D Printing Instructions

## Before Printing

> [!NOTE] 
> We assume you have basic experience with consumer-level 3D printers (BambuLab, Prusa, etc.). This means you already know how to properly 3D print STL files with basic PLA filaments, and you're familiar with reorienting parts, adding supports, adjusting infill, and modifying print speed etc., to achieve your desired balance of material strength, efficiency, and model detail quality.

- You can also check out the 3D priting instructions for [Lekiwi](https://github.com/SIGRobotics-UIUC/LeKiwi/blob/main/3DPrinting.md) and [SO100 Arm](https://github.com/TheRobotStudio/SO-ARM100#printing-the-parts) for more detailed information first if you like.

- All the 3D printed part in the demo videos and pictures of XLeRobot are printed with **BambuLab A1 with BambuLab PLA Matte Black**.
- You can also use filaments that has better mechanical properties such as **PETG HF, PLA CF,** etc, to enhance the arm strength.

An example comparison: ![image](https://github.com/user-attachments/assets/3d0eeb80-1fc6-47cb-bd15-bc2f023030f4)


## ⏫ Extra Parts for XLeRobot ⏫

If you already have 2 SO100 Arms and 1 Lekiwi base, you'll only need 3 additional parts for the 0.0.1 version of the XLeRobot hardware.

(but also check the _Build From Scratch_ section below since the list is not 100% the same)


### [Arm bases](3D_Models/3D_models_for_printing/XLeRobot_special/SO_5DOF_ARM100_Assemblybases.stl)

- The bases is designed to rotate 15 degrees outward, expanding the workspace area on both sides while ensuring normal collaboration between the two arms.
- <img src="https://github.com/user-attachments/assets/f612c9d8-fca2-406e-ab25-d015ea5e62c4" width="500" />
- To reduce filament waste, the current design is hollow in the middle, and you can put a used Bambulab filament Cardboard Spool inside to provide stable structural support.
- <img src="https://github.com/user-attachments/assets/384c5cb1-849c-43e5-a5e5-8f31d39712f8" width="300" />


### [Lekiwi base supporter](3D_Models/3D_models_for_printing/XLeRobot_special/base_connector.stl)

- Connect the top plate of Lekiwi base to the bottom of the IKEA cart. Modified from the Lekiwi [base motor mount](https://github.com/SIGRobotics-UIUC/LeKiwi/blob/main/3DPrintMeshes/drive_motor_mount_v2.stl), with redesigned structure to enhance stability.
- <img src="https://github.com/user-attachments/assets/2702b0b2-18ce-471b-bc65-015d9d8b456e" width="300" />


- If your cart is **not an authentic IKEA cart**, you can slightly adjust the z-axis scale directly in the slicer software (keeping the xy-axis scale unchanged), so that both the Lekiwi base and the wheels of the cart can have a balanced pressure distribution.

### [Thinner Lekiwi base top plate](3D_Models/3D_models_for_printing/XLeRobot_special/base_plate_layer2_thinner.stl)

- Same as the Lekiwi base top plate, only thinner. Secure the connector to the bottom of the IKEA cart.
- <img src="https://github.com/user-attachments/assets/17d63ccf-469c-4811-860f-e55ffdee396b" width="400" />
- A second version will be iterated soon to make installation on the metal mesh of the cart bottom more convenient, though currently Lekiwi base and the cart can achieve a stable connection)

## 🌿 Print from scratch 🌿

If you haven't printed any SO100 arm or Lekiwi base, Just follow their instructions ([Lekiwi](https://github.com/SIGRobotics-UIUC/LeKiwi/blob/main/3DPrinting.md) and [SO100 Arm](https://github.com/TheRobotStudio/SO-ARM100#printing-the-parts)) along with the suggestions below.
### SO100 Arms 
- In the basic version, you only need to print two [follower arms](3D_Models/3D_models_for_printing/SO100). You only need to print the [leader arm](https://github.com/TheRobotStudio/SO-ARM100/tree/main/stl_files_for_3dprinting/Leader) when you need to teleope the dual arms with leader-follower joint control.
- <img src="https://github.com/user-attachments/assets/d1a5870e-ab96-4c57-a949-1e5daf84bbb3" width="800" />

- This is the [Wrist Camera (MF) Mount] and its [installation guide](https://github.com/TheRobotStudio/SO-ARM100/tree/main/Optional/Wrist_Cam_Mount_32x32_UVC_Module) for SO100, which can optimize data collection efficiency.
- <img src="https://github.com/user-attachments/assets/8f74f9f4-321c-4689-acbe-6d7280922bfe" width="400" />

### Lekiwi Base
- For the lekiwi base, you only need to print the [top](3D_Models/3D_models_for_printing/Lekiwi/base_plate_layer1.stl) and [bottom plates](3D_Models/3D_models_for_printing/Lekiwi/base_plate_layer2.stl), 3x [motor mounts](3D_Models/3D_models_for_printing/Lekiwi/drive_motor_mount_v2.stl), and 3x [wheel-servo hubs](3D_Models/3D_models_for_printing/Lekiwi/servo_wheel_hub.stl). XLeRobot won't use other parts.
- <img src="https://github.com/user-attachments/assets/7c35c7cc-ab69-4cf6-bfa9-0e4b3b983e22" width="800" />


