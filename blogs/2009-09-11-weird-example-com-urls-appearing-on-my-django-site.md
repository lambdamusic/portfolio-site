---
title: "Weird 'example.com' urls appearing on my django site..."
date: "2009-09-11"
categories: 
  - "techlife"
  - "tips-and-tricks"
tags: 
  - "django"
---

It all started when I added the [get\_absolute\_url method](http://docs.djangoproject.com/en/dev/ref/models/instances/#get-absolute-url) on my model objects:

\# includes a mysterious example.com ?????
@models.permalink
def get\_absolute\_url(self):
    return ('person\_detail', \[str(self.id)\])

When you do that, the admin site automatically picks it up and adds some nice **'view on site' buttons** on all of your individual object pages...:

![Picture 3](/media/static/blog_img/picture-3.png "Picture 3")

The problem is, the links are being attached to a mysterious _'example.com'_ domain. I left it aside the other day, cause of it was the last of a long series of weird bugs, but today the solution appeared to be quite simple ([found it on stackoverflow](http://stackoverflow.com/questions/344851/django-admins-view-on-site-points-to-example-com-instead-of-my-domain) too).

### The solution:

[Django has a nice **'sites' framework**](http://docs.djangoproject.com/en/dev/ref/contrib/sites/#ref-contrib-sites) which comes by default with the contrib application. If you are like me, you probably have wondered at the beginning of your django-adventure what that was for, and then just forgot about it. Well, I realized today that **actually the sites framework is really useful** when you are running multiple sites and want, for example, to share stuff between them:

> The Django-powered sites LJWorld.com and Lawrence.com are operated by the same news organization – the Lawrence Journal-World newspaper in Lawrence, Kansas. LJWorld.com focuses on news, while Lawrence.com focuses on local entertainment. But sometimes editors want to publish an article on both sites.
> 
> The **brain-dead way of solving the problem** would be to require site producers to publish the same story twice: once for LJWorld.com and again for Lawrence.com. But that’s inefficient for site producers, and it’s redundant to store multiple copies of the same story in the database.
> 
> The **better solution is** simple: Both sites use the same article database, and an article is associated with one or more sites.

Another thing the sites-framework does - and **this is what solves the _example.com_ problem** - is setting the 'default site' for the django-admin button behaviour. And there you go, that's where that unexpected domain name was originating from....

This value (= 'example.com') is stored in the database, so it's enough to change it through the admin interface, and everything should go into its own place :-) For example, below I changed it into the localhost value/port I'm running django on...

![Picture 2](/media/static/blog_img/picture-2.png "Picture 2")
