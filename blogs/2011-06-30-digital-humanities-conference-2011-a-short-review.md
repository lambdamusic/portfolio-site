---
title: "Event: Digital Humanities conference 2011"
date: "2011-06-30"
categories: 
  - "culturalinformatics"
tags: 
  - "conference"
  - "events"
---

Last week I went to Stanford for the [Digital Humanities 2011](https://dh2011.stanford.edu/) international conference. This is arguably the most important event for researchers and academics who employ digital methods to tackle questions and problems normally associated to 'humanities' disciplines. In this blog post I will start by summarising the things I was invited to talk about; then in the near future I'll try to integrate this article with other reflections and pointers to interesting materials I ran into at the conference.

I had two papers, one by myself and one with [Matteo Romanello](http://www.kcl.ac.uk/artshums/depts/ddh/people/students/romanello/index.aspx), a bright PhD student at [DDH](http://www.kcl.ac.uk/artshums/depts/ddh/index.aspx) whom I'm co-supervising (well sort of.. since the college hasn't formally recognized me in that role yet).

The first paper is about DJFacet, a **faceted search engine** I created and [already discussed elsewhere](http://www.michelepasin.org/blog/2011/06/09/djfacet-a-django-faceted-browser/), so I won't bore you with the technical details here. The aspect of it I discussed at the conference deals with the specific employment of DJFacet with **complex humanities databases**.

DJFacet lets you easily build a search interface consisting of many entry point (facets); in particular, thanks to the availability of an advanced functionality called '**pivoting**' it is possible to switch the main perspective of a search dynamically (that is, the main result type you're searching for) while still keeping the search parameters previously chosen. This means for example that when searching for 'people' using facets such as 'surname' or 'age', you could change the result type to 'documents' and keep using the same 'surname' or 'age' facets. This is made possible by the implicit connection existing in the database between, for example, the objects of type 'people' and the objects of type 'document' (eg, 'authors of').

However, despite the fact that this approach proved to be, from the logical and computational point of view, completely feasible, it also **opened up a number of research questions** from the point of view of the **meaning** of these multifaceted **searches** across different results types. In other words, we realized that often the accumulation of filters ontologically distant from each other could be **hardly translated by the end user** into real-world questions; analogously, the opposite may happen, in so far as simple type of searches may be impeded by the highly structured architecture of a faceted browser. The paper attempted to address these problems and provide some initial solutions to them. Here're the slides:

**[DH11: Browsing Highly Interconnected Humanities Databases Through Multi-Result Faceted Browsers](http://www.slideshare.net/mpasin/dh11-browsing-highly-interconnected-humanities-databases-through-multiresult-faceted-browsers "DH11: Browsing Highly Interconnected Humanities Databases Through Multi-Result Faceted Browsers")** 

<iframe src="http://www.slideshare.net/slideshow/embed_code/8587975?rel=0" width="425" height="355" frameborder="0" marginwidth="0" marginheight="0" scrolling="no"></iframe>

The second paper (headlined by Matteo) is about HuCit (available at www.purl.com/net/hucit), a **formal ontology** we're developing together that is aimed at the formal representation of **humanities citation structures**.

The key idea here derives from the fact that while in the sciences a citation is normally represented in the form of a _relation_ between two publications (and often that's all is needed eg to generate all sorts of interesting citation network analysis algorithms), in the humanities (and especially in classics) citations are normally analyzed by scholars with a much higher attention to details.

For example, citations may exhibit a particular style which scholars want to study and classify (for example when faced with ancient citations) to the purpose of better understanding and contextualizing the meaning of a citation. Secondly, in classics we have interesting 'phenomena' like **canonical citations**: these are citations that do not point at any publication in particular, but at an _idealized_ version of a classic text (eg Homer's Iliad) which is used as a reference systems for all subsequent editions of that text. Canonical citations fundamentally act as a reference to a point in a (textual) coordinate system which is agreed upon by the scholarly community - and thus needs to be followed so to facilitate discussion in that community. So, in a nutshell, the HuCit ontology is providing the representational primitives needed to support computational reasoning about the 'humanistic' way of working with citations. Here're the slides of the talk:

**[An Ontological View of Canonical Citations](http://www.slideshare.net/mpasin/an-ontological-view-of-canonical-citations-8597680 "An Ontological View of Canonical Citations")** 

<iframe src="http://www.slideshare.net/slideshow/embed_code/8597680?rel=0" width="425" height="355" frameborder="0" marginwidth="0" marginheight="0" scrolling="no"></iframe>

All in all, I had a really good time at the conference. The campus and weather in Stanford are just amazing; the DH community really down to earth and approachable. I'll try to update this post in the next weeks, with more information about people and projects that stimulated my imagination. Stay tuned!
