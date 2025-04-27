# 3D Printing Instructions

## Before Printing

> [!NOTE] 
> We assume you have basic experience with consumer-level 3D printers (BambuLab, Prusa, etc.). This means you already know how to properly 3D print STL files with basic PLA filaments, and you're familiar with adding supports, adjusting infill, and modifying print speed to achieve your desired balance of material strength, efficiency, and model detail quality.

- You can also check out the 3D priting instructions for [Lekiwi](https://github.com/SIGRobotics-UIUC/LeKiwi/blob/main/3DPrinting.md) and [SO100 Arm](https://github.com/TheRobotStudio/SO-ARM100#printing-the-parts) first if you like.

- All the 3D printed part in the demo videos and pictures of XLeRobot are printed with **BambuLab A1 with BambuLab PLA Matte Black**.
- You can also use filaments that has better mechanical properties such as **PETG HF, PLA CF,** etc, to enhance the arm strength.
  - An example comparison: ![image](https://github.com/user-attachments/assets/3d0eeb80-1fc6-47cb-bd15-bc2f023030f4)


## ⏫ Extra Parts for XLeRobot ⏫

If you already have 2 SO100 Arms and 1 Lekiwi base, you'll only need these additional parts 

(but also check the _Build From Scratch_ section below since the list is not 100% the same)


## Extra parts

If you already have Lekiwi and SO100 arm

The additional parts needed for the first version hardware are only:

1. arm base

The base is designed to rotate 15 degrees outward, expanding the workspace area on the sides while ensuring normal collaboration between the two arms.

To reduce material waste, the current design is hollow in the middle, and you can place an unused Tuzhu filament spool inside to provide stable structural support.

1. lekiwi base supporter

Modified from the lekiwi base motor mount, with redesigned structure to enhance stability.

If your cart is not an authentic IKEA cart, you can slightly adjust the z-axis scale directly in the slicer software (keeping the xy-axis scale unchanged), so that: ...

1. A thin lekiwi base top plate, used to secure the supporter to the bottom of the IKEA cart

(A second version will be iterated soon to make installation on the mesh more convenient, although the lekiwi base and cart can currently achieve a stable connection)

# Print from scratch

If you don't have any SO100 arm or Lekiwi base

Just follow their repo.

note for SO100: In the basic version, you only need to print two follower arms. You only need to print the leader arm when you need master-slave arm control for dual arms.

This is the direct camera mount for SO100 provided by xxx, which can optimize data collection efficiency.

Note that for the lekiwi base, you only need to print the top and bottom plates, the middle motor frame, and the omni wheel connector. XLerobot won't use other parts.
