---
title: "Modeling Representations (take 2)"
date: "2007-03-30"
categories: 
  - "informationarchitecture"
tags: 
  - "ontology"
  - "rdf"
  - "representations"
---

I [wrote something](http://www.michelepasin.org/blog/2007/03/05/ontology-of-representations/) in the last weeks about the difficulties related to the modeling of representations and their contents. So today I just read this [article by Stefano Mazzocchi](http://www.betaversion.org/~stefano/linotype/news/101/), which basically hints at the same issue, but from an 'RDF perspective'. It's a very interesting article, so I just wanted to quote and comment a few passages

> The concept of **data integration** is even older than computers, it's as old as the idea of data itself: all datasets that we use today, from a book to a collection of pictures, from a library catalog to census data, had to be collected by different people/entities and integrated.

Very true! I always thought that a "lessons learned from the (far away) past" class would be extremely useful to SW people. Maybe in a future SW academic course...

> There is an implicit assumption among semantic web practitioners that once the data is in RDF and it's using different ontologies, all it's left to do is to find a way to map the various ontologies together and voila', data integration at a global scale!
> 
> RDF might help simplify certain operations but the problem of integration is not about just the identifiers used by the data models but also by **the act of modeling itself**!

Very true. This is lessons learned #2. Philosophers spent two thousand years (in the western world only) trying to do this mapping, without success (or even the desire for it in some cases).

> There are modeling mismatches that simply cannot be solved with ontological mappings alone.
> 
> This is a form of 'undermodeling', similar to the concept of aliasing and artifacts introduced by sampling: a data model is a way of sampling an information space. In audio processing, it's obvious that mixing two samples with different sampling resolutions would result in total garbage no matter how one decides to align them in time.
> 
> We have a similar problem here: given a set of images of paintings where only one image per painting existed, the data model 'undersamples' that information space collapsing the two into one concept.
> 
> Following the same sampling rationale, we need to '**resample**' the data model and decouple the 'works' from the 'images', or convert the Museum location into coordinates. But this is far from trivial and clearly not something that can be done without intimate domain knowledge.

I really like this _sampling - modeling_ metaphor! That's really it! And here's the conclusion:

> This 'resampling' facility, in its most abstract shape, is nothing but a transformation stage: RDF comes in, RDF comes out, possibly different and more aligned with the rest we have to integrate.
> 
> Also while some of such transformation operations can be done unsupervised, in general **human intervention** (by an individual or either a voting group) **will be required**.
> 
> Also the **ability to turn supervision into a 'scripted' set of transformation operations will be required**. For XML one would use XSLT, but for RDF there is no such thing (there are rule languages on the horizon, but they hardly seem to fit these needs... even if XSLT wasn't properly designed for XML transformations either).
> 
> I honestly don't know how these tools will work , what shape they'll have and how much automation they will be able to provide to human users, but one thing is for sure, while declarative equivalences help data integration with RDF, they are far from being enough and we can no longer afford to ignore this problem.

I don't know either - but this seems a very clear problem definition. And often that's the most important thing we need to get going in the right direction!
