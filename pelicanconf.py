#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Humphrey Butau'
SITENAME = 'pyzim'
SITEURL = ''
THEME = 'html5-dopetrope'
THEME_STATIC_DIR = 'theme'

PATH = 'content'

TIMEZONE = 'Africa/Harare'

DEFAULT_LANG = 'en'

MENUITEMS = (
    ('Django Indaba', '/'),
#    ('Schedule', '/schedule'),
    ('Donate', '/sponsorship'),
#    ('Call for Proposals', '/call_for_proposals'),
    ('Volunteering', '/call_for_volunteers'),
    ('CoC', '/coc'),
    ('Recent Developments', '/#developments'),
#    ('About', '/about'),
)
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ABOUT_TEXT = 'Whats this aldjkdfksjkasjfkjasdkasl about?'
ABOUT_IMAGE = 'theme/images/pic10.jpg'
MAIL = 'pyzim@gmail.com'
PHONE = 'Your phone number.'
TWITTER_USER  = 'pycon_zim'
GOOGLEPLUS_USER = '110831175850960549188'
ABOUT_LINK = 'about'
FACEBOOK_USER = 'pyzim'
GITHUB_USER = 'pyzim'
LINKEDIN_USER = 'pyzim'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

STATIC_PATHS = [
    'theme/images',
    'theme/js',
    'theme/css',
    'extra/robots.txt',
    'README.md',
]
DISQUS_SITENAME = "https-pyzim-github-io"
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
