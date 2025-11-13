import os

project = 'Manifesto Documentation'
author = 'a.h.s. boy'
copyright = '2025, a.h.s. boy'
release = '4.0b'

# Sphinx ≥5 prefers root_doc; master_doc still works on older versions.
root_doc = 'index'  # was: master_doc = 'index'

extensions = []
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# On Read the Docs, you can omit this and RTD will use its theme automatically.
# If you want to pin it explicitly, ensure the package is available on RTD:
html_theme = 'sphinx_rtd_theme'
# Otherwise, remove the next line:
#html_theme = 'default'

html_static_path = ['_static']

# Optional; mainly useful with extensions like sphinx-sitemap
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "")

# Make sure html_context exists before assigning to it
html_context = {}
if os.environ.get("READTHEDOCS", "") == "True":
    html_context["READTHEDOCS"] = True
