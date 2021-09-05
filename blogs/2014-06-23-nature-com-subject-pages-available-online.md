---
title: "Nature.com subject pages available online!"
date: "2014-06-23"
categories: 
  - "informationarchitecture"
  - "justblogging"
  - "semantic-web"
tags: 
  - "nature"
  - "ontology"
---

Subject pages are pages that aggregate content from across nature.com based on the tagging of that content by [NPG subject ontology](http://www.michelepasin.org/blog/2013/06/21/messing-around-wih-d3-js-and-hierarchical-data/) terms. After six months of work on this project we've finally launched the first release of the site, which is reachable online at [http://www.nature.com/subjects](http://www.nature.com/subjects). Hooray!

This has been a particularly challenging experience cause I've essentially been wearing two hats for the past six months: _product owner_, leading the team in the day to day activities and prioritization of tasks, and _information architect_, dealing with the way content is organized and presented to users (my usual role).

In a nutshell, the goal of the [project](http://www.nature.com/subjects) was to help our readers discover content more easily by using an internally-developed subject ontology to publish a page per term. The ontology is actually a [poly-hierarchical taxonomy of scientific topics](http://www.michelepasin.org/blog/2013/06/21/messing-around-wih-d3-js-and-hierarchical-data/), which has been used in the last couple of years to tag all articles published on nature.com.

Besides helping users browse the site more easily, [subject pages](http://www.nature.com/subjects) also contribute to making NPG content more discoverable via Google and other external search engines. All of this powered by a new backend platform which combines the expressiveness of **linked data technologies** (RDF) with the scalability of more traditional **XML data stores** (MarkLogic).

The main features are: - **one page per subject** term which collates all content tagged with that term across nature.com - **RSS** and **ATOM** feeds for each of the subject terms (~2500) - dedicated pages that collate content from different journals based on their **article types** (e.g. news, research etc..) - a **visual tool** to navigate subjects based on the ontology relations - subject **email alerts** (to be released in the coming weeks) It's been a lot of work to bring all of this content together within a single application (keep in mind that the content comes from more than [80 different journals](http://www.nature.com/catalog/)!) but this is just the beginning.

In the **next months** we're looking at extending this work by making this content available in other formats (e.g. RDF), providing more ways to navigate through the data (facets, visualizations) and to integrate it with other datasets available online.. so stay tuned for more!

[![Screen Shot 2014 06 23 at 3 35 53 PM](/media/static/blog_img/Screen-Shot-2014-06-23-at-3.35.53-PM.png "Screen Shot 2014-06-23 at 3.35.53 PM.png")](http://www.nature.com/subjects)

[![Screen Shot 2014 06 23 at 3 36 24 PM](/media/static/blog_img/Screen-Shot-2014-06-23-at-3.36.24-PM.png "Screen Shot 2014-06-23 at 3.36.24 PM.png")](http://www.nature.com/subjects/computer-modelling)

[![Screen Shot 2014 06 23 at 3 36 48 PM](/media/static/blog_img/Screen-Shot-2014-06-23-at-3.36.48-PM.png "Screen Shot 2014-06-23 at 3.36.48 PM.png")](http://www.nature.com/subjects/systems-biology)
