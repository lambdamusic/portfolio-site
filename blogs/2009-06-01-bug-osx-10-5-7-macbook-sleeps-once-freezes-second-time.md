---
title: "Bug: OSx 10.5.7 - Macbook sleeps once, freezes second time"
date: "2009-06-01"
categories: 
  - "techlife"
  - "tips-and-tricks"
tags: 
  - "bug"
  - "osx"
---

![Picture 1](/media/static/blog_img/picture-11.png "Picture 1")

Quite a disturbing surprise finding out that your laptop doesn't work anymore after an OS update. And it makes you think - **why the hell haven't I waited for the rest of the world to test it out first**?

But the desire to be up-to-date and on top of things is too strong, I suppose. Or maybe it's just a passive attitude towards the 'software update' dialog box....

Anyways - here's the problem: **Macbooks tend to crash after going to sleep mode** - and even worse, mine switched on from sleep while in the case and the fan started running like crazy. If I hadn't realized what happened... I could have cooked an egg on that neat metallic cover. I googled about this for a while, in my opinion the **most informative posts** are on the Apple discussion forum - [here](http://discussions.apple.com/thread.jspa?threadID=2008589&tstart=0) and [here](http://discussions.apple.com/thread.jspa?threadID=2005687&tstart=0).

The fix is not available yet, so **the options you have are**:

1) disable the sleep option in system preferences 2) revert back to OSX 10.5.6 ([instructions here](http://www.macfixit.com/article.php?story=20090514132546680)) 3) use a (temp?) hack. In fact, apparently, **there's a [workaround](http://www.macfixit.com/article.php?story=20090518095106449)**:

> According to several reports around support forums and from e-mail correspondence from our readers, this issue appears to be related to the Ethernet settings on notebooks.
> 
> MacFixIt reader "Andreas S." reports:
> 
> "It appears that if the **Ethernet is not enabled (airport only network settings)** that on the MacBook Pro the sleep only works once and crashes the second time."
> 
> To re-enable the Ethernet port settings:
> 
> 1\. Open System Preferences > Network 2-1. If you see your Ethernet port in your list of network ports (on the left-side of the window) and it says "Inactive," activate the port by clicking the gear wheel icon and selecting "Make Service Active." Click "Apply." 2-2. If you do not see your Ethernet port in your list of network ports (on the left-side of the window), click the "" button in the bottom-left corner.+ 3. In the "Interface" drop-down menu, select "Ethernet." 4. Enter a name and select "Create." You should see your new Ethernet connection appear. 5. Click "Apply."
> 
> Note: If you are having this issue and your Ethernet port is already enabled, try disabling it (using the gear wheel icon menu > "Make Service Inactive"). Log out or restart your Mac, then enable it. Be sure to "Apply" your changes.
> 
> Test your MacBook or MacBook Pro by closing the clamshell. Be sure to try this twice as most reports point to the second attempt at sleep as being the culprit for the freeze. If it does not work, try resetting your Mac and test again.

**UPDATE**

I tried the workaround and it does work
