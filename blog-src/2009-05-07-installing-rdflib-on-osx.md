---
title: "Installing RDFlib on osX"
date: "2009-05-07"
categories: 
  - "techlife"
  - "tips-and-tricks"
tags: 
  - "python"
  - "rdf"
---

[RDFlib](https://code.google.com/p/rdflib/) is a Python library for working with RDF, a simple yet powerful language for representing information.

[![picture-12](/media/static/blog_img/picture-12.png "picture-12")](http://www.rdflib.net/)

Installing it is easier than what you might think. I googled it and it seems that several people had problems ([missing components mainly](http://xplus3.net/2009/03/09/how-to-install-rdflib/)) with  this.. but in my case it was easy-beasy (well you need to have [easy-install](http://www.michelepasin.org/blog/2009/01/27/python-easyinstall-the-peak-developers-center/)):

```

[mac]@ganimede:~/Code/python/_libs/rdflib-2.4.0>sudo easy_install -U "rdflib>=2.4"
Password:
Searching for rdflib>=2.4
Reading http://pypi.python.org/simple/rdflib/
Reading http://rdflib.net/
Best match: rdflib 2.4.1
Processing rdflib-2.4.1-py2.5-macosx-10.5-i386.egg
Adding rdflib 2.4.1 to easy-install.pth file
Installing rdfpipe script to /usr/local/bin

Using /Library/Python/2.5/site-packages/rdflib-2.4.1-py2.5-macosx-10.5-i386.egg
Processing dependencies for rdflib>=2.4
Finished processing dependencies for rdflib>=2.4
[mac]@ganimede:~/Code/python/_libs/rdflib-2.4.0>python
Python 2.5.1 (r251:54863, Jan 13 2009, 10:26:13)
[GCC 4.0.1 (Apple Inc. build 5465)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import rdflib
>>> from rdflib.Graph import Graph
>>> g.parse("http://bigasterisk.com/foaf.rdf")
<Graph identifier=ooYPCFuN0 ()>
>>> len(g)
62

```

Done!
