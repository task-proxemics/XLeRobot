# XLeRobot 


[![GitHub](https://img.shields.io/badge/GitHub-XLeRobot-181717?logo=github&style=flat)](https://github.com/Vector-Wangel/XLeRobot) [![Stars](https://img.shields.io/github/stars/Vector-Wangel/XLeRobot?style=social)](https://github.com/Vector-Wangel/XLeRobot) [![Twitter/X](https://img.shields.io/twitter/follow/VectorWang?style=social)](https://twitter.com/VectorWang2) [![Apache License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) [![Discord](https://img.shields.io/badge/Discord-Join%20Chat-7289da.svg?logo=discord&logoColor=white)](https://discord.gg/bjZveEUh6F)

<!-- [![en](https://img.shields.io/badge/lang-en-blue.svg)](..)
[![中文](https://img.shields.io/badge/lang-中文-brown.svg)](README_CN.md)

<div class="lang-switch">
  <a onclick="switchLang('en')" class="active">
    <img src="https://img.shields.io/badge/lang-en-blue.svg" alt="English" />
  </a>
  <a onclick="switchLang('zh')">
    <img src="https://img.shields.io/badge/lang-中文-brown.svg" alt="中文" />
  </a>
</div>

<div class="lang-en">
[English content...]
</div>

<div class="lang-zh">
[Chinese content...]
</div> -->

![image](https://github.com/user-attachments/assets/f9c454ee-2c46-42b4-a5d7-88834a1c95ab)

## 介绍

**🚀 让具身AI走向全世界每个家庭！比iPhone还便宜📱！**

**⏰ <4小时总组装时间**


| 价格 | 美国 | 欧盟 | 中国 |
| --- | --- | --- | --- |
| **基础版** (无树莓派，使用自己的笔记本电脑) | **~$660** | **~€680** | **~¥4000** |
| **标准版** (网络摄像头RGB头部相机) | **~$750** | **~€770** | **~¥4500** |
| **专业版** (RealSense RGB-D头部相机) | **~$960** | **~€980** | **~¥6000** |

*站在巨人的肩膀上: [LeRobot](https://github.com/huggingface/lerobot), [SO-100/SO-101](https://github.com/TheRobotStudio/SO-ARM100), [Lekiwi](https://github.com/SIGRobotics-UIUC/LeKiwi), [Bambot](https://github.com/timqian/bambot)*

---

<video width="100%" controls>
  <source src="./_static/videos/Real_demos/xlerobot_025_001.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## 更新


- **2025.07.30**: XLeRobot 0.2.5 发布！[控制XLeRobot](https://xlerobot.readthedocs.io/en/latest/software/index.html) 在野外的真实环境中使用Xbox控制器。无需wifi，零延迟。

- **2025.07.14**: XLeRobot 0.2.3 (**XLeVR**) 发布！**VR Quest 3 全身控制系统**。捕获所有输入：姿态、摇杆、按钮。基于网页，最少依赖。模块化设计适配不同机器人。开源，20分钟快速设置。

- **2025.07.08**: **完整仿真**，全面支持新的XLeRobot硬件和3个摄像头（2个手部RGB + 1个头部RGB-D），配有urdf文件、键盘末端控制脚本和教程，让您能在10分钟内开始使用。

- **2025.06.14**: XLeRobot 0.2.0的硬件设置正式发布！这是第一个官方硬件版本，完全具备自主家务任务能力，成本为960美元。

---

## 🌟 为什么选择XLeRobot？ 🌟

<video width="100%" style="max-width: 100%;" controls>
  <source src="https://github.com/user-attachments/assets/98312e30-9a5d-41a1-a6ce-ef163c3abfd5" type="video/mp4">
  Your browser does not support the video tag.
</video>

让我们来分解一下，因为 **XLeRobot = XL + LeRobot**

### 为什么选择"LeRobot"核心？

- **廉价材料** 💴: 90%的3D打印组件，配合经济实惠的电机和电子元件。
- **简易组装** 🔨: 67分钟即可组装2个SO101手臂并配置电机。
- **即插即用** 🧩: 通过简单的pip安装和几行代码让机器人运行起来。
- **蓬勃发展的LeRobot社区** 🌍:
世界上最大的低成本机器人社区，特色包括
    - 多个[最先进的预训练AI模型🧠](https://huggingface.co/lerobot)、数据集📊和工具🔨，随时可以部署。
    - 7000+聪明才智的头脑进行头脑风暴和讨论🧑‍🤝‍🧑。

### 为什么需要"XL"增强？

![image](https://github.com/user-attachments/assets/b48a0a41-7422-4f10-8dc6-a66a2fd746ad)

- 🏠 该领域/市场缺乏价格合理、稳定的双臂家用机器人，能够与LeRobot的简易组装相匹配。
- 🖨️ 传统3D打印底盘耐久性、稳定性和负载能力有限——使其不适合日常使用。
- ⚡ DIY移动机器人面临电源供应挑战，导致复杂的接线设置。
- 🤖 **XLeRobot**保持与LeRobot社区的桌面双臂SO-100/SO-101配置的兼容性，实现代码和策略的无缝转移。

### XLeRobot的整体优势/目标

![image](https://github.com/user-attachments/assets/3feb1bc5-8f2b-489e-9dbf-841153ff222e)


- **经济实惠** 💴: 完整构建成本$660，或者从现有SO100Arm和Lekiwi升级仅需$250。
- **轻松升级** ⏫ (物理和电气)对于**Lekiwi**和**SO-100/SO-101**
    - 硬件：无需更改电机ID或硬件修改
    - 软件：与桌面单臂/双臂设置相同——直接从SO-100/SO-101手臂转移您训练好的策略
- **实用可靠** 💪: 执行许多日常任务，可与市场上$20,000的替代品相媲美。
    - 更多任务在LeRobot黑客马拉松中展示，包括[深圳](https://www.youtube.com/watch?v=_r9v04Rc3xA&ab_channel=SeeedStudio)、[上海](https://www.youtube.com/watch?v=1oXvINlYsls&ab_channel=SeeedStudio)和[圣何塞](https://www.youtube.com/watch?v=QvzhsDliGII&ab_channel=SeeedStudio)([获奖者](https://www.hackster.io/contests/embodiedAI#winners))，以及[第一个](https://www.youtube.com/watch?v=i3D94400vq0&ab_channel=HuggingFace)。
    - **注意**：目前不适用于手内灵巧操作🤹、重物提升(每臂超过1kg)🏋️或高度动态运动🏃
- **丰富的开源资源** 📕
    - LeRobot的即插即用代码🧩和广泛的AI模型库🧠
    - 由活跃、不断增长的贡献者社区支持🧑‍🤝‍🧑
- **⚠️安全始终重要⚠️**: XLeRobot具有固有的物理硬件限制(低扭矩电机、短臂长、轮式基础)，使其几乎不可能伤害人类，同时仍然保持执行许多家庭任务的能力。
    - **低扭矩电机**🦾: 即使在意外接触的情况下，机器人也极不可能造成伤害。此外，其扭矩限制防止其执行高速、动态运动。
    - **短臂长**🦵: 在不太可能的情况下，如果它持有尖锐物体，可以通过翻倒宜家推车快速禁用机器人。
    - **轮式基础**🧑‍🦼‍➡️: 它无法爬过高于10cm的障碍物，所以在未授权访问尝试的情况下，您可以使用障碍物或楼梯轻松限制其移动。

这些👆是摆拍照片，但它们展示了XLeRobot平台在其硬件限制内可以实现的功能。(场景有点凌乱，但嘿，这就是生活！)

---

## 🎯 XLeRobot适合谁？

- 🚀 **初创公司和实验室**: 使用世界上最便宜的模块化平台更快地构建原型
- 👩🔬 **自研人员**: 在不破产的情况下实验具身AI 💸
- 🎓 **教育英雄**:
    - 高中教师: 将前沿机器人技术带入STEM课堂 🧪
    - 大学教授: 机器人/AI课程的经济实惠平台 📚
    - 学生: 从初学者到研究人员 🎒→🎓
- 🤖 **DIY爱好者**: 完美适合室内项目 - 植物护理、递送机器人、家庭自动化 🌱📦

---

## 局限性

(嘿，这个价格，还要什么自行车？)

- 🔒 固定高度——添加稳定的升降平台将显著增加成本和组装难度
- 📏 与Aloha相比工作空间较小——虽然我们最大化了SO100的工作空间，但手臂有尺寸限制，不过XLeRobot仍能有效处理大多数任务
- ⚖️ 单臂负载能力有限——这就是为什么我们使用宜家推车
- 🛒 底座移动精度可能受到宜家推车轮子的影响——这可以通过闭环反馈控制解决

综合考虑——成本、社区支持、组装便捷性和实用性——XLeRobot脱颖而出，成为室内应用最具吸引力的低成本机器人之一！

---

## 主要贡献者

- [我](https://vector-wangel.github.io/)。
- 王跃嵩: Mujoco仿真

这只是金字塔中的一小块砖，由[LeRobot](https://github.com/huggingface/lerobot)、[SO-100](https://github.com/TheRobotStudio/SO-ARM100)、[Lekiwi](https://github.com/SIGRobotics-UIUC/LeKiwi)和[Bambot](https://github.com/timqian/bambot)共同实现。感谢这些详细且专业项目背后所有才华横溢的贡献者。

期待与任何有兴趣为该项目做出贡献的人合作！

---

## 引用

如果您愿意，可以使用以下方式引用本工作：

```
@misc{wang2025xlerobot,
    author = {Wang, Gaotian},
    title = {XLeRobot: A Practical Low-cost Household Dual-Arm Mobile Robot Design for General Manipulation},
    howpublished = "\\url{<https://github.com/Vector-Wangel/XLeRobot>}",
    year = {2025}
}

```

---

## 🪧 免责声明 🪧

> 如果您基于此仓库构建、购买或开发XLeRobot，您将对其对您或他人造成的所有物理和精神损害负全部责任。
>

---

```{toctree}
:maxdepth: 1
hardware/index
simulation/index
software/index
demos/index
relatedworks/index
```
