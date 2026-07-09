# Sphinx configuration file
# Concept Art English: Survival & Influence in AAA Pipelines

project = 'Concept Art English'
copyright = '2026, Concept Art English Project'
author = 'Concept Art English Team'

extensions = [
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx_markdown_tables',
    'myst_parser',
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
]

# -- Language ----------------------------------------------------------
language = 'en'

# -- Intersphinx -------------------------------------------------------
# Disabled: requires external network access
# intersphinx_mapping = {
#     'python': ('https://docs.python.org/3', None),
# }
