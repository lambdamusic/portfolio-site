---
title: "Django admin and MPTT #2"
date: "2009-08-18"
categories: 
  - "techlife"
tags: 
  - "admin"
  - "django"
  - "mptt"
  - "tree"
  - "visualization"
---

This is a follow up to the [previous post on managing and visualizing trees using django](http://www.michelepasin.org/blog/?p=255). I've been using MPTT quite a bit now and it's great - also, I looked deeper into the admin integration (basically, the issue of being able of manage trees from within the admin).

The major issue I had with the patch discussed in my previous post was the fact that it is mainly a javascript hack - everything is done in the browser - i.e. it looked wonderful but it didn't really scale up. So if you had a lot of items in your tree (say thousands) the **js-driven pagination (basically, hiding and showing things on demand) would crash** - at least, it did that to me all the time!

The solution has been to reuse the admin management section from the [FeinCMS project](http://spinlock.ch/pub/feincms/html/) - this is a great CMS created by a bunch of django-ers in Switzerland - it relies heavvily on django's admin so they had the same problem when having to provide a way for users to add structure to the pages in a website. With some [help from google and **Matthias**](http://groups.google.com/group/django-feincms/topics?start=) **(tx! he's one of the guys behind FeinCMS**) I got it all working.. here's the main steps:

**1\. upgrade to django 1.1** This might not be necessary, cause everything is supposed to work also with the previous release - I tried it with django 1.0 too but I had to fix a couple of urls to make it work (Basically media files which were not loaded properly). So, if you want a hassle-free installation just upgrade to django 1.1 ! (which is great btw)

**2\. download and add [feincms](http://github.com/matthiask/feincms/tree/master), [mptt](http://code.google.com/p/django-mptt/) to you installed apps in settings.py** As simple as that.

INSTALLED\_APPS = (
    ....
    'mptt',
    'feincms',
)

**3\. specify a url-path for feincms media in settings.py, and also a location** (this may vary in your live server, if you want apache to serve these files directly).

FEINCMS\_ADMIN\_MEDIA = '/feincms\_media/'
FEINCMS\_ADMIN\_MEDIA\_LOCATION = '/My/local/path/to/feincms/media/'

**4\. add a url handler for feincms media files in urls.py. Again, these settings are ok on a development server, on production phase [you might wanna do things differently :-)](http://docs.djangoproject.com/en/dev/howto/static-files/#the-big-fat-disclaimer)**

from django.conf import settings
    urlpatterns = patterns('',
    .....
    (r'^feincms\_media/(?P<path>.\*)$', 'django.views.static.serve',
         {'document\_root': settings.FEINCMS\_ADMIN\_MEDIA\_LOCATION, 'show\_indexes': True}),
)

**5\. register your hierarchical model with mptt, then remember to set the Meta option correctly**.. this is needed for a correct display of the tree in the admin (obviously you need to run syncdb to create the table in the db!):

from django.db import models
import mptt

**class** TreeNode(models.Model):
   name = models.CharField(max\_length=50, unique=True)
   parent = models.ForeignKey('self', null=True, blank=True, related\_name='children')

   **def** \_\_unicode\_\_(self):
                **return** self.name

   **class** Meta:
          ordering = \['tree\_id', 'lft'\]

mptt.register(TreeNode,)

**6\. create a model admin that inherits from feincms TreeEditor class**:

from django.contrib import admin
from django.utils.translation import ugettext\_lazy as \_
from django.conf import settings as django\_settings
from feincms.admin import editor
from myproject.myapp.models import \*

**class** TreeNodeAdmin(editor.TreeEditor):
    **pass**

admin.site.register(TreeNode, TreeNodeAdmin)

**End**! That should be it! Let me know if I forgot something.. Here's a screenshot of the new tree-management admin page we created:

![Picture 1](/media/static/blog_img/picture-1.png "Picture 1")

**UPDATE 09/2009: how to add more actions to the tree bar.** Just override the _\_actions\_column_ method on the TreeNodeAdmin class, as follows::

class TreeNodeAdmin(editor.TreeEditor):
        def \_actions\_column(self, page):
                actions \= super(TreeNodeAdmin, self).\_actions\_column(page)
                actions.insert(0, u'<a href\="add/?parent=%s" title\="%s"\><img
                       src\="%simg/admin/icon\_addlink.gif" alt\="%s"\></a\>' %
                       (page.pk, \_('Add child page'),
                       settings.ADMIN\_MEDIA\_PREFIX , \_('Add child page')))
               actions.insert(0, u'<a href\="%s" title\="%s"\><img
                       src\="%simg/admin/selector-search.gif" alt\="%s" /\></a\>' %
                       (page.get\_absolute\_url(), \_('View on site'),
                       django\_settings.ADMIN\_MEDIA\_PREFIX, \_('View on site')))
                return actions

admin.site.register(TreeNode, TreeNodeAdmin
