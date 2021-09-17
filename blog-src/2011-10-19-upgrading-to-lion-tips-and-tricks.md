---
title: "Upgrading to Lion: tips and tricks"
date: "2011-10-19"
categories: 
  - "tips-and-tricks"
tags: 
  - "lion"
  - "mac"
  - "osx"
---

I've finally decided to upgrade my mac operating system from Snow Leopard (10.6.8) to Lion (10.7.2). Not really for the [new features](http://www.apple.com/uk/macosx/whats-new/features.html) such as Mission Control and LaunchPad (which although being pretty cool are not going to change my life) but mostly for the fact that the new OS is well integrated with [iCloud](http://www.apple.com/uk/icloud/). Sharing my iCal calendars, Address book contacts and other useful stuff across my apple computers and mobile devices is going to be a digital-life-changer, hopefully for the better.

Unfortunately as usual an OS upgrade is never as smooth as I would like it to be; so here's a list of the problems I ran into (and still am), with pointers to solutions whenever I found one.

> Tip: A useful place where to get info about Lion is here: [http://osxdaily.com/tag/mac-os-x-10-7/](http://osxdaily.com/tag/mac-os-x-10-7/)

### 1\. Wi-Fi disconnection issues

This is quite a bad one: my wifi connection wouldn't stay on for more than 2-3 minutes at times, making it impossible to do any continuative work online. After a lot of swearing and searching online, I found a good solution on [this article on iLounge.com](http://www.ilounge.com/index.php/backstage/comments/os-x-lion-serious-wi-fi-disconnect-problems-for-macs-and-solutions/). The article offers many solutions, but the one that worked for me is to manually downgrading the Atheros WiFi driver which seems to be ill on Lion to the version provided with Snow Leopard (comment 53). Here's the recipy:

> 1\. run kextstat | grep -i atheros if a line was returned, you are most likely using Atheros WiFi card and the related kext 2. In your home folder create two directories: cd && mkdir New Old 3. If you have a copy (time machine backup) or other system installed with Snow Leopard (as latest as possible), take a copy of /System/Library/Extensions/IO80211Family.kext and put it into ~/Old/ directory \[_P.S. if you don't know where to get that file, I've uploaded a copy here: [IO80211Family.kext.zip](http://www.box.net/shared/8igl4hybcml0e4zc5dzx)_\] 4. (Back on to your main system) gain root access: sudo -s 5. Move: mv /System/Library/Extensions/IO80211Family.kext ~/New/ 6. Move cache file: mv /System/Library/Caches/com.apple.kext.caches/Startup/kernelcache ~/New/ 7. copy old kext: cp -r ~/Old/IO80211Family.kext /System/Library/Extensions/ 8. go to: cd /System/Library/Caches/com.apple.kext.caches/Startup/ 9. rebuild cache: kextcache -v 1 -a i386 -a x86\_64 -mkext kernelcache /System/Library/Extensions 10. Using GUI Utilities->Disk Utility->Macintosh HD->Repair permissions 11. pray and reboot

### 2\. Install the latest Xcode and Developer Tools

This is number 2 in the list, but really it should be number 1 if you are a software developer. The latest Xcode (4.2, get it on the [apple store](http://itunes.apple.com/us/app/xcode/id448457090?mt=12) for free) includes all sorts of low and high level programming frameworks, from C compilers to Python interpreters. In other words, without reinstalling Xcode tons of software development environments won't run as usual!

Installing Xcode is very easy, here's a nice tip to keep in mind though (as found [here](http://jessenoller.com/2011/07/30/quick-pythondeveloper-tips-for-osx-lion/)):

> When installing XCode, for some unknown unholy rea­son, if you have not quit itunes, and itunes helper (see activ­ity mon­i­tor) prior to start­ing the XCode installer, the install will hang. Do your­self a favor and kill it with fire.

Also, two more crucial things to keep in mind:

> \- Remem­ber; the binary direc­tory for the dev tools is in /Developer/usr/bin/ — this includes gcc-4.2 - Do your­self a favor, drop “export ARCHFLAGS="-arch x86\_64"” into your .bash\_profile.

The last point is extremely important; make sure you do that otherwise you'll easily run into all sorts of 32 vs 64 bits architectures conflicts that (if you're like me) you have no time to get into ([more info here](http://stackoverflow.com/questions/5256397/python-easy-install-fails-with-assembler-for-architecture-ppc-not-installed-on)).

### 3\. Fix your Python installation

On my iMac I couldn't run [iPython](http://ipython.org/) anymore; this was surprisingly easy to fix, I just run again easy\_install ipython from the command line and there you go iPython went back up (version 2.7, the default one with Lion).

This didn't work on my other mac though (a slightly older MacBook); the easy\_install ipython trick failed with a DistributionNotFound error; if this is the case, you probably have to re-install Apple's Developer Tools (see point 2 above). However before doing that you might want to consider this **good tip** which I found here:

> 1\. Make a list of all the third-party libraries you currently have installed under Python 2.6, because you’ll have to reinstall all of them for 2.7 and you won’t have the 2.6 site-packages directory to refer to. 2. Update to Lion. 3. Update to Xcode 4.1. It’s free in the App Store.

Good, so I installed XCode 4 (= Apple's Developer Tools) but I still had a problem: for some reason the default python binary (/usr/bin/python) was still pointing at the 2.5 release, instead of the 2.7 that comes with Lion. This was easily fixed by issuing this command:

> defaults write com.apple.versioner.python Version 2.7

Two final steps are then required:

> a) [Download](http://pypi.python.org/pypi/setuptools#downloads) the 2.7 version of setuptools and install it (e.g. sudo sh setuptools-0.6c11-py2.7.egg); b) re-install iPython via setuptools: sudo easy\_install ipython

Obviously I'll have to manually install under 2.7 all the libraries I used to have on 2.6, but that can be done incrementally and thanks to easy\_install it's also quite quick.

For more discussions on python and Lion, check out these posts: [Quick Python/Developer tips for OSX Lion](http://jessenoller.com/2011/07/30/quick-pythondeveloper-tips-for-osx-lion/) and [Python problems on Lion](http://www.leancrew.com/all-this/2011/07/python-problems-on-lion-mostly-self-inflicted/).

### 4\. The Mercurial binaries disappeared

What the heck. You need to reinstall Mercurial using the package available here: [http://mercurial.berkwood.com/](http://mercurial.berkwood.com/) and Python problems on Lion

### 5\. Omnigraffle can't save files anymore

My 5.0 copy of Omnigraffle loaded and let me create stuff just fine, but it won't save files anymore. I got an error message that looked like an internal error ("class bla bla can't be subclassed by bla bla bla") each time I tried to save my work. Bugger.

Couldn't find a solution to this; I guess that getting the latest version (5.3 I think) will solve the issue (it' 70 dollars though).

### 6\. Java runtime missing

Lion does not provide a Java runtime by default, so you need to install it separately. No worries: that's going to happen automatically as soon as you try to run a Java application; alternatively, you can do that manually [here](http://support.apple.com/kb/dl1421).

### 7\. The Finder Sidebar Icons colours (well lack of..) are depressing

Why on earth haven't they made that a preference we can change? There's a way around it though, and it is [described here](http://osxdaily.com/2011/08/25/get-color-sidebar-icons-back-in-mac-os-x-10-7-lion-finder-windows/). This is the gist of it:

> \- Download and install SIMBL, which you can [get here](http://www.culater.net/software/SIMBL/SIMBL.php) - Download the [ColorfulSidebar SIMBL plugin](http://cooviewerzoom.web.fc2.com/ColorfulSidebar1.0.dmg.zip) (direct link) or [visit the developers home](http://cooviewerzoom.web.fc2.com/colorfulsidebar.html) and mount the DMG file - Move the ColorfulSidebar.bundle into the following SIMBL plugin folder: ~/Library/Application Support/SIMBL/Plugins/ - Either login and logout of Mac OS X, or just kill the Finder through the Terminal to relaunch it: killall Finder

Unfortunately this solution won't stick after an OS reload; but it's enough to relaunch the Finder (killall Finder) to reload the plugin.

P.S. If you can't access the ~/Library folder using Finder, check out point 12 below!

### 8\. Safari Won't Reopen To HomePage

Apple [changed](https://discussions.apple.com/message/15662314#15662314) the way new windows open. In Safari, if you set the "New windows open with" preference to "Homepage", then ALL new windows will now open with your homepage setting, including the initial startup window. In past versions, you could set that preference to "Same Page" while startup would auto open the homepage.

Solution: go to _System Preferences/General/_ and uncheck the "Restore windows when quitting and re-opening apps" option.

### 9\. The CD-TO utility disappeared

A small utility I've been using all the time is [cdto](http://code.google.com/p/cdto/), a mini application that opens a Terminal.app window cd'd to the front most finder window.

That doesn't work anymore, but the good news is that as of Mac OS X Lion 10.7, Terminal includes exactly this functionality as a Service, which you can set by going to System Preferences > Keyboard > Keyboard Shortcuts > Services (check this useful [blog post for more details](http://www.tech-recipes.com/rx/16708/os-x-lion-how-to-easily-open-a-new-terminal-or-terminal-tab-at-a-folder/)). Also, a more in-depth discussion of the various options available can be found on [stackOverflow](http://stackoverflow.com/questions/420456/open-terminal-here-in-mac-os-finder).

In addition, Lion Terminal will open a new terminal window if you drag a folder (or pathname) onto the Terminal application icon, and you can also drag to the tab bar of an existing window to create a new tab.

**Update**: CDTO has a [Lion version](http://code.google.com/p/cdto/downloads/list) available too. Also, another free software that offers the same functionalities is [Go2Shell](http://itunes.apple.com/us/app/go2shell/id445770608?mt=12).

### 10\. Visor doesn't work anymore

Yes because Visor (a pumped-up version of the terminal application) relied on SIMBL, which is handled different on Lion. Not a problem, just download [TotalTerminal](http://totalterminal.binaryage.com/), which is an updated and more stable version of Visor.

For original Visor 2.2 users: TotalTerminal plugin is not injected into Terminal.app automatically like with SIMBL. You have to launch TotalTerminal.app to inject the plugin into Terminal.app. You might want to put TotalTerminal.app into Startup Items.

### 11\. VmwareFusion won't work

VmwareFusion is a Virtual-PC software that people use to run windows on a mac; I was using an older version of it and it looks as if this is incompatible with the 64-bit architecture of the Lion operating system.

Solution: nothing else than getting the [latest version of VmwareFusion](http://www.vmware.com/products/fusion/overview.html), which currently sells for 50 dollars. Bugger.

### 12\. Customize the Finder

Get the Library folder to show again: by default, the Library folder in your home directory doesn't show in Finder. Just type this into your terminal app to fix it:

> chflags nohidden ~/Library/

Show hidden files in finder: beware though, this might result in a lot of information being displayed which is not needed.

> defaults write com.apple.finder AppleShowAllFiles -bool YES

Show full paths in finder: it's quite useful to know always where you are.

> defaults write com.apple.finder \_FXShowPosixPathInTitle -bool YES

.. and many more customisations are listed on [http://secrets.blacktree.com/](http://secrets.blacktree.com/).

Alternatively, you can customise your mac to the bone without touching the console by downloading a free utility software called [TinkerTool](http://www.bresink.com/osx/0TinkerTool/download.php5).

### 13\. Get the Old Apple Mail Back

The new Apple Mail interface is quite slick, but I still have some problems adapting to it.

You can easily revert back to the old interface just by going to the Mail menu and choose Preferences. From there, click Viewing and you'll find the options you want right at the top.

### 14\. .. ? (still looking for it!)
