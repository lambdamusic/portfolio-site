#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

# Add Items To The List Below When Adding New Pages/urls
# 2011-09-09: added these to filter out all 'bad' urls
VALID_PAGES_RESEARCH = [
    'about', 'projects', 'papers', 'code', 'hacks', 'software', 'code', 'speaking',
    'contact'
]
VALID_PAGES_STUFF = [
    'livecoding',
    'music',
    'photos',
    'videos',
    'ontologies',
]
STATIC_PAGES = ['contact', 'about']
RESEARCH_CATEGORY = {'name': "work", 'folder': 'pages'}
FREETIME_CATEGORY = {'name': "misc", 'folder': 'pages'}

# note: the twitrss feed fails on local due to an old-python version issue
# it works on live server though
RSS_FEEDS = [
    # "http://www.michelepasin.org/blog/?feed=rss2",
    "http://www.michelepasin.org/blog/feed/",
    # "https://twitrss.me/twitter_user_to_rss/?user=lambdaman",
    # "http://www.rssitfor.me/getrss?name=lambdaman",
    # "https://api.twitter.com/1/statuses/user_timeline.rss?screen_name=lambdaman",
    # "http://www.michelepasin.org/papers/feed/",
    # "http://www.michelepasin.org/videos/feed/",
    # "http://www.michelepasin.org/music/feed/",
    # "http://www.michelepasin.org/software/feed/",
    # "http://www.michelepasin.org/projects/feed/",
]

RSS_MY_BLOG = ["http://www.michelepasin.org/blog/feed/"]

FEEDSREADER_MAX_AGE = timedelta(hours=24, minutes=0)
FEED_DISPLAY_MAX_AGE = timedelta(12 * 60)
