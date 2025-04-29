<img src="media/XLeRobot.png" alt="Alt text" width="1200" />

> [!NOTE] 
> Currently actively working. There could be incorrect information. Planning on finish the first version **XLeRbot 0.1.0** in a few days, will delete this note when the first version is finished. Please be patient....

# XLeRobot 🤖

[![Apache License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Twitter/X](https://img.shields.io/twitter/follow/VectorWang?style=social)](https://twitter.com/VectorWang2)
[![Discord](https://dcbadge.vercel.app/api/server/C5P34WJ68S?style=flat)](https://discord.gg/s3KuuzsPFb)
---

[![en](https://img.shields.io/badge/lang-en-red.svg)](README.md)
[![中文](https://img.shields.io/badge/lang-中文-green.svg)](README_CN.md)
[![es](https://img.shields.io/badge/lang-es-yellow.svg)](README_ES.md)
[![de](https://img.shields.io/badge/lang-de-blue.svg)](README_DE.md)

**🚀 Bringing Embodied AI to Everyone - Cheaper Than an iPhone! 📱**  
*Built upon the giants: [LeRobot](https://github.com/huggingface/lerobot), [SO-100](https://github.com/TheRobotStudio/SO-ARM100), [Lekiwi](https://github.com/SIGRobotics-UIUC/LeKiwi), [Bambot](https://github.com/timqian/bambot)*

---

## 🌟 Why XLeRobot? 🌟
We answer this separately since    **XLeRobot = XL + LeRobot**

<table>
  <tr>
    <td>
      
### Why "LeRobot" Core?
- **Cheap Materials** 💴: 90% 3D printed, with cheap motors and electronics.
- **Easy Assembly** 🔨: Screw for 2hrs and here it is.
- **Plug-&-Play** 🧩: Make robots perform by simple pip install and running a few lines.
- **Thriving Community** 🌍:
  World's largest low-cost robotics community with
  - Multiple SOTA pretrained AI models🧠, datasets📊, and tools🔨 for direct deploy. 
  - 5000+ brilliant minds for brainstrom and discussions🧑‍🤝‍🧑.
    
    </td>
    </tr>
    <tr>
    <td>
 
### Why "XL" Enhancement? 
- 🏠 Currently, there is a lack of affordable, stable, general-purpose home mobile robots with dual arms that are as easy to build as LeRobot.
- 🖨️ 3D printed frames have limited durability, stability, and load capacity, while being complex to assemble and impractical for daily use.
- ⚡ Power supply remains a challenge for DIY mobile robots, resulting in complicated wiring configurations.
- 🤖 **XLerobot** uses the same setup configuration as most tabletop dual-arm SO100 in the LeRobot community, making code and policy transfer straightforward.
  
    </td>
  </tr>
 </table>       
 
### Overall Advantages/Goals of XLeRobot

- **Cost-effective** 💴: complete make for ~\$660 , with upgrades from existing SO100Arm and Lekiwi for ~\$250 .
- **Easy upgrade** ⏫ (physical and electrical) for **Lekiwi** and **SO100**
    - Hardware: No motor id changes or hardware modifications required
    - Software: Same tabletop single-arm/dual-arm setup, directly transfer your trained policy from tabletop SO100 arm to here
- **Practical and reliable** 💪: capable of completing many daily tasks performed by $20,000 dual-arm mobile robots on the market.
 
<img width="598" alt="Examples" src="https://github.com/user-attachments/assets/ca418604-13fc-43bf-811a-6036a4455a69" />
    - Though these👆 are only staged photos, but this shows what **XLeRobot** platform is capable of under its hardware limits. (Sorry the scenes are a little messy, but hey, that's life.)
    - More tasks demonstrated in the Lerobot hackathon in [Shanghai](https://www.youtube.com/watch?v=1oXvINlYsls&ab_channel=SeeedStudio) and [Mountain View](https://x.com/asierarranz/status/1905306686648132061).
    - **Note**: Currently not designed for tasks requiring in-hand dexterity 🤹, heavy lifting (over 1kg per arm) 🏋️, or highly dynamic movements 🏃
- **Rich open-source resources** 📕
    - LeRobot's plug-and-play code🧩 and numerous AI models🧠
    - Supported by an active, growing community of contributors🧑‍🤝‍🧑






---
## 🎯 Demo 0.1.0 🎯
> [!NOTE]
> Currently just a single arm version by directly implementing Lekiwi, teleoped by the other follower arm. 3x speed.

https://github.com/user-attachments/assets/2e9eb3c9-af16-4af2-8748-8f936278c8eb

---

## 💵 Total Cost 💵

> [!NOTE] 
> Doesn't include the cost of 3D printing, tools, shippings and taxes.

| Price| US  | EU  | CN |
|---------|----:|----:|----:|
| **Build from Scratch** |  **~$660**  |  **~€650**  |  **~¥3900**  |
| **Upgrade from 2 SO100 arms**  |  **~$400**  |  **~€440**  |  **~¥2400**  |
| **Upgrade from 1 Lekiwi (base + arm)** |  **~$370**  |  **~€350**  |  **~¥1900**  |
| **Upgrade from 1 Lekiwi and 1 SO100 arm** |  **~$250**  |  **~€240**  |  **~¥1200**  |

For details please see [Bill of Materials](BOM.md).

---
---
## 🚀 Get Started（Detailed Tutorial）🚀
> [!NOTE] 
> I am a hardware rookie myself, so I want to make sure this tutorial is friendly to every fellow rookie.
1. 💵 **Buy your parts**: [Bill of Materials](BOM.md)
2. 🖨️ **Print your stuff**: [3D printing instructions](3Dprint.md)
3. 🔨 ~~Avengers~~: [**Assemble**!](Assembly.md)
4. 💻 **Software**: [Get your robot moving!](Software.md)
---
---
> [!NOTE] 
> The content above provides efficient instructions for building the **XLeRobot**. The content below explains the project's purpose and vision in greater detail.

## 🛠️ Hardware Intro 🛠️

**XLeRobot** = Lekiwi + 1x SO100 arm + **IKEA RÅSKOG Cart** + **Anker Battery**

= 2x SO100 Arms + 3x omni wheels + RasberryPi + **IKEA RÅSKOG Cart** + **Anker Battery**

> [!NOTE]
> *All compute handled by your PC - Raspberry Pi only manages data communication via wifi 📶*

<table>
  <tr>
    <td>
      
### Why IKEA RÅSKOG Cart?
- 🌎 Global availability with standardized design
- 💰 Cheap
- 🏗️ Simple structure yet sturdy construction
- 🔧 Metal Mesh bottom enables easy mounting of components
- 📦 Perfect for storage and transportation of items
- 📏 Ideal height for common household surfaces—from stovetop to coffee table
- 📏 Also the plane size is compact and can fit in 99% rooms (Thanks to the designers in IKEA).


    </td>
    </tr>
    <tr>
    <td>
    
### Why Anker SOLIX C300 Power Station? 
- 🌍 Global availability
- ⚡ 288Wh capacity, 300W maximum output power, 280W maximum charging power
- 🔌 Powers both 12V arms, base, and Raspberry Pi at full capacity through three Type-C charging cables—eliminating complex wiring system
- 🔋 Exceptional battery life: 12+ hours with normal use, 8 hours under intensive operation, and only 1 hour to fully charge
- 💡 Integrated lighting for nighttime operation
- ☀️ Optional solar panel mounting for continuous power supply
- 🎒 Versatile and detachable—serves beyond robotics in daily life as emergency backup power or camping power source

    </td>
  </tr>
</table>
<img width="843" alt="1745819677076" src="https://github.com/user-attachments/assets/ad081621-1e69-4bc6-a50f-d89cf92f35c3" />

Even if you don't play with robots (hopefully that won't happen) anymore, these two products can still play a role in your daily life.

---

## 💻 Software Intro 💻
Here's a general idea of how you can control the robot and make it smart:

### 🕹️ Basic Control

- **Joint** (motor angle) control → leader-follower arm control

- **End effector pose** control → VR remote control
  
> [!NOTE]
> For the first version we mainly focus on the hardware. The LeRobot code hasn't been modified yet. You can run the original Lekiwi demo by connecting one arm to the RaspberryPi and another arm to the desktop to recreate the Demo 0.0.5 by remote control. The Lerobot code for XLeRobot will be soon updated with highest priority.


### 🧠 Paths towards General Embodied Machine Intelligence (TODO)






### 🔈🇦🇩 Advertisment:
- **Our lab**: [Rice RobotPI Lab](https://robotpilab.github.io/)
    - One of our visions: use [Caging in Time](https://robotpilab.github.io/publication/caging/) and Funnel-based Manipulation methodology to realize robust object manipulation under imperfect real world situations perception noise, network lag, [contact rich](https://robotpilab.github.io/publication/collision-inclusive-manipulation/), etc.
- **Simulation platform** (my personal preference): [Maniskill](https://www.maniskill.ai/)
    - 🚀Fast GPU acceleration for parallel simulations
    - 🎨Nice photorealistic visual by ray-tracing
    - 🪶Light-weight, consistent, easy to use (compared with Isaac Lab, in my opinion)
    - 🤖Support for [multiple robots](https://maniskill.readthedocs.io/en/latest/robots/index.html) (including [SO100 arm](https://x.com/Stone_Tao/status/1910101218241978537))


---
## Future Plans

### Hardware
<table>
  <tr>
    <td>
      
**Urgent**

- 🔧 Add two arm base options: clamp-held (current) or screw-mounted
- 🛠️ Add a connector plate that is fully compatible with the metal mesh of IKEA cart
    </td>
    </tr>
    <tr>
    <td>
    
**In the near future**

- 📸 Add a RealSense depth camera to the head complement the hand RGB cameras for precise environmental perception
- 🔦 Add a Lidar and some SLAM to make it navigate freely at home just like a Roomba
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
    <td>
      
**Urgent**

- ⚙️ Basic control algorithms
- 🎮 Optimized end effector control
- 🎲 Maniskill simulation environment
- 🕶️ Quest3 VR control and teleop
- 🤖 Simple tasks using existing VLA models from Lerobot codebase
    </td>
    </tr>
    <tr>
    <td>
    
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

All things considered—cost, community support, ease of assembly, and practical utility—XLeRobot stands out as the most compelling low-cost robot for indoor application (personal opinion)


---

### Main Contributors

Currently just [me](https://vector-wangel.github.io/). 

This is just a very small brick on the pyramids, definitely not possible with [LeRobot](https://github.com/huggingface/lerobot), [SO-100](https://github.com/TheRobotStudio/SO-ARM100), [Lekiwi](https://github.com/SIGRobotics-UIUC/LeKiwi), and [Bambot](https://github.com/timqian/bambot). Thanks again for these detailed and professional projects done by their talented contributors.

Looking forward to collaborate with anyone interested in making contribuions for this project!

Not affiliated with IKEA (but we love swedish meatball! 🍝)


