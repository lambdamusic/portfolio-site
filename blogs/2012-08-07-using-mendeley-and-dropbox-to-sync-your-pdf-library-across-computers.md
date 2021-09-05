---
title: "Using Mendeley and Dropbox to sync your pdf library across computers"
date: "2012-08-07"
categories: 
  - "tips-and-tricks"
tags: 
  - "mendeley"
  - "reference"
---

[Mendeley](http://www.michelepasin.org/blog/2009/08/21/social-reference-manager-mendeley/) is a pdf and reference manager software that has a number of cool [features](http://www.mendeley.com/features/): online/offline support, tools for creating public groups (=collections of references), and last but not least, it's fast and easy to use. Since your references are synchronised via the online service, you can run Mendeley on more than one computer/device. However unless you pay for a fee you will be able to synchronise only up to 1 gig of data through it, which is probably [not enough for some people](http://feedback.mendeley.com/forums/4941-mendeley-feedback/suggestions/301592-pdfs-should-be-attached-with-paths-relative-to-a-u?ref=title). So here's a simple method for using a cloud service like Dropbox to sync your entire pdf library without having to pay a cent.

The **basic idea**: keep all of your pdf files in the cloud using a Dropbox folder; also, keep the Mendeley database and preferences in the cloud, so that they are shared across computers. Finally, point Mendeley to that Dropbox folder and let it do the rest for us (e.g. keeping it organised etc.).

> **Warning**: since with this method the preferences and database are shared across computers, you must make sure you don't use Mendeley at the same time on both computers as that could lead to some conflict!

This recipe assumes that you have two macs and both [Dropbox](https://www.dropbox.com/) and [Mendeley](http://www.mendeley.com/) **installed** on both of them. We'll call one of the two machines _mac-1_, and the other one _mac-2_. Also, the method **requires** that you are using the **same username** on both macs. I know, this is a big limitation, but since Mendeley indexes pdf files using their full path that's the only way for things to be wired up correctly (otherwise on one of the two macs the path of the pdf files will be broken).

### 1\. Set up Mendeley and DropBox on mac-1

On Mac-1, create a Mendeley folder in your Dropbox. Within that, create two new folders, pdf and db. Now launch Mendeley Desktop and in the preferences panel set the pdf-files location to the pdf folder you just created. After clicking on 'apply' Mendeley will move your existing library (if you have one) into the new folder. Wait till that's finished before moving on to step 2.

[![Mendeley Prefs](/media/static/blog_img/7738619978_0762a77e91.jpg)](http://www.flickr.com/photos/mikele/7738619978/ "Mendeley Prefs by MagIcReBirth, on Flickr")

### 2\. Add Mendeley database to DropBox on mac-1

Close Mendeley Desktop on mac-1. Now open up the terminal and [symlink](http://en.wikipedia.org/wiki/Symbolic_link) the ~/Library/Application Support/Mendeley Desktop folder to the db folder just created in Dropbox. This way the DB and preferences can be shared across computers.

\[mac\]@mac1:~/Library/Application Support>cp -r Mendeley\\ Desktop/ ~/Dropbox/Mendeley/db/
\[mac\]@mac1:~/Library/Application Support>mv Mendeley\\ Desktop/ \_backup\_Mendeley\_Desktop/
\[mac\]@mac1:~/Library/Application Support>ln -s ~/Dropbox/Mendeley/db/Mendeley\\ Desktop .

Dropbox will start cloud-syncing the new folder we added. In the meantime, you can try launching Mendeley and checking that everything works at it should.

### 3\. Set things up on mac-2

Put to sleep mac-1 and wake up mac-2. If you're online, Dropbox on mac-2 will immediately start downloading all the new stuff you previously added to it (via mac-1). In the meantime, quickly open up Mendely and update the preferences as we did in step 1 above. Then closed it down.

Once the Dropbox download is finished, we can set up the symlink to the Mendeley database as we did in step 2 (no need to copy the db folder this time, because we're using the folder already present in Dropbox/Mendeley/db):

\[mac\]@mac2:~/Library/Application Support>mv Mendeley\\ Desktop/ \_backup\_Mendeley\_Desktop/
\[mac\]@mac2:~/Library/Application Support>ln -s ~/Dropbox/Mendeley/db/Mendeley\\ Desktop .

**That's it**. You now should be able to open up Mendeley and have your entire library synchronised across the two computers (effectively, you're working on a _single_ library since your database is shared too).

Obviously you can still use the **web-sync** service, which is handy for example if you use also some mobile device. There you'll still have the 1gig limitation for the pdf files, but at least for me that's hardly a problem cause I don't need to have my entire library on the go all the time (I just have a folder called 'syncedStuff' in Mendeley Desktop and synchronise only the files attached to that).

### If things go wrong..

Well, I'd expect any wise pdf-collectors to make **regular backups** of their precious databases. In some cases though it's not just a matter of putting things back as they were; for example once I moved the pdf source files to a different location, launched Mendeley and discovered that although my library was still there all the pdf links were broken. Since I wanted to keep the new paths for all the pdf files, as a last resort I tried to **hack into Mendeley's own** [SQLite](http://en.wikipedia.org/wiki/SQLite) database and clean things up myself.

> Here's another post that explains how to modify Mendeley's database manually: [Using Mendeley effectively on multiple systems using an external storage drive](http://n30bli7z.blogspot.co.uk/2009/10/using-mendeley-effectivey-on-multiple.html)

This is pretty easy actually. Mendeley stores the **full file paths** to your files in its database. In particular, the database file can be found in /Application Support/Mendeley Desktop, and it is named like this: youremail@www.mendeley.com.sqlite.

All you have to do is this: close down Mendeley (if it's running), make a backup copy of the database file for safety purposes, then open it up using a SQLite GUI (e.g. on mac you can use [SQLite Browser](http://sourceforge.net/projects/sqlitebrowser/) which is free). You'll see that the **Files table** contains all the (wrong) paths to your pdf files; now you can update these paths by launching a simple 'execute' command, e.g.:

update Files set 
  localurl = replace(localurl, '/Users/me/Dropbox/Mendeley/old/path/', '/Users/me/Dropbox/Mendeley/new/path/');

Make sure the command did its job by checking the Files table contents; if that's the case, the next time you launch Mendeley it won't have no broken links anymore!
