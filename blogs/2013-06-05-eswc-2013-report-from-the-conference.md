---
title: "ESWC 2013 - report from the conference"
date: "2013-06-05"
categories: 
  - "justblogging"
  - "semantic-web"
tags: 
  - "conference"
  - "eswc"
  - "semanticweb"
---

Last week I attended the European Semantic Web Conference ([ESWC'13](http://2013.eswc-conferences.org/)) in Montpellier and had a really good time meeting old friends and catching up with the latest research in this area. In this post I'll collect a few pointers to papers and ideas that caught my attention.

For a high level summary of the talks, you can check out the [pdf program](http://2013.eswc-conferences.org/sites/default/files/ESWC2013_Programm_Web.pdf), the [workshops page](http://2013.eswc-conferences.org/program/workshops) or the [tutorials page](http://2013.eswc-conferences.org/program/tutorials).

In particular the semantic publishing workshop [SEPublica13](http://sepublica.mywikipaper.org/drupal/node/25) was very relevant for my current work, as its stated purpose is to discuss and review "_accessing and reusing the computable data that the literature represents and describes_" - something that all digital publishers are thinking about these days.

As for the rest of the conference, here's a more lengthy summary of (some of) the presentations I managed to attend, organised by topic.

## Keynote: less _semantics_ and more _web_

The keynote from MIT's [David Karger](http://people.csail.mit.edu/karger/) was quite remarkable. In a talk titled “[The Semantic Web for End Users](http://groups.csail.mit.edu/haystack/blog/2013/06/05/keynote-at-the-european-semantic-web-conference-part-1-the-state-of-end-user-information-management/)” he challenged several widespread assumptions about the SW (maybe most intriguingly the '_if it's using RDF/OWL then it's SW_' principle). Karger argued for a a less AI-oriented, more user-centric and web-centric view of semantic web research, according to which one of the key opportunities for SW practitioners is to "**_make it easier for end users to produce, share, and consume structured data_**", irrespectively of whether these are encoded in any of the RDF family of languages. Rather, SW tools should be measured in terms of how much they allow people to deal effectively with '**_applications whose schema is expected to change_**'. In general, the semantic web (like the web) should not be making 'new things possible' but rather 'old things simpler'.

## Semantic Science

> Gon, B., Porto, F., & Moura, A. M. C.. _On the semantic engineering of scientific hypotheses as linked data_.

The paper addresses the **engineering of hypotheses as linked data**, and builds upon the [Linked Science Core vocabulary](http://linkedscience.org/lsc/ns/) by extending it in order allow the definition of scientific hypotheses as assumptions that constrain the interpretation of observed phenomena for computer simulation. A prototype application built by eliciting and linking hypotheses in a published research in Computational [Hemodynamics](http://en.wikipedia.org/wiki/Hemodynamics) (the study of the human cardiovascular system) is discussed to illustrate the notion of 'conceptual traceability' of research statements.

> Gil, Y., Ratnakar, V., & Hanson, P. C. _Organic Data Publishing : A Novel Approach to Scientific Data Sharing_.

The paper introduces an approach called '**organic data sharing**' that 1) links dataset contributions directly to science questions, 2) reduces the burden of data sharing by enabling any scientist to contribute metadata, and 3) tracks and exposes credit for all contributors. An initial prototype that is built as an extension of a [semantic wiki](http://en.wikipedia.org/wiki/Semantic_wiki), can import Linked Data, and can publish as Linked Data any new content created by users.

> Zhao, J., & Klyne, G. (2013). _How Reliable is Your workflow : Monitoring Decay in Scholarly Publications_.

The paper addresses the notion of [workflow](http://alpha.myexperiment.org/) 'decay'. Increasingly, **scientific workflows are being treated as first-class artifacts**, for exchanging and transferring actual scholarly findings, either as part of scholarly articles or as stand-alone objects. However scientific workflows are commonly subject to a decayed or reduced ability to be executed or repeated, largely due to the volatility of the external resources that are required for their executions. Based on our this hypothesis, the authors present a minimal set of information to be associated in a workflow to reduce its decay and be effectively exchanged as a reproducible research object.

> Callahan, A., Cruz-toledo, J., Ansell, P., & Dumontier, M. (2013). _Bio2RDF Release 2 : Improved coverage , interoperability and provenance of Life Science Linked Data_.

[Bio2RDF](http://bio2rdf.org/) is an open-source project that provides **linked data for the life sciences** using Semantic Web technologies. Bio2RDF scripts (available on [github](https://github.com/bio2rdf/bio2rdf-scripts)) convert heterogeneously formatted data (e.g. flat-files, tab-delimited files, dataset specific formats, SQL, XML etc.) into a common format, RDF. The paper describes the new features of the latest Bio2RDF release, which provides a federated network of [SPARQL endpoints](http://sourceforge.net/apps/mediawiki/bio2rdf/index.php?title=SPARQL_endpoints) over 19 datasets. Other new features include provenance information via [PROV](http://www.w3.org/TR/prov-o/), mapping of dataset-specific vocabulary to the [Semanticscience Integrated Ontology](https://code.google.com/p/semanticscience/wiki/SIO) (SIO), context-sensitive SPARQL query formulation using [SparQLed](http://sindicetech.com/sindice-suite/sparqled/) and a central registry of datasets in order to normalize generated [IRIs](http://en.wikipedia.org/wiki/Internationalized_Resource_Identifier).

## Semantic Publishing

> T. Kuhn, P. E. Barbano, M. L. Nagy, and M. Krauthammer, _Broadening the Scope of Nanopublications_.

Traditionally, [nanopublications](http://nanopub.org/wordpress/) are described as an approach to (1) subdivide scientific results into minimal pieces, (2) to represent these results — called assertions — in an RDF-based formal notation, (3) to attach RDF-based provenance information on this “atomic” level, and (4) to treat each of these tiny entities as a separate publication. The authors of this paper challenge assumption (2) as unrealistic, essentially due to the proven difficulties in acquiring structured, logic-based assertions from people, and propose a new system ([nanobrowser](http://purl.org/nanobrowser)) that allows authors and curators to **attach English sentences to nanopublications**, thus allowing for informal representations of scientific claims.

> Lord, P., & Marshall, L. (2013). _Twenty-Five Shades of Greycite : Semantics for referencing and preservation_.

The paper describes two new systems: [greycite](http://greycite.knowledgeblog.org/) and [kblog-metadata](http://knowledgeblog.org/kblog-metadata). The former, addresses the **problem of bibliographic metadata**, without resorting to a single central authority, extracting this metadata directly from URI end-points. The latter provides more specialised support for generating appropriate metadata within the popular **wordpress** blogging platform. The underlying rationale for both systems, claims the author, is that semantic metadata must be of value to all participants in the publishing process, most importantly the authors.

> Mavergames, C., Oliver, S., & Becker, L. (2013). _Systematic Reviews as an interface to the web of ( trial ) data : Using PICO as an ontology for knowledge synthesis in evidence-based healthcare research The Cochrane Collaboration_

The paper describes a prototype application that makes use of linked data technologies to **improve discovery of information** stored in the [Cochrane Database of Systematic Reviews](http://www.thecochranelibrary.com/), a resource in the domain of healthcare research (in particular the area of evidence-based medicine). The approach described relies on the [PICO framework](http://en.wikipedia.org/wiki/PICO_process) (Population, Intervention, Comparison, Outcome) as an ontology to aid in better discoverability, presentation, and synthesis of the knowledge available in the documents offered by the database. A prototype web application based on [Drupal's SW module](https://groups.drupal.org/semantic-web) is presented.

> Wiljes, C., Jahn, N., Lier, F., Paul-stueve, T., Vompras, J., Pietsch, C., & Cimiano, P. (2013). _Towards Linked Research Data : An Institutional Approach._

The paper describes an infrastructure used that **enables researchers to manage their publications** and the underlying research data in an easy and efficient way within a academic institution, Bielefeld University and the associated [Center of Excellence Cognitive Interaction Technology](https://www.cit-ec.de/). The platform created follows a Linked Data approach and uses [Virtuoso](http://virtuoso.openlinksw.com/) to store data sources from inside the university and outside sources like DBpedia.

## NLP, knowledge extraction

> Iorio, A. Di, Nuzzolese, A. G., & Peroni, S. (2013). _Towards the automatic identification of the nature of citations._

The paper presents an algorithm, called [CiTalO](http://wit.istc.cnr.it:8080/tools/citalo), to **infer automatically the function of citations** by means of Semantic Web technologies and NLP techniques. CiTalO infers the function of citations by combining techniques of ontology learning from natural language, sentiment-analysis, word-sense disambiguation, and ontology mapping. These techniques are applied in a pipeline whose input is the textual context containing the citation and the output is a one or more properties of the [CiTO](http://purl.org/spar/cito) ontology.

> Jael, L., Castro, G., Berlanga, R., Rebholz-schuhmann, D., & Garcia, A. (2013). _Connections across scientific publications based on semantic annotations._

The paper presents an experiment aimed at **evaluating different concept annotation solutions** on full text documents to determine to which extend relatedness can be inferred from such annotations. Eleven full-text articles from the open-access subset of [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/) have been extracted and annotated semantically using [MeSH](http://www.nlm.nih.gov/mesh/), [UMLS](http://www.nlm.nih.gov/research/umls/), and other ontologies. The authors show that connections across articles from annotations automatically identified with entity recognition tools, e.g., [Whatizit](http://www.ebi.ac.uk/webservices/whatizit/), [NCBO Annotator](http://bioportal.bioontology.org/annotator), and CMA, are similar to those connections exhibit based on the PubMed MeSH terms, thus validating their approach.

> A. Gangemi, _A Comparison of Knowledge Extraction Tools for the Semantic Web_.

This article **reviews a number of Natural Language Processing tools** (for various purposes, such as name-entity recognition or word sense disambiguation) that have been configured for Semantic Web tasks including ontology learning, linked data population, entity resolution, NL querying to linked data and others. The tools have been compared using a sample taken from an online article of The New York Times and the results are [available online](http://stlab.istc.cnr.it/stlab/KnowledgeExtractionToolEval). The tools reviewed are: [AIDA](http://www.mpi-inf.mpg.de/yago-naga/aida/), [AlchemyAPI](http://www.alchemyapi.com/api/demo.html), [Apache Stanbol](http://dev.iks-project.eu:8081/enhancer), [DBpedia Spotlight](http://dbpedia-spotlight.github.com/demo), [CiceroLite](http://demo.languagecomputer.com/cicerolite), [FOX](http://aksw.org/Projects/FOX.html), [FRED](http://wit.istc.cnr.it/stlab-tools/fred), [NERD](http://nerd.eurecom.fr), [Open Calais](http://viewer.opencalais.com/), [PoolParty Knowledge Discoverer](http://poolparty.biz/demozone/general), [ReVerb](http://reverb.cs.washington.edu), [Semiosearch Wikifier](http://wit.istc.cnr.it/stlab-tools/wikifier), [Wikimeta](http://www.wikimeta.com/wapi/semtag.pl), [Zemanta](http://www.zemanta.com/demo/).

> E. Cabrio, S. Villata, F. Gandon, and I. S. Antipolis, _A Support Framework for Argumentative Discussions Management in the Web_.

The paper presents an approach based on NLP for automatically **extracting argumentative relationships from highly active wiki pages**. The overall purpose is to support community managers in managing the discussions and have an overall view of the ongoing deabtes so to detect the winning arguments. Argumentative discussions are formalized using an extension of the [SIOC Argumentation vocabulary](http://rdfs.org/sioc/spec/).

> O. Medelyan, S. Manion, J. Broekstra, A. Divoli, A. Huang, and I. H. Witten, _Constructing a Focused Taxonomy from a Document Collection_

The paper describes a new method for **constructing custom taxonomies from document collections**, called [F-STEP](https://sites.google.com/site/focusedtaxonomies/). It involves identifying relevant concepts and entities in text; linking them to knowledge sources like Wikipedia, [DBpedia](http://dbpedia.org/About), [Freebase](http://www.freebase.com/), and any supplied taxonomies from related domains; disambiguating conflicting concept mappings; and selecting semantic relations that best group them hierarchically. By using this approach the authors constructed a custom taxonomy with 10,000 concepts and 12,700 relations from 2000 news articles. An evaluation with human judges has shows high rates of precision (90%) and recall (75%).

## SW tech in real world systems

> P. Szekely, C. A. Knoblock, F. Yang, X. Zhu, E. E. Fink, R. Allen, and G. Goodlander, _Connecting the Smithsonian American Art Museum to the Linked Data Cloud_.

This paper describes the process and lessons learned in **publishing the data from the** [Smithsonian American Art Museum](http://americanart.si.edu/). The paper contains detailed descriptions of a) how relational data have been mapped to RDF (a system called [Karma](http://www.isi.edu/integration/karma/) was used), b) how links to other linked data URIs have been created, and c) the process of curation to ensure that both the published information and its links to other sources within the LOD are accurate. The dataset uses an extended version of the [Europeana Data Model](http://www.europeana.eu/schemas/edm/), which is the metamodel used in the [Europeana project](http://www.europeana.eu/portal/) to represent data from Europe’s cultural heritage institutions, plus other standards like [PROV](http://www.w3.org/TR/prov-o/) and [Schema.org](http://schema.org/).

> L. M. Garshol and A. Borge, _Hafslund Sesam – an archive on semantics_.

The paper describes an architecture based on RDF and Virtuoso, constructed to facilitate data integration and reuse within [Hafslund](http://www.hafslund.no/), a **Norwegian energy company**. Documents are tagged with URIs from the triple store, and these URIs connect the document metadata with enterprise data extracted from backend systems. All source systems are integrated using a custom-built client-server solution based on [SDShare](http://www.sdshare.org/) - a specification for synchronizing RDF data using [Atom feeds](http://en.wikipedia.org/wiki/Atom_(standard)).

## Random notes

- [SparQLed](http://sindicetech.com/sindice-suite/sparqled/) is an open source app that gives you an interactive SPARQL editor with context-aware recommendations (via autocompletion and other tricks). Definitely worth taking a look at.
- I missed the excellent [Semantic Data Management Techniques in Graph Databases](http://www.labf.usb.ve/TUTORIAL2013/ESWC2013Tutorial/Home.html) tutorial, but luckily the [slides are available online](http://www.labf.usb.ve/TUTORIAL2013/ESWC2013Tutorial/Home_files/SlidesTutorialGraphDatabases_MAC.pdf). If you're interested in graph databases, check them out, they include a detailed **analysis and comparison of various graph databases** including Neo4j, Hypergraph and many others.
- David Karger pointed out a web app called [If THis Then That](https://ifttt.com). Rule-based reasoning on the web, without any fancy AI. Pretty cool!
- [identifiers.org/](http://identifiers.org/) is yet another service that aims at providing resolvable persistent URIs used to identify data for the scientific community
