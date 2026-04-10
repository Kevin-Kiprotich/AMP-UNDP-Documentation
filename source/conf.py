# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Africa Minigrids Program'
copyright = '2026, LocateIT Ke'
author = 'LocateIT Ltd'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_css_files=['css/custom.css']

html_theme_options = {
    "logo": {
        "image_light": "_static/amp/AMP-logo-blue.png",
        "image_dark": "_static/amp/AMP-logo-blue.png",
        "text": "AFRICA MINIGRIDS PROGRAM (AMP) DIGITAL PLATFORM",
    },
    "navbar_start": ["navbar_logo"],
    # "navbar_center": ["navbar-nav"],
    "navbar_end": ["amp_partners", "theme-switcher", "navbar-icon-links"],
    "header_links_before_dropdown": 5,
    "show_nav_level": 1,
    "navigation_with_keys": True,
}