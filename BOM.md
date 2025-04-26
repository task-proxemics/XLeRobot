# Bill of Materials

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
