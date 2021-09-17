---
title: "Humanities Computing and web2.0"
date: "2008-02-04"
categories: 
  - "culturalinformatics"
  - "justblogging"
tags: 
  - "digitalhumanities-2"
  - "presentation"
  - "web2"
  - "workshop"
---

Last week I spent two interesting days in London, at the [Epistemic Networks and GRID Web 2.0 for Arts and Humanities workshop](http://www.arts-humanities.net/event/epistemic_networks_grid_web_20_arts_humanities). I went there representing [PhiloSURFical](http://philosurfical.open.ac.uk/) and [Cohere](http://cohereweb.net/), but unfortunately due to technical reasons the fliers I've prepared to let this community know about our work were not handed out on time. The printers at Imperial College didnt want to work for me :-). Too bad.. I managed anyway to spread the word a bit, and the reactions have been very very positive.  

But let's talk about the workshop. I found out quite a few humanities-related resources providers I was not aware of, which is pretty cool. I'm going to try accessing them using the APIs (where) provided, and see whether some interesting cross-sites services can be built out of that. As usual, I found quite boring the long and never ending talks about super-solid architectures that do marvellous things, or the ones about the state-of-the-art of such and such technologies bla bla bla. You can hear enough of them at the semantic web conferences, so I am not going to report on any of those. I found much more interesting the presentations about existing systems that do stuff for us (in this case 'us' should be the humanities scholars, i suppose). And the good news is that most of the talks presented systems like that!

So here we go (in order of appearance, and based on what I remember - sorry if I'm missing out something):

- **Paul Watry (univ. of Liverpool)**: _Named Entity and Identity Services for the National Archives_: the [Multivalent](http://multivalent.sourceforge.net/) software, and its descendant [FabFour](http://bodoni.lib.liv.ac.uk/fab4/) browser. The first one, to my understanding, is an extensive suite of tools for humanities-computing with a very long list of features organized into four sections: Browser, Tools, Developer and Research.

> **Browser**  
> Natively view HTML, PDF, TeX DVI, man pages, and other document formats  
> Annotate in situ on all formats, robustly anchored  
> Notemarks  
> Lenses (show OCR, decypher, magnify)  
> **Tools**  
> PDF: impose, compress, uncompress, info, encrypt / decrypt, split and merge, validate  
> HTML: Robust Hyperlink signing  
> All document formats: UPDATED Extract text, structure, and links. Full-text search with Lucene  
> **Developer**  
> Deep and pervasive browser extension via behaviors  
> Parse all formats, extract content and style from DOM, format and extract layout geometry  
> Render all formats  
> and embed in Swing  
> PDF library: read - modify - write (supports PDF 1.5)  
> **Research**  
> NEW Digital Preservation  
> A Platform for New Ideas  
> Robust Hyperlinks  
> Robust Locations  
> PDF Compression: "Two Diet Plans for Fat PDF" and Compact PDF Specification

It's quite impressive. I haven't tried it out but I [downloaded instead the FabFour browser](http://bodoni.lib.liv.ac.uk/fab4/fab4.html) which is built on top of Multivalent. It's a java application for browsing/annotation:

> \* Can open HTML, PDF, DVI, SVG, JPEG and other formats natively, without native helper applications  
> \* Allows shared, distributed annotations using open standards (SRW, SOAP, ...)  
> \* Uses the XML digital signature standard to guarantee provenance of the annotations  
> \* Annotations are stored separate from the original file, so the original file remains untouched  
> \* Annotations are attached to the documents using different identifiers, so they are location and file format independent (you can annotate an ODF file with Fab4, email the file converted to PDF, and the receiver will be able to see the same annotations as in the original ODF file)  
> \* Public notes are indexed in a Cheshire database, so they can be searched and documents can be retrieved trough their annotations.  
> \* Supports copy editing, style editing and lenses to enrich the document view

Really nice. It worked smoothly on my mac, and it looks powerful and easy to use. I think it's a tool I'll try to integrate in my daily workflow, for studying & annotating what I find on the web!

- **Marc Wilhelm Kuster** , _TEXTGRID_ . It's an [eclipse-based platform for textual research in the humanities.](http://www.textgrid.de/index.php?id=ueber_textgrid&L=5) I tried to look for stuff to download online but couldnt find anything, so here's their blurb:

> Integrated tools that satisfy the specific requirements of text sciences could transform the way scholars process, analyse, annotate, edit and publish text data. Working towards this vision, TextGrid aims at building a virtual workbench based on e-Science methods.  
> The installation of a grid-enabled architecture is obvious for two reasons. On the one hand, past and current initiatives for digitising and accessioning texts already accrued a considerable data volume, which exceeds multiple terabytes. Grids are capable of handling these data volumes. Also the dispersal of the community as well as the scattering of resources and tools call for establishing a Community Grid. This establishes a platform for connecting the experts and integrating the initiatives worldwide. The TextGrid community is equipped with a set of powerful software tools based on existing solutions and embracing the grid paradigm.

It seemed a comprehensive suite of tools for distributed text analysis - the only downside, from my non-german perspective, the fact that it's all tailored to the German language for now.

- **Greg Crane** (_Department of the Classics, Tufts University) - Perseus project_

> [Perseus](http://www.perseus.tufts.edu/) is an evolving digital library, engineering interactions through time, space, and language. Our primary goal is to bring a wide range of source materials to as large an audience as possible. We anticipate that greater accessibility to the sources for the study of the humanities will strengthen the quality of questions, lead to new avenues of research, and connect more people through the connection of ideas.

It's a gigantic collection of literary texts, something you'd really want to check out. Plus, it also provides a few ways to **analyze all this material using [visualizations and statistical tools.](http://www.perseus.tufts.edu/cgi-bin/perscoll?collection=Perseus:collection:PersInfo&type=interactive resource)** I really liked this..We are using computers right? So we should [take advantage of their number crunching capabilities](http://www.newleftreview.org/?view=2482)!

- **David Shotton** - _ClarosWEB project_. These guys are based in Oxford and although they haven't produced any software yet, they impressed me for the clear intention of contributing to a 'data web' (= sparql endpoints, rdf-ed data etc.). What the [project](http://www.clarosnet.org/about/default.htm) is about:

> CLAROS - CLassical Art Research Online Services - developed from discussions between European university research centres held in Oxford in 2000, but the concept dates back to the early 1990s, when the Beazley Archive participated in the EU R&D project RAMA (Remote Access to Museum Archives). The development of web technology has made it possible for RAMA's aspirations to be realised.  
> CLAROS aims to use Web 2.0 and image recognition technologies to bring classical art to anyone, any time, anywhere thanks to collaboration with the University of Oxford's OeRC and the Departments of Engineering Science and Zoology.

In particular, the data-web branch of the project is called **FlyWeb**, more information about it can be found [here](http://imageweb.zoo.ox.ac.uk/wiki/index.php/FlyWeb_project).

- **Kalina Bontcheva**: _AKT and GATE: GRID-WEB Services AKT/GATE._ Kalina gave an overview of [Gate](http://gate.ac.uk/), which is a well-known tool in the NLP community. The [interesting thing is that they're now working on a web (web2?) version of it, called SAFE](http://www.gate.ac.uk/safe/)

- **Marco Passarotti** \- _Index Thomisticus Treebank_. I dont remember much about the Latin language, but this seemed a pretty serious software for analyzing and annotating Latin works

> [Lessico Tomistico Biculturale](http://gircse.marginalia.it/~passarotti/) aims to develop IT in a lexicon, whose lexical entries are all the IT lemmas. Each entry is a report about the morphological, syntactic and semantic uses and values of the lemmas in IT.

The software is java-based. The thing I really liked is that they've also done a web-friendly implementation of it: [LemLat](http://www.ilc.cnr.it/lemlat/).  

- **Jurgen Renn** - _The Epistemic Web, Max Planck Berlin_. This talk mentioned another big source of humanities resources, the [ECHO project](http://echo.mpiwg-berlin.mpg.de/home)

> more than 330 authors represented by ECHO collections  
> 70 seed collections in several disciplines and thematic fields,  
> in particular history of science  
> more than 206,600 documents  
> more than 265,000 high resolution images  
> of historical and cultural source documents and artefacts  
> more than 240 film sequences of scientific source material  
> more than 57,500 full-text page transcriptions in several languages

For that regards the tools, that's all. Other two talks I liked, are the ones by **Martin Doerr** (about an interesting first-order-logic framework for managing co-reference on the semantic web) and by **Annamaria Carusi** (on the relationship between technology and human practice, i.e., among other things, about how and when the digital instruments we use are chaging the way we do things also in humanities-research).  

## Conclusion:

Interesting experience, cool softwares, but one major remark... _where is the web2 in all of this?_ [The web should be the platform, right?](http://en.wikipedia.org/wiki/Web_2) And how about the other principles (users' collaboration, contents syndication, lightweight business models, ease of use, ajax, folksonomies, mashups etc. etc.) ?

Interestingly enough, these aspects have not been mentioned a lot in the presentations. I think it's a clear sign that humanities&computing is a little bit behind in this respect. We should start thinking how to get more results from all those wasted ['cycles of human computations'](http://video.google.com/videoplay?docid=-8246463980976635143), or better, '_cycles of humanists' ruminations_', by finding cheap and effective ways to get more people in the loop and letting them have fun on the web & at the same time contribute to it.  
[Cohere is trying to go this direction](http://cohere.open.ac.uk/), in the next months we'll surely find out how many humanists will find it useful!
