---
title: "HunchenToot day"
date: "2006-12-11"
categories: 
  - "techlife"
tags: 
  - "lisp"
---

Quite an intense experience getting everything to work properly with lisp and [Hunchentoot](file:///Users/michelepasin/Documents/Lisp/hunchentoot-0.4.11/doc/index.html) (a CM web-server), but I succeeded eventually yahoooo .... I am just giving a brief overview here, and some pointers. Among them, a [blog entry by Bill Clementson](http://bc.tech.coop/blog/061013.html) was pretty useful in keeping me in a good mood :-)

First of all, it's a good idea to install [ASDF](http://www.cliki.net/asdf) and [ASDF-install](http://www.cliki.net/ASDF-Install), two lisp libraries that automatically manages packages and installations. There is a [detailed tutorial originally done by Edi Weitz](http://common-lisp.net/project/asdf-install/tutorial/index.html), which can guide you through that. I had some troubles at first, and had to create two hidden files to configure LispWorks properly (shouldn't the first one be there already?):

> \----> **~/.lispworks** ;; lispworks load set up #-:asdf (load "/Users/michelepasin/Documents/Lisp/asdf/asdf") (pushnew "/Users/michelepasin/Documents/Lisp/asdf/registry/" asdf:\*central-registry\* :test #'equal) #-:asdf-install (asdf:operate 'asdf:load-op :asdf-install)
> 
> \----> **~/.asdf-install** ;; set up for the asdf library (setq asdf-install: \*proxy\* "http://openuniversityunbreakableproxy:portNumber")

Basically ASDF-install lets you retrieve properly packaged libraries very easily from the [CLiki repository](http://www.cliki.net/ASDF-Install); so for example:

> CL-USER 6 : 3 > **(asdf-install:install :cl-who)** Install where? 1) System-wide install: System in /usr/local/asdf-install/site-systems/ Files in /usr/local/asdf-install/site/ 2) Personal installation: System in /Users/michelepasin/.asdf-install-dir/systems/ Files in /Users/michelepasin/.asdf-install-dir/site/ 0) Abort installation. --> 2 ;;; ASDF-INSTALL: Downloading 19057 bytes from http://weitz.de/files/cl-who.tar.gz to asdf-install-0.asdf-install-tmp ... ;;; ASDF-INSTALL: Downloading 188 bytes from http://weitz.de/files/cl-who.tar.gz.asc to asdf-install-1.asdf-install-tmp ...

Quite easy now uh? So I installed all the libraries needed by Hunchentoot just by typing the names they are listed as - unfortunately not all of them worked fine with asdf (MD5 for example) - but you can find them easily on the web and install from your local machine:

> CL-USER 30 : 2 > (asdf-install:install "/Users/michelepasin/Documents/Lisp/ Hunchentoot-libraries/md5-1.8.5.tar.gz")

With a terminal command you can see exactly what's been stored:

> michelepasin:~ michelepasin$ **ls ~/.asdf-install-dir/systems** cffi-examples.asd cl-base64.asd cl-who.asd md5.asd cffi-tests.asd cl-ppcre-test.asd cl-who.system rfc2388.asd cffi-uffi-compat.asd cl-ppcre-test.system flexi-streams.asd trivial-gray-streams.asd cffi.asd cl-ppcre.asd hunchentoot-test.asd url-rewrite.asd chunga.asd cl-ppcre.system hunchentoot.asd url-rewrite.system

That's pretty much it - I just had to set up properly the apache httpd.conf file for letting it forward calls to a specific port to hunchentoot, and check out the hello-world example provided (the CL-WHO library is needed for this example). Thanks to [Edi Weitz](http://weitz.de/) for this handy tool!
