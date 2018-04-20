#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kevin Michael'
SITENAME = 'xDjSkaly'
SITESUBTITLE = 'Sound and Music Production'
SITEURL = ''

CACHE_CONTENT = False
LOAD_CONTENT_CACHE = False

PATH = 'content'
PAGE_PATHS = ['pages']
THEME = 'theme/simplex'
OUTPUT_PATH = 'output/'
THEME_STATIC_DIR = 'theme/simplex'
STATIC_EXCLUDES = ['pages']
THEME_STATIC_PATHS = ['static']
DIRECT_TEMPLATES = []
STATIC_PATHS = ['extra']
EXTRA_PATH_METADATA = {
    'extra/.htaccess': {'path': '.htaccess'},
    'extra/browserconfig.xml': {'path': 'browserconfig.xml'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/humans.txt': {'path': 'humans.txt'},
    'extra/icon.png': {'path': 'icon.png'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/site.webmanifest': {'path': 'site.webmanifest'},
    'extra/tile-wide.png': {'path': 'tile-wide.png'},
    'extra/tile.png': {'path': 'tile.png'}
}

TIMEZONE = 'Africa/Harare'
LOCALE = ('en_ZA', 'C')

DEFAULT_LANG = 'en-ZA'

DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (
    ('Home', '#home'),
    ('About Me', '#about'),
    ('Tracklist', '#music'),
    ('Contact Me', '#contact')
)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOUNDCLOUD_URL = 'https://soundcloud.com/xdjskaly'
FACEBOOK_URL = 'https://www.facebook.com/xdjskaly'
TWITTER_URL = 'https://twitter.com/xdjskaly'
INSTAGRAM_URL = 'https://www.instagram.com/xdjskaly'
YOUTUBE_URL = 'https://www.youtube.com/channel/UCG6XQCZc45R7yVyXdwFA7rQ'
EMAIL = 'mailto:xdjskaly@gmail.com'
SOCIAL_WIDGET_NAME = 'Social'
SOCIAL = (
    ('Soundcloud', SOUNDCLOUD_URL),
    ('Facebook', FACEBOOK_URL),
    ('Twitter', TWITTER_URL),
    ('Instagram', INSTAGRAM_URL),
    ('YouTube', YOUTUBE_URL),
    ('Email', EMAIL)
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

INDEX_SAVE_AS = 'index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
