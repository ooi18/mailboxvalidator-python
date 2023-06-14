# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'MailboxValidator'
copyright = '2023, MailboxValidator'
author = 'MailboxValidator'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    # 'myst_parser',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

autosummary_generate = True  # Turn on sphinx.ext.autosummary

templates_path = ['_templates']

# -- Options for HTML output

# html_theme = 'sphinx_rtd_theme'
# html_theme = 'press'
html_theme = 'sphinx_material'
# html_theme = 'furo'
# html_theme = 'renku'

''''''
# Material theme options (see theme.conf for more information)
html_theme_options = {

    # Set the name of the project to appear in the navigation.
    'nav_title': 'MailboxValidator',

    # Set you GA account ID to enable tracking
    # 'google_analytics_account': 'UA-XXXXX',

    # Specify a base_url used to generate sitemap.xml. If not
    # specified, then no sitemap will be built.
    'base_url': 'https://github.com/ooi18/mailboxvalidator-python',

    # Set the color and the accent color
    'color_primary': 'blue',
    'color_accent': 'light-blue',

    # Set the repo location to get a badge with stats
    # 'repo_url': 'https://github.com/ooi18/mailboxvalidator-python',
    'repo_url': 'https://github.com/mailboxvalidator/mailboxvalidator-python',
    'repo_name': 'Project',

    # Visible levels of the global TOC; -1 means unlimited
    'globaltoc_depth': 3,
    # If False, expand all TOC entries
    'globaltoc_collapse': False,
    # If True, show hidden TOC entries
    'globaltoc_includehidden': False,
}

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = 'images/mbv-logo-square-256.png'

html_title = "MailboxValidator Email Validation"

# -- Options for EPUB output
epub_show_urls = 'footnote'
