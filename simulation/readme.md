Here I will put my code in [Maniskill Simulator](https://www.maniskill.ai/).

Follow the [install instructions](https://maniskill.readthedocs.io/en/latest/user_guide/getting_started/installation.html) in Maniskill first. It's best to pip install Maniskill in the same environment as lerobot so that you can do sim2real later.

Get yourself familiar with Maniskill with its [quickstart guide](https://maniskill.readthedocs.io/en/latest/user_guide/getting_started/quickstart.html) and [demo scripts](https://maniskill.readthedocs.io/en/latest/user_guide/getting_started/quickstart.html).

Navigate to the Maniskill package folder in your lerobot environment, in ubuntu if you're using conda it should be something like:

..../miniconda3/envs/lerobot(or the name of your environment)/lib/python3.10/site-packages/mani_skill

Then directly replace the fetch robot code and assets with the XLeRobot I provide here (make a copy of fetch if you still want to use that robot later).

.\agents\robots\fetch
.\assets\robots\fetch

Put the control code for both joint control and ee control into \example

in your terminal, run:

python -m mani_skill.examples.demo_xlerobot_joint_control -e "ReplicaCAD_SceneManipulation-v1" \
  --render-mode="human" --shader="rt-fast" # faster ray-tracing option but lower quality

for joint control, and

python -m mani_skill.examples.demo_xlerobot_ee_control -e "ReplicaCAD_SceneManipulation-v1" \
  --render-mode="human" --shader="rt-fast" # faster ray-tracing option but lower quality

for end effector control

You can also change the scene to other mobile robot scences in Maniskill, such as: ai2thor, kitchen counter, and "OpenCabinetDrawer-v1"
  

  
