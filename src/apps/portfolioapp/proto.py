#!/usr/bin/env python
# encoding: utf-8

"""
Layout prototypes (branch `layout-prototypes`, not for the live site).

`?layout=a|b|c` picks a prototype and keeps it in the session, so it sticks
while clicking around; `?layout=off` goes back to the current design.

    a   top bar: the drawer becomes a visible nav strip, homepage unchanged
    b   sidebar: the drawer stays open as a permanent left column
    c   front page: top bar, and the homepage becomes a hub of recent
        writing, talks and sounds above a short selection of projects

All three share the unified Words list (pages/words-proto.html).

`?post=rail|quiet|margin` does the same for the blog post page, independently
of the layout (pages/detail-blogs-proto.html); `?post=off` restores it.

    rail     the article plus a right-hand column: date, reading time,
             topic, tags, contents and related posts
    quiet    one column; a single date line under the title, tags and
             related posts moved to the end of the article
    margin   the title runs wide; date and tags sit in a left margin
"""

LAYOUTS = {
    'a': 'Top bar',
    'b': 'Sidebar',
    'c': 'Front page',
}


def current_layout(request):
    """the active prototype key, or '' for the current design"""
    choice = request.GET.get('layout')
    if choice is not None:
        request.session['layout'] = choice if choice in LAYOUTS else ''
    return request.session.get('layout', '')


POST_LAYOUTS = {
    'rail': 'Right rail',
    'quiet': 'Quiet header',
    'margin': 'Left margin',
}


def current_post_layout(request):
    """the active blog-post prototype key, or ''"""
    choice = request.GET.get('post')
    if choice is not None:
        request.session['post_layout'] = choice if choice in POST_LAYOUTS else ''
    return request.session.get('post_layout', '')
