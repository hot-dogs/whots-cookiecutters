# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.abspath("."))

# -- Project information -----------------------------------------------------

project = "WHOTS-{{cookiecutter.current_whots_deployment_number}}"
copyright = f"{datetime.now().year}, Hawaii Ocean Time-series (HOT)"
author = "{{cookiecutter.creator}}"

# The full version, including alpha/beta/rc tags
release = "1.0.0"
version = "1.0.0"

# -- General configuration ---------------------------------------------------
extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "nbsphinx",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
    "sphinxcontrib.bibtex",
]
bibtex_bibfiles = ["latex_templates/refs.bib"]
bibtex_default_style = "unsrt"
bibtex_reference_style = "author_year"

myst_url_schemes = ["http", "https"]

# Added cross reference for headings
myst_heading_anchors = 3

# Add numbered roles
numfig = true

# Enable some MyST extensions.
myst_enable_extensions = [
    "colon_fence",
]

# Make sure the explicity target is unique
autosectionlabel_prefix_document = true
autosectionlabel_maxdepth = 3

# Add any paths that contain templates here, relative to this directory.

templates_path = ["_templates"]
source_suffix = {".rst": "restructuredtext", ".md": "markdown"}
master_doc = "index"


# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "_build",
    "build",
    "thumbs.db",
    ".ds_store",
    ".env",
    ".rst",
    "Thumbs.db",
    ".DS_store",
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_theme = "sphinx_book_theme"
html_logo = "_static/_images/new_logo_hot.png"
html_title = "Data Report #{{cookiecutter.current_whots_deployment_number}}"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_theme_options = {
    "repository_url": "https://github.com/hot-dogs/whots{{cookiecutter.current_whots_deployment_number}}-data-report",
    "repository_branch": "main",
    "path_to_docs": "docs/source/",
    "use_repository_button": true,
    "use_issues_button": true,
    "home_page_in_toc": false,
    "use_edit_page_button": true,
}

# -- Options for LaTeX output ---------------------------------------------
latex_engine = "pdflatex"

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = "_static/_images/all_whots_report.pdf"

latex_additional_files = [
    "latex_templates/maketitle.sty",
    "latex_templates/mystyle.sty",
]

latex_elements = {
    "extraclassoptions": "openany,oneside",
    "papersize": "a4paper",
    # sonny, lenny, glenn, conny, rejne, bjarne and bjornstrup # 'fncychap': '\\usepackage[lenny]{fncychap}',
    "fncychap": "\\usepackage[bjornstrup]{fncychap}",
    "fontpkg": "\\usepackage{amsmath,amsfonts,amssymb,amsthm}",
    "figure_align": "htbp",
    "pointsize": "10pt",
    # ===================== preamble ======================================
    "preamble": r"""
        \input{mystyle.sty}
        \usepackage[notocbib]{apacite}
    """,
    # ============== cover page + table of contents  ======================
    "maketitle": r""" 
        \input{maketitle.sty}
    """,
    # latex figure (float) alignment
    # 'figure_align': 'htbp',
    "sphinxsetup": "hmargin={0.7in,0.7in}, vmargin={1in,1in}, \
        verbatimwithframe=true, \
        titlecolor={rgb}{0,0,0}, \
        headerfamily=\\rmfamily\\bfseries, \
        innerlinkcolor={rgb}{0,0,1}, \
        outerlinkcolor={rgb}{0,0,1}",
    "tableofcontents": " ",
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    (
        "index",
        "whots{{cookiecutter.current_whots_deployment_number}}-data-report.tex",
        "WHOTS-{{cookiecutter.current_whots_deployment_number}}: Data Report",
        "{{cookiecutter.creator}}",
        "manual",
    ),
]
# If false, no module index is generated.
latex_domain_indices = true

# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = "whots-epub-test"
epub_author = "{{cookiecutter.creator}}"
epub_publisher = "{{cookiecutter.creator}}"
epub_copyright = (
    f"{{cookiecutter.created_on}}-{datetime.now().year}, {{cookiecutter.creator}}"
)

# A list of files that should not be packed into the epub file.
epub_exclude_files = ["search.html"]
