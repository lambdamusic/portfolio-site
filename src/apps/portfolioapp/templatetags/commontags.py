from django import template
from django.urls import reverse

# from config.linkeddata.triplestore import *

register = template.Library()


@register.filter()
def powerup(x):
    """
    Make sizes more interesting for force directed graph 
    """
    try:
        xmax = 500
        xmin = 1
        out = (x - xmin) / (xmax - xmin) * 100
        print(x, "becomes", out)
        return out
    except:
        return s


@register.filter(name='trim_unwanted_words')
def trim_unwanted_words(s):
    """
    Remove 'abstract' keyword from text
    """
    try:
        if s.startswith("Abstract"):
            return s[8:]
    except:
        return s


@register.filter(name='tagcloud_sizing')
def tagcloud_sizing(n, base=7):
    """
    For the tag cloud on several pages
    """
    BASE = base
    MAX = 30
    try:
        if n <= BASE:
            return BASE
        else:
            t = BASE + ((BASE * (n - 1)) / 7)
            if t > MAX:
                return MAX
            else:
                return t
    except:
        return BASE


@register.filter
def url_last_bit(uri):
    """
    Gets the last path element of a url
    """
    try:
        return url.split("/")[-1]
    except:
        return ""
