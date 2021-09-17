---
title: "Installing GraphDB (aka OWLIM) triplestore on mac os"
date: "2014-10-16"
categories: 
  - "semantic-web"
  - "techlife"
tags: 
  - "database"
  - "graph"
  - "rdf"
  - "sparql"
  - "triplestore"
---

[GraphDB](http://www.ontotext.com/products/ontotext-graphdb/) (formerly called OWLIM) is an RDF triplestore which is used - among others - by large organisations like the [BBC or the British Museum](http://www.ontotext.com/customers/). I've recently installed the LITE release of this graph database on my mac, so what follows is a simple write up of the steps that worked for me.

Haven't played much with the database yet, but all in all, the installation was much simpler than expected (ps: this old [recipe on google code](https://code.google.com/p/sgvizler/wiki/HowTo_MacOWLIMLiteTomcat7Apache) was very helpful in steering me in the right direction with the whole Tomcat/Java setup).

### 1\. Requirements

**OSX**: Mavericks 10.9.5 **XCode**: latest version [available from Apple](https://developer.apple.com/xcode/downloads/) **HOMEBREW**: ruby -e "$(curl -fsSkL raw.github.com/mxcl/homebrew/go)" **Tomcat7**: brew install tomcat **JAVA**: available [from Apple](http://support.apple.com/kb/dl1572)

Finally - we obviously want to get a copy of **OWLIM-Lite** too: [http://www.ontotext.com/owlim/downloads](http://www.ontotext.com/owlim/downloads)

### 2\. Setting up

After you have downloaded and unpacked the archive, you must simply **copy** these two files: owlim-lite/sesame\_owlim/openrdf-sesame.war owlim-lite/sesame\_owlim/openrdf-workbench.war

..to the Tomcat webapps folder: /usr/local/Cellar/tomcat/7.0.29/libexec/webapps/

Essentially that's because OWLIM-Lite is packaged as a storage and inference layer for the [Sesame RDF framework](http://rdf4j.org/), which runs here as a component within the [Tomcat](http://tomcat.apache.org/) server (note: there are [other ways to run OWLIM](https://confluence.ontotext.com/display/OWLIMv53/OWLIM-Lite+Installation#OWLIM-LiteInstallation-Usefulinformation), but this one seemed the quickest).

### 3\. Starting Tomcat

First I created a symbolic link in my ~/Library folder, so to better manage new versions (as suggested [here](http://wolfpaulus.com/jounal/mac/tomcat7)).

sudo ln -s /usr/local/Cellar/tomcat/7.0.39 ~/Library/Tomcat

Then in order to start/stop Tomcat it's enough to use the catalina command:

\[michele.pasin\]@here:~/Library/Tomcat/bin>./catalina start
Using CATALINA\_BASE:   /usr/local/Cellar/tomcat/7.0.39/libexec
Using CATALINA\_HOME:   /usr/local/Cellar/tomcat/7.0.39/libexec
Using CATALINA\_TMPDIR: /usr/local/Cellar/tomcat/7.0.39/libexec/temp
Using JRE\_HOME:        /System/Library/Java/JavaVirtualMachines/1.6.0.jdk/Contents/Home
Using CLASSPATH:       /usr/local/Cellar/tomcat/7.0.39/libexec/bin/bootstrap.jar:/usr/local/Cellar/tomcat/7.0.39/libexec/bin/tomcat-juli.jar

\[michele.pasin\]@here:~/Library/Tomcat/bin>./catalina stop
Using CATALINA\_BASE:   /usr/local/Cellar/tomcat/7.0.39/libexec
Using CATALINA\_HOME:   /usr/local/Cellar/tomcat/7.0.39/libexec
Using CATALINA\_TMPDIR: /usr/local/Cellar/tomcat/7.0.39/libexec/temp
Using JRE\_HOME:        /System/Library/Java/JavaVirtualMachines/1.6.0.jdk/Contents/Home
Using CLASSPATH:       /usr/local/Cellar/tomcat/7.0.39/libexec/bin/bootstrap.jar:/usr/local/Cellar/tomcat/7.0.39/libexec/bin/tomcat-juli.jar

> Tip: Tomcat runs by default on port 8080. That can be changed pretty easily by modifying a parameter in server.xml in {Tomcat installation folder}/libexec/conf/ more [details here](http://www.mkyong.com/tomcat/how-to-change-tomcat-default-port/).

### 4\. Testing the Graph database

Start a browser and go to the Workbench Web application using a URL of this form: http://localhost:8080/openrdf-workbench/ (substituting localhost and the 8080 port number as appropriate). You should see something like this:

[![SesameWorkbench](/media/static/blog_img/SesameWorkbench.png)](http://www.michelepasin.org/blog/wp-content/uploads/2014/10/SesameWorkbench.png)

After selecting a server, click ‘New repository’.

Select ‘**OWLIM-Lite**’ from the drop-down and enter the repository ID and description. Then click ‘next’.

Fill in the fields as required and click ‘create’.

That's it! A message should be displayed that gives details of the new repository and this should also appear in the repository list (click ‘repositories’ to see this).

### 5\. Loading a big dataset

I've set out to load the [NPG Articles](http://data.nature.com/downloads/2012-07-16/articles.2012-07-16.nq.tar.gz) dataset available at nature.com's legacy linked data site [data.nature.com](http://www.nature.com/developers/documentation/linked-data-platform/releases/snapshot-downloads/).

The dataset contains around **40M triples** describing (at the metadata level) all that's been published by NPG and Scientific American from 1845 till nowadays. The file size is **~6 gigs** so it's not a huge dataset. Still, something big enough to pose a challenge to my macbook pro (8gigs RAM).

First, I **increased the memory** allocated to the Tomcat application to 5G. It was enough to create a setenv.sh file in the ${tomcat-folder}\\bin\\ folder. The file contains this line:

CATALINA\_OPTS="$CATALINA\_OPTS -server -Xms5g -Xmx5g"

> More details on Tomcat's and Java memory issues are [available here](http://www.mkyong.com/tomcat/tomcat-javalangoutofmemoryerror-permgen-space/).

Then I used OWLIM's **web interface** to create a new graph repository and upload the dataset file into it (I previously downloaded a copy of the dataset to my computer so to work with local files only).

It took around 10 minutes for the application to upload the file into the triplestore, and 2-3 minutes for OWLIM to process it. **Much much faster than what I expected**. Only minor issue, the lack of notifications (in the UI) of what was going on. Not a big deal in my case, but with larger dataset uploads it might be a potential downer.

Note: I used the web form to upload the dataset, but there are also [ways to do that from the command line](http://answers.ontotext.com/questions/1045/archive-loading-a-large-triple-store-using-owlim-se) (which will probably result in even faster uploads).

### 6\. Useful information

**\> Sparql endpoints**

All of your repositories come also with a handy SPARQL endpoint, which is available at this url: http://localhost:8080/openrdf-sesame/repositories/test1 (just change the last bit so that it matches your repository name).

**\> Official documentation**- [https://confluence.ontotext.com/display/GraphDB6](https://confluence.ontotext.com/display/GraphDB6/)

**\> Ontotext's Q&A forum**- [http://answers.ontotext.com](http://answers.ontotext.com)
