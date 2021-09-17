---
title: "[coming soon] RDF semantics - genius or madness?"
date: "2013-05-20"
categories: 
  - "informationarchitecture"
  - "semantic-web"
tags: 
  - "logic"
  - "metamodel"
  - "owl"
  - "rdf"
  - "semanticweb"
---

What is rdfs:Class instance of? How come that we normally define and instantiate _rdfs_ classes, but don't do the same with properties too? Fueled by a couple of posts I found online (e.g. see [this thread](http://answers.semanticweb.com/questions/3597/is-the-predicate-in-an-rdf-triple-a-class-or-an-instance) on semantic web overflow ) I decided to take a look at all this in more details.

You may have heard that the semantics of the RDF family of languages was complex.

Well, you don’t really need to understand all the nuances of [RDF semantics](http://www.w3.org/TR/rdf-mt/) if all you want is developing a web-app that consumes or produces [Linked Data](http://en.wikipedia.org/wiki/Linked_data). But there comes a time where you begin questioning the foundations, and you can’t refrain from looking under the carpet to see what is it really that you’ve been walking on all of this time. This is what this post is about..

### Visualizing RDF/OWL metamodel: not even Topbraid's can handle that!

These days I’ve been using Top Braid composer quite a bit, and got to like it too. It has a lot of functionalities, and despite the usual eclipse-based UI I’d say is more user friendly that its competitors. Anyways, once thing you’d note right away when you load up an ontology in Topbraid is the class hierarchy on the left… why so many top level entities? You might expect to see only one, that is, the usual owl:Thing root node or something like that. The answer is, TopBraid gives you immediately a peek into the meta-level model of RDF and OWL.

\-topbraid screenshot-

If you are wondering what a meta model is, here’s a [good summary from Woody Pidcock](http://infogrid.org/wiki/Reference/PidcockArticle):

> A meta-model is an explicit model of the constructs and rules needed to build specific models within a domain of interest. A valid meta-model is an ontology, but not all ontologies are modeled explicitly as meta-models. A meta-model can be viewed from three different perspectives: 1) as a set of building blocks and rules used to build models 2) as a model of a domain of interest, and 3) as an instance of another model.

So the RDF/OWL metamodels are essentially conceptual models that can be instantiated in order to create other, less abstract, models. In other words, they are the representational primitives of the knowledge representation language. Up to this point, it’s all clear. So using TopBraid excellent graphical interface I set out to take a look at the metamodel. Here’s where the difficulties began…

