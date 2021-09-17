---
title: "SciGraph publishes 1 billion facts as Linked Open Data"
date: "2017-11-14"
categories: 
  - "semantic-web"
---

Last Thursday we reached a major milestone for the SciGraph project: nearly 1 billion facts (= [RDF statements](https://en.wikipedia.org/wiki/Resource_Description_Framework#Examples)) have been [released as Linked Open Data](http://scigraph.springernature.com/explorer/downloads/), most of it under a CC-BY license!

This data release follows and improves on the previous data release ([February 2017](https://github.com/springernature/scigraph/wiki/Data-Release:-2017Q1)) which included metadata for all journal articles published in the last 5 years.

[![](/media/static/blog_img/scigraph2-300x244.jpg)](http://www.michelepasin.org/blog/wp-content/uploads/2017/11/scigraph2.jpg)

 

[![](/media/static/blog_img/scigraph3-300x230.jpg)](http://www.michelepasin.org/blog/wp-content/uploads/2017/11/scigraph3.jpg)

 

[![](/media/static/blog_img/scigraph6-300x193.jpg)](http://www.michelepasin.org/blog/wp-content/uploads/2017/11/scigraph6.jpg)

 

 

## What's in this release:

- **Datasets downloads.** Almost [1 billion triples](http://scigraph.springernature.com/explorer/downloads/) (23.2 GB compressed, or 205.2 GB uncompressed) comprising our SciGraph ontology, SKOS taxonomies and instance data covering the complete archive of Springer Nature publications, i.e. books and journals (1801-2017), conferences, affiliations, funders, research projects and grants. The data is current to end of 2017Q3.
- **Data Explorer.** The [data explorer](http://scigraph.springernature.com/explorer) allow users to visualize each single node in the graph and to move to other related nodes interactively. Furthermore, the Explorer allow users to get rich data descriptions for SciGraph things by traversing the knowledge graph and using content negotiation on SciGraph URLs. In other words, the Explorer is like a **Linked Data API** for developers: the RDF data is [dereferenceable](http://linkeddatabook.com/editions/1.0/#htoc8) (Turtle, N-Triples, RDF/XML) and both HTTP and HTTPS protocols are supported.
- **Dual Licence.** The majority of SciGraph data is [being released](http://scigraph.springernature.com/explorer/license/) under a Creative Commons Attribution (**CC BY**) 4.0 International License, with a small portion of the data (specifically abstracts and grants) separately licensed under a Creative Commons Attribution-NonCommercial (**CC BY-NC**) 4.0 International License.
- **Model Mappings.** To align the SciGraph ontology with other well-known vocabularies we include several mappings and have used extensively two external datasets: ANZSRC (Australian and New Zealand Standard Research Classification) [Fields of Research codes](https://vocabs.ands.org.au/anzsrc-for), and [GRID](https://grid.ac/) (Global Research Identifier Database) identifiers.

## Who is this for?

In general, for people who are interested in reusing our metadata e.g. for data analysis tasks, for developing applications that benefit from linking to Springer Nature content etc.. For example:

- **\*** Researchers and (linked) open data enthusiasts i.e. see the [Linked Data Cloud](http://lod-cloud.net/).
- **\*** Metadata and information specialists e.g. [librarians](https://ontotext.com/linked-data-libraries/).
- **\*** Developers and Data Scientists.

Furthermore, we are in contact with various organisations who are interested in reusing large parts of our datasets, e.g. [Wikidata](https://meta.wikimedia.org/wiki/WikiCite), [DBpedia](http://wiki.dbpedia.org/) and [EMBL-EBI](https://www.ebi.ac.uk/).

## Questions?

Any questions of feedback, leave a comment or email knowledge-graph@springernature.com.

We'd love to hear from you! Also, you can follow the [#scigraph tag on twitter](https://twitter.com/hashtag/scigraph?f=tweets&vertical=default&src=hash) for last-minute news.
