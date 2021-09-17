---
title: "Subversion on OSX"
date: "2007-10-01"
categories: 
  - "techlife"
  - "tips-and-tricks"
tags: 
  - "mac"
  - "osx"
  - "subversion"
  - "svn"
---

Day one - part time job - semantic web services. Need to install SVN on me mac… I've bothered at least two people in kmi till i found this really useful [tutorial here.....](http://www.wikihow.com/Install-Subversion-on-Mac-OS-X)

I've firstly tried to install it using DarwinPorts, but I was always getting theÂ  same error: `michelepasin:~ michelepasin$ sudo port install subversion Password: --->Â  Fetching db44 --->Â  Attempting to fetch patch.4.4.20.1 from http://www.oracle.com/technology/products/berkeley-db/db/update/4.4.20/ --->Â  Attempting to fetch patch.4.4.20.1 from http://svn.macports.org/repository/macports/distfiles/db44 --->Â  Attempting to fetch patch.4.4.20.1 from http://svn.macports.org/repository/macports/distfiles/general/ --->Â  Attempting to fetch patch.4.4.20.1 from http://svn.macports.org/repository/macports/downloads/db44 Error: Target org.macports.fetch returned: fetch failed Error: The following dependencies failed to build: apr-util db44 expat libiconv sqlite3 readline ncurses ncursesw gettext neon openssl zlib Error: Status 1 encountered during processing.`

basically all you gotta do is get a pre-packaged [easy-to-install version of subversion here](http://homepage.mac.com/martinott/) (we love the terminal, but the lessÂ  i have to deal with it the simpler my life is, apparently), and thenÂ  you may also install a subversion environment manager, such as [SVNX](http://www.apple.com/downloads/macosx/development_tools/svnx.html)... et voila subversion's running!
