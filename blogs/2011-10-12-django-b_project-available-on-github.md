---
title: "Django B_project available on gitHub"
date: "2011-10-12"
categories: 
  - "techlife"
tags: 
  - "django"
  - "git"
---

I've put together and shared on gitHub all the files needed to get started with a [Django](https://www.djangoproject.com/) project - essentially this is a clean file structure usable to get going with a Django project nice and easy. The idea is that after downloading this, you just have to change a couple of names (see the [README](https://github.com/magicrebirth/b_project/tree/master/_help) file for more details) and there you go you have a complete Django project ready to be ran and customized.

The code is here: [bitbucket.org/magicrebirth/django\_bproject](https://bitbucket.org/magicrebirth/django_bproject). Feel free to download or fork it as you like!

Currently the B\_project is set up to work with Django 1.3 and it has a few 'batteries' included (= commonly used apps):- [MPTT](https://github.com/django-mptt/django-mptt/): Utilities for implementing a modified pre-order traversal tree in django
- [REGISTRATION](https://bitbucket.org/ubernostrum/django-registration/): A user-registration application for Django.
- [DJANGO EXTENSIONS](https://github.com/django-extensions/django-extensions): global custom management extensions for the Django Framework.
- [PICKLEFIELD](http://pypi.python.org/pypi/django-picklefield): an implementation of a pickled object field.

[![Django B_project structure](/media/static/blog_img/6237287046_5774ef8ea7_z.jpg)](http://www.flickr.com/photos/mikele/6237287046/ "Django B_project structure by MagIcReBirth, on Flickr")  

The other things included in the framework are:- a _settings.py_ file that calls localized settings specifications depending on parameters (eg dev server or live one)
- a bunch of generic python utilities
- a few 'enhanced' model classes
- all that is needed for working with trees in the admin (as discussed here: [Django admin and MPTT](http://www.michelepasin.org/blog/2009/08/18/django-admin-and-mptt-2/))
- a javascript autocomplete framework, integrated in the admin (as discussed here: [Autocomplete in Django](http://www.michelepasin.org/blog/2009/10/12/autocomplete-in-django-2/))
- some basic templates and templatetags

Enjoy!
