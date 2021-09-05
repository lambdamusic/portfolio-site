---
title: "Nature.com Subjects Stream Graph"
date: "2016-01-03"
categories: 
  - "informationarchitecture"
tags: 
  - "d3"
  - "infographics"
  - "nature"
  - "visualization"
---

The [nature.com subjects stream graph](http://www.nature.com/developers/hacks/articles/stream/by-subject/) displays the distribution of content across the subject areas covered by the nature.com portal.

This is an experimental interactive visualisation based on a freely available dataset from the [nature.com linked data platform](http://www.nature.com/ontologies/datasets/), which I've been working on in the last few months. [![streamgraph](/media/static/blog_img/streamgraph6-1024x657.png)](http://www.michelepasin.org/blog/wp-content/uploads/2014/10/streamgraph6.png)

The main visualization provides an overview of selected content within the level 2 disciplines of the [NPG Subjects Ontology](http://www.nature.com/ontologies/models/subjects/). By clicking on these, it is then possible to explore more specific subdisciplines and their related articles.

For those of you who are not familiar with the Subjects Ontology: this is a categorization of scholarly subject areas which are used for the indexing of content on nature.com. It includes subject terms of varying levels of specificity such as Biological sciences (top level), Cancer (level 2), or B-2 cells (level 7). In total there are more than 2500 subject terms, organized into a [polyhierarchical tree](http://www.nature.com/developers/hacks/subjects/tree). Starting in 2010, the various journals published on nature.com have adopted the subject ontology to tag their articles (note: different journals have started doing this at different times, hence some variations in the graph starting dates).

[![streamgraph2](/media/static/blog_img/streamgraph22.png)](http://www.michelepasin.org/blog/wp-content/uploads/2014/10/streamgraph22.png)

[![streamgraph3](/media/static/blog_img/streamgraph33-1024x472.png)](http://www.michelepasin.org/blog/wp-content/uploads/2014/10/streamgraph33.png)

The visualization makes use of various [d3.js](http://d3js.org/) modules, plus some simple customizations here and there. The hardest part of the work was putting the different page components together, to the effect of a more fluent 'narrative' achieved by gradually zooming into the data.

The back end is a [Django](https://www.djangoproject.com/) web application with a relational database. The original dataset is [published as RDF](http://www.nature.com/ontologies/downloads/), so in order to use the Django APIs I've recreated it as a relational model. That let me also add a few extra data fields containing search indexes (e.g. article counts per month), so to make the stream graph load faster.

Comments or suggestions, as always very welcome.
