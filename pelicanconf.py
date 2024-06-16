#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHORS = 'Sven', 'Patrick', 'Neels'
COPYRIGHT = '2024'
SITENAME = 'sps-nerdarray'
SITEURL = '/'
SITESUBTITLE = 'Ein deutschsprachiger Podcast über sps-Programmierung'
PATH = 'content'
TIMEZONE = 'Europe/Rome'
DEFAULT_LANG = 'de'

THEME = 'themes/flat'
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['readtime', 'neighbors']
STATIC_PATHS = ['images']
EXTRA_PATH_METADATA = {
    'images/logo.ico': {'path': 'logo.ico'},
    'images/logo.png': {'path': 'logo.png'},
    'images/logo.jpeg': {'path': 'logo.jpeg'},
    'images/logoF.ico': {'path': 'logoF.ico'}
}
# Article summary length on main index page
SUMMARY_MAX_LENGTH = 100
DEFAULT_PAGINATION = 10

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
RSS_FEED_SUMMARY_ONLY = True

# Social widget
SOCIAL = (
    ('twitter', 'https://twitter.com/i/flow/login?redirect_after_login=%2Fsps_nerdarray'),
    ('linkedin', 'https://www.linkedin.com/in/sps-nerdarray-2045b72ab'),
    ('facebook', 'https://www.facebook.com/profile.php?id=100082499066145'),
    ('spotify', 'https://www.facebook.com/profile.php?id=100082499066145'),
    ('apple', 'https://podcasts.apple.com/de/podcast/sps-nerdarray/id1608239478'),
)
# DISQUS_SITENAME = ''
# GOOGLE_ANALYTICS = ''

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
