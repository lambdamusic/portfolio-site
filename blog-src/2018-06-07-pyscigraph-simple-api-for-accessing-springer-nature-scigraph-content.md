---
title: "PySciGraph: simple API for accessing SN SciGraph content"
date: "2018-06-07"
categories: 
  - "semantic-web"
---

PySciGraph is a small open source Python library that makes it easier to access data from [Springer Nature SciGraph.](https://scigraph.springernature.com/explorer) It is available on [Pypi](https://pypi.org/project/pyscigraph/) and [Github](https://github.com/lambdamusic/pyscigraph). I created it mainly because I wanted to be able to quickly check from the command line whether an object exists in SN SciGraph, or what metadata it returns. But of course this could be developed further e.g. so to allow to navigate the graph by following links from one object to the other.

> **What is SN SciGraph?** SciGraph is the Springer Nature Linked Data platform that collates information from across the research landscape, i.e. the things, documents, people, places and relations of importance to the science and scholarly domain. Metadata for millions of entities are available to explore, as well as for downloading to reuse within your own application under a CC-BY and CC-BY-NC license (you can follow [SN SciGraph blog posts here](https://researchdata.springernature.com/users/82895-sn-scigraph))

[![scigraph](/media/static/blog_img/scigraph.png)](https://www.springernature.com/gp/researchers/scigraph)

Here's an example of how the library can be used from the command line:

```bash
# check if an object is on SciGraph via its URI
$ pyscigraph --uri http://www.grid.ac/institutes/grid.443610.4
Parsing 12 triples..
URI:  http://www.grid.ac/institutes/grid.443610.4
DOI:  N/A
Label:  Hakodate University
Title:  N/A
Types:  foaf:Organization grid:Education

# check if a publication is on SciGraph via its DOI
$ pyscigraph --doi 10.1038/171737a0
Parsing 251 triples..
URI:  http://scigraph.springernature.com/things/articles/f5ac1e9c7a520ca2a34cb13af4809bdd
DOI:  10.1038/171737a0
Label:  Article: Molecular Structure of Nucleic Acids: A Structure for Deoxyribose Nucleic Acid
Title:  Molecular Structure of Nucleic Acids: A Structure for Deoxyribose Nucleic Acid
Types:  sg:Article

# retrieve all metadata via an RDF serialization
$ pyscigraph --doi 10.1038/171737a0 --rdf n3
Parsing 251 triples..
@prefix dc: <http://purl.org/dc/elements/1.1/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix grid: <http://www.grid.ac/ontology/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sg: <http://scigraph.springernature.com/ontologies/core/> .
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix vann: <http://purl.org/vocab/vann/> .
@prefix vivo: <http://vivoweb.org/ontology/core#> .
@prefix void: <http://rdfs.org/ns/void#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://scigraph.springernature.com/things/articles/f5ac1e9c7a520ca2a34cb13af4809bdd> a sg:Article ;
    rdfs:label "Article: Molecular Structure of Nucleic Acids: A Structure for Deoxyribose Nucleic Acid" ;
    sg:coverDate "1953-04-25"^^xsd:date ;
    sg:coverYear "1953-01-01"^^xsd:gYear ;
    sg:coverYearMonth "1953-04-01"^^xsd:gYearMonth ;
    sg:ddsIdJournalBrand "41586" ;
    sg:doi "10.1038/171737a0" ;
    sg:doiLink <http://dx.doi.org/10.1038/171737a0> ;
    sg:hasArticleType <http://scigraph.springernature.com/things/article-types/af> ;
    sg:hasContributingOrganization <http://www.grid.ac/institutes/grid.5335.0> ;
    sg:hasContribution <http://scigraph.springernature.com/things/contributions/7325bd1cadf3a1cc253c611682bc62fd>,
        <http://scigraph.springernature.com/things/contributions/989a6a2607c882ffd99341144836d1fc> ;
    sg:hasFieldOfResearchCode <http://purl.org/au-research/vocabulary/anzsrc-for/2008/03>,
        <http://purl.org/au-research/vocabulary/anzsrc-for/2008/0306> ;
    sg:hasJournal <http://scigraph.springernature.com/things/journals/5ea8996a5bb089dd0562d3bfe24eaad9>,
        <http://scigraph.springernature.com/things/journals/723ba46cf7980ad6089b3da0ba4b0b47> ;
    sg:hasJournalBrand <http://scigraph.springernature.com/things/journal-brands/012496b06989edb434c6b8e1d0b0a7db> ;
    sg:issnElectronic "1476-4687" ;
    sg:issnPrint "0028-0836" ;
    sg:issue "4356" ;
    sg:license <http://scigraph.springernature.com/explorer/license/> ;
    sg:npgId "171737a0" ;
    sg:pageEnd "738" ;
    sg:pageStart "737" ;
    sg:publicationDate "1953-04-25"^^xsd:date ;
    sg:publicationYear "1953-01-01"^^xsd:gYear ;
    sg:publicationYearMonth "1953-04-01"^^xsd:gYearMonth ;
    sg:scigraphId "f5ac1e9c7a520ca2a34cb13af4809bdd" ;
    sg:title "Molecular Structure of Nucleic Acids: A Structure for Deoxyribose Nucleic Acid" ;
    sg:volume "171" .
```

The current release (0.4) just offers basic functionalities but I'm planning to do more work on this over the next months.

Any ideas? Comments? Please [open an issue on Github!](https://github.com/lambdamusic/pyscigraph/issues)
