#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

# Load extensions / plugins
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.do']}
PLUGINS = [
    'pelican_bibtex',  # https://github.com/scmmmh/pelican-bibtex
    'pelican_page_hierarchy',  # https://github.com/scmmmh/pelican-page-hierarchy.git
    'pelican_page_order',  # https://github.com/scmmmh/pelican-page-order
    'pelican_cv'
    ]

# General settings
AUTHOR = 'Mark Hall'
SITENAME = 'Work @ Room3b'
SITEURL = ''

DEFAULT_LANG = 'en'
TIMEZONE = 'Europe/Berlin'

DEFAULT_PAGINATION = 10

# Where the content can be found
PATH = 'content'

# Date when the site was last generated
GENERATION_DATE = datetime.now()

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Set the links to use in the footer
LINKS = (('Institut für Informatik (Halle a/d Saale)', 'http://www.informatik.uni-halle.de/'),)
SOCIAL = (('@hallicek', 'https://twitter.com/hallicek'),)

# Set the theme to the local theme
THEME = './theme'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Settings for generating the publications page
STATIC_PATHS = ['publications']
PUBLICATIONS_SRC = 'content/publications/mhall.bib'

CVS_SRC = ['content/cv/cv.json']
