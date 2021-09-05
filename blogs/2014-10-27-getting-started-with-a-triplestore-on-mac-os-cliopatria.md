---
title: "Installing ClioPatria triplestore on mac os"
date: "2014-10-27"
categories: 
  - "semantic-web"
  - "techlife"
tags: 
  - "cliopatria"
  - "graph"
  - "rdf"
  - "triplestore"
---

ClioPatria is a "[SWI-Prolog](http://www.swi-prolog.org/) application that integrates SWI-Prolog's the SWI-Prolog libraries for RDF and HTTP services into a ready to use (semantic) web server". It is actively developed by the folks at the [VU University of Amsterdam](http://www.cs.vu.nl/en/index.asp) and is freely available online.

While at a conference last week I saw a pretty cool demo ([DIVE](http://dive.beeldengeluid.nl/)) which, I later learned, is powered by the ClioPatria triplestore. So I thought I'd give it a try and by doing so write a follow up on my recent post on [installing OWLIM on Mac OS](http://www.michelepasin.org/blog/2014/10/16/getting-started-with-a-triplestore-on-mac-os-graphdb-aka-owlim/).

### 1\. Requirements

**OSX**: Mavericks 10.9.5 **XCode**: latest version [available from Apple](https://developer.apple.com/xcode/downloads/) **HOMEBREW**: ruby -e "$(curl -fsSkL raw.github.com/mxcl/homebrew/go)" **Prolog**: build it from source [using brew](http://www.swi-prolog.org/build/macos.html): brew install swi-prolog **ClioPatria**: git clone https://github.com/ClioPatria/ClioPatria.git

### 2\. Setting up

After you have downloaded and unpacked the archive, all you need to do is [start a new project](http://cliopatria.swi-prolog.org/help/source/doc/home/vnc/prolog/src/ClioPatria/web/help/CreateProject.html) using the ClioPatria script. In short, this is done by creating a new directory and telling ClioPatria to configure it as a project:

\[michele.pasin\]:~/Documents/ClioPatriaProjects/firstproject> ../path/to/ClioPatria/configure

A bunch of files are created, including a script run.pl which you can use later to run the server.

### 3\. Running ClioPatria

I tried running the run.pl as per documentation but that didn't work:

\[michele.pasin\]@Tartaruga:~/Documents/ClioPatriaProjects/firstproject>./run.pl 
./run.pl: line 3: :-: command not found
./run.pl: line 5: /Applications: is a directory
./run.pl: line 6: This: command not found
./run.pl: line 8: syntax error near unexpected token \`('
./run.pl: line 8: \`    % ./configure			(Unix)'

According to a thread on stack overflow, the [Prolog shebang line isn't interpreted correctly by OSx](http://stackoverflow.com/questions/25467090/how-to-run-swi-prolog-from-the-command-line), meaning that Mac OS doesn't recognise that script as a Prolog program.

That can be easily **solved** by calling the Prolog interpreter (swipl) explicitly:

\[michele.pasin\]@Tartaruga:~/Documents/ClioPatriaProjects/firstproject>swipl run.pl 
ERROR: /Applications/-Other-Apps/8-Languages-IDEs/ClioPatria/rdfql/sparql\_runtime.pl:1246:14: Syntax error: Operator expected
% run.pl compiled 1.64 sec, 25,789 clauses
% Started ClioPatria server at port 3020
% You may access the server at http://tartaruga.local:3020/
% Loaded 0 graphs (0 triples) in 0.00 sec. (0% CPU = 0.00 sec.)
Welcome to SWI-Prolog (Multi-threaded, 64 bits, Version 6.6.6)
Copyright (c) 1990-2013 University of Amsterdam, VU Amsterdam
SWI-Prolog comes with ABSOLUTELY NO WARRANTY. This is free software,
and you are welcome to redistribute it under certain conditions.
Please visit http://www.swi-prolog.org for details. 

You should be able to access the server with your browser on **port 3020** (ps: the previous command caused a syntax error too, but luckily that isn't a game stopper).

[![Cliopatria](/media/static/blog_img/cliopatria.png)](http://www.michelepasin.org/blog/wp-content/uploads/2014/10/cliopatria.png)

#### First impression:

Super-easy to install, **clean** and **intuitive** user interface. I subsequently added a couple of RDF datasets and it all went very very smoothy.

One cool feature is the fact that ClioPatria has a [built-in package management system](http://cliopatria.swi-prolog.org/help/source/doc/home/vnc/prolog/src/ClioPatria/web/help/cpack/index.txt), which allows you to easily install **extensions** to the application. For example what follows allows one to quickly extend the UI with a couple of 'intelligent' SPARQL query interfaces ([Yasque](http://yasqe.yasgui.org/) and [Flint](http://openuplabs.tso.co.uk/demos/sparqleditor)):

\[michele.pasin\]@Tartaruga:/Applications/ClioPatria>sudo git submodule update --init web/yasqe web/yasr
Password:

\[michele.pasin\]@Tartaruga:/Applications/ClioPatria>sudo git submodule update --init web/FlintSparqlEditor

### 4\. Loading a big dataset

As in my [previous post](http://www.michelepasin.org/blog/2014/10/16/getting-started-with-a-triplestore-on-mac-os-graphdb-aka-owlim/), I've tried loading the [NPG Articles](http://data.nature.com/downloads/2012-07-16/articles.2012-07-16.nq.tar.gz) dataset available at nature.com's legacy linked data site [data.nature.com](http://www.nature.com/developers/documentation/linked-data-platform/releases/snapshot-downloads/). The dataset contains around **40M triples** describing (at the metadata level) all that's been published by NPG and Scientific American from 1845 till nowadays. The file size is **~6 gigs** so it's not a huge dataset. Still, something big enough to pose a challenge to my macbook pro (8gigs RAM).

I used the **web UI** ('load local file') to load the dataset but I quickly ran into a **'not enough memory' error**. Tried fiddling with the settings accessible via the web interface (_Stack limit_, _Time limit_), but that didn't seem to do much. So I **increased the memory allocated to the Prolog process** (more info [here](http://www.swi-prolog.org/FAQ/StackSizes.html)) however this wasn't enough since after around 20mins the whole thing crashed again due to an _out of memory_ error.

\[michele.pasin\]@Tartaruga:~/Documents/ClioPatriaProjects/firstproject>swipl -G6g run.pl

In the end I got in touch with the ClioPatria creators via the [mailing list](http://mailman.few.vu.nl/pipermail/cliopatria-list/): in their (incredibly fast) reply they suggested to **load the dataset manually using the server Prolog console**. You'd do that simply by using the rdf\_load command after starting the ClioPatria server (as shown above):

?- rdf\_load('/Users/michele.pasin/Downloads/NPGcitationsGraph/articles.2012-07-16/articles.nq')
|    .
% Parsed "articles.nq" in 1149.71 sec; 0 triples

**That worked**: the dataset was loaded in around 20 mins. Job done!

**However** when I tried to run some queries the application became very slow and ultimately **not responding** (especially with queries like trying to retrieve all named classes from the graph). I tried **restarting the triplestore**, and realised that once you do that, ClioPatria begins by re-loading all repositories previously created - which, in the case of my 40M triples repo, would take around 10-15 minutes.

After restarting the server, queries were a bit faster but in many cases still pretty slowish on my 8G ram laptop.

#### Conclusion:

I am sure there are many more things which could be optimised, however I'm no Prolog expert nor I could figure out where to start just based on the online documentation. So I kind of gave up on using it to work on large datasets on my macbook for now.

On the other hand, I **really liked** ClioPatria's intuitive and simple UI, its ease of installation and the fact you can perform operations transparently and interactively via a Prolog-console (assuming you know how to do that).

All in all, ClioPatria seems to me a really good option if you want to get up and running quickly e.g. in order to prototype linked data applications or explore small to medium-sized RDF datasets (10M triples or so I guess). For bigger datasets, you better [equip your mac](http://mac.appstorm.net/how-to/hardware-how-to/how-and-why-to-upgrade-your-macs-ram/) with a few gigs of extra RAM!

### 5\. Useful resources

**\> Whitepaper with technical analysis**- [http://cliopatria.swi-prolog.org/help/whitepaper.html](http://cliopatria.swi-prolog.org/help/whitepaper.html)

**\> Mailing list**- [http://mailman.few.vu.nl/mailman/listinfo/cliopatria-list](http://mailman.few.vu.nl/mailman/listinfo/cliopatria-list)
