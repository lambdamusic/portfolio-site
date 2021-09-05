---
title: "Trying out Django-cms"
date: "2010-08-03"
categories: 
  - "techlife"
tags: 
  - "cms"
  - "django"
---

I tried installing [django-cms](http://www.django-cms.org/en/), an open-source project from Switzerland's company [Divio](http://www.divio.ch/). It is a content management system based on the web framework [Django](http://www.djangoproject.com/) and is written in Python.

Among the interesting [features](http://www.django-cms.org/en/tour/) of DjangoCms (besides the fact that it is based on django, which I happen to have fun with in most of my programming work):

> - Flexible Plugin Architecture. Build flexible pages with a wide range of plugins.
> - SEO Optimization. The structure of the pages is optimized for SEO.
> 
> - Editorial workflow. Workflows for publishing and approval.
> - Permission Management. Set specific rights to different users.
> - Versioning. Each modification of the page will be saved. You can restore any state you wish.
> - Multisites. Administrate multiple websites over the same admin interface.
> - Multilanguage. Support for different languages (i.e. arabic, chinese or russian)
> - Applications (Apps). Add apps to different pages of the CMS.
> - Media Asset Manager (MAM). MAM allows you to manage all kind of assets (pictures, PDFs, videos and other documents).

It's quite interesting to check out the other alternatives too, if you want a django-based CMS. [This comparison webpage](http://code.djangoproject.com/wiki/CMSAppsComparison) has all the info you need.

\-----------------------------------------

Getting to the meaty part: here are the steps I followed during **installation**:

1\. went to [gitHub](http://github.com/divio/django-cms/downloads) and tried to install the latest version available (2.1.0.beta2). Tried to run the example app within that package, but it was throwing too many errors so I decided to go for the 2.0 stable release ([django-cms-2.0.0.final.tar.gz](http://github.com/divio/django-cms/tarball/2.0.0)).

2\. This version worked fine, I just had to **set the MEDIA directory** giving using the full path on my machine, and **remove** all references to '**South**' and '**Reversion**' django apps (in 'installed apps') cause I don't use them.

3\. fill out the **DB specs** as needed (_'DATABASE\_ENGINE = 'sqlite3'_), update the DB using '_python manage.py syncdb_', and then start the server using '_python manage.py runserver_'

4\. That's it. Go to /admin, **set up some pages**, add content and see the result.

[![Screen shot 2010-08-03 at 14.19.23.png](/media/static/blog_img/Screen-shot-2010-08-03-at-14.19.23.png)](http://www.michelepasin.org/blog/wp-content/uploads/2010/08/Screen-shot-2010-08-03-at-14.19.23.png)

The templates that come by default are good at giving you an idea of how the information is structured and retrieve, but they are a bit messy in my opinion. So I **created my own template** and added it to the default ones (all the info on how to do this on the [official docs](http://www.django-cms.org/en/documentation/2.0/configuration/))

[![Screen shot 2010-08-03 at 14.22.04.png](/media/static/blog_img/Screen-shot-2010-08-03-at-14.22.04.png)](http://www.michelepasin.org/blog/wp-content/uploads/2010/08/Screen-shot-2010-08-03-at-14.22.04.png)

The end result: not a masterwork, but a decent starting point for certain!

[![Screen shot 2010-08-03 at 14.26.29.png](/media/static/blog_img/Screen-shot-2010-08-03-at-14.26.29.png)](http://www.michelepasin.org/blog/wp-content/uploads/2010/08/Screen-shot-2010-08-03-at-14.26.29.png)

\---------------------------------

Other places online where you might find useful django-cms tips:

\- django-cms [mailing list](http://groups.google.ch/group/django-cms) on google groups - another mailing list on [gmame.org](http://blog.gmane.org/gmane.comp.python.django.django-cms)

That's it for now. I like very much the plugin architecture (plugins or extensions can be [downloaded here](http://www.django-cms.org/en/extensions/)), maybe I'll be posting some more about that in the future...

...
