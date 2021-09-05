---
title: "What Lisp to choose, really?"
date: "2007-04-24"
categories: 
  - "justblogging"
tags: 
  - "lisp"
---

During the last days, I almost switched from Lispworks (too many tabs, too many things in general) back to MCL (essential, fast, with a powerful meta-dot command). But I run into many problems, the most important of them is getting ASDF to run, so to be able to run the server (Hunchentoot) from there. I set up the init file to load ASDF in MCL, and tried to share the same registry which I previously created through Lispworks and asdf-install.... but it doesnt want to work! Why's that?

..............LISTENER  
Welcome to Macintosh Common Lisp Version 5.0!  
? (asdf:operate 'asdf:compile-op :asdf-install)  
\> Error: Error component "asdf-install" not found  
\> While executing: ASDF:FIND-SYSTEM  
\> Type Command-. to abort.  
See the Restartsâ€¦ menu item for further choices.  
1 > asdf:\*central-registry\*  
("Macintosh HD:Users:michelepasin:Documents:Lisp:asdf-mcl-install-dir:systems:" \*DEFAULT-PATHNAME-DEFAULTS\*)  
1 > (asdf:operate 'asdf:compile-op :cl-who)  
\> Error: Error component "cl-who" not found  
\> While executing: ASDF:FIND-SYSTEM  
\> Type Command-. to abort.  
See the Restartsâ€¦ menu item for further choices.  
2 >

...............INIT file (in MCL folder)  
#-:asdf (load "Macintosh HD:Users:michelepasin:Documents:Lisp:asdf:asdf")

(pushnew "Macintosh HD:Users:michelepasin:Documents:Lisp:asdf-mcl-install-dir:systems:" asdf:\*central-registry\* :test #'equal)

Then later today I found out about [this (basically, Digitool's misteriosly 'silent' about MCL and intel-macs)](http://digitool.com/pipermail/info-mcl_digitool.com/2006-October/000460.html). So the question is: what's the right framework to choose?
