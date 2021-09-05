---
title: "Ontology of Representations"
date: "2007-03-05"
categories: 
  - "informationarchitecture"
tags: 
  - "dolce"
  - "frbr"
  - "kr"
  - "ontology"
---

It's been three days that I'm struggling with concepts of **_content_**, **_form_**, **_representation_** and so on.. I wonder whether there's a well-formalized theory of representations out there.. the one in [DOLCE](http://en.wikipedia.org/wiki/Upper_ontology_(information_science)#DOLCE_and_DnS) is a useful design pattern, but I'm still reluctant to say that it is complete (I hope I'll find out to be wrong). Another clever view of the issue can be found in a [tutorial by Richiiro Mizoguchi](http://www.ei.sanken.osaka-u.ac.jp/pub/miz/Part3V3.pdf), and this is what this post is about.

In this tutorial Mizoguchi talks about **representation** - **represented-thing** - **representational-form** etc.. No mention of **information-objects**, which are instead (only as a term, maybe) always present everywhere else (Dolce, Cidoc, Cyc). So what's the proper mapping? _Is an IO a representation_? Moreover, I am trying to put also another model in the picture, [FRBR](http://www.ifla.org/VII/s13/frbr/frbr.htm). This bibliographic standard focuses around concepts such as **work**, **expression** and **manifestation**, mainly. So how do these come into the game?

Sometimes I end up in some sort of ontological relativism. Since the objects we study are essentially multidimensional, and since we humans can only rationally perceive a portion of such dimensions at a given time, it follows that whatever perspective we decide to take on our objects of investigation, it will be fundamentally arbitrary and partial. In other words, there is no chance of having a single unifying perspective on reality, one which can contain all the others. No chance. So every representation gives you one side of the story only - which can be _related_ to other sides, but never in its entirety. If this is the case, we better keep all the possible 'sides' of this story, and just use the one we need whenever we need it. A pragmatist approach? Well.. more on this to come soon! (i'd also like to go back to [Peirce](http://plato.stanford.edu/entries/peirce/#mind), and check how all of this relates to his work)  

Back to us: this is the model used in Dolce (more precisely, in the DnS module of Dolce, as described in Gangemi, A., Borgo, S., & Catenacci, C. (2005). _Metokis deliverable D07 - Task Taxonomies for Knowledge Content_. Deliverable of the EU FP6 project Metokis):

[![Dolce DnS](/media/static/blog_img/6243934618_882f6dec69.jpg)](http://www.flickr.com/photos/mikele/6243934618/ "Dolce DnS by MagIcReBirth, on Flickr")

And this is an example of its instantiation:

[![Dolce DnS instantiation](/media/static/blog_img/6243934674_a5c18eb663.jpg)](http://www.flickr.com/photos/mikele/6243934674/ "Dolce DnS instantiation by MagIcReBirth, on Flickr")

The **theory of Mizoguchi**, as I said, it's quite different. Here's an interesting excerpt from the article Mizoguchi, R. (2004). _Tutorial on ontological engineering - Part 3: Advanced course of ontological engineering_. New Generation Computing, 22(2), 198–220.

> A representation is composed of two parts, form and content.
> 
> Representation .......p/o "form": Representational form .......p/o"content": Proposition
> 
> where p/o stands for part-of relation/slot, “form” slot name and “: Representation” is a class constraint the slot value has to satisfy. Its identity is inherited from the form which is usually what people sense its existence. On the other hand, the content is the hidden part and it is a proposition which the author of the representation would like to convey through the representation. \[...\] It is critical to distinguish among proposition(content), representation and form of representation. In fact, although a novel is written in terms of sentences, novel is not a subclass of representation. What exists as a subclass of representation are what have the form of representation as its intrinsic property, that is, sentence, musical score, painting, etc. The sentences of Tale of Genji are instance-of sentence. However, representation and form of representation are different. Concerning a novel, representation is “sentence” which is composed of its content(novel) and “natural language” which is the syntactic part of the sentence, as the form of representation.

This is a quite impressive visual rendering of this ontological theory:

[![Mizoguchi representation ontology](/media/static/blog_img/6243934736_fb1b033e9f_z.jpg)](http://www.flickr.com/photos/mikele/6243934736/ "Mizoguchi representation ontology by MagIcReBirth, on Flickr")

How are these theories different from each other? What are their pros and cons, where is it that they could be used more successfully? There's work to be done here..
