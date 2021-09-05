---
title: "ISWC14 paper: a hybrid semantic publishing architecture combining XML and RDF"
date: "2014-11-25"
categories: 
  - "justblogging"
  - "semantic-web"
tags: 
  - "conference"
  - "paper"
---

I'm posting here a short summary of the paper I've given at the last International Semantic Web conference in Riva del Garda ([ISWC14](http://iswc2014.semanticweb.org/)) together with my colleague [Tony Hammond](https://twitter.com/tonyhammond).

The presentation focused on an hybrid data architecture (**XML** for **storage**&**querying**, **RDF** for **modeling**&**integration**) which emerged as the most practical solution during the process of re-engineering of the publishing platform which has occurred within our company ([Macmillan S&E](http://se.macmillan.com/)) in the last years.

This is the abstract:

> This paper presents recent work carried out at Macmillan Science and Education in evolving a traditional XML-based, document- centric enterprise publishing platform into a scalable, thing-centric and RDF-based semantic architecture. **Performance** and **robustness** guarantees required by our online products on the one hand, and the need to support **legacy architectures** on the other, led us to develop a hybrid infrastructure in which the data is modelled throughout in RDF but is replicated and distributed between RDF and XML data stores for efficient retrieval. A recently launched product – dynamic pages for scientific subject terms – is briefly introduced as a result of this semantic publishing architecture.

The [paper is available online](http://www.michelepasin.org/papers/47/); slides from the presentation can be found below.

The **ISWC industry track** was packed with interesting papers so I think it's worth taking a look at the [online proceedings](https://dkm-static.fbk.eu/resources/iswc2014/proceedings/ISWC2014IndustryTrack-Extended%E2%80%93Abstracts.pdf). The uptake of tech outside academia is always revealing of the many real-world difficulties involved in making something fit within pre-existing work practices and legacy technologies. This is especially true of larger companies, where investment in older technologies (and in people who know about them) can be considerable, hence upgrades are costly and need to be evaluated more carefully.

This is the sort of background that led me and my colleagues at MacMillan to opt for a hybrid solution that combines the power of an established [enterprise MarkLogic](http://www.marklogic.com/what-is-marklogic/enterprise-nosql/) installation with more cutting edge data integration approaches based on RDF.

[![HybrydXMLRDF](/media/static/blog_img/hybrydXMLRDF.png)](http://www.michelepasin.org/blog/wp-content/uploads/2014/11/hybrydXMLRDF.png)

[Nature.com subject pages](http://www.nature.com/subjects) were one of the first products built on top of this architecture. And many more will come: we're still heavily involved in this work though, so stay tuned for more stuff in this space.

Soon, we will also be releasing our public ontologies online and making available a new and improved version of the [nature.com datasets](http://www.nature.com/developers/documentation/linked-data-platform/releases/).

<iframe src="//www.slideshare.net/slideshow/embed_code/41989468" width="425" height="355" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen></iframe>
