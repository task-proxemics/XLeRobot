# Get Started

Here's the full video for keyboard EE control

<video width="100%" style="max-width: 100%;" controls>
  <source src="https://github.com/user-attachments/assets/b8e630bd-1133-4941-acd1-d974f60098ff" type="video/mp4">
  Your browser does not support the video tag.
</video>

### Prerequisites

- Ubuntu operating system
- Basic familiarity with terminal commands
- [Miniconda](https://docs.anaconda.com/free/miniconda/index.html) (recommended)

### Installation

#### 1. Create a Conda Environment

If you already have a `lerobot` conda environment, you can use that. Otherwise, create a new environment:

```bash
conda create -y -n lerobot python=3.10
conda activate lerobot

```

> Note: It's recommended to have ManiSkill and lerobot code in the same environment for future sim2real deployment.
> 

#### 2. Install ManiSkill

Follow the [official installation instructions](https://maniskill.readthedocs.io/en/latest/user_guide/getting_started/installation.html) for ManiSkill.

```bash
# Basic installation
pip install mani-skill

# Download scene dataset
python -m mani_skill.utils.download_asset "ReplicaCAD"

```

If the dataset downloading goes wrong, you can directly download the dataset from [this google drive link](https://drive.google.com/file/d/1mqImztNX1LYZFBzt9z895C814RsyGe4N/view?usp=sharing). And then folder contents should go to

```bash
~/.maniskill/data/scene_datasets/replica_cad_dataset

```

Familiarize yourself with ManiSkill using the [quickstart guide](https://maniskill.readthedocs.io/en/latest/user_guide/getting_started/quickstart.html) and [demo scripts](https://maniskill.readthedocs.io/en/latest/user_guide/getting_started/quickstart.html). 

Try this command to test whether you have successfully installed Maniskill:
```bash
python -m mani_skill.examples.demo_random_action -e "ReplicaCAD_SceneManipulation-v1" \\
  --render-mode="human" --shader="rt-fast"

```

And you should be looking at something like this:

![image](https://github.com/user-attachments/assets/c7509843-f037-4f37-9b1c-e7cad939037c)

#### 3. Additional Dependencies

```bash
pip install pygame
```

#### 4. Replace Robot Files


Navigate to the ManiSkill package folder in your conda environment:

```bash
cd ~/miniconda3/envs/lerobot/lib/python3.10/site-packages/mani_skill
```

Replace the fetch robot code and assets with the XLeRobot files:

1. Download the [**replacement files for XLeRobot** here](https://github.com/Vector-Wangel/XLeRobot/tree/main/simulation/Maniskill):
2. Replace the files in /agents and /assets:
    
    ![image](https://github.com/user-attachments/assets/2675fb26-0302-45ec-a994-d4133ce8c239)
    
    ![image](https://github.com/user-attachments/assets/5a85d244-b342-45f5-bfa3-72f1ce11c83a)
    
3. Add control code to /examples:
    
    ![image](https://github.com/user-attachments/assets/654556ab-473f-44d2-8ff7-107c346882c6)
    

##### Usage

> The name of the files may be slightly different, check and change if you need.


##### Joint Control

Run the joint control demo with:

```bash
python -m mani_skill.examples.XLeRobot_demo_joint_ctrl -e "ReplicaCAD_SceneManipulation-v1"   --render-mode="human" --shader="rt-fast" -c "pd_joint_delta_pos_dual_arm"

```

#### Debug: Rename the links

If you encounter this error:

![image](https://github.com/user-attachments/assets/c81569a3-5c4f-4ba6-99d9-65d84937e767)

Navigate to the corresponding script

![image](https://github.com/user-attachments/assets/afda5567-3dfa-4e04-997f-4b5eff0dd1bc)

and change "torso_lift_link" to "head_camera_link"

![image](https://github.com/user-attachments/assets/05b52683-5e50-47fc-9cf7-9c021927db18) 


##### End Effector Control

Run the end effector control demo with:

```bash
python -m mani_skill.examples.demo_ctrl_action_ee -e "ReplicaCAD_SceneManipulation-v1"   --render-mode="human" --shader="rt-fast" -c "pd_joint_delta_pos_dual_arm"

```
![image](https://github.com/user-attachments/assets/11f6d417-9d1b-45d7-84c7-58b9d1611922)

##### End Effector Control with Camera Visualization via Rerun

To have camera visualization in real time, pip install rerun first:

```bash
pip install rerun-sdk

```
Then, run:

```bash
python -m mani_skill.examples.demo_ctrl_action_ee_cam_rerun -e "ReplicaCAD_SceneManipulation-v1"   --render-mode="human" --shader="rt-fast" -c "pd_joint_delta_pos_dual_arm"

```
![image](https://github.com/user-attachments/assets/12129988-e386-4d71-b1b2-79fe8492f419)

