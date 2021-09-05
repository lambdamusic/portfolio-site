---
title: "Komodo-Edit :: a nice free python editor!"
date: "2009-02-09"
categories: 
  - "techlife"
tags: 
  - "ide"
  - "python"
---

Finding the perfect IDE for a programming language is always an ongoing process - [even more if your language is python](http://groups.google.com/group/google-appengine/browse_thread/thread/2d9e2884959d726a?pli=1) - i've been happily using eclipse/pydev for a while now, but recently i run into KomodoEdit and I liked it. Mostly, cause it's lightweight and it's built with a 'snippet-oriented' philosophy (something like [textmate](http://macromates.com/)).

You'll find lots of interesting [reviews](http://delicious.com/popular/komodo) of KomodoEdit, for example [here](http://arstechnica.com/open-source/news/2008/03/hands-on-open-source-scripting-environment-komodo-edit-4-3.ars) and [here](http://www.blogenough.com/blog/2008/04/19/using-komodo-edit-as-an-ide-for-google-app-engine.html), even if for learning purposes i believe it's always best to [download it and try to break it yourself](http://www.activestate.com/komodo_edit/)!!!

![picture-3](/media/static/blog_img/picture-3.png "picture-3")

By the way - I found out that if you want the [snippet auto-completion to work](http://praveenpn.com/blog/2008/05/02/komodo-edit-a-powerful-free-editor/) (a nice [introductory video is here](http://www.vimeo.com/954472)) you gotta **make sure all the snippets you create stay in the same folder/hierarchy the IDE gives you by default**. That is to say - in the figure below the 'django' snippet at the top-level won't be recognized when you press 'model1' + tab (or whatever you auto-completion key is set to). Instead, if you moved that snippet into the 'abbreviations/python' folder everything will work fine........... .. is this a bug or what? maybe i'll post it to the komodo forum...

![komodosnippet](/media/static/blog_img/picture-2.png "picture-2")
