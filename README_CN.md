<img src="media/XLeRobot.png" alt="Alt text" width="1200" />

> [!NOTE] 
> 目前正在积极开发中。可能存在不准确的信息。计划在几天内完成第一个版本 **XLeRbot 0.1.0**，完成后将删除此说明。请耐心等待....

# XLeRobot 🤖

[![Apache License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Twitter/X](https://img.shields.io/twitter/follow/VectorWang?style=social)](https://twitter.com/VectorWang2)
[![Discord](https://dcbadge.vercel.app/api/server/C5P34WJ68S?style=flat)](https://discord.gg/s3KuuzsPFb)
---

[![en](https://img.shields.io/badge/lang-en-red.svg)](README.md)

**🚀 让具身智能服务每个人 - 比小米还便宜！📱**  
*基于巨人的肩膀：[LeRobot](https://github.com/huggingface/lerobot), [SO-100](https://github.com/TheRobotStudio/SO-ARM100), [Lekiwi](https://github.com/SIGRobotics-UIUC/LeKiwi), [Bambot](https://github.com/timqian/bambot)*

---

## 🌟 为什么选择XLeRobot？🌟
我们单独回答这个问题，因为 **XLeRobot = XL + LeRobot**

<table>
  <tr>
    <td>
      
### 为什么选择"LeRobot"核心？
- **廉价材料** 💴：90%是3D打印的，使用便宜的电机和电子元件。
- **易于组装** 🔨：拧2小时螺丝就完成了。
- **即插即用** 🧩：通过简单的pip安装和运行几行代码让机器人工作。
- **蓬勃发展的社区** 🌍：
  世界上最大的低成本机器人社区，拥有
  - 多个最先进的预训练AI模型🧠、数据集📊和工具🔨，可直接部署。
  - 5000多名优秀人才进行头脑风暴和讨论🧑‍🤝‍🧑。
    
    </td>
    </tr>
    <tr>
    <td>
 
### 为什么需要"XL"增强？ 
- 🏠 目前，市场上缺乏价格合理、稳定、通用的家用移动双臂机器人，且像LeRobot一样易于构建。
- 🖨️ 3D打印框架的耐久性、稳定性和负载能力有限，同时组装复杂，不适合日常使用。
- ⚡ 电源供应仍然是DIY移动机器人的一个挑战，导致复杂的接线配置。
- 🤖 **XLerobot** 使用与LeRobot社区中大多数桌面双臂SO100相同的设置配置，使代码和策略转移变得简单直接。
  
    </td>
  </tr>
 </table>       
 
### XLeRobot的整体优势/目标

- **成本效益** 💴：完整制作约需 ~¥3900，从现有SO100Arm和Lekiwi升级约需 ~¥1200。
- **轻松升级** ⏫（结构和电路）适用于 **Lekiwi** 和 **SO100**
    - 硬件：无需更改电机ID或硬件修改
    - 软件：相同的桌面单臂/双臂设置，直接将您从桌面SO100手臂训练的策略转移到这里
- **实用且可靠** 💪：能够完成市场上2万美元双臂移动机器人执行的许多日常任务。
    - 例如👇 
    - <img width="598" alt="Examples" src="https://github.com/user-attachments/assets/ca418604-13fc-43bf-811a-6036a4455a69" />
    - 虽然这些👆只是摆拍的照片，但这显示了**XLeRobot**平台在其硬件限制下的能力。（抱歉场景有点凌乱，但嘿，这就是生活。）
    - 更多任务演示可在Lerobot黑客马拉松中看到，分别在[上海](https://www.youtube.com/watch?v=1oXvINlYsls&ab_channel=SeeedStudio)和[山景城](https://x.com/asierarranz/status/1905306686648132061)。
    - **注意**：目前不适用于需要手内灵巧性🤹、重物搬运（每臂超过1kg）🏋️或高度动态运动🏃的任务
- **丰富的开源资源** 📕
    - LeRobot的即插即用代码🧩和众多AI模型🧠
    - 由活跃、不断增长的贡献者社区支持🧑‍🤝‍🧑






---
## 🎯 演示 0.0.5 🎯
> [!NOTE]
> 目前只是通过直接实现Lekiwi的单臂版本，由另一个跟随臂进行遥控。3倍速。

https://github.com/user-attachments/assets/2e9eb3c9-af16-4af2-8748-8f936278c8eb

---

## 💵 总成本 💵

> [!NOTE] 
> 不包括3D打印、工具、运输和税费的成本。

| 价格| 美国  | 欧盟  | 中国 |
|---------|----:|----:|----:|
| **从零开始构建** |  **~$660**  |  **~€650**  |  **~¥3900**  |
| **从2个SO100手臂升级**  |  **~$400**  |  **~€440**  |  **~¥2400**  |
| **从1个Lekiwi升级** |  **~$370**  |  **~€350**  |  **~¥1900**  |
| **从1个Lekiwi和1个SO100手臂升级** |  **~$250**  |  **~€240**  |  **~¥1200**  |

详情请参阅[材料清单](BOM.md)。

---
---
## 🚀 开始使用（详细教程）🚀待完成
> [!NOTE] 
> 我自己也是硬件新手，所以我想确保这个教程对每位新手都友好。
1. 💵 **购买零件**：[材料清单](BOM.md)
2. 🖨️ **打印部件**：[3D打印说明](3Dprint.md)
3. 🔨 ~~复仇者联盟~~：[**组装**！](Assembly.md)
4. 💻 **软件**：让你的机器人动起来！
---
---
> [!NOTE] 
> 上面的内容提供了构建**XLeRobot**的高效指导。下面的内容更详细地解释了项目的目的和愿景。

## 🛠️ 硬件介绍 🛠️

**XLeRobot** = Lekiwi + 1个SO100手臂 + **宜家RÅSKOG推车** + **Anker电源**

= 2个SO100手臂 + 3个全向轮 + 树莓派 + **宜家RÅSKOG推车** + **Anker电源**

> [!NOTE]
> *所有计算由您的PC处理 - 树莓派仅通过wifi管理数据通信 📶*

<table>
  <tr>
    <td>
      
### 为什么选择宜家RÅSKOG推车？
- 🌎 全球可获得且设计标准化
- 💰 便宜
- 🏗️ 结构简单但坚固耐用
- 🔧 金属网格底部便于安装组件
- 📦 完美适合物品的存储和运输
- 📏 高度适合常见家庭表面—从炉灶到咖啡桌

    </td>
    </tr>
    <tr>
    <td>
    
### 为什么选择Anker SOLIX C300电源站？ 
- 🌍 全球可获得
- ⚡ 288Wh容量，300W最大输出功率，280W最大充电功率
- 🔌 通过三根Type-C充电线为两个12V手臂、底座和树莓派提供全容量电力—消除了复杂的接线系统
- 🔋 卓越的电池寿命：正常使用10小时，密集操作6小时，仅需1小时即可充满
- 💡 集成照明，适合夜间操作
- ☀️ 可选太阳能电池板安装，提供持续电力供应
- 🎒 多功能且可拆卸—不仅用于机器人，还可作为日常生活中的应急备用电源或露营电源

    </td>
  </tr>
</table>
<img width="843" alt="1745819677076" src="https://github.com/user-attachments/assets/ad081621-1e69-4bc6-a50f-d89cf92f35c3" />

即使你不再玩机器人（希望不会发生），这两款产品仍然可以在你的日常生活中发挥作用。

---

## 💻 软件介绍 💻
以下是关于如何控制机器人并使其变得智能的一般思路：

### 🕹️ 基本控制

- **关节**（电机角度）控制 → 主从手臂控制

- **末端执行器姿态**控制 → VR远程控制
  
> [!NOTE]
> 对于第一个版本，我们主要关注硬件。LeRobot代码尚未修改。您可以通过将一个手臂连接到树莓派，另一个手臂连接到桌面电脑，通过远程控制重现演示0.0.5。XLeRobot的Lerobot代码将很快以最高优先级更新。


### 🧠 通用具身机器智能的路径（待完成）






### 🔈🇦🇩 广告时间：
- **我们的实验室**：[Rice RobotPI Lab](https://robotpilab.github.io/)
    - 我们的愿景之一：使用[时之笼](https://robotpilab.github.io/publication/caging/)和基于漏斗的操作方法，在不完美的现实世界情况下实现稳健的物体操作，如感知噪声、网络延迟、[丰富接触](https://robotpilab.github.io/publication/collision-inclusive-manipulation/)等。
- **模拟平台**（个人偏好）：[Maniskill](https://www.maniskill.ai/)
    - 🚀GPU加速并行模拟
    - 🎨通过光线追踪实现逼真的视觉效果
    - 🪶轻量级、一致、易于使用（相比Isaac Lab，个人认为）
    - 🤖支持[多种机器人](https://maniskill.readthedocs.io/en/latest/robots/index.html)（包括[SO100手臂](https://x.com/Stone_Tao/status/1910101218241978537)）


---
## 未来计划

### 硬件
<table>
  <tr>
    <td>
      
**紧急**

- 🔧 添加两种手臂基座选项：夹持式（当前）或螺钉固定式
- 🛠️ 添加与宜家推车金属网格完全兼容的连接板
    </td>
    </tr>
    <tr>
    <td>
    
**近期**

- 📸 在头部添加RealSense深度相机，补充手部RGB相机，实现精确的环境感知
- 👆 基本触觉感应
    </td>
  </tr>
</table>


> [!NOTE]
> 虽然更高级的升级完全可能（如切换到Jetson处理器、升级底盘或使用更好的电机），但这些会与本项目的核心使命相矛盾：**创建世界上最实惠、最易安装、即插即用的通用机器人开源平台**。但这些升级可以在未来作为可选附加组件列出，而不是主要方向。

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
- 🤖 使用Lerobot代码库中现有VLA模型执行简单任务
    </td>
    </tr>
    <tr>
    <td>
    
**近期**

- 🎯 基于AprilTag的精确校准
- 🗺️ 单RGBD相机自主导航
- 🌐 数字孪生对齐，用于sim2real应用
- 🧠 世界模型和基于物理的稳健操作
- 💬 连接MCP直接利用LLMs
    </td>
  </tr>
</table>

---

## 🎯 XLerobot适合谁？

- 🚀 **初创公司和实验室**：使用世界上最便宜的模块化平台更快地构建原型
- 👩🔬 **自研人员**：在不破费的情况下实验具身AI 💸
- 🎓 **机器人教育**：
  - 高中教师：将前沿机器人技术引入STEM课堂 🧪
  - 大学教授：为机器人/AI课程提供经济实惠的平台 📚
  - 学生：从初学者到研究人员 🎒→🎓
- 🤖 **DIY爱好者**：适合室内项目 - 植物护理、送货机器人、家庭自动化 🌱📦
---

## 局限性

（这个价格，还要啥自行车🚲？）

- 🔒 固定高度—添加稳定的升降平台将显著增加成本和组装难度
- 📏 与Aloha相比工作空间较小—虽然我们尝试充分利用SO100的工作空间，但手臂尺寸确实有限—不过XLeRobot仍然可以处理大多数任务
- ⚖️ 单臂负载能力有限—这就是为什么需要宜家推车
- 🛒 底座移动精度可能受到宜家推车轮子的影响—可以通过SLAM+闭环反馈控制解决

综合考虑—成本、社区支持、组装便捷性和实用性—XLeRobot脱颖而出，成为室内应用最具吸引力的低成本机器人（个人观点，轻喷）


---

### 主要贡献者

目前只有[我](https://vector-wangel.github.io/)。

这只是金字塔上的一小块砖，绝对离不开[LeRobot](https://github.com/huggingface/lerobot)、[SO-100](https://github.com/TheRobotStudio/SO-ARM100)、[Lekiwi](https://github.com/SIGRobotics-UIUC/LeKiwi)和[Bambot](https://github.com/timqian/bambot)。再次感谢这些由才华横溢的贡献者完成的详细而专业的项目。

期待与任何对为该项目做出贡献感兴趣的人合作！

与宜家没有利益关联（但瑞典肉丸香！🍝）
