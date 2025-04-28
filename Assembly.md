#  ⚒️ Assemble! ⚒️

## 🤔 Before Assembly 🤔
- If you don't have assembled 2x SO100 arms or Lekiwi:
    - Please follow the instruction in [SO100 arm Repo](https://github.com/huggingface/lerobot/blob/main/examples/10_use_so100.md) to
        - [Install Lerobot on your PC](https://github.com/huggingface/lerobot/blob/main/examples/10_use_so100.md#b-install-lerobot)
        - [Configure Motor](https://github.com/huggingface/lerobot/blob/main/examples/10_use_so100.md#c-configure-the-motors): both 


First, set up the motor index according to the LeRobot and LeKiwi tutorials. You'll need two motor driver boards: one for the SO100 arm (motors 1-6) and another for motors 1-9.

If you haven't used LeKiwi before, follow their tutorial to set up the Raspberry Pi and establish SSH connection with your PC before beginning assembly.

If you already have a configured SO100 arm and LeKiwi, you can skip the above steps.

## SO100 Arms
If you already have 2x SO100 arm, proceed here.
If not, please see xxx.

>Estimated Assembly time 

If you already have 2x SO100 arm, proceed here. If not, please see xxx.

If building from scratch, complete the "Assemble from Scratch" section below before continuing.

## SO100 Arms

Installing the Base

https://github.com/SIGRobotics-UIUC/LeKiwi/blob/main/Assembly.md#1-assemble-wheel-modules-3-per-robot

First, verify that the LeKiwi base wiring matches the diagram.

1. Place the base on the bottom of the cart
    1. In this initial hardware version, it may be challenging to align all six screws perfectly.
2. Connect the extended cables or self-made cable extensions.
3. Use needle-nose pliers to cut out the metal mesh at the corresponding holes in the top base (only remove the central "x" to maintain structural integrity) for cable routing.
    1. Repeat this process for the upper two layers. Choose the location as needed—I selected the middle of the back edge for minimal cable length and to avoid interfering with cart storage. Alternatively, you can route cables along the sides for a cleaner look.

Installing the Arms

In the current version, for easier debugging, the SO100 arm clamps directly onto the cart. Position the arm base at the two corners of the cart's top layer, then secure with clamps.

A second version will be released soon, featuring a bolted connection between the arm and cart, with standardized spacing between the two arms based on xxx's design.

Installing the Battery:

Place the battery on the middle or lower level to maintain a low center of gravity. I keep it on the middle level for shorter cable runs and easy access (useful for hiking and camping).

Wiring:

See iPad wiring diagram

When extending the signal cable yourself, be careful with the polarity—reversed connections will cause errors.

Connect all three Type-C power cables to the high-power charging section at the bottom of the power supply. Each cable provides up to 100W when charging simultaneously, which testing confirms is sufficient for 12V motor operation.

Important: Connect the power last

## Assemble from Scratch

## Arms

Refer to the SO100 repo

### Personal Tips

- Replace the motor's stock cross-head screws with M3 hex screws—they're more durable, easier to install, and the black screws blend better with the black arm.
