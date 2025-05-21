# XLeRobot

XLeRobot is a versatile robotic control system built upon ManiSkill and RoboCasa. Special thanks to Stone Tao, the main leader on ManiSkill3, for his patient guidance and detailed discussions that helped accelerate our integration with ManiSkill.

## Capabilities

XLeRobot offers multiple control modes and features:

- **Keyboard base movement and joint control** ([demo video](#))
- **Keyboard base movement and end effector control** with built-in analytical IK function (used in main demos)
- **VR-based end effector control** using Oculus Quest:
  - Choose between VR joystick or purely hand tracking
  - Currently offers position control only
  - Pose control and gripper control based on hand gestures coming soon

All demos can be run in multiple different scenes according to your needs.

**Research Opportunities:**
- MPC (Model Predictive Control)
- Imitation learning
- Data collection
- Reinforcement learning
- Vision-language-action (VLA)
- And much more...

## Hardware Setup Options

XLeRobot provides 4 versions of hardware setup:

1. **Basic fixed arm bases (back)** - Arms mounted on the back of the cart to fully utilize storage space *(Available in XLeRobot 0.2.0)*
2. **Fixed arm bases (front)** - Arms mounted on the front for better dual-arm manipulation but reduced cart storage *(Available in XLeRobot 0.2.0)*
3. **Moving arm bases on the z-axis (front)** - For potential future applications
4. **Moving arm bases on the z-axis (back)** - For potential future applications

> **Note:** The two fixed base versions will be completed in the upcoming XLeRobot 0.2.0 release next month.

## Installation

### 1. Create a Conda Environment

```bash
conda create -y -n lerobot python=3.10
conda activate lerobot
```

### 2. Install ManiSkill

Follow the [official installation instructions](https://maniskill.readthedocs.io/en/latest/user_guide/getting_started/installation.html) for ManiSkill.

```bash
# Basic installation
pip install mani-skill

# Download scene dataset
python -m mani_skill.utils.download_asset
```

### 3. Install Additional Dependencies

```bash
pip install pygame
```

### 4. Replace Robot Files

Navigate to the ManiSkill package folder in your conda environment:

```bash
cd ~/miniconda3/envs/lerobot/lib/python3.10/site-packages/mani_skill
```

Replace the fetch robot code and assets with the XLeRobot files:

```bash
# Replace with your provided files
cp -r /path/to/your/xlerobot/agents/robots/fetch ./agents/robots/
cp -r /path/to/your/xlerobot/assets/robots/fetch ./assets/robots/
cp -r /path/to/your/xlerobot/examples/* ./examples/
```

## Usage

### Joint Control

```bash
python -m mani_skill.examples.demo_xlerobot_joint_control -e "ReplicaCAD_SceneManipulation-v1" --render-mode="human" --shader="rt-fast"
```

### End Effector Control

```bash
python -m mani_skill.examples.demo_xlerobot_ee_control -e "ReplicaCAD_SceneManipulation-v1" --render-mode="human" --shader="rt-fast"
```

## Teleop Demos in Simulation

- All demos are implemented in `demo_ee_control.py` using 3 different scenes in ManiSkill
- A custom hybrid joint-ee controller has been developed specifically for the SO100 arm
- All tasks in the demos were completed in a single take (only removing periods with no operation and manual camera adjustments)
- Robot actions are controlled entirely via keyboard
- Camera integration coming in XLeRobot 0.2.0

**Current Implementation Notes:**
- For convenience, XLeRobot currently replaces the Fetch robot's URDF model and settings in ManiSkill
- Future ManiSkill releases will support XLeRobot as an independent robot
- The current base in simulation only has forward/backward movement and steering (2 DoF)
- The real XLeRobot uses omnidirectional wheels with 3 DoF (forward/backward, left/right, rotation)
- Some simulation instability may occur due to collision model parameters, resulting in unstable grasping or high-frequency vibrations

## The Hybrid Joint-EE Controller

XLeRobot uses a hybrid controller that decouples traditional IK into different components that can be either directly controlled or solved via simple analytical solutions:

### Horizontal Plane Control
- Uses polar coordinates rather than Cartesian coordinates
- Can be directly controlled by joint1
- Advantages of polar coordinates:
  - More intuitive for human control, simplifying keyboard/VR interaction
  - Beneficial for task planning by leveraging rotational symmetry (reducing search/state space from 3D to 2D)
  - Provides symmetry benefits for AI model training (focusing on the vertical plane)
  - SO2 rotational symmetry has been proven superior in papers by researchers like Dian Wang (Equivariant Models for RL, VLA, grasp optimization)

### Vertical Plane Control
- Without considering robot orientation, the vertical plane becomes a 2-joint linkage
- With SO100's angle>0 constraint, there's a unique analytical solution based on the law of cosines

### Tip Orientation
- With 5 DoF, yaw cannot be changed
- SO100's 5th joint directly corresponds to roll
- SO100's 4th joint directly corresponds to pitch (compensating for vertical plane height)

## Limitations

The basic fixed base version has areas it can't reach. This is a design consideration: do you want a robot that could potentially be hacked or misbehave to have physical access to every drawer you own?

## Advanced Strategies

### Mobile Base Integration
- The mobile base provides additional degrees of freedom and driving force to compensate for the SO100 arm's limitations (5 DoF, small range, low payload)
- Example: When opening a refrigerator door, despite the arm's 1.2kg payload limit, using the cart's backward motion with an extended arm creates pulling force limited by wheel motor torque, gripper friction, and tire-ground friction (generally higher than arm payload)

### Non-Prehensile Manipulation
- Utilizing non-grasping manipulation greatly improves efficiency, robustness, and extends physical limits
- Understanding the physical world: The robot needs to comprehend the physical environment and predict interactions through intuitive physics
- Before developing complete intelligence, cost function/energy function-based optimization/MPC/model-based RL can assist with complex planning

### Advanced Techniques
- Collision-based grasping for cluttered environments
- Strategy-level error correction (e.g., switching targets when a bottle tips over)
- Reference: "Caging in Time" (accepted by IJRR) provides methods for robust object manipulation, especially non-prehensile manipulation
- Rice RobotPI Lab's main track is funnel-based manipulation

## Troubleshooting

If you encounter errors, try these solutions:

- If you see "link name" errors, navigate to the script and change the link name
- If you experience collision-related errors, try commenting out the avoid collision list

## VR Integration

To enable VR with Oculus:

1. Install Oculus reader according to the official documentation
2. Replace the reader.py file with our provided version:
   ```bash
   cp /path/to/your/reader.py /path/to/oculus/reader/
   ```
3. Update the path of the Oculus reader folder in your configuration