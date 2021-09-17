---
title: "MultimediaN semantic navigator"
date: "2006-11-23"
categories: 
  - "culturalinformatics"
  - "semantic-web"
---

Winner of the [Semantic Web challenge 2006](http://challenge.semanticweb.org/), the [MultimediaN e-Culture demonstrator](http://e-culture.multimedian.nl/demo/search) looks at

> \[...\] the development of a set of e-culture demonstrators providing multimedia **access to distributed collections of cultural heritage objects**. The demonstrators are intended to show various levels of syntactic and semantic interoperability between collections and various types of personalized and context--dependent presentation generation.
> 
> \[...\] to demonstrate the use of semantic interoperability, semantic information access and visualization, and **context-specific presentation generation**. The project integrates results from computer science in the areas of: semantic Web technology, multimedia indexing and search, and web interfacing and data visualization to facilitate display of (part of) our cultural heritage.

A quick list of features:

- indexing and search support for virtual collections
- architecture fully based on open standards (XML, SVG, RDF/OWL, SPARQL)
- all built with SWI-Prolog in the back end, + SW APIs
- knowledge sources: 4 thesauri plus Wordnet
- 'knowledge integration': e.g. "..these images are paintings by artists who have painted in the Art-Noveau style, but the style is not part of the metadata of the image itself"
- presence of noise : "..This may retrieve some paintings which are not really Art-Noveau, but it is a reasonable strategy if there are no (or only few) images directly annotated with Art-Noveau"
- basic search / faceted search / time-based search
- search algorithm: first it matches all RDF literals in the repository for matches on the given keyword. Second, from each match, it traverses the RDF graph until a resource of interest is found (target resource). Finally, based on the paths from the matching literals to their target resources, the results are clustered.
- Various techniques to avoid combinatorial explosion of results (one-direction only, threshold)
- "semantic paths" are considered at the schema level, not the instance level ; they are displayed when hovering over a resulting image
- knowledge integration derived semi-automatically from texts on art history + grammars and parsing to match and enhance the various knowledge sources
- annotation of new user-selected images: categories based on VRA3.0 (subset of dublin core for images)

**I tried a few queries** to see how the results are ordered, and the navigation organized. If we search for _impressionism_ **we get various results**, ordered in the following manner: **_the first ones_** directly match the string queried in their main description (label)

[![Pasted Graphic 4.jpg](/media/static/blog_img/Pasted%20Graphic%204.jpg)](http://people.kmi.open.ac.uk/mikele/blog/wp-content/uploads/2006/11/Pasted%20Graphic%204.jpg "Pasted Graphic 4.jpg")

**_Second line_** (AAT refers to the Art and Architecture Thesaurus): results from another metadata set, where the slot label matches the slot hasStyle

[![Pasted Graphic 5.jpg](/media/static/blog_img/Pasted%20Graphic%205.jpg)](http://people.kmi.open.ac.uk/mikele/blog/wp-content/uploads/2006/11/Pasted%20Graphic%205.jpg "Pasted Graphic 5.jpg")

_**Third line**_: results from neighboring values to impressionism, for the slot hasStyle [![Pasted Graphic 6.jpg](/media/static/blog_img/Pasted%20Graphic%206.jpg)](http://people.kmi.open.ac.uk/mikele/blog/wp-content/uploads/2006/11/Pasted%20Graphic%206.jpg "Pasted Graphic 6.jpg")

_**Fourth line**_: results from teachers of the artists producers of the works above, marked up as impressionist [![Pasted Graphic 8.jpg](/media/static/blog_img/Pasted%20Graphic%208.jpg)](http://people.kmi.open.ac.uk/mikele/blog/wp-content/uploads/2006/11/Pasted%20Graphic%208.jpg "Pasted Graphic 8.jpg")

_**Fifth line**_: same as above, but for the student-of relation

[![Pasted Graphic 9.jpg](/media/static/blog_img/Pasted%20Graphic%209.jpg)](http://people.kmi.open.ac.uk/mikele/blog/wp-content/uploads/2006/11/Pasted%20Graphic%209.jpg "Pasted Graphic 9.jpg")

_**Sixth line**_: inferred closure of an artist who worked in the same style of an artist matched above. That is, the rationale is that if they worked at least in one similar style, they are likely to be related even through other styles.

[](http://people.kmi.open.ac.uk/mikele/blog/wp-content/uploads/2006/11/Pasted%20Graphic%2010.jpg "Pasted Graphic 10.jpg")[![Pasted Graphic 10.jpg](/media/static/blog_img/Pasted%20Graphic%2010.jpg)](http://people.kmi.open.ac.uk/mikele/blog/wp-content/uploads/2006/11/Pasted%20Graphic%2010.jpg "Pasted Graphic 10.jpg") At the _**bottom**_, there's an automatically created timeline, which results a little confusing sometimes:

[![Pasted Graphic 11.jpg](/media/static/blog_img/Pasted%20Graphic%2011.jpg)](http://people.kmi.open.ac.uk/mikele/blog/wp-content/uploads/2006/11/Pasted%20Graphic%2011.jpg "Pasted Graphic 11.jpg")

There's many other features, which I am not covering here. However, one remark. What's the purpose of this cool application? Probably it just wants to exhibit the semi-automatic agglomeration of data integrated from different and distributed sources. But **they just remains data, they are not given any shape** (e.g. thanks to the "semantic description") and they do not even reach the level of information, from my point of view (and also from an information visualization perspective see --> \[Information Visualization, Robert Spence\] ) .

Too many clickable links... I have the impression that these navigations, beyond being a technological show-off for data-integration and clustering techniques, very often go beyond being helpful in understanding a resource collection, but produce an overwhelming amount of results and links.

A reflection: we are using semantic data to get out of the "syntactic" data overload on the internet - but **we are going straight into a "semantic" data overload** .... The semantics we should support, instead, is HUMAN semantics, not just a formal semantic ......
