<img src="media/XLeRobot.png" alt="Alt text" width="1200" />
This is the open-source repo for XLeRobot, including hardware desgins, bill of materials, modified LeRobot codes, etc. Currently actively working, planning on finish the first version XLeRbot 0.1.0 in a week, please be patient....

# XLeRobot 🤖
**🚀 Bringing Embodied AI to Everyone Cheaper Than the iPhone! 📱**

Built upon [LeRobot](https://github.com/huggingface/lerobot), [SO-100](https://github.com/TheRobotStudio/SO-ARM100), [Lekiwi](https://github.com/SIGRobotics-UIUC/LeKiwi), and [Bambot](https://github.com/timqian/bambot). This project could not be possible without standing on the shoulder of giants!


[![Apache License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Twitter/X](https://img.shields.io/twitter/follow/VectorWang?style=social)](https://twitter.com/VectorWang2)
[![Discord](https://dcbadge.vercel.app/api/server/C5P34WJ68S?style=flat)](https://discord.gg/s3KuuzsPFb)
---

<table>
  <tr>
    <td width="40%">
      <img src="media/realpic.jpg" alt="RealPic" width="100%">
    </td>
    <td width="60%">

## 🌟 Why XLeRobot? 
**We're on a mission to build the world's most affordable general-purpose applicable household robot** 🏡✨  
Imagine a modular, dual-arm mobile robot that costs less than your smartphone! By combining open-source magic 🧙♂️, IKEA hacks 🛠️, and modern AI algorithms 🤖, we're making robotics accessible to **EVERYONE**.

### Key Features:
- 🎯 **Cheapest DIY Robot Base**: Built on the IKEA RÅSKOG Cart ($39) - cheap but stable, available worldwide 🌍
- 🤝 **Massive Open Community**: Collaborate with thousands robot researchers and enthusiasts via [LeRobot Community](https://github.com/huggingface/lerobot)
- 🔋 **24/7 Power**: Utilize Anker power stations & solar panels ☀️ (Bonus: Use the battery for camping! ⛺)
- 🧩 **Lekiwi-Based Wiring**: For wiring it's the same as a single SO100 arm + Lekiwi, no need to rename your existed motors.
- 🧠 **AI That Actually Works**: Pre-trained models & datasets ready to deploy 🚀
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

## 🛠️ Total Cost (without 3D printed parts)
> [!NOTE] 
> We want XLeRobot to be powerful so there's only 12V version. 

| Price| US  | EU  | CN |
|---------|----:|----:|----:|
| **Build from Scratch** |  **$482**  |  **€545.8**  |  **¥2891**  |
| **Build from 2 SO100 arms**  |  **$499**  |  **€526**  |  **¥2829**  |
| **Build from 1 Lekiwi** |  **$248**  |  **€295**  |  **¥1571**  |


#### Parts For Two SO100 Arms (12V version, both follower arms):
| Part                                        | Amount | Unit Cost (US) | Buy US                                                                                                    | Unit Cost (EU) | Buy EU                                                                                            | Unit Cost (RMB) | Buy CN                                                                          |
| ------------------------------------------- | ------ | -------------- | --------------------------------------------------------------------------------------------------------- | -------------- | ------------------------------------------------------------------------------------------------- | --------------- | ------------------------------------------------------------------------------- |
| STS3215 Servo<sup>[1](#myfootnote1)</sup>   | 12     | $15            | [Alibaba](https://www.alibaba.com/product-detail/6PCS-7-4V-STS3215-Servos-for_1600523509006.html)         | 13€            | [Alibaba](https://www.alibaba.com/product-detail/6PCS-7-4V-STS3215-Servos-for_1600523509006.html) | ￥97.72         | [TaoBao](https://item.taobao.com/item.htm?id=712179366565&skuId=5268252241438)  |
| Motor Control Board                         | 2      | $11            | [Amazon](https://www.amazon.com/Waveshare-Integrates-Control-Circuit-Supports/dp/B0CTMM4LWK/)             | 12€            | [Amazon](https://www.amazon.fr/-/en/dp/B0CJ6TP3TP/)                                               | ￥27            | [TaoBao](https://detail.tmall.com/item.htm?id=738817173460&skuId=5096283384143) |
| USB-C Cable 2 pcs                           | 1      | $7             | [Amazon](https://www.amazon.com/Charging-etguuds-Charger-Braided-Compatible/dp/B0B8NWLLW2/?th=1)          | 7€             | [Amazon](https://www.amazon.fr/dp/B07BNF842T/)                                                    | ￥23.9\*2       | [TaoBao](https://detail.tmall.com/item.htm?id=44425281296&skuId=5611379016222)  |
| Power Supply<sup>[2](#myfootnote2)</sup>    | 2      | $10            | [Amazon](https://www.amazon.com/Facmogu-Switching-Transformer-Compatible-5-5x2-1mm/dp/B087LY41PV/)        | 13€            | [Amazon](https://www.amazon.fr/-/en/dp/B01HRR9GY4/)                                               | ￥22.31         | [TaoBao](https://item.taobao.com/item.htm?id=544824248494&skuId=4974994129990)  |
| Table Clamp 4pcs                            | 1      | $9             | [Amazon](https://www.amazon.com/TAODAN-Trigger-Ratchet-Woodworking-Processes/dp/B0DJNXF8WH?rps=1&sr=1-18) | ￥9.2          | [TaoBao](https://detail.tmall.com/item.htm?id=801399113134&skuId=5633627126649)                   |
| Screwdriver Set<sup>[3](#myfootnote3)</sup> | 1      | $6             | [Amazon](https://www.amazon.com/Precision-Phillips-Screwdriver-Electronics-Computer/dp/B0DB227RTH)        | 10€            | [Amazon](https://www.amazon.fr/dp/B08ZXVMVYD/)                                                    | ￥14.9          | [TaoBao](https://detail.tmall.com/item.htm?id=675684600845&skuId=4856851392176) |
| Total                                       | ---    | $232           | ---                                                                                                       | 244€           | ---                                                                                               | ￥1343.16       | ---                                                                             |

Not affiliated with IKEA (but we love swedish meatball! 🍝)

---

## 🎯 Demo Video 0.0.5

This is currently just a single arm version of directly implementing Lekiwi, teleoped with another arm 
(FYI: The follow arm hardware can be also used as the leader arm, the only difference is that it's geared so there will be some resistance)

https://github.com/user-attachments/assets/2e9eb3c9-af16-4af2-8748-8f936278c8eb


