---
title: "Recent projects from CrossRef.org"
date: "2015-06-14"
categories: 
  - "justblogging"
  - "semantic-web"
tags: 
  - "doi"
  - "linkeddata"
  - "publishing"
---

We spent the day with the CrossRef team in Oxford last week, talking about our recent work in the linked data space (see the [nature ontologies portal](https://campus.macmillan.com/groups/data-information-architecture/blog/2015/04/23/new-release-of-naturecomontologies)) and their recent initiatives in the scholarly publishing area.

So here's a couple of interesting follow ups from the meeting. ps. If you want to know more about CrossRef, make sure you take a look at their [website](http://www.crossref.org/) and in particular the labs section: [http://labs.crossref.org/](http://labs.crossref.org/).

## Opening up article level metrics

[http://det.labs.crossref.org/](http://det.labs.crossref.org/)

CrossRef is using the open source **Lagotto** application (developed by PLOS [https://github.com/articlemetrics/lagotto](https://github.com/articlemetrics/lagotto)) to **retrieve article metrics data from a variety of sources** (e.g. wikipedia, twitter etc. see the full list [here](http://det.labs.crossref.org/docs/sources)).

The model used for storing this data follows an agreed ontology containing for example a classification of 'mentions' actions (viewed/saved/discussed/recommended/cited - see this [paper](http://www.niso.org/publications/isq/2013/v25no2/lin/) for more details).

In a nutshell, CrossRef is planning to collect and make the metrics (raw) data for all the DOIs they track in the form of '[DOI events](http://events.labs.crossref.org/)'

An interesting demo application shows the [stream of DOIs citations coming from Wikipedia](http://events.labs.crossref.org/) (one of the top referrers of DOIs, unsurprisingly). More discussions on this [blog post](http://crosstech.crossref.org/2015/03/real-time-stream-of-dois-being-cited-in-the-wikipedia.html).

[![Screen Shot 2015 05 20 at 16 30 00 1024x760](/media/static/blog_img/Screen-Shot-2015-05-20-at-16.30.00-1024x760.png)](http://www.michelepasin.org/blog/wp-content/uploads/2015/06/Screen-Shot-2015-05-20-at-16.30.00-1024x760.png)

## Linking dataset DOIs and publications DOIs

[http://www.crosscite.org/](http://www.crosscite.org/)

CrossRef has been working with [Datacite](https://www.datacite.org/) to the goal of **harmonising their databases**. Datacite is the second major register of DOIs (after CrossRef) and it has been focusing on assigning persistent identifiers to **datasets**.

This work is now gaining more momentum as Datacite is [enlarging its team](https://www.datacite.org/news/job-offer-technical-architect-thor-project-datacite.html). So in theory it won't be long before we see a service that allows to interlink publications and datasets, which is great news.

## Linking publications and funding sources

[http://www.crossref.org/fundref/](http://www.crossref.org/fundref/)

FundRef provides a **standard way to report funding sources for published scholarly research**. This is increasingly becoming a fundamental **requirement** for all publicly funded research, so several publishers have agreed to help extracting funding information and sending it to CrossRef.

A recent platform built on top of Fundref is Chorus [http://www.chorusaccess.org/](http://www.chorusaccess.org/), which enables users to discover articles reporting on funded research. Furthermore it provides **dashboards** which can b used by funders, institutions, researchers, publishers, and the public for monitoring and tracking public-access compliance for articles reporting on funded research.

For example see [http://dashboard.chorusaccess.org/ahrq#/breakdown](http://dashboard.chorusaccess.org/ahrq#/breakdown)

[![Screen Shot 2015 06 11 at 12 57 39](/media/static/blog_img/Screen-Shot-2015-06-11-at-12.57.39.png)](http://www.michelepasin.org/blog/wp-content/uploads/2015/06/Screen-Shot-2015-06-11-at-12.57.39.png)

## Miscellaneous news & links

\- [JSON-LD](http://json-ld.org/) (an RDF version of JSON) is being considered as a candidate data format for the next generation of the [CrossRef REST API](https://github.com/CrossRef/rest-api-doc/blob/master/rest_api.md).

\- The prototype [http://www.yamz.net/](http://www.yamz.net/) came up in discussion; a quite interesting stack-overflow meets ontology-engineering kind of tool. Def worth a look, I'd say.

\- [Wikidata](http://www.wikidata.org/wiki/Wikidata:Main_Page) (a queryable structured [data version](http://www.wikidata.org/wiki/Wikidata:Data_access) of wikipedia) seems to be gaining a lot of momentum after it's [taken over Freebase from Google](http://searchengineland.com/google-close-freebase-helped-feed-knowledge-graph-211103). Will it eventually replace its main rival [DBpedia](https://en.wikipedia.org/wiki/DBpedia)?

[![Screen Shot 2015 06 11 at 12 58 20](/media/static/blog_img/Screen-Shot-2015-06-11-at-12.58.20.png)](http://www.michelepasin.org/blog/wp-content/uploads/2015/06/Screen-Shot-2015-06-11-at-12.58.20.png)
