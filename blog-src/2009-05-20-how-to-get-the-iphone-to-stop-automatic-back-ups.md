---
title: "How to get the iPhone to stop automatic back ups"
date: "2009-05-20"
categories: 
  - "justblogging"
  - "techlife"
  - "tips-and-tricks"
tags: 
  - "iphone"
---

This is a problem that irritated me so many times - i'm so glad I found a solution now, [thanks to this blog post](http://klauskjeldsen.dk/?s=copy+applications+to+iphone+without+sync). Basically the issue is that every time you link up your iPhone for syncing contacts or songs the _whole damn_ application library gets backed up **automatically**.

Which obviously **takes longer and longer** with each new application you download .. I tried to disable the 'sync applications' option in iTunes but then a scary message appears:

![Picture 1](/media/static/blog_img/picture-15.png "Picture 1")

Who wants all the applications being removed?????? Surely _not_ me.

So, I'm just reporting the instructions as posted by this nice fellow who published them on the [blog](http://klauskjeldsen.dk/) above:

> 1) Quit iTunes. 2) Open a Terminal (Applications > Utilities > Terminal) 3) Type or copy the following command: defaults write com.apple.iTunes AutomaticDeviceBackupsDisabled -bool true 4) Open iTunes. 5) Connect the iPhone. 6) Make Sync without backing up.

To enable automatic backup in iTunes again use this command instead: _defaults write com.apple.iTunes AutomaticDeviceBackupsDisabled -bool false_

That should do the trick! I tried it and the following sync took less than a minute.

Only thing to remember: **making backups is not at all a bad idea**, so make sure you do it **manually** every once in a while!

![Untitled](/media/static/blog_img/untitled.png "Untitled")

...
