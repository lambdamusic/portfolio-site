---
title: "Fink fhink think"
date: "2006-12-12"
categories: 
  - "justblogging"
tags: 
  - "mac"
  - "osx"
---

There a class of applications that conquered a big slice of new mac users, after the appearance of OSX: the applications coming from [UNIX](http://www.unix.org/). I'm not one of them unfortunately (or maybe luckily), but with the time I'm more and more appreciating all that free stuff, apparently difficult to understand. Cause it makes you feel you're getting the best out the wonderful machine you're spending most of the time on....

[![Picture 13.png](/media/static/blog_img/Picture%2013.png)](http://people.kmi.open.ac.uk/mikele/blog/wp-content/uploads/2006/12/Picture%2013.png "Picture 13.png")

So today I finally spent some time installing [FINK](http://fink.sourceforge.net/download/), cause I required it in order to then download [DARCS](http://darcs.net/DarcsWiki/FrontPage) (a source code management system.).

> **What is Fink?**
> 
> Fink is a project that wants to bring the full world of Unix [Open Source](http://www.opensource.org/) software to [Darwin](http://www.opensource.apple.com/) and [Mac OS X](http://www.apple.com/macosx/). As a result, we have two main goals. First, to modify existing Open Source software so that it will compile and run on Mac OS X. (This process is called porting.) Second, to make the results available to casual users as a coherent, comfortable distribution that matches what Linux users are used to. (This process is called packaging.) The project offers precompiled binary packages as well as a fully automated build-from-source system.

You don't need anything special, just [download an image disk](http://fink.sourceforge.net/download/index.php?phpLang=en) and follow the instructions. Then you can use [Fink Commander](http://finkcommander.sourceforge.net/), a graphical front end, to start using Fink and download all the pre-packaged stuff you like! Installing a package is also possible from the terminal window, with the command "apt-get install". A quite good tutorial from o'Reilly can be found [here](http://www.onlamp.com/pub/a/mac/2005/09/30/fink.html?page=1).. [![Picture 22.png](/media/static/blog_img/Picture%2022.png)](http://people.kmi.open.ac.uk/mikele/blog/wp-content/uploads/2006/12/Picture%2022.png "Picture 22.png")

However, my initial goal of installing DARCS is not reached yet, cause among the many apps available through fink, I can't really see it...... too bad. So I set out to install [DARWINPORTS](http://darwinports.com/), which is another download manager along the lines of fink.

[![Picture 3.png](/media/static/blog_img/Picture%203.png)](http://people.kmi.open.ac.uk/mikele/blog/wp-content/uploads/2006/12/Picture%203.png "Picture 3.png")

Unfortunately, also here some troubles: the installer doesnt create the directory "opt/local/bin/portslocation/dports" as it should, according to [this website......](http://darwinports.com/) but after some trials I got it working. The main tweak was to add a "./" after the sudo command.. (I guess it has to do with the shell syntax).

> michelepasin:/opt/local/bin michelepasin$ sudo ./port install darcs ---> Fetching zlib ---> Attempting to fetch zlib-1.2.3.tar.bz2 from http://www.zlib.net/ ---> Verifying checksum(s) for zlib ---> Extracting zlib........

It started running for more than half an hour...downloading and unpacking lots of things... so i guess we'll have to get back to this later (i dont want to stay up all night just to install this d\*\*n darcs.....)

[![Picture 4.png](/media/static/blog_img/Picture%204.png)](http://people.kmi.open.ac.uk/mikele/blog/wp-content/uploads/2006/12/Picture%204.png "Picture 4.png")
