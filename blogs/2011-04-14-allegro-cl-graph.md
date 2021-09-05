---
title: "RDF programming with AllegroCL and AllegroGraph"
date: "2011-04-14"
categories: 
  - "semantic-web"
  - "techlife"
tags: 
  - "ide"
  - "lisp"
  - "triplestore"
---

Allegro Common Lisp ([wikipedia](http://en.wikipedia.org/wiki/Allegro_Common_Lisp)) is a commercial implementation of the [Common Lisp](http://en.wikipedia.org/wiki/Common_Lisp) programming language developed by [Franz Inc](http://www.franz.com/). Allegro CL provides the full ANSI Common Lisp standard - but more interestingly for me, it also provides a very comprehensive suite of tools for semantic web programming. So I decided to give it a go, in what follows I just put together some notes on how to get started quickly.

Franz Inc. offers a whole bunch of semantic technologies, including:

- **AllegroCL**: a Common **Lisp implementation** ([homepage](http://www.franz.com/products/allegro-common-lisp/) | [install](http://www.franz.com/downloads/clp/validate_survey) | [faq](http://www.franz.com/support/faq//) | [documentation](http://www.franz.com/support/documentation/8.2/doc/introduction.htm)) described as the "_most powerful dynamic object-oriented development system available today_". It runs on all major operating systems, and it includes a cross-platform GUI too (which is not always the case for Lisp implementations!).

- **AllegroGraph**: ([home](http://www.franz.com/agraph/allegrograph/) | [docs](http://www.franz.com/agraph/support/documentation/v4/agraph-introduction.html) | [install](http://www.franz.com/agraph/downloads/)) this is a high-performance, persistent RDF **triplestore**. It allegedly can "_scale to billions of triples while maintaining superior performance_" and supports SPARQL, RDFS++, and Prolog reasoning from numerous client applications (python too, as discussed in a [previous post](http://www.michelepasin.org/blog/2011/02/24/survey-of-pythonic-tools-for-rdf-and-linked-data-programming/)).

- **AllegroCache**: ([home](http://www.franz.com/products/allegrocache/) | [docs](http://www.franz.com/products/allegrocache/acache_docs.lhtml) | [install](http://www.franz.com/products/allegrocache/download/dist/download)) this is a dynamic object caching **database** system. It allows programmers to work directly with objects as if they were in memory while in fact the object data is always stored persistently. It supports a full transaction model with long and short transactions, and meets the classic ACID requirements for a reliable and robust database.

- **Gruff**: ([home](http://www.franz.com/agraph/gruff/) | [docs](http://www.franz.com/agraph/gruff/gruff_documentation.html) | [install](http://www.franz.com/agraph/gruff/index.lhtml#download)) is an rdf **graphical browser** that attempts to make data retrieval more pleasant and powerful with a variety of tools for laying out cyclical graphs, displaying tables of properties, managing queries, and building queries as visual diagrams (btw thanks to [Matteo](http://twitter.com/mr56k) for mentioning Gruff to me!)

### Installing AllegroCL

The **good news** is that if you follow the installation instructions for AllegroCL, this will include also AllegroGraph and AllegroCache. Long story short, I was able to get started with this environment _surprisingly_ quickly. The [installation](http://www.franz.com/downloads/clp/validate_survey) on OSX involves only two steps (after filling out a form): getting the GTK+ framework (a [cross-platform graphical toolkit](http://en.wikipedia.org/wiki/GTK%2B)) and then downloading the Lisp image. Double-click, install, and et-voila' you're done with it.

Here's how the Lisp IDE looks like:

[![Screen shot 2011 04 14 at 13 46 49](/media/static/blog_img/Screen-shot-2011-04-14-at-13.46.491.png)](http://www.michelepasin.org/blog/wp-content/uploads/2011/04/Screen-shot-2011-04-14-at-13.46.491.png)

The IDE includes also an integrated patches-loading tool, which you should run straightaway to get the latest versions of several libraries needed by AllegroCL (wonder whether it's _that_ easy to install all the standard Lisp packages too..):

[![Screen shot 2011 04 14 at 13 31 43](/media/static/blog_img/Screen-shot-2011-04-14-at-13.31.431.png)](http://www.michelepasin.org/blog/wp-content/uploads/2011/04/Screen-shot-2011-04-14-at-13.31.431.png)

Finally, in order to run AllegroGraph too it's necessary to invoke an update command manually, which is easily done:

CG-USER(3): (SYSTEM.UPDATE:INSTALL-ALLEGROGRAPH)
Checking available AllegroGraph versions...
Making temporary directory (/tmp/tempa18825120705a/)
Retrieving agraph-3.3\-acl8.2\-macosx86.tgz into temporary directory
Extracting tar archive /tmp/tempa18825120705a/agraph-3.3\-acl8.2\-macosx86.tgz
Installing /Applications/AllegroCL/code/agraph.fasl
Installing /Applications/AllegroCL/agraph/

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

To use the newly downloaded AllegroGraph you can load it by
evaluating the following forms:

  (REQUIRE :AGRAPH)

Ancillary files are located in \`\`/Applications//AllegroCL/agraph/''.

### Installing Gruff

I also downloaded [Gruff](http://www.franz.com/agraph/gruff/) and ran it. Again, on OSx the whole process was very very straightforward. I loaded up an ontology stored in an RDF/XML file and here's the result:

[![Screen shot 2011 04 14 at 14 18 56](/media/static/blog_img/Screen-shot-2011-04-14-at-14.18.561.png)](http://www.michelepasin.org/blog/wp-content/uploads/2011/04/Screen-shot-2011-04-14-at-14.18.561.png)

Very very impressive - that's my conclusion. [Gruff](http://www.franz.com/agraph/gruff/) offers plenty of features for viewing and also editing the rdf graph (check out the [video tutorials on the homepage](http://www.franz.com/agraph/gruff/index.lhtml#download)); with a little practice, I think it wouldn't be that difficult to use it for creating rdf models by hand (eg as an alternative to tools like Protege). The main advantage in my view is that it's highly interactive: being able to switch very quickly from a graph-view to a tabular one is extremely practical when inspecting or creating an rdf model.

### Time to write some code

Haven't been writing Lisp in a while, but since we've got till here it would be a shame not to get our hands dirty a little, right?

- **Tip**: a nice folk named [Mark Watson](http://www.markwatson.com/) has written a couple of books that show how to use Allegro Graph, and he's making them available for free on his website (thanks!). Check them out: [Practical Semantic Web and Linked Data Applications, Common Lisp Edition](http://www.markwatson.com/opencontent/book_lisp.pdf), and [Practical Semantic Web and Linked Data Applications, Java, Scala, Clojure, and JRuby Edition](http://www.markwatson.com/opencontent/book_java.pdf)

I had a quick look at the first book mentioned ("_Practical Semantic Web and Linked Data Applications, Common Lisp Edition_"), and tried to follow the examples presented. Here's the result..

First, let's load up AllegroGraph from AllegroCL and set up a Lisp reader macro (named '!') that makes it easier to enter URIs and literals:

CG-USER(2): (REQUIRE :AGRAPH)
; Fast loading /Applications/AllegroCL/code/AGRAPH.fasl
;   Fast loading
;      /Applications/AllegroCL/code/acache-2.1.12.fasl
AllegroCache version 2.1.12
;     Fast loading /Applications/AllegroCL/code/SAX.001
;;; Installing sax patch, version 1.
;       Fast loading from bundle code/ef-e-anynl.fasl.
;         Fast loading from bundle code/ef-e-crlf.fasl.
;         Fast loading from bundle code/ef-e-cr.fasl.
;   Fast loading from bundle code/streamp.fasl.
;   Fast loading /Applications/AllegroCL/code/ACLRPC.fasl
Loaded patch file /Applications/AllegroCL/update/pim001.001.
;   Fast loading /Applications/AllegroCL/code/PROLOG.001
;;; Installing prolog patch, version 1.
;   Fast loading /Applications/AllegroCL/code/DATETIME.001
;;; Installing datetime patch, version 1.
;   Fast loading /Applications/AllegroCL/code/streamc.002
;;; Installing streamc patch, version 2.
;     Fast loading from bundle code/efft-utf8-base.fasl.
;     Fast loading from bundle code/efft-void.fasl.
;     Fast loading from bundle code/efft-latin1-base.fasl.
;   Fast loading from bundle code/streamm.fasl.
;   Fast loading from bundle code/ef-e-crcrlf.fasl.
Loaded patch file /Applications/AllegroCL/update/agraph/3.3/pio001.001.
Loaded patch file /Applications/AllegroCL/update/agraph/3.3/pio002.001.
Loaded patch file /Applications/AllegroCL/update/agraph/3.3/pio003.001.
Loaded patch file /Applications/AllegroCL/update/agraph/3.3/pio004.001.
Loaded patch file /Applications/AllegroCL/update/agraph/3.3/pio005.001.
Loaded patch file /Applications/AllegroCL/update/agraph/3.3/pio006.001.
Loaded patch file /Applications/AllegroCL/update/agraph/3.3/pio007.001.
Loaded patch file /Applications/AllegroCL/update/agraph/3.3/pio008.001.
Loaded patch file /Applications/AllegroCL/update/agraph/3.3/pio009.001.
Loaded patch file /Applications/AllegroCL/update/agraph/3.3/pio010.001.
Loaded patch file /Applications/AllegroCL/update/agraph/3.3/pio011.001.
Loaded patch file /Applications/AllegroCL/update/agraph/3.3/pio012.001.
Loaded patch file /Applications/AllegroCL/update/agraph/3.3/pio013.001.
Loaded patch file /Applications/AllegroCL/update/agraph/3.3/pio014.001.
Loaded patch file /Applications/AllegroCL/update/agraph/3.3/pio015.001.
Loaded patch file /Applications/AllegroCL/update/agraph/3.3/pio016.001.
Loaded patch file /Applications/AllegroCL/update/agraph/3.3/pio017.001.
Loaded patch file /Applications/AllegroCL/update/agraph/3.3/pio018.001.
Loaded patch file /Applications/AllegroCL/update/agraph/3.3/pio019.001.
AllegroGraph Lisp Edition 3.3 \[built on February 17, 2010 13:53:35 GMT-0800\]
Copyright (c) 2005\-2010 Franz Inc.  All Rights Reserved.
AllegroGraph contains patent-pending technology.
With patches: io001, io002, io003, io004, io005, io996, io007, io008, io009, io010, io011, io012, io013, io014, io015, io016, io017, io018, io019.
T
CG-USER(3): (in-package :db.agraph.user)
#<The DB.AGRAPH.USER package\>
TRIPLE-STORE-USER(4): (enable-!-reader)
#<Function READ-TOKEN\>
T
TRIPLE-STORE-USER(5): (enable-print-decoded t)
T
TRIPLE-STORE-USER(6): (triple-store:display-namespaces)
rdfs \=\> http://www.w3.org/2000/01/rdf-schema#
err \=\> http://www.w3.org/2005/xqt-errors#
fn \=\> http://www.w3.org/2005/xpath-functions#
rdf \=\> http://www.w3.org/1999/02/22\-rdf-syntax-ns#
xs \=\> http://www.w3.org/2001/XMLSchema#
xsd \=\> http://www.w3.org/2001/XMLSchema#
owl \=\> http://www.w3.org/2002/07/owl#
TRIPLE-STORE-USER(9): !rdfs:class
!rdfs:class

Next thing, we want to **create a local triplestore**, **register** a dummy **namespace** and **add** a couple of **triples** to it. Finally, we **dump** the whole triplestore in a **file**.

TRIPLE-STORE-USER(10): (triple-store:create-triple-store "~/tmp/rdfstore\_1")
#<DB.AGRAPH::TRIPLE-DB /Users/mac/tmp/rdfstore\_1, open @ #x21dfc80a\>
TRIPLE-STORE-USER(11): (register-namespace "kb" "http://michelepasin.org/rdfs#")
"http://michelepasin.org/rdfs#"
TRIPLE-STORE-USER(12): (triple-store:display-namespaces)
rdfs \=\> http://www.w3.org/2000/01/rdf-schema#
err \=\> http://www.w3.org/2005/xqt-errors#
fn \=\> http://www.w3.org/2005/xpath-functions#
rdf \=\> http://www.w3.org/1999/02/22\-rdf-syntax-ns#
xs \=\> http://www.w3.org/2001/XMLSchema#
xsd \=\> http://www.w3.org/2001/XMLSchema#
owl \=\> http://www.w3.org/2002/07/owl#
kb \=\> http://michelepasin.org/rdfs#
TRIPLE-STORE-USER(13): (defvar \*doc1\* (resource "http://www.michelepasin.org/research/"))
\*DOC1\*
TRIPLE-STORE-USER(14): \*doc1\*
!<http://www.michelepasin.org/research/\>
TRIPLE-STORE-USER(15): (triple-store:add-triple \*doc1\* !rdf:type !kb:article)
1
TRIPLE-STORE-USER(16): (triple-store:add-triple \*doc1\* !rdf:comment !"what a wonderful book")
2
TRIPLE-STORE-USER(17): (triple-store:get-triples-list)
(< type article\> < comment what a wonderful book\>)
NIL
TRIPLE-STORE-USER(18): (print-triples (triple-store:get-triples-list))
<http://www.michelepasin.org/research/\> <http://www.w3.org/1999/02/22\-rdf-syntax-ns#type\> <http://michelepasin.org/rdfs#article\> .
<http://www.michelepasin.org/research/\> <http://www.w3.org/1999/02/22\-rdf-syntax-ns#comment\> "what a wonderful book" .
TRIPLE-STORE-USER(19): (with-open-file (output "~/tmp/testoutput" :direction :output :if-does-not-exist :create)
(print-triples (triple-store:get-triples-list) :stream output :format :ntriple))

If we open the contents of the newly created "~/tmp/testoutput" file, here's what we would find:

<http://www.michelepasin.org/research/\>
    <http://www.w3.org/1999/02/22\-rdf\-syntax\-ns#type> 
        <http://michelepasin.org/rdfs#article> .
<http://www.michelepasin.org/research/\>
    <http://www.w3.org/1999/02/22\-rdf\-syntax\-ns#comment> 
        "what a wonderful book" .

Finally, let's use [SPARQL](http://www.xml.com/pub/a/2005/11/16/introducing-sparql-querying-semantic-web-tutorial.html?page=1) to launch a (quite dumb) query that retrieves all triples from the triplestore :

TRIPLE-STORE-USER(53): (sparql:run-sparql 
 " PREFIX kb: <http://www.michelepasin.org/research#\> 
   SELECT ?article\_uri ?pred ?obj WHERE {
   ?article\_uri ?pred ?obj . 
   }"
 )
<?xml version\="1.0"?\>
<!\-- Generated by AllegroGraph 3.3 --\>
<sparql xmlns\="http://www.w3.org/2005/sparql-results#"\>
  <head\>
    <variable name\="article\_uri"/\>
    <variable name\="pred"/\>
    <variable name\="obj"/\>
  </head\>
  <results\>
    <result\>
      <binding name\="article\_uri"\>
        <uri\>http://www.michelepasin.org/research/</uri\>
      </binding\>
      <binding name\="pred"\>
        <uri\>http://www.w3.org/1999/02/22\-rdf-syntax-ns#type</uri\>
      </binding\>
      <binding name\="obj"\>
        <uri\>http://michelepasin.org/rdfs#article</uri\>
      </binding\>
    </result\>
    <result\>
      <binding name\="article\_uri"\>
        <uri\>http://www.michelepasin.org/research/</uri\>
      </binding\>
      <binding name\="pred"\>
        <uri\>http://www.w3.org/1999/02/22\-rdf-syntax-ns#comment</uri\>
      </binding\>
      <binding name\="obj"\>
        <literal\>what a wonderful book</literal\>
      </binding\>
    </result\>
  </results\>
</sparql\>
T
:SELECT
(|?article\_uri| |?pred| |?obj|)
TRIPLE-STORE-USER(54):

That's all for now; this is enough to get started with Allegro-CL and the semantic web programming libraries it contains.

Mind that I've only scratched the surface here, there's **lots and lots more** that can be done with this environment. If you want to explore these topics further make sure you have a look at [Watson's book](http://www.markwatson.com/opencontent/book_lisp.pdf), 'cause that's a great (and free) resource, really!
