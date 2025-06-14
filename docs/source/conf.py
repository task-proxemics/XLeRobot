import os
import sys
# conf.py

# -- Project Information -----------------------------------------------------

project = 'XLeRobot'
author = 'Your Name or Team'
release = '0.1'

# -- General Configuration ---------------------------------------------------

extensions = [
    'myst_parser',       # Enables Markdown support
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for Markdown/MyST ----------------------------------------------

myst_enable_extensions = [
    "colon_fence",       # Allows ::: blocks (like admonitions)
]

# -- Options for HTML Output ------------------------------------------------

html_theme = 'furo'       # Or 'sphinx_rtd_theme', 'alabaster', etc.
html_static_path = ['_static']
