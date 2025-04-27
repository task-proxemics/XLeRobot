<img src="media/XLeRobot.png" alt="Alt text" width="1200" />

> [!NOTE] 
> Currently actively working. There could be incorrect information. Planning on finish the first version **XLeRbot 0.1.0** in a week, will delete this note when the first version is finished. Please be patient....

# XLeRobot 🤖

[![Apache License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Twitter/X](https://img.shields.io/twitter/follow/VectorWang?style=social)](https://twitter.com/VectorWang2)
[![Discord](https://dcbadge.vercel.app/api/server/C5P34WJ68S?style=flat)](https://discord.gg/s3KuuzsPFb)
---


**🚀 Bringing Embodied AI to Everyone - Cheaper Than Half of an iPhone! 📱**  
*Built upon the giants: [LeRobot](https://github.com/huggingface/lerobot), [SO-100](https://github.com/TheRobotStudio/SO-ARM100), [Lekiwi](https://github.com/SIGRobotics-UIUC/LeKiwi), [Bambot](https://github.com/timqian/bambot)*

---

## 🌟 Why XLeRobot?  
We answer this separately since    **XLeRobot = XL + LeRobot**
<table>
  <tr>
    <td width="50%">
      
### Why "LeRobot" Core?
- **Cheap Materials** 💴: 90% 3D printed, with cheap motors and electronics.
- **Easy Assembly** 🔨: Screw for 2hrs and here it is.
- **Plug-&-Play** 🧩: Make robots perform by simple pip install and running a few lines.
- **Thriving Community** 🌍:
  World's largest low-cost robotics community with
  - Multiple SOTA pretrained AI models🧠, datasets📊, and tools🔨 for direct deploy. 
  - 5000+ brilliant minds for brainstrom and discussions🧑‍🤝‍🧑.     
    </td>
    <td width="50%">
    
### Why "XL" Enhancement? 
- 🏠 Currently, there is a lack of affordable, stable, general-purpose home mobile robots with dual arms that are as easy to build as LeRobot.
- 🖨️ 3D printed frames have limited durability, stability, and load capacity, while being complex to assemble and impractical for daily use.
- ⚡ Power supply remains a challenge for DIY mobile robots, resulting in complicated wiring configurations.
- 🤖 XLerobot uses the same setup configuration as most dual-arm tabletop manipulation systems in the LeRobot community, enabling straightforward code and policy transfer.   
    </td>
  </tr>
</table>


<table>
  <tr>
    <td width="35%">
      <img src="media/realpic_2.jpg" alt="Alt text" width="1200" />
    </td>
    <td width="65%">
      
### Overall advantages/goals of XLeRobot

- **Cost-effective** 💴: complete make under $700 , with upgrades from existing SO100Arm and Lekiwi for less than $250 .
- **Easy upgrade** ⏫ (physical and electrical) for **Lekiwi** and **SO100**
    - No motor id changes or hardware modifications needed
    - Directly transfer your trained policy from tabletop SO100 arm to here
- **Practical and reliable** 💪: capable of completing many daily tasks performed by $20,000 dual-arm mobile robots on the market.
    - Such as: open doors🚪, serve drinks☕, clean tables🧹, moving clothes to baskets👕, grab from the fridge🍱, etc.
    - More tasks demonstrated in the Lerobot hackathon in [Shanghai](https://www.youtube.com/watch?v=1oXvINlYsls&ab_channel=SeeedStudio) and [Mountain View](https://x.com/asierarranz/status/1905306686648132061).
    - **Note**: Currently not designed for tasks requiring in-hand dexterity 🤹, heavy lifting (over 1kg per arm) 🏋️, or highly dynamic movements 🏃
- **Rich open-source resources** 📕
    - Lerobot's plug-and-play code🧩 and numerous AI models🧠
    - Supported by an active, growing community of contributors🧑‍🤝‍🧑

    </td>
  </tr>
</table>



---
## 🎯 Demo 0.0.5
> [!NOTE]
> Currently just a single arm version by directly implementing Lekiwi, teleoped by the other follower arm. 3x speed.

https://github.com/user-attachments/assets/2e9eb3c9-af16-4af2-8748-8f936278c8eb

---

## 🛠️ Total Cost TODO
> [!NOTE] 
> We want XLeRobot to be powerful, so there's only a 12V version.
> Doesn't include cost of 3D printing

| Price| US  | EU  | CN |
|---------|----:|----:|----:|
| **Build from Scratch** |  **$XX**  |  **€XX**  |  **¥XX**  |
| **Build from 2 SO100 arms**  |  **$XX**  |  **€XX**  |  **¥XX**  |
| **Build from 1 Lekiwi** |  **$XX**  |  **€XX**  |  **¥XX**  |
| **Build from 1 Lekiwi and 1 SO100 arm** |  **$XX**  |  **€XX**  |  **¥XX**  |

For details please see [Bill of Materials](BOM.md).
---
---
## 🚀 Get Started（Detailed Tutorial）TODO
1. **Buy your parts**: Bill of Materials
2. **Print your stuff**: 3D printing instructions
3. Avengers: **Assemble**!
4. **Software**: Get your robot moving!
---
---

## 🛠️ Hardware Intro 🛠️

XLeRobot = Lekiwi + 1x SO100 arm + **IKEA RÅSKOG Cart** + **Anker Battery**

= 2x SO100 Arms + 3x omni wheels + RasberryPi + **IKEA RÅSKOG Cart** + **Anker Battery**

> [!NOTE]
> *All compute handled by your PC - Raspberry Pi only manages data communication via wifi 📶*

<table>
  <tr>
    <td width="50%">
      
### Why IKEA RÅSKOG Cart?
- 🌎 Global availability with standardized design
- 💰 Cheap
- 🏗️ Simple structure yet sturdy construction
- 🔧 Metal Mesh bottom enables easy mounting of components
- 📦 Perfect for storage and transportation of items
- 📏 Ideal height for common household surfaces—from stovetop to coffee table
<img src="media/realpic_back.jpg" alt="Alt text" width="250" />
    </td>
    <td width="50%">
    
### Why Anker SOLIX C300 Power Station? 
- 🌍 Global availability
- ⚡ 288Wh capacity, 300W maximum output power, 280W maximum charging power
- 🔌 Powers both 12V arms, base, and Raspberry Pi at full capacity through three Type-C charging cables—eliminating complex wiring system
- 🔋 Exceptional battery life: 10 hours with normal use, 6 hours under intensive operation, and only 1 hour to fully charge
- 💡 Integrated lighting for nighttime operation
- ☀️ Optional solar panel mounting for continuous power supply
- 🎒 Versatile and detachable—serves beyond robotics in daily life as emergency backup power or camping power source
<img src="media/realpic_battery.jpg" alt="Alt text" width="250" />
    </td>
  </tr>
</table>


---

## 💻 Software Intro 💻
Here's a general idea of how you can control the robot and make it smart:

### 🕹️ Basic Control

- **Joint** (motor angle) control → leader-follower arm control

- **End effector pose** control → VR remote control
  
> [!NOTE]
> For the first version we mainly focus on the hardware. The LeRobot code hasn't been modified yet. You can run the original Lekiwi demo by connecting one arm to the Raspberry Pi and another arm to the desktop to recreate the Demo 0.0.5 by remote control. The Lerobot code for XLeRobot will be soon updated with highest priority.


### 🧠 Paths towards General Embodied Machine Intelligence

**Two main approaches for making robots intelligent, reflecting the primary methods in current academic robotics manipulation research** (This is a simplified comparison, as many works combine benefits from both approaches. And all the statements below are my personal opinions, they might not be correct. Just for your reference, open to discussions.)

<table>
  <tr>
    <td width="50%">
      
### 🕸️End to End Visual-motor Policy (VLA)

(Please don’t judge me for this since i am not an expert in VLMs and VLAs)

- Most used recently on Lerobot
- E.g. Pi-0, GR0OT, RT-1, RT-2, RDT, etc.
- 👍 **Pros**:
  - Doesn't need accurate calibration when it comes to direct joint control (perfect for current lerobot
  - Enables direct learning from visual input to motor actions
  - Can learn complex behaviors from demonstration data
- 👎 **Cons**:
  - Often requires large amounts of training data
  - Can be computationally expensive during training phase
  - Less interpretable
  - Challenge in generalization to novel tasks without additional training
  - May struggle with long-horizon planning compared to explicit planning methods
  - Performance highly dependent on data quality and diversity
    </td>
    <td width="50%">
### 🌎Hierarchical Sim2real/World Model that Understand and Predict Physics🌎

- **General idea**: Requires a (world) model to "understand" the physics and dynamics of the task/world and predict the next states. 
  - E.g. Explicit physics models, latent models (JEPA), video generation (Cosmos)
  - Policy approaches: RL-based or Optimization-based (MPC), or hybrid
  - Key techniques: Diffusion models, real2sim2real, object segmentation
  - Applications: Contact-rich tasks, non-prehensile manipulation, dynamic tasks
- 👍**Pros**:
  - Physics understanding enables action interpretation and modification
  - Can learn without human demonstrations
  - Offers interpretability and explainability
  - Supports counterfactual reasoning
  - More sample-efficient than end-to-end approaches
  - Better at long-horizon planning
- 👎**Cons**:
  - Normally require an accurate robot model (current LeRobot calibration method doesn't really fulfill this) 
  - Hierarchical failure points (perception, segmentation, model mismatch)
  - Sim2real gap remains challenging
  - Task-specific action strategies limit transfer
  - Difficulty modeling complex contacts and friction
  - Integration challenges between components 

    </td>
  </tr>
</table>





### 🔈🇦🇩 Ads time:
- **Our lab**: [Rice RobotPI Lab](https://robotpilab.github.io/)
    - One of our visions: use [Caging in Time](https://robotpilab.github.io/publication/caging/) and Funnel-based Manipulation methodology to realize robust object manipulation under imperfect real world situations perception noise, network lag, [contact rich](https://robotpilab.github.io/publication/collision-inclusive-manipulation/), etc.
- **Simulation platform** (my personal preference): [Maniskill](https://www.maniskill.ai/)
    - 🚀Fast GPU acceleration for parallel simulations
    - 🎨Nice photorealistic visual by ray-tracing
    - 🪶Light-weight, consistent, easy to use (compared with Isaac Lab)
    - 🤖Support for [multiple robots](https://maniskill.readthedocs.io/en/latest/robots/index.html) (including [SO100 arm](https://x.com/Stone_Tao/status/1910101218241978537))


---
## Future Plans

### Hardware
<table>
  <tr>
    <td width="50%">
      
**Urgent**

- 🔧 Add two arm base options: clamp-held (current) or screw-mounted
- 🛠️ Add a connector plate that is fully compatible with the metal mesh of IKEA cart
    </td>
    <td width="50%">
    
**In the near future**

- 📸 Add a RealSense depth camera to the head complement the hand RGB cameras for precise environmental perception
- 👆 Basic tactile sensing
    </td>
  </tr>
</table>


> [!NOTE]
> While fancier upgrades are totally possible (like switching to a Jetson processor, upgrading the chassis, or using better motors), these would contradict this project's core mission: **creating the world's most affordable, easy-to-install, plug-and-play universal robot opensource platform**. But these upgrades can be listed as optional add-ons in the future instead of the main track.

### Software

(software updates will also depend on the development of LeRobot community)
<table>
  <tr>
    <td width="50%">
      
**Urgent**

- ⚙️ Basic control algorithms
- 🎮 Optimized end effector control
- 🎲 Maniskill simulation environment
- 🕶️ Quest3 VR control and teleop
- 🤖 Simple tasks using existing VLA models from Lerobot codebase
    </td>
    <td width="50%">
    
**In the near future**

- 🎯 AprilTag-based precise calibration
- 🗺️ Single RGBD camera autonomous navigation
- 🌐 Digital twin alignment for sim2real applications
- 🧠 World model and physics-based robust manipulation
- 💬 Connect with MCP to directly utilize LLMs
    </td>
  </tr>
</table>

---

## 🎯 Who is XLerobot For?

- 🚀 **Startups & Labs**: Build prototypes faster with the world's cheapest modular platform
- 👩🔬 **Self Researchers**: Experiment with embodied AI without breaking the bank 💸
- 🎓 **Education Heroes**:
  - High School Teachers: Bring cutting-edge robotics to STEM classes 🧪
  - University Professors: Affordable platform for robotics/AI courses 📚
  - Students: From beginners to researchers 🎒→🎓
- 🤖 **DIY Enthusiasts**: Perfect for indoor projects - plant care, delivery bots, home automation 🌱📦
---

## Limitations

(Hey, for this price, what more could you ask for?)

- 🔒 Fixed height—adding a stable lifting platform would significantly increase costs and assembly difficulty
- 📏 Smaller workspace compared to Aloha—though we try to fully utilize the workspace of SO100, the arm size does have limits—though XLeRobot can still handles the majority of its tasks
- ⚖️ Limited payload capacity for a single arm—that's why the IKEA cart is here
- 🛒 Base movement precision may be affected by the wheels of IKEA cart—can be addressed through closed-loop feedback control

All things considered—cost, community support, ease of assembly, and practical utility—XLeRobot stands out as the most compelling low-cost robot for indoor applications


---

### Main Contributors

Currently only [me](https://vector-wangel.github.io/) alone. This is just a very small brick on the pyramids, definitely not possible with [LeRobot](https://github.com/huggingface/lerobot), [SO-100](https://github.com/TheRobotStudio/SO-ARM100), [Lekiwi](https://github.com/SIGRobotics-UIUC/LeKiwi), and [Bambot](https://github.com/timqian/bambot). Thanks again for these detailed and professional projects done by their talented contributors.

Not affiliated with IKEA (but we love swedish meatball! 🍝)


