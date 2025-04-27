# 3D Printing Instructions

## Before Printing

> [!NOTE] 
> We assume you have basic experience with consumer-level 3D printers (BambuLab, Prusa, etc.). This means you already know how to properly 3D print STL files with basic PLA filaments, and you're familiar with adding supports, adjusting infill, and modifying print speed to achieve your desired balance of material strength, efficiency, and model detail quality.

- You can also check out the 3D priting instructions for [Lekiwi](https://github.com/SIGRobotics-UIUC/LeKiwi/blob/main/3DPrinting.md) and [SO100 Arm](https://github.com/TheRobotStudio/SO-ARM100#printing-the-parts) first if you like.

- All the 3D printed part in the demo videos and pictures of XLeRobot are printed with **BambuLab A1 with BambuLab PLA Matte Black**.
- You can also use filaments that has better mechanical properties such as **PETG HF, PLA CF,** etc, to enhance the arm strength.

An example comparison: ![image](https://github.com/user-attachments/assets/3d0eeb80-1fc6-47cb-bd15-bc2f023030f4)


## ⏫ Extra Parts for XLeRobot ⏫

If you already have 2 SO100 Arms and 1 Lekiwi base, you'll only need these additional parts for the 0.0.1 version of hardware

(but also check the _Build From Scratch_ section below since the list is not 100% the same)


### [Arm base](3D_Models/3D_models_for_printing/XLeRobot_special/SO_5DOF_ARM100_Assemblybases.stl)

- The base is designed to rotate 15 degrees outward, expanding the workspace area on the sides while ensuring normal collaboration between the two arms.
- <img src="https://github.com/user-attachments/assets/f612c9d8-fca2-406e-ab25-d015ea5e62c4" width="500" />
- To reduce filament waste, the current design is hollow in the middle, and you can put a used Bambulab filament Cardboard Spool inside to provide stable structural support.
- <img src="https://github.com/user-attachments/assets/384c5cb1-849c-43e5-a5e5-8f31d39712f8" width="300" />


### [Lekiwi base supporter]

- Modified from the Lekiwi base motor mount, with redesigned structure to enhance stability.

- If your cart is **not an authentic IKEA cart**, you can slightly adjust the z-axis scale directly in the slicer software (keeping the xy-axis scale unchanged), so that both the Lekiwi base and the wheels of the cart can have a balanced pressure distribution.

### A thinner Lekiwi base top plate

used to secure the supporter to the bottom of the IKEA cart

(A second version will be iterated soon to make installation on the mesh more convenient, although the lekiwi base and cart can currently achieve a stable connection)

## 🌿 Print from scratch 🌿

If you don't have any SO100 arm or Lekiwi base

Just follow their repo.

note for SO100: In the basic version, you only need to print two follower arms. You only need to print the leader arm when you need master-slave arm control for dual arms.

This is the direct camera mount for SO100 provided by xxx, which can optimize data collection efficiency.

Note that for the lekiwi base, you only need to print the top and bottom plates, the middle motor frame, and the omni wheel connector. XLerobot won't use other parts.
