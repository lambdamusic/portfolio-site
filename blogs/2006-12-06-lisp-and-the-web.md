---
title: "Lisp and the Web"
date: "2006-12-06"
categories: 
  - "techlife"
---

I'll be posting more about this - it's a very _lisp-ed_ period of life. Who said you cannot develop webapps using the old-fashioned lisp? The more i look for this sort of stuff, the more I find resources. After the usual 'parenthesis fright', and installation angers you can get it going: [Hunchentoot](http://weitz.de/hunchentoot/).

> Hunchentoot is a web server written in Common Lisp and at the same time a toolkit for building dynamic websites. As a stand-alone web server, Hunchentoot is capable of HTTP/1.1 chunking (both directions), persistent connections (keep-alive), and SSL, but it can also sit behind the popular [Apache](http://httpd.apache.org/) using Marc Battyani's [mod\_lisp](http://www.fractalconcept.com/asp/html/mod_lisp.html).
> 
> Hunchentoot provides facilities like automatic session handling (with and without cookies), logging (to Apache's log files or to a file in the file system), customizable error handling, and easy access to GET and POST parameters sent by the client.
> 
> Hunchentoot talks with its front-end or with the client over TCP/IP sockets and uses multiprocessing to handle several requests at the same time. Therefore, it cannot be implemented completely in [portable Common Lisp](http://www.lispworks.com/documentation/HyperSpec/Front/index.htm). It currently works with [LispWorks](http://www.lispworks.com/) (which is the main development and testing platform), [CMUCL](http://www.cons.org/cmucl/) (with MP support), [SBCL](http://sbcl.sourceforge.net/) (with Unicode and [thread](http://abstractstuff.livejournal.com/26811.html) [support](http://common-lisp.net/pipermail/tbnl-devel/2006-November/000780.html)), [OpenMCL](http://openmcl.clozure.com/), and [Allegro Common Lisp](http://www.franz.com/products/allegrocl/).

I'm struggling with the installation of the dozens other libraries needed... but it looks worth it. The screenshot below is from an art website that uses it: [Heike Stephan](http://heikestephan.de/)

[![Picture 12.png](/media/static/blog_img/Picture%2012.png)](http://people.kmi.open.ac.uk/mikele/blog/wp-content/uploads/2006/12/Picture%2012.png "Picture 12.png")