> All things described by RDF are called resources, and are instances of the class rdfs:Resource. This is the class of everything. All other classes are subclasses of this class. rdfs:Resource is an instance of rdfs:Class. \[…\]
> 
> Resources may be divided into groups called classes. The members of a class are known as instances of the class. Classes are themselves resources. They are often identified by RDF URI References and may be described using RDF properties. The rdf:type property may be used to state that a resource is an instance of a class. ([http://www.w3.org/TR/rdf-schema/#ch\_resource](http://www.w3.org/TR/rdf-schema/#ch_resource))

Here’s the schema representing all the major classes. Ps: the arcs with unreadable labels actually say both rdfs:subClassOf and rdf:type (the dataviz algorithm fails, and to be honest, my capacity to grasp the meaning of that modelling decision too).

[![RDF semantics #1](/media/static/blog_img/8444299335_f079204b78_b.jpg)](http://www.flickr.com/photos/mikele/8444299335/sizes/o/in/photostream/ "RDF semantics #1 by MagIcReBirth, on Flickr")

Here’s a modified version of the same diagram, this time including also some properties in the graph:

[![RDF semantics #2](/media/static/blog_img/8452134065_c922480d8b_b.jpg)](http://www.flickr.com/photos/mikele/8452134065/sizes/o/in/photostream/ "RDF semantics #2 by MagIcReBirth, on Flickr")

> This is another nice visual representation of the class system: [http://www.infowebml.ws/website/graphical-representations.htm](http://www.infowebml.ws/website/graphical-representations.htm)

What does all of this mean? I haven’t quite figured it out myself, but I’ll try to point out a couple of key things that derive from this model.

### 1\. Something can be a class and an instance at the same time.

Probably the main tricky point is that something can be at the same time both an instance and a class. This is not too hard to understand, e.g. if you think of the classic example… However if you build a knowledge representation framework that relies on such notions then you might have to work on it a bit more.

> A class may be a member of its own class extension and may be an instance of itself. The group of resources that are RDF Schema classes is itself a class called rdfs:Class. ([http://www.w3.org/TR/rdf-schema/#ch\_class](http://www.w3.org/TR/rdf-schema/#ch_class))

For example, an owl:class is both an instance of rdfs:Class and a subclass of rdfs:Class. In other words, that means that an owl:class is both an individual member of the rdfs:Class set, and a subset of it. Go figure.

[![Owl:class](/media/static/blog_img/8452151273_f0a1d36400.jpg)](http://www.flickr.com/photos/mikele/8452151273/ "Owl:class by MagIcReBirth, on Flickr")

### 2\. Everything is Instance, Hurra!

Another consequence is that whatever you say in Rdf/OWL, it can always be seen as a sequence of instances.

In all of the patterns above, you can say you have triples of instances. Obviously, the instances are defined are different levels of abstraction - still, all instances within the same representation language.

-----------------------------------------
Another way to look at this, is that in RDF the meta-level and the universe of discourse are constantly intertwined. Which is really cool, if you think of the introspection features of RDF. Not that cool though, if you are looking for a crystal clear semantics…
-----------------------------------------

### 3\. Instantiating Classes VS instantiating Properties

rdf:Property is the class of RDF properties. rdf:Property is an instance of rdfs:Class. \[..\] The rdfs:subPropertyOf property may be used to state that one property is a subproperty of another. If a property P is a subproperty of property P', then all pairs of resources which are related by P are also related by P'.

The main consideration here is ..

Usually you instantiate an rdf:Property (or owl:ObjectProperty) and thus doing you create an individual new property (e.g. ‘lives-in’). That can be used to link two other instances. So there is a (confusing) misalignment between
- classes, which are defined by subclassing owl:Thing, or instantiating owl:Class
- instances which are created by instantiating owl:Thing (or one of its subclasses)
- properties (e.g. relations) which are created by instantiating rdf:Property. Note that also rdfs:subClassOf and rdfs:subPropertyOf are instances of rdf:Property

-----------------------------------------

\[REVISE THIS\]

Rdf provides a mechanism for creating hierarchies of classes (rdfs:SubClassOf), which is what you’d do when you create the taxonomical backbone of an ontology. Then these classes get instantiated and usually that’s where the factual knowledge of your application resides.

With relations it’s different: you don’t subclass an rdf:Property (or owl:ObjectProperty), but rather, you instantiate it. And in order to create hierarchies, rdf provides a special property (rdfs:subPropertyOf) that links two instances of properties.

So, while both the rdfs:domain and the rdfs:range of rdfs:subClassOf is rdfs:Class, and is used to state that all the instances of one class are instances of another.
Instead, both the rdfs:domain and the rdfs:range of rdfs:subPropertyOf is rdf:Property.
\[actually it does make sense: the problem is just in the use of it: we don’t instantiate properties…\]

is used to state that all resources related by one property are also related by another.

-----------------------------------------

Entities that represent predicates are considered to be universal - that is, for example, the ‘married-to’ binary relation is always the same for all people that are married. That is to say, you don’t have a new individual instance of the ‘married-to’ relation each time two people get married. (another way to look at this, is that each time two people are marries a new relation does get instantiated, but this relationship has always a single type: ‘married-to’. So we kind of take a shortcut, mention the type and forger the instance. If you used an event-based modelling approach, you can see how all of these relations can be treated at the same level of classes-instances)

Entities that represent unary predicates (or classes) such as ‘red things’ or ‘things that are humans’ are considered to represent sets, whose members are individuals that share a specific feature.

Ps: If you look at rdf metamodel (= the …..) both classes and properties are instances - so when you combine them you can always say that you’re constructing a statement where all three components are instances.

-----------------------------------------

### Conclusions

Genius or madness? Definitely madness I'd say. It feels as if someone wanted to show 

However there's also genius here, in so far as this architecture, despite being so variegated, works. Meaning that you can focus on the abstraction layer you're mostly interested in, and sort of forget the rest. 

It's all in the semantics. 

[![Mallet comic strip on Semantics](/media/static/blog_img/8453239658_1cbbc66e4f_c.jpg)](http://www.flickr.com/photos/mikele/8453239658/ "Mallet comic strip on Semantics by MagIcReBirth, on Flickr")
