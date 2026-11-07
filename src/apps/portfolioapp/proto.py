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
