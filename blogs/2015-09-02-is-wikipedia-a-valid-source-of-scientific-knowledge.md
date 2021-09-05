---
title: "Is wikipedia a valid source of scientific knowledge?"
date: "2015-09-02"
categories: 
  - "informationarchitecture"
  - "semantic-web"
tags: 
  - "citation"
  - "d3"
  - "nature"
  - "wikipedia"
---

Is wikipedia a valid source of scientific knowledge? Many would say [yes](http://www.nature.com/news/2008/081216/full/news.2008.1312.html). Others are still quite skeptical, or maybe just [cautious](http://www.quora.com/How-reliable-is-Wikipedia-as-a-source-of-information-and-why) about it. What seems to be the case though - and this is what this post is about - is that wikipedians are increasingly including references to scientific literature, and when they do it they do it right.

Based on data we've recently [extracted](http://www.nature.com/ontologies/linksets/articles/) from Wikipedia, it looks like that the vast majority of **citations to nature.com** content have been done according to the established scientific practice (i.e. using [DOIs](https://en.wikipedia.org/wiki/Digital_object_identifier)). Which makes you think that whoever added those citations is either a scientist or has some familiarity with science.

In the context of the [nature.com ontologies portal](http://www.nature.com/ontologies/) we've done some work aimed at surfacing links between our articles and other datasets. Wikipedia and [DBpedia](http://wiki.dbpedia.org/) (an RDF database version of wikipedia) have come to our attention quite soon: _how much do wikipedia articles cite scientific content published on nature.com_? Also, _how well_ do they cite it?

So here's an [interactive visualization](http://www.nature.com/developers/hacks/wikilinks/) that lets you see all incoming references from Wikipedia to the nature.com archive. The actual dataset is encoded in RDF and can be downloaded [here](http://data.nature.com/downloads/latest/linksets/nq/) (look for the _npg-articles-dbpedia-linkset.2015-08-24.nq.tar.gz_ file).

[![NewImage](/media/static/blog_img/NewImage.png "NewImage.png")](http://www.nature.com/developers/hacks/wikilinks/)

## About the data

In a nutshell, what we've done was simply extracting all mentions of either NPG DOIs or nature.com links using the wikipedia APIs (for example, see [all references to the DOI "10.1038/ng1285"](https://en.wikipedia.org/w/index.php?title=Special%3ASearch&profile=default&search=%2210.1038%2Fng1285%22&fulltext=Search)).

These links have then been validated against the nature.com articles database and encoded in RDF in two ways: a [cito:isCitedBy](http://www.essepuntato.it/lode/http://purl.org/spar/cito) relationship links the article URI to the citing Wikipedia page, and a [foaf:topic](http://xmlns.com/foaf/spec/) relationship links the same article URI to the corresponding DBpedia page.

[![Screen Shot 2015 09 03 at 12 37 33 PM](/media/static/blog_img/Screen-Shot-2015-09-03-at-12.37.33-PM.png "Screen Shot 2015-09-03 at 12.37.33 PM.png")](http://www.michelepasin.org/blog/wp-content/uploads/2015/09/Screen-Shot-2015-09-03-at-12.37.33-PM.png) In total there are **51309 links over 145 years**.

Quite interestingly, the vast majority of these links are explicit DOI references (only ~900 were links to nature.com without a DOI). So, it seems that people do recognize the importance of DOIs even within a loosely controlled context like wikipedia.

## Using the dataset

Considering that for many wikipedia is become the _de facto_ largest and most cited encyclopedia out there (see the articles below), this may be an interesting dataset to **analyze** e.g. to highlight citation patters of influential articles. Also, this could become quite useful as a data source for **content enrichment**: the wikipedia links could be used to drive subject tagging, or they could even be presented to readers on article pages e.g. as contextual information.

[![Toparticles](/media/static/blog_img/toparticles.png "toparticles.png")](http://www.michelepasin.org/blog/wp-content/uploads/2015/09/toparticles.png)

We haven't really had time to explore any follow up on this work, but hopefully we'll do that soon.

All of this data is open source and freely available on [nature.com/ontologies](http://www.nature.com/ontologies/). So if you're reading this and have more ideas about potential uses or just want to collaborate, please do [get in touch](http://www.michelepasin.org/contact/)!

## Caveats

This dataset is obviously just a **snaphot** of wikipedia links at a specific moment in time.

If one were to use these data within a real-world application he'd probably want to come up with some strategy to keep it up to date (e.g. monitoring the [Wikipedia IRC recent changes channel](https://meta.wikimedia.org/wiki/IRC/Channels#Recent_changes)). Good news is, work is already happening in this space:- **CrossRef** is looking at collecting citation events from Wikipedia in real time and release these data freely as part of their service e.g. see [http://crosstech.crossref.org/2015/05/coming-to-you-live-from-wikipedia.html](http://crosstech.crossref.org/2015/05/coming-to-you-live-from-wikipedia.html)
- **Altmetric** scans wikipedia for references too e.g. see [http://nature.altmetric.com/details/961190/wikipedia](http://nature.altmetric.com/details/961190/wikipedia) and [http://www.altmetric.com/blog/new-source-alert-wikipedia/](http://www.altmetric.com/blog/new-source-alert-wikipedia/), however the source data is not freely available.

## Readings

Finally, here are a couple of interesting background readings I've found in the nature.com archive:- _Wikipedia rival calls in the experts_ (2006) [http://www.nature.com/nature/journal/v443/n7111/full/443493a.html](http://www.nature.com/nature/journal/v443/n7111/full/443493a.html)
- _Publish in Wikipedia or perish_ (2008) [http://www.nature.com/news/2008/081216/full/news.2008.1312.html](http://www.nature.com/news/2008/081216/full/news.2008.1312.html)
- _Time to underpin Wikipedia wisdom_ (2010) [http://www.nature.com/nature/journal/v468/n7325/full/468765c.html](http://www.nature.com/nature/journal/v468/n7325/full/468765c.html)

_Enjoy_!
