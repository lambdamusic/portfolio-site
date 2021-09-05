---
title: "Representing hierarchical data with Django and MPTT"
date: "2009-08-06"
categories: 
  - "informationarchitecture"
  - "techlife"
tags: 
  - "django"
  - "mptt"
  - "tree"
---

[![Picture 3](/media/static/blog_img/picture-31.png "Picture 3")](http://www.qompr.com/charts/63;django-hierarchical-tree-data/)

Apparently, you've got two options for managing **hierarchical data in django** - [django-mptt](http://code.google.com/p/django-mptt/) and [django-treebeard](http://code.google.com/p/django-treebeard/). I didn't have any time to test both of them carefully, so I just played a bit with the first one (and with great results!). \[p.s. the comparison table above is not mine, but I found it quite useful. Click on the image to find out how it was created... \]

I guess that the key feature I was looking for is the **admin-integration**. Trees must be **displayed** and **edited** properly in the admin... unfortunately both projects don't provide that feature by default, but luckily for there are attempts ([#1](http://code.google.com/p/django-mptt/issues/detail?id=33) and [#2](http://code.google.com/p/django-treebeard/issues/detail?id=2&colspec=ID%20Type%20Status%20Priority%20Milestone%20Owner%20Summary%20Stars%20Opened%20Modified%20Reporter%20Component)) to fix this issue.

In order to use MPTT with your models you just have to download it, add it to your 'installed application' settings and register the models you intend to use:

\# A mimimal example usage of \`\`mptt.register\`\` is given below, where the
\#  model being set up for MPTT is suitable for use with the default
\# arguments which specify fields and the tree manager attribute::

   from django.db import models

   import mptt

   class Genre(models.Model):
       name \= models.CharField(max\_length\=50, unique\=True)
       parent \= models.ForeignKey('self', null\=True, blank\=True, related\_name\='children')

   mptt.register(Genre, order\_insertion\_by\=\['name'\])

Then, after installing the patches, create a tree-friendly admin by subclassing _MpttModelAdmin_ (check out the [docs](http://django-mptt.googlecode.com/svn/trunk/docs/models.txt) for more info).

![Picture 4](/media/static/blog_img/picture-41.png "Picture 4")

**Here's the result** - not bad at all! I just had to install **django-mptt** and the [patches](http://code.google.com/p/django-mptt/issues/detail?id=33#c1) needed for using the [jquery nested-sortable library](http://code.google.com/p/nestedsortables/) with the admin. I'll be working more on this during the next days so probably I'll be posting more stuff....
