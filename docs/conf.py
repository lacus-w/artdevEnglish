# Sphinx configuration file
# Concept Art English: Survival & Influence in AAA Pipelines

project = 'Concept Art English'
copyright = '2025, Concept Art English Project'
author = 'Concept Art English Team'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx_markdown_tables',
]

source_suffix = '.md'
master_doc = 'index'

# -- Theme configuration ------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Markdown extensions ------------------------------------------------
# Uses recommonmark or myst-parser (recommended)
# pip install myst-parser

# If using myst-parser:
myst_enable_extensions = [
    "deflist",
    "tasklist",
    "fieldlist",
    "html_admonition",
    "html_image",
    "colon_fence",
    "table",
]

# -- Language ----------------------------------------------------------
language = 'en'

# -- Intersphinx -------------------------------------------------------
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}