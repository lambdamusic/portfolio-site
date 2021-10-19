---
title: "Exploring scholarly publications using DBPedia concepts: an experiment"
date: "2018-11-23"
categories: 
  - "informationarchitecture"
  - "semantic-web"
tags: 
  - "d3-js"
  - "dbpedia"
  - "linkeddata"
---

This post is about a recent [prototype](http://hacks2019.michelepasin.org/dbpedialinks) I developed, which allows to explore a sample collection of Springer Nature publications using subject tags automatically extracted from DBPedia.

> [DBpedia](https://wiki.dbpedia.org/about) is a crowd-sourced community effort to extract structured content from the information created in various Wikimedia projects. This structured information resembles an open knowledge graph (OKG) which is available for everyone on the Web.

### Datasets

The dataset I used is the result of a **collaboration with [Beyza Yaman](https://twitter.com/beyza__yaman?lang=en)**, a researcher working with the [DBpedia](https://wiki.dbpedia.org/about) team in Leipzig, who used the [SciGraph datasets](https://scigraph.springernature.com/explorer) as input to the [DBPedia-Spotlight](https://www.dbpedia-spotlight.org/) entity-mining tool.

By using [DBPedia-Spotlight](https://www.dbpedia-spotlight.org/) we automatically associated DBpedia subjects terms to a  subset of abstracts available in the SciGraph dataset (around 90k abstract from 2017 publications).

The prototype allows to search the Springer Nature publications using these subject terms.

Also, DBpedia subjects include definitions and semantic relationships (which we are currently not using, but one can imagine how they could be raw material for generating more thematic 'pathways').

### Results: serendipitous discovery of scientific publications

**The results are pretty encouraging:** despite the fact that the concepts extracted sometimes are only marginally relevant (or not relevant at all), the breadth and depth of the DBpedia classification makes the interactive **exploration** quite **interesting** and **serendipitous**.

You can judge for yourself: **the tool is available here**: [http://hacks2019.michelepasin.org/dbpedialinks](http://hacks2019.michelepasin.org/dbpedialinks/)

The purpose of this prototype is to evaluate the quality of the tagging and generate ideas for future applications. So any kind of feedback or ideas is very welcome!

We are working with Beyza to write up the results of this investigation as a research paper. The data and software is already freely available on [github](https://github.com/dbpedia/sci-graph-links/).

### A couple of screenshots:

Eg see the topic '[artificial intelligence](http://hacks2019.michelepasin.org/dbpedialinks/entities/63004)'

[![Screen Shot 2018-11-23 at 17.15.07.png](/media/static/blog_img/Screen-Shot-2018-11-23-at-17.15.07.png)](/media/static/blog_img/Screen-Shot-2018-11-23-at-17.15.07.png)

One can add more subjects to a search in order to 'zoom in' into a results set, eg by [adding 'China'](http://hacks2019.michelepasin.org/dbpedialinks/entities/63004?filters=61361) to the search:

[![Screen Shot 2018-11-23 at 17.16.38](/media/static/blog_img/Screen-Shot-2018-11-23-at-17.16.38.png)](/media/static/blog_img/Screen-Shot-2018-11-23-at-17.16.38.png)

### Implementation details

- Main webapp is using Python and [Django](https://www.djangoproject.com/). I've finally found a good excuse to upgrade to the latest release ([2.1](https://docs.djangoproject.com/en/2.1/)) so very proud of myself!
- [Bootstrap](https://getbootstrap.com/docs/3.3/components/)
- [d3.js](https://d3js.org/) and in particular I've learned a lot from this great [force-directed layout example](http://bl.ocks.org/eyaler/10586116)
- The Springer Nature [SciGraph](https://scigraph.springernature.com) dataset of scientific publications
- The [DBpedia Spotlight](https://www.dbpedia-spotlight.org/demo/) tool
