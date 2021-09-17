---
title: "Semantic Wikipedia: some issues"
date: "2006-10-23"
categories: 
  - "semantic-web"
---

Just went to a talk by [Denny Vrandecic](http://www.aifb.uni-karlsruhe.de/Personen/viewPersonenglish?id_db=2097 "homepage"), one of the people who developed the [Semantic MediaWiki](http://wiki.ontoworld.org/index.php/Semantic_MediaWiki "You can download it here"). A little description:

![](/media/static/blog_img/SemanticMediaWiki_200.png)


> Within only a few years, the free encyclopedia [Wikipedia](http://www.en.wikipedia.org/) has become one of the most important online knowledge sources. The project "[Semantic MediaWiki](http://wiki.ontoworld.org/)" engages in the conception and development of semantic extensions of MediaWiki â€“ the software underlying Wikipedia. The goal is to enable simple, machine-based processing of Wiki-content by allowing users to provide suitable semantic annotations. However, the special Wiki environment and the multitude of envisaged applications impose a number of additional requirements.
> 
> The overall objective of the project is to develop a single solution for semantic annotation that fits the needs of most Wikimedia projects and still meets the Wiki-specific requirements of usability and performance. It is understood that _ad hoc_ implementations (i.e. "hacks") may sometimes solve single problems, but agreeing on common editing syntax, underlying technology, exchange formats, etc. bears huge advantages for all participants.

The importance and greatness of the wikipedia is not questionable (12000 hits per second, a milion and a half articles only in english... [more statistics here](http://en.wikipedia.org/wiki/Wikipedia:Statistics "Statistics of all kinds!")). Making it "queriable" through a classification schema, i.e. an ontology (or more than one) sounds pretty useful, but I'd just like to lay down a couple of thoughts to inspire and make their life harder :-)

- what's the issue with the **metadata consistency**?? We can either choose a "lighweight" and pretty simple ontology, so to reach an easy agreement between the parts involved (who are they, by the way? the _whole lot_ of wikipedia users?), but of course you'd like to get more from any knowledge modeling enterprise. So I guess there are serious consistency issues, "internal" (since it's needed a powerful model which inglobates various subtle perspectives, in the form of classes and relations..), and "external" (I guess people won't agree easily on metadata, will they? - so how to support of solve this problem?)
- the classic **Knowledge Acquisition problem**: who and why will "tag" the wiki articles? Is automatic KA an answer maybe? Can an average wikipedia user be bothered about levels of abstractions, and the manual hassle of adding parenthesis and categories? Maybe not, but I guess quite a lot of hard-core wikipedias would..
- **Reasoning**: what are the added values then, beyond a simple string-search, or an inconsistency check? This is the interesting stuff i believe. The whole wikipedia-knowledge being _reorganized_ depending on perspective..
- **Argumentation**: I believe one of the strenghts (if not the main one) of wikipedia, is the collaborative work behind it. And the collaboration is guaranteed by a solid (and simple) infrastructure which supports debating, arguing, in general reaching consensus through interaction. Is this now totally forgotten? I think there's loads of metadata to be extracted there, and one fundamental research question still unanswered: how do _discourse semantics_ interact and relate to _content semantics_? KMi's work on discourse representation, mainly around the [ScholOnto project](http://kmi.open.ac.uk/projects/scholonto/), could be of great help here.....
