# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'a'
copyright = '2024, a'
author = 'a'
release = 'a'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
'css/custom.css',
]

custom.css
img[alt="pic"] {
max-width: 600px;
display: block;
}


from recommonmark.parser import CommonMarkParser
from recommonmark.transform import AutoStructify
    source_parsers = {
    '.md': CommonMarkParser,
    }

    source_suffix = ['.rst', '.md']
    extensions = [
    'sphinx_markdown_tables',
    'recommonmark'
    ]

    Update theme:
    html_theme = 'sphinx_rtd_theme'