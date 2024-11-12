# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

import os
import re

# Set canonical URL from the Read the Docs Domain
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "")

html_context = {}
# Tell Jinja2 templates the build is running on Read the Docs
if os.environ.get("READTHEDOCS", "") == "True":
    html_context["READTHEDOCS"] = True

# The master toctree document.
master_doc = "index"

project = "Neural Network Tutorial"
author = "Min Ye, Veit Schiele"
copyright = f"2024, {author}"

# The full version, including alpha/beta/rc tags
release = re.sub("^v", "", os.popen("git describe --abbrev=0").read().strip())


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "nbsphinx",
    "IPython.sphinxext.ipython_console_highlighting",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.graphviz",
    "sphinx.ext.todo",
    "sphinxcontrib.cairosvgconverter",
    "sphinxext.opengraph",
    "sphinx_copybutton",
    "sphinx_inline_tabs",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "de"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "**/.ipynb_checkpoints",
    "**/.*.ipynb",
    "**/input.ipynb",
    "**/output*.ipynb",
]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "furo"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# Change default HTML title
html_title = f"{project} {release}"

# html_theme_options = {}
# html_sidebars = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_logo = "_static/images/logo/logo.png"
html_favicon = "_static/images/logo/favicon.ico"

html_css_files = [
    "css/alerts.css",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'a4paper',
    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '9pt',
    # Additional stuff for the LaTeX preamble.
    "preamble": r"\usepackage{pmboxdraw}",
    # Latex figure (float) alignment
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "NeuralNetworkTutorial.tex",
        "Neural Network Tutorial",
        "Min Ye",
        "manual",
    ),
]

# -- nbsphinx configuration --------------------------------------------------

nbsphinx_allow_errors = True
# nbsphinx_execute = 'always'

# -- intersphinx configuration -----------------------------------------------

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}


def setup(app):
    # from sphinx.ext.autodoc import cut_lines
    # app.connect('autodoc-process-docstring', cut_lines(4, what=['module']))
    app.add_object_type(
        "label",
        "label",
        objname="label value",
        indextemplate="pair: %s; label value",
    )


# -- graphviz configuration --------------------------------------------------

graphviz_output_format = "svg"