---
title: "DJFacet 0.9.7: MPTT hierarchical facets now supported!"
date: "2012-05-16"
categories: 
  - "informationarchitecture"
tags: 
  - "faceted"
  - "mptt"
  - "search"
  - "ui"
---

[DJFacet](http://www.michelepasin.org/artifacts/software/djfacet/) is a pluggable module for the [Django](https://www.djangoproject.com/) web application framework that allows you to navigate the data in your webapp using an approach based on 'facets'. I've [already written](http://www.michelepasin.org/blog/2011/06/09/djfacet-a-django-faceted-browser/) about DJFacet in the past; now the good news is that I've released a major update to the software, as now there is complete support for hierarchical facets too.

[Wikipedia](http://en.wikipedia.org/wiki/Faceted_search) describes faceted search as

> "a technique for accessing a collection of information represented using a faceted classification, allowing users to explore by filtering available information. A faceted classification system allows the assignment of multiple classifications to an object, enabling the classifications to be ordered in multiple ways, rather than in a single, pre-determined, taxonomic order".

Although faceted search systems aim at providing search interfaces that go beyond the model of a single, rigid, top-down catalogue for an information space, **taxonomical classifications remain always one of the most useful ways to organise a dataset**, as they implicitly provide support for 'zoom in' and 'zoom out' search operations. A good compromise then is to allow the simultaneous selection of search filters coming from different taxonomical schemas - or mixing them with non-taxonomical ones.

Version 0.9.7 of Djfacet, among several other things, includes full support for displaying and navigating through hierarchical facets as long as they are expressed in the DB via [django-MPTT](http://code.google.com/p/django-mptt/). A **demo** is available [here](http://demos.michelepasin.org/djfacet/) (just browse into the 'religion' facet to see what I mean).

[![Djfacet: support for hierarchies](/media/static/blog_img/7210452232_528c1e14be.jpg)](http://www.flickr.com/photos/mikele/7210452232/ "Djfacet: support for hierarchies by MagIcReBirth, on Flickr")

There are still a few things to sort out before reaching version 1.0 (including updating the online docs), but it's getting closer - stay tuned!

### Links:

  

- Source code on Bitbucket: [bitbucket.org/magicrebirth/djfacet](https://bitbucket.org/magicrebirth/djfacet)
- Documentation: [michelepasin.org/support/djfacet/docs/](http://michelepasin.org/support/djfacet/docs/)
- Demo installation: [demos.michelepasin.org/djfacet/](http://demos.michelepasin.org/djfacet/)
- Project page: [www.michelepasin.org/artifacts/software/djfacet/](http://www.michelepasin.org/artifacts/software/djfacet/)
