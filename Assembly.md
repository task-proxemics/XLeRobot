#  ⚒️ Assemble! ⚒️ 


>Estimated Assembly time: with assembled SO100 arms: 1-2 hrs; from scratch: 4-6 hrs
## 🤔 Before Assembly 🤔
> [!TIP]  
> If you'd rather skip the fun of tightening screws (though every robot enthusiast should try it at least once), some companies sell [pre-assembled kits](https://github.com/TheRobotStudio/SO-ARM100#kits) for SO100 arms at a higher price. The SO100 arm assembly does take the most time, 4-6 hrs for 2 arms. After the arms are assembled the remaining assembly time only takes 1-2 hrs.

- If you don't have assembled SO100 arms or Lekiwi: Please follow the instruction in [SO100 arm Repo](https://github.com/huggingface/lerobot/blob/main/examples/10_use_so100.md) to
    - [Install Lerobot on your PC](https://github.com/huggingface/lerobot/blob/main/examples/10_use_so100.md#b-install-lerobot)
- Configure the motors according to the [SO100](https://github.com/huggingface/lerobot/blob/main/examples/10_use_so100.md#c-configure-the-motors) and [LeKiwi](https://github.com/huggingface/lerobot/blob/main/examples/11_use_lekiwi.md#configure-motors) tutorials.
    - You need two sets of motors for 2 motor control boards: one for the SO100 arm (motors 1-6) and another for Lekiwi (motors 1-9).
    - Tips: write the numbers on motors with marker and distinguish motors for different boards (such as L1-L6 and R1-R6).
    - ![image](https://github.com/user-attachments/assets/f3be78fe-0faa-454c-926d-ab1843b31d1f)


If you already have assembled and motor-configured SO100 arm and LeKiwi, you can skip the above steps.

## 🦾🦾 Assemble 2x SO100 Arms 🦾🦾
- If you already have 2x SO100 arm, skip.
- If not, please see this [SO100 Step-by-Step Assembly Instructions](https://github.com/huggingface/lerobot/blob/main/examples/10_use_so100.md#d-step-by-step-assembly-instructions), follow the instructions to build 2 identical follower arms with 2 sets of motors (both preivous indexed as 1-6) for 2 control boards.
- If you are building SO101 arm, follow [its new tutorial](https://github.com/huggingface/lerobot/blob/main/examples/12_use_so101.md).
![image](https://github.com/user-attachments/assets/68cba2d4-9777-49bc-ad8a-b2931658c474)

> [!TIP]  
> Replace the motor's default cross-head screws with M3 hex screws—they're more durable, easier to install, and the black screws blend better with the black arm.

## 🧑‍🦼‍➡️ Assemble 1x Lekiwi Base 🧑‍🦼‍➡️

- If you already have a Lekiwi base, distach the battery, servo mounts, etc. Base plate will only have 3 mounted motors with wheels (keep the wirings).
    - If not, follow the [tutorial](https://github.com/SIGRobotics-UIUC/LeKiwi/blob/main/Assembly.md#2-bottom-plate-assembly) but also stop after mounting motors on the base plate with wheels.
    - No matter what, the simplified Lekiwi base should look like this:
    - ![image](https://github.com/user-attachments/assets/1b0b0600-e666-4825-9233-807ed63e9020)

- Wiring the motors regularly as the [tutorial](https://github.com/SIGRobotics-UIUC/LeKiwi/blob/main/Assembly.md#2-bottom-plate-assembly), after that instead of connecting the wire to the control board, use the extended wire/connector kit to extend the wire, and leave it hanging (don't pull it out from the top plate just yet).
- ![image](https://github.com/user-attachments/assets/8d81267b-4b58-4af5-8bb3-e77b01d3df7f)

## 🛒 Install the IKEA RÅSKOG Cart 🛒

- Just in case you accidentally throw your manual away, [here it is](https://github.com/Vector-Wangel/XLeRobot/blob/main/others/Manuals_raskog_utility_cart.pdf).
- <img width="925" alt="1745897734515" src="https://github.com/user-attachments/assets/f9f95840-5080-4084-bebb-ea456a097d55" />



## 🧑‍🦼‍➡️ Install the Lekiwi Base 🛒

- Mount the 3 [connectors](https://github.com/Vector-Wangel/XLeRobot/blob/main/3D_Models/3D_models_for_printing/XLeRobot_special/base_connector.stl) on the top plate, anywhere you think could give a stable support
![image](https://github.com/user-attachments/assets/c8233b2d-c58a-4ce5-8b25-b0e7832a60f3)

> [!TIP]  
> Put the Lekiwi base with the connectors under the cart to see whether it can give enough pressure to the cart, with four wheels of the cart can still touch the ground. If not, try to modify the connectors' 3D model by slightly adjust the z-axis scale directly in the slicer software (keeping the xy-axis scale unchanged) and print them again.

> [!TIP]  
> You might want to filp the cart over to do the assembly below.


- Now install the Lekiwi base with the connectors onto the bottom of the IKEA cart, with [the duplicated thinner top plate](https://github.com/Vector-Wangel/XLeRobot/blob/main/3D_Models/3D_models_for_printing/XLeRobot_special/base_plate_layer2_thinner.stl) on the other side.
> [!NOTE] 
> In the first version of hardware, it may be challenging to align all 3x4=12 screws perfectly. You can try to adjust the position and wiggle a little bit to find a place that can install the most screws distributed evenly. Currently the best I can do is 2 screws for each connector, which can give a very stable support. We will also update a new hardware version compatible with the IKEA cart metal mesh shortly.
- ![image](https://github.com/user-attachments/assets/fe28320e-1851-495b-afc3-4e9302f92626)

- Use needle-nose pliers to cut out the metal mesh at the corresponding holes in the top base, removing only the central "x" to maintain structural integrity. This creates openings for cable routing. Then, run the previously extended wire up through the cart from below.
- ![image](https://github.com/user-attachments/assets/b30abce8-a12c-44c8-8e0b-ee720cc1b8fa)




## 🦾🦾 Install the Arms 🛒

- In the current version, for easier testing, the SO100 arm clamps directly onto the cart. Position the [arm bases](https://github.com/Vector-Wangel/XLeRobot/blob/main/3D_Models/3D_models_for_printing/XLeRobot_special/SO_5DOF_ARM100_Assemblybases.stl) at the two corners of the cart's top layer, then secure with clamps.
- Don't forget to put the bambulab filament cardboard spool inside to provide stable structural support.
- ![image](https://github.com/user-attachments/assets/daaa6731-8886-4770-8042-77a5a0afdb74)
- ![image](https://github.com/user-attachments/assets/46239c09-3d37-4115-8dbd-3438ee5b3bac)


- A second version will be released soon, featuring an option for bolted connection between the arms and the cart, with standardized spacing between the two arms.

> [!NOTE] 
> To test the basic single-arm version of XLeRobot directly with the original Lekiwi code before the code for XLeRobot is released, only clamp the SO100 arm that shares the same motor control board with the Lekiwi base. And clamp the other one on your table to act as the leader arm.


## 🔋 Place the Battery 🛒

- You can put it anywhere you like on the middle or lower level of the cart to maintain a low center of mass. The battery has an anti-slip bottom so it won't easily silde during normal operations.
    - I keep it on the middle level for shorter cable runs and easy access (for hiking and camping).
- Just in case you also accidentally throw this manual away, [here it is](https://github.com/Vector-Wangel/XLeRobot/blob/main/others/Manual_Anker_SOLIX_C300_DC_Portable_Power_Station.pdf).
- ![image](https://github.com/user-attachments/assets/c29b14c7-9bd7-45a9-bebd-8a7308a18a2a)


##  🧵 Last, Wiring 🧵
- Up til now, this is what XLeRbot should look like:
- ![image](https://github.com/user-attachments/assets/395e00c7-b8cf-4c4e-ac41-4b80c93c81a4)

- Use needle-nose pliers to cut out the metal mesh at for the upper two layers for cable routing the same way as the bottom layer previously. Choose the location as needed
    - I selected the middle of the back edge for minimal cable length and to avoid interfering with cart storage. Alternatively, you can route cables along the sides for a cleaner look.
- Prepare the extended 5264 wire with the connector kit if you don't have one already.
> [!NOTE] 
> When extending the 5264 wire yourself, be careful with the polarity—reversed connections will cause errors.

- Follow the wiring diagram below and:
    - Connect the extended 5264 motor cable from **the Lekiwi base** to **one of the SO100 arms** (this makes the base and the arm as Lekiwi).
    - Connect the 2 USB-C to USB-A Cable from each **motor control board** to **RasberryPi** (the Rasberry Pi still has 2 USB-A slots open for the cameras later).
    - Connect all three Type-C power cables from to the high-power charging section at the bottom of the power supply. Each cable provides up to 100W when charging simultaneously, which is tested sufficient for 12V version operation.
> [!IMPORTANT]
> 
- ![image](https://github.com/user-attachments/assets/5367eb11-377e-4243-a9ff-746266012901)
- Close-up:
- <img width="725" alt="1745906421978" src="https://github.com/user-attachments/assets/cfaf47d6-b112-4c89-93ce-cb2e21515ee0" />


