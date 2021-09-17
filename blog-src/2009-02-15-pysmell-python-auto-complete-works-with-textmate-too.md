---
title: "pysmell - Python auto-complete - works with TextMate too!"
date: "2009-02-15"
categories: 
  - "techlife"
  - "tips-and-tricks"
tags: 
  - "autocompletion"
  - "ide"
  - "pysmell"
  - "python"
  - "textmate"
---

One of the reasons that kept me away (sigh) from TextMate is the lack of autocompletion support.. especially in Python. Seems like those days have ended - I just downloaded and installed [Pysmell](http://code.google.com/p/pysmell/), and it works great!!!

The [instructions](http://code.google.com/p/pysmell/) are very clear, you install it, dbl click the TextMate bundle file and you're already half way through. Just remember that you always need to generate a a PYSMELLTAGS file from your project, and put it at the root level so that TextMate finds it:

`cd /root/of/project pysmell .`

For example, I wanted to add the django package to my 'tags' library:

`[mac]@ego:/Library/Python/2.5/site-packages/django>pysmell . -o ~/PYSMELLTAGS.djangolib`

And generate tags for the standard Python lib:

`[mac]@ego:/System/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5>pysmell *.py -o ~/PYSMELLTAGS.stndlib`

Then I just moved these files to the root of my python project.. and it magically works!

![picture-22](/media/static/blog_img/picture-22.png "picture-22")

\>>>

At first sight, the main drawbacks seem to be:

1) the 'tags' file you generate needs to be put into the project directory, not really handy if you have multiple projects.. (or if you say - update a library)

2) it may be slow (of course, depending on the size of the TAGS file you generate)

However - it's great stuff, can't wait to test it further!!!!
