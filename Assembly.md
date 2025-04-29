#  ⚒️ Assemble! ⚒️ TODO

> [!NOTE] 
> Currently actively working. There could be incorrect information. Planning on finish the first version **XLeRbot 0.1.0** in a few days, will delete this note when the first version is finished. The assembly is actually pretty simple so you can also try to do it yourself with the incomplete guides below😂.

>Estimated Assembly time: with assembled SO100 arms: 1-2 hrs; from scratch: 4-6 hrs
## 🤔 Before Assembly 🤔
> [!TIP]  
> If you'd rather skip the fun of tightening screws (though every robot enthusiast should try it at least once), some companies sell [pre-assembled kits](https://github.com/TheRobotStudio/SO-ARM100#kits) for SO100 arms at a higher price. The SO100 arm assembly does take the most time, 4-6 hrs for 2 arms. After the arms are assembled the remaining assembly time only takes 1-2 hrs.

- If you don't have assembled SO100 arms or Lekiwi: Please follow the instruction in [SO100 arm Repo](https://github.com/huggingface/lerobot/blob/main/examples/10_use_so100.md) to
    - [Install Lerobot on your PC](https://github.com/huggingface/lerobot/blob/main/examples/10_use_so100.md#b-install-lerobot)
- Configure the motors according to the [SO100](https://github.com/huggingface/lerobot/blob/main/examples/10_use_so100.md#c-configure-the-motors) and [LeKiwi](https://github.com/huggingface/lerobot/blob/main/examples/11_use_lekiwi.md#configure-motors) tutorials.
    - You need two sets of motors for 2 motor control boards: one for the SO100 arm (motors 1-6) and another for Lekiwi (motors 1-9).
    - Tips: write the numbers on motors with marker and distinguish motors for different boards (you can name it L1-L6 and R1-R6).

![image](https://github.com/user-attachments/assets/f3be78fe-0faa-454c-926d-ab1843b31d1f)


If you already have assembled and motor-configured SO100 arm and LeKiwi, you can skip the above steps.

## Assemble 2x SO100 Arms
- If you already have 2x SO100 arm, skip.
- If not, please see this [SO100 Step-by-Step Assembly Instructions](https://github.com/huggingface/lerobot/blob/main/examples/10_use_so100.md#d-step-by-step-assembly-instructions), follow the instructions to build 2 identical follower arms with 2 sets of motors (both preivous indexed as 1-6) for 2 control boards.
> [!TIP]  
> Replace the motor's default cross-head screws with M3 hex screws—they're more durable, easier to install, and the black screws blend better with the black arm.

## Assemble 1x Lekiwi Base

- If you already have a Lekiwi base, distach the battery, servo mounts, etc. Base plate will only have 3 mounted motors with wheels. it so that there's
    - If not, follow the [tutorial](https://github.com/SIGRobotics-UIUC/LeKiwi/blob/main/Assembly.md#2-bottom-plate-assembly) but also stop after mounting motors on the base plate with wheels.
- Wiring the motors regularly as the [tutorial](https://github.com/SIGRobotics-UIUC/LeKiwi/blob/main/Assembly.md#2-bottom-plate-assembly), afetr that instead of connecting the wire to the control board, use the extended wire/connector kit to extend the wire, and assemble the top plate, and pull it out. 


## Install the Lekiwi Base
> [!TIP]  
> You might want to filp the cart over to do this.

1. Place the base on the bottom of the cart
    1. In this initial hardware version, it may be challenging to align all six screws perfectly.
2. Connect the extended cables or self-made cable extensions.
3. Use needle-nose pliers to cut out the metal mesh at the corresponding holes in the top base (only remove the central "x" to maintain structural integrity) for cable routing.
    1. Repeat this process for the upper two layers. Choose the location as needed—I selected the middle of the back edge for minimal cable length and to avoid interfering with cart storage. Alternatively, you can route cables along the sides for a cleaner look.
![image](https://github.com/user-attachments/assets/6b71c525-18ca-46dd-b1c6-02646d3f399f)

## Install the Arms

In the current version, for easier debugging, the SO100 arm clamps directly onto the cart. Position the arm base at the two corners of the cart's top layer, then secure with clamps.

A second version will be released soon, featuring a bolted connection between the arm and cart, with standardized spacing between the two arms.

## Install/Put the Battery:

Place the battery on the middle or lower level to maintain a low center of gravity. I keep it on the middle level for shorter cable runs and easy access (for hiking and camping).

## Last Wiring

See iPad wiring diagram

When extending the signal cable yourself, be careful with the polarity—reversed connections will cause errors.

Connect all three Type-C power cables to the high-power charging section at the bottom of the power supply. Each cable provides up to 100W when charging simultaneously, which testing confirms is sufficient for 12V motor operation.


