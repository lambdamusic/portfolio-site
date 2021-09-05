---
title: "KR workshop #2: introducing CIDOC-CRM and FRBR-OO"
date: "2010-08-30"
categories: 
  - "culturalinformatics"
  - "informationarchitecture"
  - "semantic-web"
tags: 
  - "cidoc"
  - "frbr"
  - "frbr-oo"
  - "ontology"
---

This is the second appointment with the [knowledge representation seminar](http://www.michelepasin.org/blog/?p=781) we're having at [CCH](http://www.kcl.ac.uk/schools/humanities/depts/cch) (Kings College, London). If you are in the area and are interested in taking part in this, please drop me an email. We're looking at these topics from the specific perspective of the digital humanities, but even if your take on things is different, we'd love to hear from you!

Last meeting we discussed quite generally about ontologies and other KR technologies, so this time we decided to start looking more meticulously into the details of a widely known **ontology** for the **cultural heritage domain**, the [CIDOC-CMR](http://www.cidoc-crm.org/) conceptual model (an ISO standard since 2006).

> Doerr. [The CIDOC conceptual reference module: an ontological approach to semantic interoperability of metadata](http://portal.acm.org/citation.cfm?id=958671.958678). AI Magazine archive (2003) vol. 24 (3) pp. 75-92

The CIDOC-CRM is the de facto standard for data integration in the museum community. Its authors claim that it "is intended to be a **common language** for domain experts and implementers to formulate requirements for information systems and to serve as a **guide for good practice of conceptual modelling**. In this way, it can provide the "**semantic glue**" needed to mediate between different sources of cultural heritage information, such as that published by museums, libraries and archives".

CIDOC contains a wealth of inspiring ideas and useful approaches; in our first meeting about it we highlighted only a few of them, including:- the need for interoperability at the semantic level
- the difference between data _capturing_ and _interpreting_ data
- the _read-only_ integration approach
- the notion of a property-centric ontology
- the top-level classes in CIDOC
- the nature of cultural historical knowledge
- general principles and methodology in CIDOC-CMR

Here are some slides including key passages from the CIDOC paper mentioned above:

**[Introducing CIDOC-CRM (Cch KR workshop #2.1)](http://www.slideshare.net/mpasin/cch-kr-workshop-22 "Introducing CIDOC-CRM (Cch KR workshop #2.1)")**

## Information objects

One thing that CIDOC doesn't cover much is the domain of _information objects_, which is a fancy term ontologists use to refer to _anything that can carry information_, such as a **book**, a **stone** **inscription**, or a **piece of music**. Modeling this type of entities using a clear (and possibly formal) language may seem straightforward at first: a book is a simple physical object, isn't it?

However this is not always the case: **things easily get muddled** as soon as you start thinking about the fact that a book can have multiple _copies_, that it can be _translated_ into many languages, or it can be _included_ into a different _edition_. In all these cases, what is the 'book' entity we're talking about? Not the physical object, apparently.

How to model information objects is a topic that **librarians** (among others) have discussed quite extensively in the years. As a result of these discussion librarians developed a conceptual model called [FRBR](http://www.ifla.org/en/publications/functional-requirements-for-bibliographic-records), which has become a **standard** to follow when dealing with this type of problems.

[![256px-FRBR-Group-1-entities-and-basic-relations.svg.png](/media/static/blog_img/256px-FRBR-Group-1-entities-and-basic-relations.svg_.png)](http://www.michelepasin.org/blog/wp-content/uploads/2010/08/256px-FRBR-Group-1-entities-and-basic-relations.svg_.png)

FRBR (represented schematically above) summarizes quite well various important features of information objects, especially when considered under the perspective many library scientists have. However it is also true that FRBR doesn't present its results using the rigourous and unambiguous language of formal ontologies. As a result, people end up **interpreting the meaning of its concepts in slightly different ways**. For example, if you are a librarian with little knowledge of computer science, you might end up using FRBR in a totally different way than that of a computer scientist who'd designing a software system for librarians.

To address this limitation, and also in order to open up the CIDOC-CRM model to the librarian community, the **CIDOC committee** has started **'ontologizing' FRBR**. The second part of our seminar focused on this (ongoing) enterprise, which is outlined in this article:

> Bekiari, C., Doerr, M., & Boeuf, P. L. (2009). [FRBR: Object-Oriented Definition and Mapping to FRBR-ER (version 1.0)](http://www.google.co.uk/url?sa=t&source=web&cd=1&ved=0CB8QFjAA&url=http%3A%2F%2Fwww.cidoc-crm.org%2Fdocs%2Ffrbr_oo%2Ffrbr_docs%2FFRBRoo_V1.0.1.pdf&ei=50mYTqjgKsGj8QOv3Nm6BQ&usg=AFQjCNH1pVTtZgsXvT9qSnfutqoqSvHZZA). International Working Group on FRBR and CIDOC CRM Harmonisation.

Here are the slides I used in the seminar, which contain some of the most salient visual representation of the ontology:

**[Introducing FRBR-OO (CCH KR workshop 2.2)](http://www.slideshare.net/mpasin/introducing-frbroo-cch-kr-workshop-22 "Introducing FRBR-OO (CCH KR workshop 2.2)")**

That's all for now - in the future we'll be looking at specific situations where using CIDOC and FRBR presents challenges to the digital humanist: stay tuned!
