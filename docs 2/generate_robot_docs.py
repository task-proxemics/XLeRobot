"""
Code to automatically generate robot documentation from the robot classes exported in the mani_skill.agents.robots module.

In the docs/ folder run generate_robot_docs.py to update the robot documentation. If a new robot is added make sure to add a entry to the
metadata/robots.json file which adds details about the robot not really needed in the code like the modelling quality.
"""


GLOBAL_ROBOT_DOCS_HEADER = """<!-- THIS IS ALL GENERATED DOCUMENTATION via generate_robot_docs.py. DO NOT MODIFY THIS FILE DIRECTLY. -->
"""

QUALITY_KEY_TO_DESCRIPTION = {
    "A+": "Values are the product of proper system identification",
    "A": "Values are realistic, but have not been properly identified",
    "B": "Stable, but some values are unrealistic",
    "C": "Conditionally stable, can be significantly improved",
}