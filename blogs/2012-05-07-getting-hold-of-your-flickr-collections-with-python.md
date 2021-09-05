---
title: "Getting hold of your Flickr collections with Python"
date: "2012-05-07"
categories: 
  - "tips-and-tricks"
tags: 
  - "api"
  - "flickr"
  - "python"
---

Recently I've been a little disappointed with [Flickr](http://www.flickr.com/), the popular online photo-sharing service. Photos gone missing, entire albums disappeared. Not really what you'd like to happen to your photo collection, especially when it's very large and therefore it's difficult to be always on top of what's there and what's not.. Time to change strategy: use flickr for sharing and my local HD for backup!

I emailed the customer service people at Flickr, they promptly replied that it wasn't their fault but most likely a bug with other apps I had previously authorised to edit my Flickr collection (e.g. iPhoto or Aperture). Bad news: apparently whatever happened now what's lost is lost forever. Not much to my consolation, the same happened to other people, for example check this [post](http://amateurtraveler.com/2010/03/27/photos-disappearing-from-flickr-when-the-cloud-fails/) or this [post](http://thomashawk.com/2007/03/flickr-users-photos-disappearing-from.html) to see alternative versions of the problem from 2010 and 2007.

So I've suddenly realised the cloud isn't that secure a place, as yet. It's time to change strategy: use flickr for sharing and my local HD for backup!

The good news is that if you know a little programming you can download your entire Flickr collection without having to pay a cent, for example by using Python. There are a few free libraries out there for accessing the [Flickr API](http://www.flickr.com/services/api/)s, such as [flickrpy](http://halotis.com/2009/09/08/download-images-from-flickr-with-python/) and [FlickrAPI](http://stuvel.eu/media/flickrapi-docs/documentation/). They both require you to fiddle a little with the code (at the very least, get a personalised passkey from Flickr and add it to the python program) in order to get what you want.

The one I've gone for instead is a little package called [flickrtouchr](https://github.com/dan/hivelogic-flickrtouchr), which is even easier to use. After downloading you just have to run it from the command line and it'll begin browsing your whole Flickr collection and download pictures at the highest resolution available. I have more than 8000 photos, and it worked like a charm - beware though - it took more than 10 hours on my TalkTalk connection.

Thanks Dan@[hivelogic.com](http://hivelogic.com/) for writing this code - couldn't be asking for more!

\[mac\]@mike:~/Dropbox/code/python/\_libs/dan\-hivelogic\-flickrtouchr\-9ba645b\>python flickrtouchr.py ~/Desktop/FlickrBackupFolder

In order to allow FlickrTouchr to read your photos and favourites
you need to allow the application. Please press return when you've
granted access at the following url (which should have opened
automatically).

http://api.flickr.com/services/auth/?api\_key\=e2245325378b5675b4af4e8cdb0564716fa9bd&perms\=read&frob\=8856734hhgbbhsksd19443\-caa77e89367asbbhfa2ba\-600258&api\_sig\=a4aasdbbnb345c7fb46bdd33cfa65ec17bb32a

Waiting for you to press return

Egypt 1 ... in set ... Sharm el Sheik, Dec 2011
Egypt 2 ... in set ... Sharm el Sheik, Dec 2011
Egypt 3 ... in set ... Sharm el Sheik, Dec 2011
Egypt 4 ... in set ... Sharm el Sheik, Dec 2011

..... etc….
