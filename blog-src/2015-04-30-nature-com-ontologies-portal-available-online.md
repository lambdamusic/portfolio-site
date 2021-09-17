---
title: "Nature.com ontologies portal available online"
date: "2015-04-30"
categories: 
  - "justblogging"
  - "semantic-web"
tags: 
  - "linkeddata"
  - "ontology"
---

The Nature [ontologies portal](http://www.nature.com/ontologies/) is new section of the nature.com site that describes our involvement with semantic technologies and also makes available to the wider public several models and datasets as RDF linked data.

We launched the portal nearly a month ago, to the purpose of sharing our experiences with semantic technologies and more generally to contribute to the wider linked data community with our data models and datasets.

[![Screen Shot 2015 04 30 at 17 35 39](/media/static/blog_img/Screen-Shot-2015-04-30-at-17.35.39.png)](http://www.michelepasin.org/blog/wp-content/uploads/2015/04/Screen-Shot-2015-04-30-at-17.35.39.png)

This April 2015 release doubles the number and size of our published data models. This now spans more completely the various things that our world contains, from [publication things](http://www.nature.com/ontologies/core/publications/) – articles, figures, etc. – to classification things – [article-types](http://www.nature.com/ontologies/models/article-types/), [subjects](http://www.nature.com/ontologies/models/subjects/), etc. – and additional things used to manage our content publishing operation – assets, [events](http://www.nature.com/ontologies/core/events/), etc. Also included is a [release page](http://www.nature.com/ontologies/releases/) for the latest data release and a separate page for archival data releases.

[![Npg models hierarchy v2 alt](/media/static/blog_img/npg-models-hierarchy-v2-alt.png)](http://www.michelepasin.org/blog/wp-content/uploads/2015/04/npg-models-hierarchy-v2-alt.png)

### Background

Is this the first time you've heard about _semantic web_ and _ontologies_?   Then you should know that even though internally at [Macmillan Science and Education](http://se.macmillan.com/) XML remains the main technology used to represent and store the things we publish, the _metadata_ about these documents (e.g. publication details, subject categories etc..) are normally encoded also using a more abstract, **graph-oriented information model**.   This is called [RDF](http://en.wikipedia.org/wiki/Resource_Description_Framework) and has two key characteristics: - it encodes all information in the form of triples e.g. <subject><predicate><object> - it was built with the web in mind: broadly speaking, each of the items in a triple can be accessed via the internet i.e. it is a [URIs](http://www.ltg.ed.ac.uk/~ht/WhatAreURIs/) (a generalised notion of a URL).   **So why using RDF?**

The RDF model makes it easier to maintain a **shared yet scalable schema** (aka an 'ontology') of the data types in use within our organization . A bit like a common language which is spoken by increasingly more data stores and thus allows to join things up more easily whenever needed.   At the same time - since the RDF model is native to the web - it facilitates the 'semantic' integration of our data with the increasing number of other organisations that publish their data using compatible models.   For example the [BBC](http://www.bbc.co.uk/ontologies), [Elsevier](http://www.elsevier.com/about/content-innovation/database-linking) or more recently [Springer](https://campus.macmillan.com/message/34445#34445)  are among the many organisations that contribute to the [Linked Data Cloud](http://lod-cloud.net/).

### What's next

We'll continue improving these ontologies and releasing new ones as they are created. But probably most interestingly for many people, we're working a new release of the whole **NPG articles dataset** (~1M articles).

So stay tuned for more!
