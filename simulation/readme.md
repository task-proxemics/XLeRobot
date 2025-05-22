(Still a draft, may have false information, will delete this after I finish)

# Step-by-step Guide for XLeRobot Playground

## Prerequisites

- Ubuntu operating system
- Basic familiarity with terminal commands
- [Miniconda](https://docs.anaconda.com/free/miniconda/index.html) (recommended)

## Installation

### 1. Create a Conda Environment

If you already have a `lerobot` conda environment, you can use that. Otherwise, create a new environment:

```bash
conda create -y -n lerobot python=3.10
conda activate lerobot
```

> **Note**: It's recommended to have ManiSkill and lerobot code in the same environment for future sim2real deployment.

### 2. Install ManiSkill

Follow the [official installation instructions](https://maniskill.readthedocs.io/en/latest/user_guide/getting_started/installation.html) for ManiSkill.

```bash
# Basic installation
pip install mani-skill

# Download scene dataset
python -m mani_skill.utils.download_asset
```

Familiarize yourself with ManiSkill using the [quickstart guide](https://maniskill.readthedocs.io/en/latest/user_guide/getting_started/quickstart.html) and [demo scripts](https://maniskill.readthedocs.io/en/latest/user_guide/getting_started/quickstart.html).

### 3. Additional Dependencies

```bash
pip install pygame
```

### 4. Replace Robot Files

Navigate to the ManiSkill package folder in your conda environment:

```bash
cd ~/miniconda3/envs/lerobot/lib/python3.10/site-packages/mani_skill
```

Replace the fetch robot code and assets with the XLeRobot files:

1. Make a backup of the original files (optional but recommended):
   ```bash
   cp -r ./agents/robots/fetch ./agents/robots/fetch_backup
   cp -r ./assets/robots/fetch ./assets/robots/fetch_backup
   ```

2. Replace the files:
   ```bash
   # Replace with your provided files
   cp -r /path/to/your/xlerobot/agents/robots/fetch ./agents/robots/
   cp -r /path/to/your/xlerobot/assets/robots/fetch ./assets/robots/
   ```

3. Add control code examples:
   ```bash
   cp -r /path/to/your/xlerobot/examples/* ./examples/
   ```

## Usage

### Joint Control

Run the joint control demo with:

```bash
python -m mani_skill.examples.demo_xlerobot_joint_control -e "ReplicaCAD_SceneManipulation-v1" --render-mode="human" --shader="rt-fast"
```

### End Effector Control

Run the end effector control demo with:

```bash
python -m mani_skill.examples.demo_xlerobot_ee_control -e "ReplicaCAD_SceneManipulation-v1" --render-mode="human" --shader="rt-fast"
```

> **Note**: `--shader="rt-fast"` provides faster ray-tracing but lower quality.

### Available Environments

You can use various environments with XLeRobot:

- `ReplicaCAD_SceneManipulation-v1` (default)
- AI2THOR scenes
- Kitchen counter scenes
- `OpenCabinetDrawer-v1`


## VR Integration

To enable VR with Oculus:

1. Install Oculus reader according to the official documentation
2. Replace the reader.py file with the provided version:
   ```bash
   cp /path/to/your/reader.py /path/to/oculus/reader/
   ```
3. Update the path of the Oculus reader folder in your configuration

## Custom Hardware Integration

To use different hardware versions:

1. Modify the URDF path in `agents/robots/fetch.py`
2. You may need to adjust the size of `qpos` depending on your hardware configuration

## Troubleshooting

### Common Errors

If you encounter an error like `xxxxxx`:
- Navigate to the script and change the link name

If you encounter an error like `yyyyyy`:
- Navigate to the script and comment out the avoid collision list

## Additional Resources

For more robotic environments, consider:
- [RoboCasa](https://github.com/StanfordVL/robocasa)
- [AI2-THOR](https://ai2thor.allenai.org/)



  
