# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "sphinx-revealjs-174"
copyright = "2024, Kazuya Takei"
author = "Kazuya Takei"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_revealjs",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", ".venv"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]
revealjs_static_path = html_static_path
revealjs_script_conf = {
    # Add the current slide number to the URL hash so that reloading the
    # page/copying the URL will return you to the same slide
    "hash": True,
    # simplemenu, see https://github.com/martinomagnifico/reveal.js-simplemenu
    #   https://martinomagnifico.github.io/reveal.js-simplemenu/demo.html#/3/3
    "simplemenu": {
        "barhtml": {"header": "<div class='menubar'><ul class='menu'></ul></div>"}
    },
}

revealjs_script_plugins = [
    {
        "src": "simplemenu.js",
        "name": "Simplemenu",
    },
]
