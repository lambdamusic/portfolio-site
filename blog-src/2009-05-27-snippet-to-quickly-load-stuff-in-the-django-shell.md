---
title: "Snippet to load stuff quickly in the Django shell"
date: "2009-05-27"
categories: 
  - "techlife"
tags: 
  - "django"
  - "python"
  - "shell"
---

Sometimes you end up testing out things a lot using the handy **[django shell](http://docs.djangoproject.com/en/dev/ref/django-admin/#ref-django-admin)**, but every time you've got to **repeat** the same commands to load all the necessary models, utils etc. etc.

[![Picture 1](/media/static/blog_img/picture-16.png "Picture 1")](http://www.djangosnippets.org/)

In order to do this automatically, I thought you had to modify the django-admin.py file or something like that. Nope! Here's a [useful django snippet that shows how to do the job.](http://www.djangosnippets.org/snippets/375/) Basically - it's very simple (I actually don't understand how I got stuck on something so obvious!), just put evetyhing you want to load  in a separate file in your project, and then load that file from the shell ;-)

E.g..

'''
Allows for a quick startup loading commonly used classes, installed apps, and console utils.
To use: After manage.py shell, enter from project.package.modulename import \*
'''

from django.conf import settings
from django.db import connection, models

\# Load each installed app and put models into the global namespace.
for app in models.get\_apps():
    exec("from %s import \*" % app.\_\_name\_\_)

def last\_query():
    "Show the last query performed."
    return connection.queries\[\-1\]

#===================================================
\# Add commonly used modules, classes, functions here
#===================================================
from django import forms
import os
from datetime import datetime

\# etc. etc.

p.s. also snippets [540](http://www.djangosnippets.org/snippets/540/) and [549](http://www.djangosnippets.org/snippets/549/) provide **alternative solutions** to the problem!
