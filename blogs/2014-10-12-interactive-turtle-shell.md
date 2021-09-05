---
title: "An interactive Turtle shell"
date: "2014-10-12"
categories: 
  - "informationarchitecture"
  - "semantic-web"
tags: 
  - "rdf"
  - "semanticweb"
  - "turtle"
---

Wouldn't it be nice to have an interactive environment where you quickly hack together an RDF model and then show it to your clients or colleagues in a more accessible format - i.e. a diagram?

Don't know if there's anything like that already, but the other day while polishing up the [OntosPy](https://github.com/lambdamusic/ontosPy) library I've taken a couple of hours of fun-coding and put together a module that lets you do that.

The idea is simple: load an interactive environment where you can quickly **sketch out** a few ideas using the (very readable) [Turtle](http://www.w3.org/TR/turtle/) rdf format.

Then **export it** onto a different representation e.g. a graphical one, so that it can be shown to people. Or just to keep working on it via a medium that offers different [affordances](http://en.wikipedia.org/wiki/Affordance).

So here it is:

\[michele.pasin\]@here:~/code/python>sketch.py 
Good morning. Ready to Turtle away. Type docs() for help.
In \[1\]: docs()

====Sketch v 0.2\====

add()  ==> add statements to the graph
...........SHORTCUTS:
...........'class' = owl:Class
...........'sub' = rdfs:subClassOf
...........TURTLE SYNTAX:  http://www.w3.org/TR/turtle/

show() ==> shows the graph. Can take an OPTIONAL argument for the format.
...........eg one of\['xml', 'n3', 'turtle', 'nt', 'pretty-xml', dot'\]

clear()	 ==> clears the graph
...........all triples are removed

omnigraffle() ==> creates a dot file and opens it with omnigraffle
...........First you must set Omingraffle as your system default app for dot files!

quit() ==> exit

====Have fun!====

In \[2\]: add()
Multi-line input. Enter ### when finished.
:person a class
:mike a :person
:person sub :agent
:organization sub :agent
:worksIn rdfs:domain :person
:worksIn rdfs:range :organization
:mike :worksIn :DamageInc
:DamageInc a :organization

In \[3\]: show()
@prefix : <http://this.sketch#\> .
@prefix bibo: <http://purl.org/ontology/bibo/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix npg: <http://ns.nature.com/terms/> .
@prefix npgg: <http://ns.nature.com/graphs/> .
@prefix npgx: <http://ns.nature.com/extensions/> .
@prefix owl: <http://www.w3.org/2002/07/owl#\> .
@prefix rdf: <http://www.w3.org/1999/02/22\-rdf-syntax-ns#\> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#\> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#\> .
@prefix xml: <http://www.w3.org/XML/1998/namespace\> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#\> .

:mike a :person ;
    :worksIn :DamageInc .

:worksIn rdfs:domain :person ;
    rdfs:range :organization .

:DamageInc a :organization .

:organization rdfs:subClassOf :agent .

:person a owl:Class ;
    rdfs:subClassOf :agent .

In \[4\]: show("xml")
<?xml version="1.0" encoding="UTF-8"?>
<rdf:RDF
   xmlns\="http://this.sketch#"
   xmlns:rdf\="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:rdfs\="http://www.w3.org/2000/01/rdf-schema#"
\>
  <rdf:Description rdf:about\="http://this.sketch#mike"\>
    <rdf:type rdf:resource\="http://this.sketch#person"/>
    <worksIn rdf:resource\="http://this.sketch#DamageInc"/>
  </rdf:Description\>
  <rdf:Description rdf:about\="http://this.sketch#organization"\>
    <rdfs:subClassOf rdf:resource\="http://this.sketch#agent"/>
  </rdf:Description\>
  <rdf:Description rdf:about\="http://this.sketch#DamageInc"\>
    <rdf:type rdf:resource\="http://this.sketch#organization"/>
  </rdf:Description\>
  <rdf:Description rdf:about\="http://this.sketch#person"\>
    <rdf:type rdf:resource\="http://www.w3.org/2002/07/owl#Class"/>
    <rdfs:subClassOf rdf:resource\="http://this.sketch#agent"/>
  </rdf:Description\>
  <rdf:Description rdf:about\="http://this.sketch#worksIn"\>
    <rdfs:domain rdf:resource\="http://this.sketch#person"/>
    <rdfs:range rdf:resource\="http://this.sketch#organization"/>
  </rdf:Description\>
</rdf:RDF\>

In \[5\]: omnigraffle()
### saves a dot file and tries to open it with your default editor
### if you're on a mac and have omnigraffle - that could be the one!

In \[6\]: quit()

If you are mac based and you have [associated](http://www.dummies.com/how-to/content/how-to-assign-a-file-type-to-an-application-in-mac.html) .dot files to the excellent [Omnigraffle](https://www.omnigroup.com/omnigraffle) app, you'd see something like this:

[![Sketch Screen Shot 2014 10 12 at 10 12 48](/media/static/blog_img/sketch_Screen-Shot-2014-10-12-at-10.12.48.png)](http://www.michelepasin.org/blog/wp-content/uploads/2014/10/sketch_Screen-Shot-2014-10-12-at-10.12.48.png)

[![Sketch Screen Shot 2014 10 12 at 10 13 32](/media/static/blog_img/sketch_Screen-Shot-2014-10-12-at-10.13.32.png)](http://www.michelepasin.org/blog/wp-content/uploads/2014/10/sketch_Screen-Shot-2014-10-12-at-10.13.32.png)

**That speeded up my work quite a bit** - especially in situations where you don't mind about precision but are more interested in quickly showing the merits of a modelling approach.

Any comments or ideas on how to develop this further?
