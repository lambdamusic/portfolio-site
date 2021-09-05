---
title: "SN SciGraph Latest Release: Patents, Clinical Trials and many new features"
date: "2019-03-22"
categories: 
  - "semantic-web"
tags: 
  - "jsonld"
  - "linkeddata"
  - "opendata"
  - "schema-org"
---

We are pleased to announce the third release of [SN SciGraph](https://scigraph.springernature.com) Linked Open Data. SN SciGraph is Springer Nature’s Linked Data platform that collates information from across the research landscape, i.e. the things, documents, people, places and relations of importance to the science and scholarly domain.

This release includes a complete refactoring of the SN SciGraph data model. Following up on users feedback, we have simplified it using [Schema.org](https://schema.org/) and [JSON-LD](https://en.wikipedia.org/wiki/JSON-LD), so to make it easier to understand and consume the data also for non-linked data specialists.  

This release includes two brand new datasets - Patents and Clinical Trials linked to Springer Nature publications - which have been made available by our partner [Digital Science](https://www.digital-science.com/), and in particular the [Dimensions](http://dimensions.ai) team.

**Highlights:**

- **New Datasets.** Data about clinical trials and patents connected to Springer Nature publications have been added. This data is sourced from [Dimensions.ai](https://www.dimensions.ai/).
- **New Ontology.** [Schema.org](https://schema.org/) is now the main model used to represent SN SciGraph data.
- **References data.** Publications data now include references as well (= outgoing citations).
- **Simpler Identifiers.** URIs for SciGraph objects have been dramatically simplified, reusing common identifiers whenever possible. In particular all articles and chapters use the URI format prefix ('pub.') + DOI (eg pub.10.1007/s11199-007-9209-1).
- **JSON-LD.** [JSON-LD](https://en.wikipedia.org/wiki/JSON-LD) is now the primary serialization format used by SN SciGraph.
- **Downloads.** Data dumps are now managed externally on [FigShare](https://sn-scigraph.figshare.com/) and are referenceable via DOIs.
- **Continuous updates.** New publications data is released on a daily basis. All the other datasets are refreshed on a monthly basis.

 

Note: crossposted on [https://researchdata.springernature.com](https://researchdata.springernature.com/users/82895-sn-scigraph/posts/45943-sn-scigraph-latest-release-patents-clinical-trials-and-many-new-features)

 

[![](/media/static/blog_img/Screenshot 2019-03-22 at 12.33.41.png)](https://scigraph.springernature.com/explorer)

 

[![](/media/static/blog_img/Screenshot 2019-03-22 at 12.33.54.png)](https://scigraph.springernature.com/explorer/datasets/data_at_a_glance/)
