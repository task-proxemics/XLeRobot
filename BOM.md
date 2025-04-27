# Bill of Materials

# 🛠️ Total Cost 
> [!NOTE] 
> We want XLeRobot to be powerful, so there's only a 12V version.
> Doesn't include cost of 3D printing

| Price| US  | EU  | CN |
|---------|----:|----:|----:|
| **Build from Scratch** |  **$XX**  |  **€XX**  |  **¥XX**  |
| **Build from 2 SO100 arms**  |  **$XX**  |  **€XX**  |  **¥XX**  |
| **Build from 1 Lekiwi** |  **$XX**  |  **€XX**  |  **¥XX**  |
| **Build from 1 Lekiwi and 1 SO100 arm** |  **$XX**  |  **€XX**  |  **¥XX**  |

# Assembly Tools

Skip this section if you already have these tools:
| Part | Amount | Unit Cost (US) | Buy (US) | Unit Cost (EU) | Buy (EU) | Unit Cost (CN) | Buy (CN) |
| - | - | - | - | - | - | - | - |
| M3 Screws and Nuts Set | 1 | $14.99 | [Amazon](https://a.co/d/4NfBpNS) | €23.5 | [Amazon](https://www.amazon.fr/Cylindrique-Inoxydable-M2-Socket-Assortiment/dp/B09Y8WYFWD/) | ¥40 | [taobao](https://item.taobao.com/item.htm?abbucket=14&detail_redpacket_pop=true&id=614760389801&ltk2=1745773029845cww4kdo78gamgx9c4hl35&ns=1&priceTId=2100c82517457730113487286e0bc2&query=m3%E5%86%85%E5%85%AD%E8%A7%92%E8%9E%BA%E4%B8%9D%E5%A5%97%E8%A3%85&skuId=4501144438660&spm=a21n57.1.hoverItem.20&utparam=%7B%22aplus_abtest%22%3A%2256d17236f81617358b208d1cf05155cf%22%7D&xxc=taobaoSearch) |
| Flush cutter | 1 | $6.99 | [Amazon](https://a.co/d/61KlrZp) | €23.5 | [Amazon](https://www.amazon.fr/Cylindrique-Inoxydable-M2-Socket-Assortiment/dp/B09Y8WYFWD/) | ¥5.8 | [taobao](https://item.taobao.com/item.htm?abbucket=14&detail_redpacket_pop=true&id=706039364576&ltk2=1745773187187erh7ued4gqcyyk5573rir&ns=1&priceTId=2100c82517457731790992641e0bc2&query=%E5%89%AA%E7%BA%BF%E9%92%B3&skuId=4964064736437&spm=a21n57.1.hoverItem.5&utparam=%7B%22aplus_abtest%22%3A%22474017eea48950332239eaf78d326730%22%7D&xxc=taobaoSearch) |
| **Total** || **$219.98** || **€209.98** || **¥1013.15** ||


# Additional Components for Xelerobot

If you have already built SO100 Arms and Lekiwi, you'll need these additional parts:
| Part | Amount | Unit Cost (US) | Buy (US) | Unit Cost (EU) | Buy (EU) | Unit Cost (CN) | Buy (CN) |
| - | - | - | - | - | - | - | - |
| IKEA RÅSKOG Utility cart | 1 | $39.99 | [IKEA](https://www.ikea.com/us/en/p/raskog-utility-cart-black-40582181/#content) | €39.99 | [IKEA](https://www.ikea.com/nl/en/p/raskog-trolley-white-30586783/) |￥249 |[IKEA](https://www.ikea.cn/cn/zh/p/raskog-la-si-ke-shou-tui-che-bai-se-70376721/)|
| Anker SOLIX C300 Power Station | 1 | $179.99 | [Anker](https://www.ankersolix.com/products/c300-dc?variant=49702163972426&ref=naviMenu_pps) | €169.99 | [Anker](https://www.anker.com/eu-en/products/a17260z1?variant=44598991323326&ref=naviMenu_pps) |￥764.15 |[Taobao](https://e.tb.cn/h.6PQRiymMOteAgrb?tk=m6L3V3frrfp )              |
| Long 5264 wires | 1 | $21.99 | [Amazon](https://www.amazon.com/dp/B0D2W47V8V) Connector Kit | €0 | [TODO]() | ¥20 | [Taobao](https://e.tb.cn/h.6ZvsvUU7wlxTIqu?tk=mz7PeJUloea) 3P-1000mm and 5264 connector|(https://e.tb.cn/h.6dM2Zgsj77fyegN?tk=SH29eF6flAb)|
| Type C to DC wire(12V/5V) | 2 | $8.99 | [Amazon 12V](https://www.amazon.com/dp/B0CDBWHXDZ) | €0 | [TODO]() | ¥20 | [Taobao 12V](https://e.tb.cn/h.6ZvuOW01EmvvHq1?tk=nzvFeJUnyuB) |
| **Total** || **$219.98** || **€209.98** || **¥1013.15** ||

- I couldn't find any ready-made long 5264 wires for purchase in US—**only connector kits** that require manual assembly to extend the length (easy to do though).
- You can definitely choose **similar cheaper cart not from IKEA**, in this case [slight change]() to the 3D printed part might be needed.
- While this battery may seem expensive, its functionality and reliability far exceed regular power banks. (Like in electric vehicles, the battery is also one of the most expensive components.)
- You can also choose **other batteries**, just make sure the maximum watts is large enough to power 2x arms, wheels, and RasberryPi at the same time.



- Extended cable kit (Important: When wiring, maintain the same wire sequence as the original to avoid errors)
- USB Type-C to DC cable

# Complete Build Guide

For those starting from scratch (without SO100 or Lekiwi arms), follow these steps:

## Required Components

- 2x SO100 arms
- 1x Lekiwi base

These components will allow you to replicate Demo 0.0.5, enabling master-slave arm control and direct PC control of both arms.

Note: There's no need to remove the leader motor gear. This is not recommended if you're only planning to use two arms.

# Optional Enhancements

- Arm cameras (reference specifications to be added)
- Additional two SO100 sets for dual-arm master-slave control
- 3M gripper tape (based on UMI gripper specifications) for improved grip stability
- VR headset for virtual reality control
- For additional add-ons and accessories, please refer to the Lerobot repository and Discord group discussions

## SO100 arm x2

## Lekiwi base

以上的零件已经能复现Demo 0.0.5，通过主从臂遥控，以及直接通过pc控制双臂。如果需要更完整的控制与自动化功能，需要添置

（Note：无需拆除leader电机的gear，我也不建议在只打算买两条臂的人这样做）

# other optional parts

- arm cameras，此处引用xxx
- 如果想实现双臂的主从臂遥控，需要额外的两套so100
- 我目前用的这个3M的gripper tape基于之前UMI gripper提供的款式，能大大增加抓取的稳定性
- 如果想实现vr遥控，of course you need a vr
- 其他各种相关add on 可以参考lerobot repo，以及lerobot discord group的讨论

This page provides a complete list of parts needed to build the XLeRobot mobile manipulator. 

> [!NOTE] 
> Part of this list is copied and reogranized based on the bill of materials of [SO100 arm](https://github.com/TheRobotStudio/SO-ARM100/blob/main/README.md) and [Lekiwi](https://github.com/SIGRobotics-UIUC/LeKiwi/blob/main/BOM.md). Please also refer to these original sources for any updates to their respective parts lists.

### Beyond SO100 and Lekiwi

| Part | Amount | Unit Cost (US) | Buy (US) | Unit Cost (EU) | Buy (EU) | Unit Cost (CN) | Buy (CN) |
| - | - | - | - | - | - | - | - |
| IKEA RÅSKOG Utility cart | 1 | $39.99 | [IKEA](https://www.ikea.com/us/en/p/raskog-utility-cart-black-40582181/#content) | €39.99 | [IKEA](https://www.ikea.com/nl/en/p/raskog-trolley-white-30586783/) |￥249 |[IKEA](https://www.ikea.cn/cn/zh/p/raskog-la-si-ke-shou-tui-che-bai-se-70376721/)|
| Anker SOLIX C300 Power Station | 1 | $179.99 | [Anker](https://www.ankersolix.com/products/c300-dc?variant=49702163972426&ref=naviMenu_pps) | €169.99 | [Anker](https://www.anker.com/eu-en/products/a17260z1?variant=44598991323326&ref=naviMenu_pps) |￥764.15 |[Taobao](https://e.tb.cn/h.6PQRiymMOteAgrb?tk=m6L3V3frrfp )              |
| **Total** || **$219.98** || **€209.98** || **¥1013.15** ||

> [!NOTE] 
> You can definitely choose cheaper cart not from IKEA, in this case slight change to the 3D printed part might be needed.
> You can also choose other kinds of batteries, just make sure the maximum watts is enough to power 2x arms, wheels, and RasberryPi.

### Lekiwi Mobile Base:
| Part | Amount | Unit Cost (US) | Buy (US) | Unit Cost (EU) | Buy (EU) | Unit Cost (CN) | Buy (CN) |
| - | - | - | - | - | - | - | - |
| 4" Omni wheels | 3 | $9.99 | [VEX Robotics](https://www.vexrobotics.com/omni-wheels.html?srsltid=AfmBOorWdWT-FIiWSAbicYWSxqYr-d5X3CJSGxMkO33WO0thwlTn4DQu) | €24.5 | [RobotShop](https://eu.robotshop.com/products/100mm-omnidirectional-wheel-brass-bearing-rollers) |￥135 |[PDD](https://mobile.yangkeduo.com/goods.html?ps=kKWPC7xuzw "https://mobile.yangkeduo.com/goods.html?ps=kKWPC7xuzw")|
| 12v ST3215 Feetech Servo | 3 | $13.89 | [Alibaba](https://www.alibaba.com/product-detail/Feetech-STS3215-SO-ARM100-Servo-12V_1601292634404.html?spm=a2700.details.you_may_like.3.5ab1478e45kY42) | €13.38 | [Alibaba](https://www.alibaba.com/product-detail/Feetech-STS3215-SO-ARM100-Servo-12V_1601292634404.html?spm=a2700.details.you_may_like.3.5ab1478e45kY42)  | ￥110 |[Taobao](https://e.tb.cn/h.64H9u3maGWzIp5Q?tk=T5liexkG6Yz "https://e.tb.cn/h.64H9u3maGWzIp5Q?tk=T5liexkG6Yz")|
| M2 M3 M4 Assorted Screw Set | 1 | $14.99 | [Amazon](https://www.amazon.com/Button-Socket-Washers-Assortment-Machine/dp/B0BMQGJP3F) | €23.5 | [Amazon](https://www.amazon.fr/Cylindrique-Inoxydable-M2-Socket-Assortiment/dp/B09Y8WYFWD/) |￥25 |[Taobao（M2x5+M3套装+M3x10+M4x12）](https://e.tb.cn/h.64O1J2A9Is4pIJd "https://e.tb.cn/h.64O1J2A9Is4pIJd")              |
| **Total** || **$44.96** || **€97** || **¥430** ||

### Sensors and Compute:

| Part| Amount | Unit Cost (US) | Buy (US) | Unit Cost (EU) | Buy (EU) |  Unit Cost (CN) | Buy (CN) |
|--|:-:|:-:|-|:-:|-|:-:|-|
| Raspberry Pi 5 (4GB)| 1 |$60.00| [Adafruit](https://www.adafruit.com/product/5812)| €57.00| [Mouser](https://eu.mouser.com/ProductDetail/Raspberry-Pi/SC1111?qs=HoCaDK9Nz5fnLhlMNnKTiQ%3D%3D)|￥410|[Taobao](https://e.tb.cn/h.64IIvlisvAL15g8?tk=fdOVexkHECW "https://e.tb.cn/h.64IIvlisvAL15g8?tk=fdOVexkHECW")|
| USB camera<sup>[2](#footnote2)</sup> | 2 | $12.98 | [Amazon](https://a.co/d/236G8Wn) | €12.00 | [Amazon](https://www.amazon.fr/Vinmooog-equipement-Microphone-Enregistrement-conf%C3%A9rences/dp/B0BG1YJWFN/) |￥48|[Taobao](https://e.tb.cn/h.64ILq3suMKATfUx?tk=IPSEexQAvxu "https://e.tb.cn/h.64ILq3suMKATfUx?tk=IPSEexQAvxu")|
| microSD card | 1 | $11.23 | [Amazon](https://www.amazon.com/SanDisk-Extreme-microSDXC-Memory-Adapter/dp/B09X7C7LL1/) | €10.00 | [Amazon](https://www.amazon.fr/Lexar-Carte-Micro-adaptateur-Smartphone/dp/B08XZ2KS1F)|￥58|[Taobao](https://e.tb.cn/h.64DMZzLz5h26s12?tk=eImPex96lCQ "https://e.tb.cn/h.64DMZzLz5h26s12?tk=eImPex96lCQ")|
| **Total** ||  **$98**  ||  **€91** ||  **¥564** ||

### Other
| Part| Amount | Unit Cost (US) | Buy (US) | Unit Cost (EU) | Buy (EU) | Unit Cost (CN) | Buy (CN) |
|--|:-:|:-:|-|:-:|-|:-:|-|
| Table Clamp 4pcs | 1 | $18 | [Amazon](https://www.amazon.com/WORKPRO-Clamps-Woodworking-One-Handed-Spreader/dp/B0CQYDJWS8/) | € 21 | [Amazon](https://www.amazon.fr/dp/B08HW9VFM8/)| ¥10.8\*4  |[Taobao](https://e.tb.cn/h.64r5eomI6L59tBE?tk=gZWeex9fnlB "https://e.tb.cn/h.64r5eomI6L59tBE?tk=gZWeex9fnlB")|
| Screwdriver Set | 1 | $6 | [Amazon](https://www.amazon.com/Precision-Phillips-Screwdriver-Electronics-Computer/dp/B0DB227RTH) | €10 | [Amazon](https://www.amazon.fr/dp/B08ZXVMVYD/) | ￥20 |[Taobao](https://e.tb.cn/h.6ReL0wwgtPuSmNV?tk=3rLDV10AVtr)  |
| USB-C to USB-A Cable 2 pcs | 1 | $7 | [Amazon](https://www.amazon.com/Charging-etguuds-Charger-Braided-Compatible/dp/B0B8NWLLW2/?th=1) | €7 | [Amazon](https://www.amazon.fr/dp/B07BNF842T/) |￥17  |[Taobao](https://e.tb.cn/h.64HOv24RLmYC4Yh?tk=AXpgexkDFd4 "https://e.tb.cn/h.64HOv24RLmYC4Yh?tk=AXpgexkDFd4")|
| **Total** ||  **$31**  ||  **€38** || **¥80.20** ||

## 12V version :battery:

### SO-100 2 Robot Arm Teleoperation Set (12V):
| Part | Amount | Unit Cost (US) | Buy (US) | Unit Cost (EU) | Buy (EU) | Unit Cost (CN) | Buy (CN) |
|:---|:---:|:---:|:---|:---:|---:|:-:|-|
| 12v ST3215 Servo | 12 | $13.89 | [Alibaba](https://www.alibaba.com/product-detail/Feetech-STS3215-SO-ARM100-Servo-12V_1601292634404.html?spm=a2700.details.you_may_like.3.5ab1478e45kY42) | €13.38 | [Alibaba](https://www.alibaba.com/product-detail/Feetech-STS3215-SO-ARM100-Servo-12V_1601292634404.html?spm=a2700.details.you_may_like.3.5ab1478e45kY42) | ￥110  |[Taobao](https://e.tb.cn/h.64H9u3maGWzIp5Q?tk=T5liexkG6Yz "https://e.tb.cn/h.64H9u3maGWzIp5Q?tk=T5liexkG6Yz")|
| Motor Control Board | 2 | $10.55 | [Amazon](https://www.amazon.com/Waveshare-Integrates-Control-Circuit-Supports/dp/B0CTMM4LWK/) | €12.00 | [Amazon](https://www.amazon.fr/Waveshare-Integrates-Control-Applicable-Integrate/dp/B0CJ6TP3TP) | ￥24 |[Taobao](https://e.tb.cn/h.64DOUpLpB5crVdH?tk=BSaTex9UHWj "https://e.tb.cn/h.64DOUpLpB5crVdH?tk=BSaTex9UHWj")|
| Power Supply | 1 | $12 | [Amazon](https://www.amazon.com/ALITOVE-Adapter-Converter-100-240V-5-5x2-1mm/dp/B01GEA8PQA) | €15 | [Amazon](https://www.amazon.fr/LEDMO-Alimentation-Adaptateur-Transformateurs-Chargeur/dp/B07PGLXK4X) | ￥22  |[Taobao](https://e.tb.cn/h.64D9xUuAdpkswUx?tk=JRRwex94phr "https://e.tb.cn/h.64D9xUuAdpkswUx?tk=JRRwex94phr")|
| **Total** | | **$199.78** | | **€199.56** | | **￥1,390** | |



> Head to [3D Printing](3DPrinting.md) for the next step!

<br></br>

## Footnotes

<a name="footnote2">2</a>: Another supported camera option is the Arducam 5MP Wide Angle found [here](https://www.amazon.com/Arducam-Camera-Computer-Without-Microphone/dp/B0972KK7BC)
