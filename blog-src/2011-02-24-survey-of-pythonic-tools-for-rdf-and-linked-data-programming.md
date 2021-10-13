---
title: "Survey of Pythonic tools for RDF and Linked Data programming"
date: "2011-02-24"
categories: 
  - "semantic-web"
  - "techlife"
tags: 
  - "linkeddata"
  - "python"
  - "rdf"
  - "rdflib"
  - "semanticweb"
---

The [Resource Description Framework](http://en.wikipedia.org/wiki/Resource_Description_Framework) (RDF) is a data model and language which is quickly gaining momentum in the open-data and data-integration worlds. In this post I'm reporting on a recent survey I made in the context of a [Linked Data](http://en.wikipedia.org/wiki/Linked_Data) project I'm working on, [SAILS](http://sailsproject.cerch.kcl.ac.uk/).  In SAILS we're developing a prototype for RDF-data manipulation and querying, but since the final application will be written in Python and Django, in what follows I tried to gather information about all the existing libraries and frameworks for doing RDF-programming using python.

## 1\. Python libraries for working with Rdf

### RdfLib [http://www.rdflib.net/](http://www.rdflib.net/)

RdfLib ([download](http://www.rdflib.net/rdflib-3.0.0.tar.gz)) is a pretty solid and extensive rdf-programming kit for python. It contains parsers and serializers for RDF/XML, N3, NTriples, Turtle, TriX and RDFa. The library presents a Graph interface which can be backed by any one of a number of store implementations, including, memory, MySQL, Redland, SQLite, Sleepycat, ZODB and SQLObject.

The latest release is **RdfLib 3.0**, although I have the feeling that many are still using the previous release, **2.4**. One big difference between the two is that in 3.0 some libraries have been separated into another package (called [rdfextras](http://code.google.com/p/rdfextras/)); among these libraries there's also the one you need for processing [sparql](http://en.wikipedia.org/wiki/SPARQL) queries (the rdf query language), so it's likely that you want to install that too. A short overview of the difference between these two recent releases of RdfLib can be found [here](http://code.google.com/p/rdflib/wiki/UpgradingToVersion3). The APIs documentation for RdfLib 2.4 is available [here](http://www.rdflib.net/rdflib-2.4.0/html/index.html), while the one for RdfLib 3.0 can be found [here](http://code.alcidesfonseca.com/docs/rdflib/index.html). Finally, there are also some other (a bit older, but possibly useful) docs on the [wiki](http://code.google.com/p/rdflib/w/list).

Next thing, you might want to check out these tutorials:

- [Getting data from the Semantic Web](http://semanticweb.org/wiki/Getting_data_from_the_Semantic_Web.html): a nice example of how to use RdfLib and python in order to get data from [DBPedia](http://dbpedia.org/), the Semantic Web version of Wikipedia.
- [How can I use the Ordnance Survey Linked Data](http://johngoodwin225.wordpress.com/2011/01/18/how-can-i-use-the-ordnance-survey-linked-data-a-python-rdflib-example/): shows how to install RdfLib and query the linked data offered by [Ordnance Survey](http://blog.ordnancesurvey.co.uk/2011/01/how-linked-data-can-reap-benefits/).
- [A quick and dirty guide to YOUR first time with RDF](http://gromgull.net/blog/2011/01/a-quick-and-dirty-guide-to-your-first-time-with-rdf/): another example of querying Uk government data found on [data.gov.uk](http://data.gov.uk/) using RdfLib and Berkely/Sleepycat DB.

### RdfAlchemy [http://www.openvest.com/trac/wiki/RDFAlchemy](http://www.openvest.com/trac/wiki/RDFAlchemy)

The goal of RDFAlchemy ([install](http://www.openvest.com/trac/wiki/RDFAlchemy#Installation) | [apidocs](http://www.openvest.com/public/docs/rdfalchemy/api/) | [usergroup](http://groups.google.com/group/rdfalchemy-dev)) is to allow anyone who uses python to have a object type API access to an RDF Triplestore. In a nutshell, the same way that [SQLAlchemy](http://www.sqlalchemy.org/) is an ORM (Object Relational Mapper) for relational database users, RDFAlchemy is an ORM (Object RDF Mapper) for semantic web users.

RdfAlchemy can also work in conjunction with other datastores, including rdflib, Sesame, and Jena. Support for SPARQL is present, although it seems less stable than the rest of the library.

### Fuxi [http://code.google.com/p/fuxi/](http://code.google.com/p/fuxi/)

FuXi is a Python-based, bi-directional logical reasoning system for the semantic web. It **requires** rdflib 2.4.1 or 2.4.2 and it is **not** compatible with rdflib 3. FuXi aims to be the 'engine for contemporary expert systems based on the Semantic Web technologies'. The documentation can be found [here](http://fuxi.googlecode.com/hg/documentation/html/index.html); it might be useful also to look at the [user-manual](http://code.google.com/p/fuxi/wiki/FuXiUserManual) and the [discussion group](http://groups.google.com/group/fuxi-discussion).

In general, it looks as if Fuxi can offer a complete solution for knowledge representation and reasoning over the semantic web; it is quite sophisticated and well documented (partly via several academic articles). The downside is that to the end of hacking together a linked data application.. well Fuxi is probably just too complex and difficult to learn.

- [About Inferencing](http://blog.okfn.org/2010/08/02/about-inferencing/): a very short introduction to what Fuxi inferencing capabilities can do in the context of an rdf application.

### ORDF [ordf.org](http://ordf.org/)

ORDF ([download](http://packages.python.org/ordf/administration.html#installation) | [docs](http://packages.python.org/ordf/index.html)) is the [Open Knowledge Foundation](http://okfn.org/)‘s library of support infrastructure for RDF. It is **based** on RDFLib and contains an object-description mapper, support for multiple back-end indices, message passing, revision history and provenance, a namespace library and a variety of helper functions and modules to ease integration with the [Pylons](http://pylonshq.com/) framework.

The current version of this library is 0.35. You can have a peek at some of its key functionalities by checking out the '[Object Description Mapper](http://packages.python.org/ordf/odm.html)' - an equivalent to what an Object-Relational Mapper would give you in the context of a relational database. The library seems to be pretty solid; for an example of a system built on top of ORDF you can see [Bibliographica](http://bibliographica.org/), an online open catalogue of cultural works.

- Why using RDF? The [Design Considerations](http://packages.python.org/ordf/design_considerations.html) section in the ORDF documentation discusses the reasons that led to the development of this library in a clear and practical fashion.

### Django-rdf [http://code.google.com/p/django-rdf/](http://code.google.com/p/django-rdf/)

Django-RDF ([download](http://code.google.com/p/django-rdf/downloads/list) | [faq](http://code.google.com/p/django-rdf/wiki/FAQ) | [discussiongroup](http://groups.google.com/group/django-rdf)) is an RDF engine implemented in a generic, reusable [Django](http://www.djangoproject.com/) app, providing complete RDF support to Django projects without requiring any modifications to existing framework or app source code. The philosophy is simple: do your web development using Django just like you're used to, then turn the knob and - with no additional effort - expose your project on the semantic web.

Django-RDF can expose models from any other app as RDF data. This makes it easy to write new views that return RDF/XML data, and/or query existing models in terms of RDFS or OWL classes and properties using (a variant of) the SPARQL query language. SPARQL in, RDF/XML out - two basic semantic web necessities. Django-RDF also implements an RDF store using its internal models such as Concept, Predicate, Resource, Statement, Literal, Ontology, Namespace, etc. The SPARQL query engine returns query sets that can freely mix data in the RDF store with data from existing Django models.

The major **downside** of this library is that it doesn't seem to be maintained anymore; the last release is from 2008, and there seem to be various conflicts with recent versions of Django. A real shame!

### Djubby [http://code.google.com/p/djubby/](http://code.google.com/p/djubby/)

Djubby ([download](http://code.google.com/p/djubby/downloads/list) | [docs](http://code.google.com/p/djubby/wiki/GettingStarted)) is a Linked Data frontend for SPARQL endpoints for the [Django](http://www.djangoproject.com/) Web framework, adding a Linked Data interface to any existing SPARQL-capable triple stores.

Djubby is quite inspired by Richard Cyganiak's [Pubby](http://www4.wiwiss.fu-berlin.de/pubby/) (written in Java): it provides a Linked Data interface to local or remote SPARQL protocol servers, it provides dereferenceable URIs by rewriting URIs found in the SPARQL-exposed dataset into the djubby server's namespace, and it provides a simple HTML interface showing the data available about each resource, taking care of handling 303 redirects and content negotiation.

### Redland [http://librdf.org/](http://librdf.org/)

Redland ([download](http://download.librdf.org/) | [docs](http://librdf.org/docs/) | [discussiongroup](http://lists.usefulinc.com/pipermail/redland-dev/)) is an RDF library written in C and including several high-level language APIs providing RDF manipulation and storage. Redland makes available also a Python interface ([intro](http://librdf.org/docs/python.html) | [apidocs](http://librdf.org/docs/pydoc/RDF.html)) that can be used to manipulate RDF triples.

This library seems to be quite complete and is actively maintained; only potential downside is the installation process. In order to use the python bindings you need to install the C library too (which in turns depends on other C libraries), so (depending on your programming experience and operating system used) just getting up and running might become a challenge.

### SuRF [http://packages.python.org/SuRF/](http://packages.python.org/SuRF/)

SuRF ([install](http://packages.python.org/SuRF/install.html#installing-rdflib) | [docs](http://packages.python.org/SuRF/#documentation)) is an Object - RDF Mapper based on the RDFLIB python library. It exposes the RDF triple sets as sets of resources and seamlessly integrates them into the Object Oriented paradigm of python in a similar manner as ActiveRDF does for ruby.

### Other smaller (but possibly useful) python libraries for rdf:

- [Sparql Interface to python](http://ivan-herman.name/2007/07/06/sparql-endpoint-interface-to-python/): a minimalistic solution for querying sparql endpoints using python ([download](http://www.ivan-herman.net/Misc/PythonStuff/SPARQL/) | [apidocs](http://www.ivan-herman.net/Misc/PythonStuff/SPARQL/Doc-SPARQL/)). _UPDATE: Ivan Herman pointed out that this library has been discontinued and merged with the 'SPARQL Endpoint interface to Python' below._
- [SPARQL Endpoint interface to Python](http://sparql-wrapper.sourceforge.net/) another little utility for talking to a SPARQL endpoint, including having select-results mapped to rdflib terms or returned in JSON format ([download](http://sourceforge.net/projects/sparql-wrapper/))
- [PySparql](http://code.google.com/p/pysparql/source/browse/trunk/src/sparql.py): again, a minimal library that does SELECT and ASK queries on an endpoint which implements the HTTP (GET or POST) bindings of the SPARQL Protocol ([code page](http://code.google.com/p/pysparql/source/browse/trunk/src/sparql.py))
- [Sparta](https://github.com/mnot/sparta/): Sparts is a simple, resource-centric API for RDF graphs, built on top of RDFLIB.
- [Oort](http://oort.to/): another Python toolkit for accessing RDF graphs as plain objects, based on RDFLIB. The project homepage hasn't been updated for a while, although there is trace of recent activity on its [google project](http://code.google.com/p/oort/) page.

  
   

## 2\. RDF Triplestores that are python-friendly

An important component of a linked-data application is the [triplestore](http://en.wikipedia.org/wiki/Triplestore) (that is, an RDF database): many commercial and non-commercial triplestores are available, but only a few offer out-of-the-box python interfaces. Here's a list of them:

### Allegro Graph [http://www.franz.com/agraph/allegrograph/](http://www.franz.com/agraph/allegrograph/)

[AllegroGraph](http://www.franz.com/agraph/allegrograph/) RDFStore is a high-performance, persistent RDF graph database. AllegroGraph uses disk-based storage, enabling it to scale to billions of triples while maintaining superior performance. Unfortunately, the official version of AllegroGraph is not free, but it is possible to get a [free version](http://www.franz.com/agraph/allegrograph/ag_commercial_edition.lhtml) of it (it limits the DB to 50 million triples, so although useful for testing or development it doesn't seem a good solution for a production environment).

The Allegro Graph Python API ([download](http://www.franz.com/agraph/allegrograph/clients.lhtml) | [docs](http://www.franz.com/agraph/support/documentation/current/python-tutorial/python-tutorial-40.html) | [reference](http://www.franz.com/agraph/support/documentation/v4/python-tutorial/python-API-40.html)) offers convenient and efficient access to an [AllegroGraph](http://www.franz.com/agraph/allegrograph/) server from a Python-based application. This API provides methods for creating, querying and maintaining RDF data, and for managing the stored triples.

- A hands-on overview of what's like to work with AllegroGraph and python can be found here: [Getting started with AllegroGraph](http://www.snee.com/bobdc.blog/2009/04/getting-started-with-allegrogr.html).

### Open Link Virtuoso [http://virtuoso.openlinksw.com/](http://virtuoso.openlinksw.com/)

[Virtuoso Universal Server](http://en.wikipedia.org/wiki/Virtuoso_Universal_Server) is a middleware and database engine hybrid that combines the functionality of a traditional RDBMS, ORDBMS, virtual database, RDF, XML, free-text, web application server and file server functionality in a single system. Rather than have dedicated servers for each of the aforementioned functionality realms, Virtuoso is a "universal server"; it enables a single multithreaded server process that implements multiple protocols. The open source edition of Virtuoso Universal Server is also known as [OpenLink Virtuoso](http://virtuoso.openlinksw.com/dataspace/dav/wiki/Main/VOSIntro).

[Virtuoso from Python](http://packages.python.org/virtuoso/) is intended to be a collection of modules for interacting with OpenLink Virtuoso from python. The goal is to provide drivers for \`SQLAlchemy\` and \`RDFLib\`. The package is installable from the [Python Package Index](http://pypi.python.org/pypi/virtuoso) and source code for development is available in a mercurial repository on [BitBucket](http://bitbucket.org/ww/virtuoso).

- A possibly useful example of using Virtuoso from python: [SPARQL Guide for Python Developer](http://www.openlinksw.com/dataspace/kidehen@openlinksw.com/weblog/kidehen@openlinksw.com%27s%20BLOG%20%5B127%5D/1651).

### Sesame [http://www.openrdf.org/](http://www.openrdf.org/)

[Sesame](http://en.wikipedia.org/wiki/Sesame_(framework)) is an open-source framework for querying and analyzing RDF data ([download](http://www.openrdf.org/download.jsp) | [documentation](http://www.openrdf.org/documentation.jsp)). Sesame supports two query languages: SeRQL and Sparql. Sesame's API differs from comparable solutions in that it offers a (stackable) interface through wich functionality can be added, and the storage engine is abstracted from the query interface (many other Triplestores can in fact be used through the Sesame API).

It looks as if the best way to interact with Sesame is by using Java; however there is also a pythonic API called [pySesame](http://pysesame.projects.semwebcentral.org/). This is essentially a python wrapper for Sesame's REST HTTP API, so the range of operations supported (Log in, Log out, Request a list of available repositories, Evaluate a SeRQL-select, RQL or RDQL query, Extract/upload/remove RDF from a repository) are somehow limited (for example, there does not seem to be any native SPARQL support).

- A nice introduction to using Sesame with Python (without pySesame though) can be found in this article: [Getting Started with RDF and SPARQL Using Sesame and Python](http://www.jenitennison.com/blog/node/153).

### Talis platform [http://www.talis.com/platform/](http://www.talis.com/platform/)

The Talis Platform ([faq](http://docs.api.talis.com/getting-started/platform-faq#TOC-What-is-the-Talis-Platform-) | [docs](http://docs.api.talis.com/))is an environment for building next generation applications and services based on Semantic Web technologies. It is a **hosted** system which provides an efficient, robust storage infrastructure. Both arbitrary documents and RDF-based semantic content are supported, with sophisticated query, indexing and search features. Data uploaded on the Talis platform are organized into stores: a **store** is a grouping of related data and metadata. For convenience each store is assigned one or more owners who are the people who have rights to configure the access controls over that data and metadata. Each store provides a uniform REST interface to the data and metadata it manages.

Stores don't come free of charge, but through the [Talis Connected Commons scheme](http://www.talis.com/platform/cc/) it is possible have quite large amounts of store space for free. The scheme is intended to support a wide range of different forms of data publishing. For example scientific researchers seeking to share their research data; dissemination of public domain data from a variety of different charitable, public sector or volunteer organizations; open data enthusiasts compiling data sets to be shared with the web community.

Good news for pythonistas too: [pynappl](http://code.google.com/p/pynappl/) is a simple client library for the Talis Platform. It relies on [rdflib 3.0](http://code.google.com/p/rdflib/) and draws inspiration from other similar client libraries. Currently it is focussed mainly on managing data loading and manipulation of Talis Platform stores ([this blog post](http://blogs.talis.com/n2/archives/887) says more about it).

- Before trying out the Talis platform you might find useful this blog post: [Publishing Linked Data on the Talis Platform](http://www.jenitennison.com/blog/node/109).

### 4store [http://4store.org/](http://4store.org/)

4store ([download](http://4store.org/trac/wiki/Download) | [features](http://4store.org/about) | [docs](http://4store.org/trac/wiki/Documentation)) is a database storage and query engine that holds RDF data. It has been used by [Garlik](http://www.garlik.com/) as their primary RDF platform for three years, and has proved itself to be robust and secure. 4store's main strengths are its performance, scalability and stability. It does not provide many features over and above RDF storage and SPARQL queries, but if your are looking for a scalable, secure, fast and efficient RDF store, then 4store should be on your shortlist.

4store offers a number of [client libraries](http://4store.org/trac/wiki/ClientLibraries), among them there are two for python: first, [HTTP4Store](http://pypi.python.org/pypi/HTTP4Store/0.2) is a client for the 4Store httpd service - allowing for easy handling of sparql results, and adding, appending and deleting graphs. Second, [py4s](https://github.com/wwaites/py4s), although this seems to be a much more experimental library (geared towards multi process queries). Furthemore, there is also an application for the Django web framework called [django-4store](https://github.com/66laps/django-4store#readme) that makes it easier to query and load rdf data into 4store when running Django. The application offers some support for constructing sparql-based Django [views](https://github.com/66laps/django-4store/blob/master/src/fourstore/views.py).

- This blog post shows how to install 4store: [Getting Started with RDF and SPARQL Using 4store and RDF.rb](http://www.jenitennison.com/blog/node/152) .

  
   

End of the survey.. _have I missed out on something_? Please let me know if I did - I'll try to keep adding stuff to this list as I move on with my project work!
