# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'UNIGIS DOCS'
copyright = '2024, UNIGIS TMS'
author = 'UNIGIS TMS'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.intersphinx','sphinx.builders.html','sphinx.ext.ifconfig','sphinx_panels',]
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
language = "es"
html_static_path = ['_static',
                    ]
html_css_files = ['custom.css',
                  ]
latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '10pt',
}
latex_documents = [
    ('index', 'GettingStarted.tex', 'Getting Started', 'UNIGIS TMS', 'article'),
]
html_theme_options = {
    "light_logo": "Logolight.svg",
    "dark_logo": "logodark.svg",
    "sidebar_hide_name": True,
    "light_css_variables": {
        "color-brand-primary": "#343434",
        "color-brand-secundary": "#343434",
        "color-brand-content": "#00979b",
    },
    "dark_css_variables": {
        "color-brand-primary": "#d0d0d0",
        "color-brand-secundary": "#343434",
        "color-brand-content": "#00979b",
    },
}
html_title = 'UNIGIS | DOCUMENTACIÓN'
html_favicon = ''
html_show_sphinx = False
html_search_language = 'es'