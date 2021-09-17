---
title: "DJFacet: a faceted browser for Django"
date: "2011-06-09"
categories: 
  - "informationarchitecture"
  - "techlife"
tags: 
  - "browser"
  - "django"
  - "faceted"
---

DJFacet is a pluggable module for the [Django](https://www.djangoproject.com/) web application framework that allows you to navigate the data in your webapp using an [approach based on 'facets'](http://www.michelepasin.org/blog/2009/03/05/faceted-browsing-a-conceptual-map/). DJFacet relies entirely on the django models you've already defined within your project and on a configuration file where you can create the facets and assign them behaviour. This makes it very easy to integrate within your Django application.

I've been working on DJFacet on and off for more than a year now, so I'm really happy to finally release a stable version of it. The software is still under active development, so be certain that in the coming months new features and bug fixes will be released!

  
   
[![djfacet screenshot](/media/static/blog_img/5814620822_1b32986a64_z.jpg)](http://www.flickr.com/photos/mikele/5814620822/ "djfacet screenshot by MagIcReBirth, on Flickr")  
   
In a nutshell, the main features of DJFacet are:

- Rapid installation and integration with existing Django projects
- It’s back-end agnostic (as it rests on Django’s Database API)
- Has a minimal and customisable look and feel, based on template override
- It follows a REST architecture: urls of a search are stable and bookmarkable
- It supports pivoting (the type of objects being searched for can be changed dynamically)
- It provides a dedicated caching system (useful for apps with many facets/zoom points)

Find out more about it using these links:

- Source code on Bitbucket: [bitbucket.org/magicrebirth/djfacet](https://bitbucket.org/magicrebirth/djfacet)
- Documentation: [michelepasin.org/support/djfacet/docs/](http://michelepasin.org/support/djfacet/docs/)
- Demo installation: [demos.michelepasin.org/djfacet/](http://demos.michelepasin.org/djfacet/)
- Project page: [www.michelepasin.org/artifacts/software/djfacet/](http://www.michelepasin.org/artifacts/software/djfacet/)
