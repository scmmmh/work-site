#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

THEME = './theme'
DELETE_OUTPUT_DIRECTORY = True

AUTHOR = 'Mark Hall'
SITENAME = 'Work @ Room3b'
SITEURL = 'https://work.room3b.eu'
TIMEZONE = 'Europe/Berlin'
DEFAULT_LANG = 'en'

RELATIVE_URLS = False
PATH = 'content'

LINKS = (('Institut für Informatik (Halle a/d Saale)', 'http://www.informatik.uni-halle.de/'),)
SOCIAL = (('@hallicek', 'https://twitter.com/hallicek'),)
