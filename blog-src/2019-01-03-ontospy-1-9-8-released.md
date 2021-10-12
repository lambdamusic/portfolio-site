---
title: "Ontospy 1.9.8 released"
date: "2019-01-03"
categories: 
  - "informationarchitecture"
  - "semantic-web"
tags: 
  - "ontospy"
  - "python"
  - "rdf"
  - "semantic-web"
---

Ontospy version 1.9.8 has been just released and it contains tons of improvements and new features. [Ontospy](http://lambdamusic.github.io/Ontospy/) is a lightweight open-source Python library and command line tool for working with vocabularies encoded in the [RDF](https://en.wikipedia.org/wiki/Resource_Description_Framework) family of languages.

Over the past month I've been working on a new version of Ontospy, which is now available for download on [Pypi](https://pypi.org/project/ontospy/). It's been quite some time in the making, so pretty glad it's finally out now.

<iframe width="560" height="315" src="https://www.youtube.com/embed/MkKrtVHi_Ks?controls=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### What's new in this version

- The library module used to generate **ontology documentation** (as html or markdown) is now included within the main Ontospy distribution. Previously, this library was distributed separately under the name `ontodocs`.  The main problem with this approach is that keeping the two projects in sync was becoming too time-consuming for me, so I've decided to merge them. NOTE one can still choose whether or not to include this extra library [when installing](http://lambdamusic.github.io/Ontospy/#installation).
- You can print out the **raw RDF data** being returned via command line argument.
- One can decided whether or not to include **'inferred' schema definitions** extracted from an RDF payload. The inferences are pretty basic for now (eg the object of `rdf:type` statements is taken to be a type) but this allows for example to quickly dereference a DBpedia URI and pull out all types/predicates being used.
- The online **documentation** are now hosted on [github pages](http://lambdamusic.github.io/Ontospy/) and available within the `/docs` folder of the project.
- Improved support for **JSON-LD** and a new utility for quickly sending JSON-LD data to the [online playground tool](https://json-ld.org/playground/).
- Several other bug fixes and improvements, in particular to the **interactive** ontology exploration mode (`shell` command), the visualization library (**new visualizations** are available - albeit still in alpha state).
