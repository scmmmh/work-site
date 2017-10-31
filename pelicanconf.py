#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

JINJA_EXTENSIONS = ['jinja2.ext.do']
PLUGINS = ['pelican_bibtex']  # https://github.com/vene/pelican-bibtex

AUTHOR = 'Mark Hall'
SITENAME = 'Work @ Room3b'
SITEURL = 'https://work.room3b.eu'

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS = (('Institut für Informatik (Halle a/d Saale)', 'http://www.informatik.uni-halle.de/'),)
SOCIAL = (('@hallicek', 'https://twitter.com/hallicek'),)

DEFAULT_PAGINATION = 10

DISPLAY_CATEGORIES_ON_MENU = True

THEME = './theme'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['publications']
PUBLICATIONS_SRC = 'content/publications/mhall.bib'
