#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Gaël'
SITENAME = 'And yet it moves!'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

OUTPUT_RETENTION = [".git"]
# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)



DEFAULT_PAGINATION = 10

PLUGIN_PATHS = ["./plugins"]
PLUGINS = ['assets', 'render_math', 'pelican-cite', 'series', 'neighbors',
        'pelican-toc', 'section_number', 'share_post', 'sub_parts']

TYPOGRIPHY=True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
