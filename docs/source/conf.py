import os
import sys
# conf.py

# -- Project Information -----------------------------------------------------

project = 'XLeRobot'
author = 'Vector & Nicole'
release = '0.1'

# -- General Configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
    "myst_parser",
    "sphinx_subfigure",
    "sphinxcontrib.video",
    "sphinx_togglebutton",
    "sphinx_design"
]
myst_enable_extensions = ["colon_fence", "dollarmath"]
myst_heading_anchors = 4
templates_path = ['_templates']
exclude_patterns = []

# -- Options for Markdown/MyST ----------------------------------------------

myst_enable_extensions = [
    "colon_fence",       # Allows ::: blocks (like admonitions)
]

# -- Options for HTML Output ------------------------------------------------

#html_theme = 'furo'       # Or 'sphinx_rtd_theme', 'alabaster', etc.
html_theme = "pydata_sphinx_theme"
html_static_path = ['_static']
