---
title: "Installing Mercurial on OSx 10.6.5"
date: "2010-12-01"
categories: 
  - "techlife"
  - "tips-and-tricks"
tags: 
  - "mac"
  - "mercurial"
  - "versioncontrol"
---

Mercurial is a free, distributed source control management tool. It efficiently handles projects of any size and offers an easy and intuitive. That's what you read on [its website](http://mercurial.selenic.com/), at least. I decided to give it a go mainly because I was looking forward to use a [decentralized version control system](http://en.wikipedia.org/wiki/Distributed_revision_control) for a couple of side projects I'm working on; moreover, because a friend pointed out that [BitBucket](http://bitbucket.org/) (an online free code-hosting service based on Mercurial) has a [free plan](https://bitbucket.org/account/signup/?plan=5_users) that doesn't force you to make your projects public by default - like most other competitor services do. Free + private = time to test it!

Installation started by [downloading](http://mercurial.selenic.com/downloads) and running the default installer. The [instructions online](http://confluence.atlassian.com/display/BITBUCKET/Bitbucket+101) are very detailed, so I tried to follow them. However, after installing, I tried to run the _hg_ command (which is how you invoke mercurial) but the following error kept coming up:

```

abort: couldn't find mercurial libraries in [/usr/platlib/Library/Python/2.6/site-packages /usr/local/bin /Library/Python/2.5/site-packages/ipython-0.9.1-py2.5.egg /Library/Python/2.5/site-packages/readline-2.5.1-py2.5-macosx-10.5-i386.egg /Library/Python/2.5/site-packages/antlr_python_runtime-3.1.1-py2.5.egg /Library/Python/2.5/site-packages/feedparser-4.1-py2.5.egg /Library/Python/2.5/site-packages/pydelicious-0.5.0-py2.5.egg /Library/Python/2.5/site-packages/virtualenv-1.3.3-py2.5.egg /Library/Python/2.5/site-packages/python_ldap-2.3.9-py2.5-macosx-10.5-i386.egg /Library/Python/2.5/site-packages/setuptools-0.6c11-py2.5.egg /Library/Python/2.5/site-packages/py2app-0.4.3-py2.5.egg /Library/Python/2.5/site-packages/macholib-1.2.1-py2.5.egg /Library/Python/2.5/site-packages/modulegraph-0.7.3-py2.5.egg /Library/Python/2.5/site-packages/yolk-0.4.1-py2.5.egg /Library/Python/2.5/site-packages/django_profiles-0.2-py2.5.egg /Library/Python/2.5/site-packages/pyglet-1.1.3-py2.5.egg /Library/Python/2.5/site-packages/PdbTextMateSupport-0.3-py2.5.egg /Library/Python/2.5/site-packages/PyXML-0.8.4-py2.5-macosx-10.5-i386.egg /Library/Python/2.5/site-packages/rdflib-3.0.0-py2.5.egg /Users/mac/Code/python/utils /Users/mac /System/Library/Frameworks/Python.framework/Versions/2.5/lib/python25.zip /System/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5 /System/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/plat-darwin /System/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/plat-mac /System/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/plat-mac/lib-scriptpackages /System/Library/Frameworks/Python.framework/Versions/2.5/Extras/lib/python /System/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/lib-tk /System/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/lib-dynload /Library/Python/2.5/site-packages /Library/Python/2.5/site-packages/PIL /System/Library/Frameworks/Python.framework/Versions/2.5/Extras/lib/python/PyObjC /System/Library/Frameworks/Python.framework/Versions/2.5/Extras/lib/python/wx-2.8-mac-unicode]
(check your install and PYTHONPATH)
```

### Fixing the errors

Mercurial couldn't find the python libraries it needs to run; after a bit of googling I [found out](http://stackoverflow.com/questions/1461374/installing-mercurial-on-mac-os-x-10-6-snow-leopard) that installing Mercurial from the Mac Disk Image will cause its files to end up here:

```

/Library/Python/2.6/site-packages/
```

Apparently the default python installation that comes with 10.6.5 puts all the python packages somewhere else, that is, in the Frameworks directory:

```

/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/site-packages
```

That's why Mercurial couldn't find them - by default OSx expects python libraries to be somewhere else. Adding the missing library location to the pythonpath in ~/.bash\_profile fixed that:

```

export PYTHONPATH="/Library/Python/2.6/site-packages:$PYTHONPATH"
```

Next step, adding the Mercurial config file at ~/.hgrc :

```

[mac]@yourname:~>touch .hgrc
[mac]@yourname:~>pico .hgrc
 # in the file add these lines:
[ui]
; editor used to enter commit logs, etc.  Most text editors will work.
editor = mate
username = MY_FIRST_NAME MY_LAST_NAME 
```

### Getting started with BitBucket

Time to get started with setting up the BiBucket repository now. First set up an account on the site, then clone your repository with these commands:

```

[mac]@yourname:~/Some/location>hg clone https://yourname@bitbucket.org/name/repository_name
http authorization required
realm: Bitbucket.org HTTP
user: yourname
password: ******
destination directory: your_dir
no changes found
updating to branch default
0 files updated, 0 files merged, 0 files removed, 0 files unresolved
```

Almost there... next thing, add some files to the repository/directory, '**add**' them and '**commit**' them. You're up and running..

```

[mac]@yourname:~/Some/location> hg add
adding -ideas/.DS_Store
adding -ideas/15June2010/untitled.scm
adding -ideas/15June2010/zeb1.patch
adding -ideas/15June2010/zeb2.patch
adding -ideas/15June2010/zeb3.patch
adding -ideas/15June2010/zeb4.patch
adding -ideas/a.scm
adding -ideas/a_better_drum_machine.scm
adding -ideas/a_progression.scm
adding -ideas/c-ColorChange.scm
adding -ideas/cassa_a_gogo.scm
adding -ideas/ccx-simple_progression.scm
adding -ideas/chords_with_drums.scm
..... etcetera....

[mac]@ yourname:~/Some/location>hg commit -m "Initial commit of all files to the repository."
[mac]@ yourname:~/Some/location>hg push # to push changes to this repo
http authorization required
realm: Bitbucket.org HTTP
user: yourname
password: ****
pushing to https://yourname@bitbucket.org/name/repository_name
searching for changes
remote: adding changesets
remote: adding manifests
remote: adding file changes
remote: added 1 changesets with 455 changes to 455 files
remote: bb/acl: yourname is allowed. accepted payload.
```

### GUIs

I also tried a couple of Graphical User Interfaces for Mercurial; the one that seemed best to me (on OSx obviously) is Murky, which is [freely available here](http://bitbucket.org/snej/murky/wiki/Home). Can't ask for more can I?

[![Screen shot 2010-12-01 at 20.28.57.png](/media/static/blog_img/Screen-shot-2010-12-01-at-20.28.57.png)](http://www.michelepasin.org/blog/wp-content/uploads/2010/12/Screen-shot-2010-12-01-at-20.28.57.png)

UPDATE: Another quite nice (and free) user interface is [MacHG](http://jasonfharris.com/machg/).
