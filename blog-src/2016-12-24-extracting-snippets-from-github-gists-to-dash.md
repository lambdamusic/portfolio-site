---
title: "How to copy snippets from Github Gists to Dash"
date: "2016-12-24"
categories: 
  - "techlife"
tags: 
  - "dash"
  - "gist"
  - "github"
  - "snippets"
---

If you’re a **Dash for MacOS** user, here’s a [little script](https://gist.github.com/lambdamusic/706698eb4cd17ee1bb97e0524cdc1c62) to copy existing code snippets saved as Github Gists into the Dash snippets database.

[Dash for MacOS](https://kapeli.com/dash) is an application that allows to keep a local library of a multitude of programming frameworks and libraries, so that you can search this library quickly using an offline intuitive interface.

[![Dash](/media/static/blog_img/dash.png)](http://www.michelepasin.org/blog/wp-content/uploads/2016/12/dash.png)

Dash has a feature for creating and [managing code snippets](https://kapeli.com/dash_guide#snippets) - there are many other [alternatives](http://alternativeto.net/software/snippets/) out there for this - but probably the fact you can store snippets alongside other documentation could be a winner in this case.

Anyhow, since I’ve been collecting lots of snippets as [Github Gists](https://gist.github.com/), I thought I’d be nice to load them up into Dash so to test it out a bit more!

**Note:**

> \- the solution below does not extract tags information at the moment
> 
> \- always a good idea to make a backup copy of the Dash database before messing with it. Then just update the value of the DASH\_DATABASE parameter in the script and start the extraction.
> 
> \- inspired by another gist: [https://raw.github.com/gist/5466075/gist-backup.py](https://raw.github.com/gist/5466075/gist-backup.py)

So here we go:

<script src="https://gist.github.com/lambdamusic/706698eb4cd17ee1bb97e0524cdc1c62.js"></script>
