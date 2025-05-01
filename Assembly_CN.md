#  ⚒️ 组装! ⚒️ 

[![en](https://img.shields.io/badge/lang-en-red.svg)](Assembly.md)
[![中文](https://img.shields.io/badge/lang-中文-green.svg)](Assembly_CN.md)

>预计组装时间：使用已组装好的SO100/SO101机械臂：1-2小时；从零开始：2-4小时
## 🤔 组装前准备 🤔
> [!TIP]  
> 如果你想跳过拧螺丝的乐趣（尽管每个机器人爱好者都应该至少尝试一次），一些公司以较高价格销售[预组装套件](https://github.com/TheRobotStudio/SO-ARM100#kits)用于SO100/SO101机械臂。
- 如果你没有组装好的SO100/SO101机械臂或Lekiwi：请按照[SO101机械臂仓库](https://github.com/huggingface/lerobot/blob/main/examples/12_use_so101.md)中的说明
    - [在你的PC上安装Lerobot](https://github.com/huggingface/lerobot/blob/main/examples/12_use_so101.md#install-lerobot)
- 根据[SO101](https://github.com/huggingface/lerobot/blob/main/examples/12_use_so101.md#configure-motors)和[LeKiwi](https://github.com/huggingface/lerobot/blob/main/examples/11_use_lekiwi.md#configure-motors)教程配置电机。
    - 你需要两组电机用于2个电机控制板：一组用于SO101机械臂（电机1-6），另一组用于Lekiwi（电机1-9）。
    - 提示：用记号笔在电机上写上编号，并区分不同控制板的电机（例如L1-L6和R1-R6）。

![image](https://github.com/user-attachments/assets/f3be78fe-0faa-454c-926d-ab1843b31d1f)


如果你已经有组装好并配置好电机的SO100/SO101机械臂和LeKiwi，可以跳过上述步骤。

## 🦾🦾 组装2个SO101机械臂 🦾🦾
> [!NOTE]
> 截至2025年4月28日，[SO101机械臂](https://github.com/TheRobotStudio/SO-ARM100)已发布，对从动机械臂模型进行了修改。这些变更包括简化零件和改进线缆管理，同时保持与XLeRobot的兼容性。我强烈建议大家构建SO101而不是SO100，因为组装速度快得多！


- 如果你已经有2个SO100/SO101机械臂，请跳过。
- 按照[SO101逐步组装说明](https://github.com/huggingface/lerobot/blob/main/examples/12_use_so101.md)构建2个相同的从动机械臂，使用2组电机（都预先编号为1-6）用于2个控制板。

![image](https://github.com/user-attachments/assets/68cba2d4-9777-49bc-ad8a-b2931658c474)

> [!TIP]  
> 用M3六角螺丝替换电机的默认十字头螺丝——它们更耐用，更容易安装，而且黑色螺丝与黑色机械臂更搭配。

## 🧑‍🦼‍➡️ 组装1个Lekiwi底座 🧑‍🦼‍➡️

- 如果你已经有Lekiwi底座，拆下电池、舵机支架等。底板上只保留3个安装好的带轮子的电机（保留接线）。
    - 如果没有，请按照[教程](https://github.com/SIGRobotics-UIUC/LeKiwi/blob/main/Assembly.md#2-bottom-plate-assembly)操作，但在底板上安装带轮子的电机后停止。
    - 无论如何，简化的Lekiwi底座应该看起来像这样：

![image](https://github.com/user-attachments/assets/1b0b0600-e666-4825-9233-807ed63e9020)

- 按照[教程](https://github.com/SIGRobotics-UIUC/LeKiwi/blob/main/Assembly.md#2-bottom-plate-assembly)正常接线，之后不要将线连接到控制板，而是使用延长线/连接器套件延长线缆，并让它悬挂着（暂时不要从顶板拉出）。

![image](https://github.com/user-attachments/assets/8d81267b-4b58-4af5-8bb3-e77b01d3df7f)

## 🛒 安装宜家RÅSKOG推车 🛒

- 以防你不小心丢弃了说明书，[这里是说明书](https://github.com/Vector-Wangel/XLeRobot/blob/main/others/Manuals_raskog_utility_cart.pdf)。

<img width="925" alt="1745897734515" src="https://github.com/user-attachments/assets/f9f95840-5080-4084-bebb-ea456a097d55" />



## 🧑‍🦼‍➡️ 安装Lekiwi底座 🛒

- 在顶板上安装3个[连接器](https://github.com/Vector-Wangel/XLeRobot/blob/main/3D_Models/3D_models_for_printing/XLeRobot_special/base_connector.stl)，放在你认为能提供稳定支撑的任何位置。或者直接按照这个示例：

![image](https://github.com/user-attachments/assets/c8233b2d-c58a-4ce5-8b25-b0e7832a60f3)

> [!TIP]  
> 将带连接器的Lekiwi底座放在推车下面，看看它是否能给推车提供足够的压力，同时推车的四个轮子仍能接触地面。如果不行，尝试直接在切片软件中略微调整连接器3D模型的z轴比例（保持xy轴比例不变）并重新打印。

> [!TIP]  
> 你可能需要将推车翻转过来进行下面的组装。


- 现在将带连接器的Lekiwi底座安装到宜家推车的底部，另一侧放置[复制的更薄顶板](https://github.com/Vector-Wangel/XLeRobot/blob/main/3D_Models/3D_models_for_printing/XLeRobot_special/base_plate_layer2_thinner.stl)。
> [!NOTE] 
> 在硬件的第一个版本中，要完美对齐所有3x4=12个螺丝可能有些困难。你可以尝试调整位置并稍微摇晃一下，找到一个可以均匀分布安装最多螺丝的位置。目前我能做到的最好效果是每个连接器2个螺丝，这可以提供非常稳定的支撑。我们也将很快更新一个与宜家推车金属网兼容的新硬件版本。

> [!NOTE] 
> 你还应该参考这个图（根据[Lekiwi教程](https://github.com/huggingface/lerobot/blob/main/examples/11_use_lekiwi.md#configure-motors)重制）来根据电机索引找到你想要的组装方向。左右是颠倒的，因为这是从下到上的视图。
>
> ![image](https://github.com/user-attachments/assets/35d4e60a-cf5a-46f1-8367-00e7990c27d3)



![image](https://github.com/user-attachments/assets/fe28320e-1851-495b-afc3-4e9302f92626)

- 使用尖嘴钳在顶部底座的相应孔处剪开金属网，只移除中央的"x"以保持结构完整性。这样就创建了布线的开口。然后，将之前延长的线从下方穿过推车向上走线。

![image](https://github.com/user-attachments/assets/b30abce8-a12c-44c8-8e0b-ee720cc1b8fa)




## 🦾🦾 安装机械臂 🛒

- 在当前版本中，为了更容易测试，SO101机械臂直接夹在推车上。将[机械臂底座](https://github.com/Vector-Wangel/XLeRobot/blob/main/3D_Models/3D_models_for_printing/XLeRobot_special/SO_5DOF_ARM100_Assemblybases.stl)放置在推车顶层的两个角落，然后用夹子固定。
- 别忘了把竹间实验室的耗材纸板线轴放在里面，提供稳定的结构支撑。

![image](https://github.com/user-attachments/assets/daaa6731-8886-4770-8042-77a5a0afdb74)

![image](https://github.com/user-attachments/assets/46239c09-3d37-4115-8dbd-3438ee5b3bac)


- 第二个版本将很快发布，提供机械臂和推车之间的螺栓连接选项，两个机械臂之间有标准化的间距。

> [!NOTE] 
> 在XLeRobot代码发布之前，要直接用原始Lekiwi代码测试XLeRobot的基本单臂版本，只需夹住与Lekiwi底座共享同一电机控制板的SO101机械臂。并将另一个夹在桌子上作为主控机械臂。


## 🔋 放置电池 🛒

- 你可以将它放在推车的中层或下层的任何位置，以保持较低的重心。电池底部有防滑设计，在正常操作期间不会轻易滑动。
    - 我将它放在中层，以便缩短线缆长度并方便使用（用于我的🥾徒步和🏕️露营）。
- 以防你也不小心丢弃了电池说明书，[这里是说明书](https://github.com/Vector-Wangel/XLeRobot/blob/main/others/Manual_Anker_SOLIX_C300_DC_Portable_Power_Station.pdf)。

![image](https://github.com/user-attachments/assets/c29b14c7-9bd7-45a9-bebd-8a7308a18a2a)


##  🧵 最后，接线 🧵
- 到目前为止，这就是XLeRobot不带电池的样子：

![image](https://github.com/user-attachments/assets/395e00c7-b8cf-4c4e-ac41-4b80c93c81a4)

- 使用尖嘴钳以与之前底层相同的方式，为上面两层的线缆布线剪开金属网。根据需要选择位置
    - 我选择了后边缘的中间位置，以最小化线缆长度并避免干扰推车存储。或者，你可以沿着侧面布线以获得更整洁的外观。
- 如果你还没有，准备好带连接器套件的延长5264线缆。
> [!NOTE] 
> 自己延长5264线缆时，要注意极性——连接反向会导致错误。

- 按照下面的接线图：
    - 将**Lekiwi底座**的延长5264**电机线缆**连接到**其中一个SO101机械臂**（这使底座和机械臂成为Lekiwi）。
    - 将2条**USB-C转USB-A数据线**从2个**电机控制板**连接到**树莓派**（留下2个USB-A插槽给摄像头）。
    - 连接所有3条**电源线**：2条**USB-C转DC(12V)**从2个**电机控制板**和1条**USB-C转USB-C**从**树莓派**，连接到电源的快充部分。同时充电时，每个插槽提供最高100W功率，经测试足以满足12V版本的运行需求。

> [!IMPORTANT]
> 为了保护电机控制板，确保最后连接电源线。在插拔其他线缆时，始终断开电源线。

> [!NOTE] 
> 在这最后一步之前，你需要先[在**树莓派**上安装软件并设置SSH](https://github.com/Vector-Wangel/XLeRobot/blob/main/Software.md)。

![image](https://github.com/user-attachments/assets/5367eb11-377e-4243-a9ff-746266012901)

<img width="725" alt="1745906421978" src="https://github.com/user-attachments/assets/cfaf47d6-b112-4c89-93ce-cb2e21515ee0" />

> [!IMPORTANT]
> XLeRobot完全组装好后，不要像推宜家推车那样推动它，因为这可能会损坏电机齿轮。相反，当你需要手动移动它时，请抬起机器人（约12kg）。

### 最后，让我们[🦾 让你的机器人动起来！ 🦿](Software.md)
