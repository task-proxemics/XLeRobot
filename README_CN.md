<img src="media/XLeRobot.png" alt="Alt text" width="1200" />

[![en](https://img.shields.io/badge/lang-en-blue.svg)](README.md)
[![中文](https://img.shields.io/badge/lang-中文-brown.svg)](README_CN.md)
[![es](https://img.shields.io/badge/lang-es-green.svg)](README_ES.md)
[![de](https://img.shields.io/badge/lang-de-orange.svg)](README_DE.md)
[![fr](https://img.shields.io/badge/lang-fr-white.svg)](README_FR.md)
[![日本語](https://img.shields.io/badge/lang-日本語-yellow.svg)](README_JP.md)

> [!NOTE] 
> **XLeRobot 0.1.0** 正式发布！当前版本包括详细的**材料清单**、**3D打印模型和说明**，以及**逐步组装指南**。虽然代码尚未提供，但您可以使用原始Lekiwi代码库在单臂版本上**运行远程操作测试**（由另一个跟随臂控制）。

# XLeRobot 🤖

[![Apache License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Twitter/X](https://img.shields.io/twitter/follow/VectorWang?style=social)](https://twitter.com/VectorWang2)
[![Discord](https://dcbadge.vercel.app/api/server/C5P34WJ68S?style=flat)](https://discord.gg/s3KuuzsPFb)
[<img src="https://img.shields.io/badge/WeChat-Join_Group-07C160?style=for-the-badge&logo=wechat&logoColor=white" width="200" />](media/temp_wechat.jpg)
---

**🚀 让每个家庭都能用上具身智能 - 比小米还便宜！📱**  
*站在巨人的肩膀上：[LeRobot](https://github.com/huggingface/lerobot), [SO-100](https://github.com/TheRobotStudio/SO-ARM100), [Lekiwi](https://github.com/SIGRobotics-UIUC/LeKiwi), [Bambot](https://github.com/timqian/bambot)*

---

## 🌟 为什么选择XLeRobot？🌟
让我们来分解一下，因为**XLeRobot = XL + LeRobot**

<table>
  <tr>
    <td>
      
### 为什么选择"LeRobot"核心？
- **廉价材料** 💴：90%的3D打印组件，配合经济实惠的电机和电子元件。
- **简易组装** 🔨：（单臂）仅需2小时的组装时间。
- **即插即用** 🧩：通过简单的pip安装和几行代码即可运行机器人。
- **蓬勃发展的LeRobot社区** 🌍：
  世界上最大的低成本机器人社区，特点是
  - 多个最先进的预训练AI模型🧠、数据集📊和工具🔨随时可部署。
  - 5,000多名优秀人才进行头脑风暴和讨论🧑‍🤝‍🧑。
    
    </td>
    </tr>
    <tr>
    <td>
 
### 为什么需要"XL"增强？ 
- 🏠 该领域/市场缺乏价格合理、稳定的双臂家用机器人，同时具备LeRobot的易组装性。
- 🖨️ 传统3D打印底盘耐久性、稳定性和负载能力有限，使其不适合日常使用。
- ⚡ DIY移动机器人面临电源供应挑战，导致复杂的接线设置。
- 🤖 **XLerobot**保持与LeRobot社区的桌面双臂SO100配置兼容，实现代码和策略的无缝转移。
  
    </td>
  </tr>
 </table>       
 
### XLeRobot的整体优势/目标

- **经济实惠** 💴：完整构建成本约$660，或从现有SO100Arm和Lekiwi升级约$250。
- **轻松升级** ⏫（物理和电气）适用于**Lekiwi**和**SO100**
    - 硬件：无需更改电机ID或硬件修改
    - 软件：与桌面单臂/双臂设置相同—直接从SO100臂转移您的训练策略
- **实用可靠** 💪：执行许多日常任务，可与市场上$20,000的替代品相媲美。
 
    - 更多任务展示在LeRobot黑客马拉松[上海站](https://www.youtube.com/watch?v=1oXvINlYsls&ab_channel=SeeedStudio)和[山景城站](https://x.com/asierarranz/status/1905306686648132061)。
    - **注意**：目前不适用于手内灵巧操作🤹、重物提升（每臂超过1kg）🏋️或高度动态运动🏃
- **丰富的开源资源** 📕
    - LeRobot的即插即用代码🧩和广泛的AI模型库🧠
    - 由活跃、不断增长的贡献者社区支持🧑‍🤝‍🧑

<img width="598" alt="Examples" src="https://github.com/user-attachments/assets/ca418604-13fc-43bf-811a-6036a4455a69" />

这些👆是摆拍照片，但它们展示了XLeRobot平台在其硬件限制内可以实现的功能。（场景有点凌乱，但嘿，这就是生活！）




---
## 🎯 演示 0.1.0 🎯
> [!NOTE]
> 目前是实现Lekiwi的**单臂版本**，由另一个跟随臂以**3倍速度**远程操作。

https://github.com/user-attachments/assets/2e9eb3c9-af16-4af2-8748-8f936278c8eb

---

## 💵 总成本 💵

> [!NOTE] 
> 成本不包括3D打印、工具、运输和税费。

| 价格| 美国  | 欧盟  | 中国 |
|---------|----:|----:|----:|
| **从零开始构建** |  **~$660**  |  **~€650**  |  **~¥3900**  |
| **从2个SO100臂升级**  |  **~$400**  |  **~€440**  |  **~¥2400**  |
| **从1个Lekiwi（底座+臂）升级** |  **~$370**  |  **~€350**  |  **~¥1900**  |
| **从1个Lekiwi和1个SO100臂升级** |  **~$250**  |  **~€240**  |  **~¥1200**  |

详情请参阅[材料清单](BOM.md)。

---
---
## 🚀 开始使用 🚀
> [!NOTE] 
> 我自己也是硬件新手，所以我想让这个教程对所有初学者都友好。
1. 💵 **购买零件**：[物料清单](BOM_CN.md)
2. 🖨️ **打印部件**：[3D打印](3Dprint_CN.md)
3. 🔨 复仇者（bushi）：[**集合**！](Assembly.md)
4. 💻 **软件**：[让你的机器人动起来！](Software.md)
---
---
> [!NOTE] 
> 上面的内容提供了构建**XLeRobot**的高效指导。下面的内容更详细地解释了项目的目的和愿景。

## 🛠️ 硬件介绍 🛠️

**XLeRobot** = Lekiwi + 1x SO100臂 + **宜家RÅSKOG推车** + **Anker电池**

= 2x SO100臂 + 3x全向轮 + 树莓派 + **宜家RÅSKOG推车** + **Anker电池**

> [!NOTE]
> *所有计算由您的PC处理—树莓派仅通过WiFi管理数据通信 📶*

<table>
  <tr>
    <td>
      
### 为什么选择宜家RÅSKOG推车？
- 🌎 全球可用，设计标准化
- 💰 经济实惠
- 🏗️ 结构简单但坚固
- 🔧 金属网格底部便于组件安装
- 📦 完美适合存储和运输
- 📏 理想高度适合常见家庭表面—从炉灶到咖啡桌
- 📏 紧凑的占地面积适合几乎任何房间（感谢宜家的周到设计）


    </td>
    </tr>
    <tr>
    <td>
    
### 为什么选择Anker SOLIX C300电源站？ 
- 🌍 全球可用
- ⚡ 288Wh容量，300W最大输出功率，280W最大充电功率
- 🔌 通过三条USB-C充电线为两个12V机械臂、底座和树莓派提供全容量电力—消除复杂接线
- 🔋 卓越的电池寿命：正常使用12+小时，密集操作8小时，1小时完全充电
- 💡 集成照明用于夜间操作
- ☀️ 可选太阳能电池板安装，提供持续电力供应
- 🎒 多功能且可拆卸—可兼作应急备用电源或露营电源

    </td>
  </tr>
</table>
<img width="843" alt="1745819677076" src="https://github.com/user-attachments/assets/ad081621-1e69-4bc6-a50f-d89cf92f35c3" />

即使您不积极使用机器人，这两种产品在日常使用中仍然很有价值。
---

## 💻 软件介绍 💻
以下是控制机器人并使其智能化的方法：

### 🕹️ 基本控制

- **关节**（电机角度）控制 → 主从臂控制

- **末端执行器姿态**控制 → VR远程控制
  
> [!NOTE]
> 对于第一个版本，我们主要关注硬件。LeRobot代码保持不变。您可以通过将一个机械臂连接到树莓派，另一个连接到桌面进行远程控制，重现Demo 0.1.0。**XLeRobot的LeRobot代码**将很快更新，这是我们的首要任务。


### 🧠 通向通用实体机器智能的路径（待办）






### 🔈广告：
- **我们的实验室**：[Rice RobotPI Lab](https://robotpilab.github.io/)
    - 我们的愿景包括使用[**时之笼**](https://robotpilab.github.io/publication/caging/)和**漏斗式操作**方法，在不完美的现实世界条件下实现稳健的物体操作—包括感知噪声、网络延迟和[丰富接触](https://robotpilab.github.io/publication/collision-inclusive-manipulation/)环境。
- **模拟平台**（我个人偏好）：[Maniskill](https://www.maniskill.ai/)
    - 🚀快速GPU加速用于并行模拟
    - 🎨通过光线追踪实现美丽的逼真视觉效果
    - 🪶轻量级、一致且用户友好（相比Isaac Lab，我个人认为）
    - 🤖支持[多种机器人](https://maniskill.readthedocs.io/en/latest/robots/index.html)（包括[SO100臂](https://x.com/Stone_Tao/status/1910101218241978537)）


---
## 未来计划

### 硬件
<table>
  <tr>
    <td>
      
**紧急**

- 🔧 添加两种机械臂底座选项：夹持式（当前）或螺钉固定式
- 🛠️ 添加与宜家推车金属网格完全兼容的连接板
    </td>
    </tr>
    <tr>
    <td>
    
**近期**

- 📸 在头部添加RealSense深度相机，补充手部RGB相机，实现精确环境感知
- 🔦 添加激光雷达和SLAM功能，实现类似Roomba的家庭导航
- 👆 基本触觉感应
    </td>
  </tr>
</table>


> [!NOTE]
> 虽然更高级的升级完全可能（如切换到Jetson处理器、升级底盘或使用更好的电机），但这些会与本项目的核心使命相矛盾：**创建世界上最经济实惠、易于安装、即插即用的通用机器人开源平台**。但这些升级可以在未来作为可选附加组件列出，而不是主要方向。

### 软件

（软件更新也将取决于LeRobot社区的发展）
<table>
  <tr>
    <td>
      
**紧急**

- ⚙️ 基本控制算法
- 🎮 优化的末端执行器控制
- 🎲 Maniskill模拟环境
- 🕶️ Quest3 VR控制和远程操作
- 🤖 使用Lerobot代码库中现有VLA模型的简单任务
    </td>
    </tr>
    <tr>
    <td>
    
**近期**

- 🎯 基于AprilTag的精确校准
- 🗺️ 自主导航
- 🌐 数字孪生对齐，用于sim2real应用
- 🧠 世界模型和基于物理的稳健操作
- 💬 与MCP连接，直接利用LLMs
    </td>
  </tr>
</table>

---

## 🎯 XLeRobot适合谁？

- 🚀 **初创公司和实验室**：使用世界上最便宜的模块化平台更快地构建原型
- 👩🔬 **自研人员**：在不破费的情况下尝试实体AI 💸
- 🎓 **教育行业**：
  - 高中教师：将前沿机器人技术引入STEM课堂 🧪
  - 大学教授：为机器人/AI课程提供经济实惠的平台 📚
  - 学生：从初学者到研究人员 🎒→🎓
- 🤖 **DIY爱好者**：完美适合室内项目 - 植物护理、递送机器人、家庭自动化 🌱📦
---

## 局限性

（这个价格，要啥自行车？）

- 🔒 固定高度—添加稳定的升降平台会显著增加成本和组装难度
- 📏 与Aloha相比工作空间较小—虽然我们最大化了SO100的工作空间，但机械臂有尺寸限制，不过XLeRobot仍能有效处理大多数任务
- ⚖️ 单臂负载能力有限—这就是我们使用宜家推车的原因
- 🛒 底座移动精度可能受宜家推车轮子影响—这可以通过闭环反馈控制解决
  
综合考虑—成本、社区支持、易于组装和实用性—XLeRobot作为室内应用最具吸引力的低成本机器人之一脱颖而出！


---

### 主要贡献者

目前只有[我](https://vector-wangel.github.io/)。

这只是金字塔中的一小块砖，由[LeRobot](https://github.com/huggingface/lerobot)、[SO-100](https://github.com/TheRobotStudio/SO-ARM100)、[Lekiwi](https://github.com/SIGRobotics-UIUC/LeKiwi)和[Bambot](https://github.com/timqian/bambot)共同实现。感谢这些详细且专业项目背后所有才华横溢的贡献者。

期待与任何有兴趣为该项目做出贡献的人合作！

隔空喊话：Anker，宜家，打钱！（但我们喜欢瑞典肉丸！🍝）

---

## 引用

如果您喜欢的话，您可以这样引用这个工作:

```bibtex
@misc{wang2025xlerobot,
    author = {Wang, Gaotian},
    title = {XLeRobot: A Practical Low-cost Household Dual-Arm Mobile Robot Design for General Manipulation},
    howpublished = "\url{https://github.com/Vector-Wangel/XLeRobot}",
    year = {2025}
}
```
