<img src="media/XLeRobot.png" alt="Alt text" width="1200" />

[![en](https://img.shields.io/badge/lang-en-blue.svg)](README.md)
[![中文](https://img.shields.io/badge/lang-中文-brown.svg)](README_CN.md)


> [!NOTE] 
> Hardware: The hardware setup for [**XLeRobot 0.2.0**](https://github.com/Vector-Wangel/XLeRobot/blob/main/XLeRobot_0_2_0_hardware/README.md) is officially out! This is the 1st official hardware version that is fully capable for autonomous household tasks, with <1000$ cost. 

> [!NOTE] 
> Simulation: **XLeRobot 0.1.5** is officially out! The current version includes [a short technical blog](simulation/sim.md) and a detailed [**Step-by-step Installation Instruction**](simulation/sim_guide.md), along with all the urdf files, control scripts that can get you started in 10 min. 

# XLeRobot 🤖

[![Apache License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Twitter/X](https://img.shields.io/twitter/follow/VectorWang?style=social)](https://twitter.com/VectorWang2)
[![Discord](https://dcbadge.vercel.app/api/server/C5P34WJ68S?style=flat)](https://discord.gg/s3KuuzsPFb)
---

**🚀 Bringing Embodied AI to Everyone - Cheaper Than an iPhone! 📱**  
**💵 ~$660 cost and ⏰ <4hrs total assembly time!!**

*Built upon the giants: [LeRobot](https://github.com/huggingface/lerobot), [SO-100/SO-101](https://github.com/TheRobotStudio/SO-ARM100), [Lekiwi](https://github.com/SIGRobotics-UIUC/LeKiwi), [Bambot](https://github.com/timqian/bambot)*

---
## ⚽ XLeRobot Playground （0.1.5）

**XLeRobot 0.1.5** is officially out! The current version includes [a short technical blog](simulation/sim.md) and a detailed [**Step-by-step Installation Instruction**](simulation/sim_guide.md), along with all the urdf files, control scripts that can get you started to replicate this demo in 10 min. 

https://github.com/user-attachments/assets/e66d8cb5-7a02-4445-b6d9-793057996f87


---

## 🌟 Why XLeRobot? 🌟
Let's break this down since **XLeRobot = XL + LeRobot**

<table>
  <tr>
    <td>
      
### Why "LeRobot" Core?
- **Cheap Materials** 💴: 90% 3D printed components with affordable motors and electronics.
- **Easy Assembly** 🔨: 67 minutes to assemble 2 SO101 arms and configure motors.
- **Plug-&-Play** 🧩: Get robots running with simple pip install and a few lines of code.
- **Thriving LeRobot Community** 🌍:
  World's largest low-cost robotics community featuring
  - Multiple [state-of-the-art pretrained AI models🧠](https://huggingface.co/lerobot), datasets📊, and tools🔨 ready for deployment.
  - ![image](https://github.com/user-attachments/assets/c685bf62-7c66-4382-a404-002142bb4690)

  - 7000+ brilliant minds for brainstorming and discussions🧑‍🤝‍🧑.
    
    </td>
    </tr>
    <tr>
    <td>
 
### Why "XL" Enhancement? 
- 🏠 The field/market lacks affordable, stable, dual-arm home robots that match LeRobot's ease of assembly.
- 🖨️ Traditional 3D printed chassis suffer from limited durability, stability, and load capacity—making them impractical for daily use.
- ⚡ DIY mobile robots face power supply challenges, leading to complex wiring setups.
- 🤖 **XLeRobot** maintains compatibility with the LeRobot community's tabletop dual-arm SO-100/SO-101 configuration, enabling seamless code and policy transfer.
  
    </td>
  </tr>
 </table>       

![image](https://github.com/user-attachments/assets/38dfbefb-5d1d-41f5-ba3b-ccb5088ff6fc)


### Overall Advantages/Goals of XLeRobot

- **Cost-effective** 💴: Complete build costs \$660, or upgrade from existing SO100Arm and Lekiwi for \$250.
- **Easy upgrade** ⏫ (physical and electrical) for **Lekiwi** and **SO-100/SO-101**
    - Hardware: No motor ID changes or hardware modifications needed
    - Software: Identical tabletop single-arm/dual-arm setup—transfer your trained policies directly from SO-100/SO-101 arm
- **Practical and reliable** 💪: Performs many daily tasks comparable to $20,000 market alternatives.
 
    - More tasks demonstrated in the LeRobot hackathon in [Shenzhen](https://www.youtube.com/watch?v=_r9v04Rc3xA&ab_channel=SeeedStudio), [Shanghai](https://www.youtube.com/watch?v=1oXvINlYsls&ab_channel=SeeedStudio) and [San Jose](https://www.youtube.com/watch?v=QvzhsDliGII&ab_channel=SeeedStudio)([Winners](https://www.hackster.io/contests/embodiedAI#winners)), and the [first one](https://www.youtube.com/watch?v=i3D94400vq0&ab_channel=HuggingFace).
    - **Note**: Not currently designed for in-hand dexterity 🤹, heavy lifting (over 1kg per arm) 🏋️, or highly dynamic movements 🏃
- **Rich open-source resources** 📕
    - LeRobot's plug-and-play code🧩 and extensive AI model library🧠
    - Backed by an active, growing community of contributors🧑‍🤝‍🧑
- **⚠️Safety always matters⚠️**: XLeRobot has inherent physical hardware limitations (low-torque motors, short arm length, wheel-based) that make it physically almost incapable of harming humans, while still maintaining its ability to perform many household tasks.
  - **Low-torque motors**🦾: Even in the case of accidental contact, the robot is highly unlikely to cause injury. Additionally, its torque limitations prevent it from performing high-speed, dynamic movements.
  - **Short arm length**🦵: In the unlikely event that it's holding a sharp object, the robot can be quickly disabled by tipping over the IKEA cart.
  - **Wheel-based**🧑‍🦼‍➡️: It cannot climb over obstacles higher than 10cm, so you can easily restrict its movement using blocks or stairs in case of unauthorized access attempts.

<img width="598" alt="Examples" src="https://github.com/user-attachments/assets/ca418604-13fc-43bf-811a-6036a4455a69" />

These👆 are staged photos, but they demonstrate what the XLeRobot platform can achieve within its hardware limitations. (The scenes are a bit messy, but hey, that's life!)





---

## 💵 Total Cost 💵

> [!NOTE] 
> Cost excludes 3D printing, tools, shipping, and taxes.

| Price| US  | EU  | CN |
|---------|----:|----:|----:|
| **Build from Scratch** |  **~$1000**  |  **~€650**  |  **~¥7000**  |
| **Upgrade from 2 SO100 arms**  |  **~$740**  |  **~€440**  |  **~¥5200**  |
| **Upgrade from 1 Lekiwi (base + arm)** |  **~$710**  |  **~€350**  |  **~¥5000**  |
| **Upgrade from 1 Lekiwi and 1 SO100 arm** |  **~$590**  |  **~€240**  |  **~¥4000**  |

For details please see [Bill of Materials](BOM.md).

---
---
## 🚀 Get Started 🚀
> [!NOTE] 
> I'm a hardware rookie myself, so I want to make this tutorial friendly for all fellow beginners.

> [!NOTE] 
> If you are totally new to programming, please spend at least a day to get yourself familiar with basic Python, Ubuntu and Github (with the help of Google and AI). At least you should know how to set up ubuntu system, git clone, pip install, use intepreters (VS Code, Cursor, Pycharm, etc.) and directly run commands in the terminals.

1. 💵 **Buy your parts**: [Bill of Materials](BOM.md)
2. 🖨️ **Print your stuff**: [3D printing](3Dprint.md)
3. 🔨 ~~Avengers~~: [**Assemble**!](Assembly.md)
4. 💻 **Software**: [Get your robot moving!](Software.md)
---
---
> [!NOTE] 
> The content above provides efficient instructions for building the **XLeRobot**. The content below explains the project's purpose and vision in greater detail.

## 🛠️ Hardware Intro 🛠️

---

## 💻 Software Intro 💻

---

## Main Contributors

- [Me](https://vector-wangel.github.io/). 
- Yuesong Wang: Mujoco simulation

This is just a small brick in the pyramid, made possible by [LeRobot](https://github.com/huggingface/lerobot), [SO-100](https://github.com/TheRobotStudio/SO-ARM100), [Lekiwi](https://github.com/SIGRobotics-UIUC/LeKiwi), and [Bambot](https://github.com/timqian/bambot). Thanks to all the talented contributors behind these detailed and professional projects.

Looking forward to collaborating with anyone interested in contributing to this project!


[![Star History Chart](https://api.star-history.com/svg?repos=Vector-Wangel/XLeRobot&type=Timeline)](https://star-history.com/#Vector-Wangel/XLeRobot&Timeline)
---

## Citation

If you want, you can cite this work with:

```bibtex
@misc{wang2025xlerobot,
    author = {Wang, Gaotian},
    title = {XLeRobot: A Practical Low-cost Household Dual-Arm Mobile Robot Design for General Manipulation},
    howpublished = "\url{https://github.com/Vector-Wangel/XLeRobot}",
    year = {2025}
}
```
---

## 🪧 Disclaimer 🪧

> [!NOTE]
> If you build, buy, or develop a XLeRobot based on this repo, you will be fully responsible for all the physical and mental damages it does to you or others.
