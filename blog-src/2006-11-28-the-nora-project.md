---
title: "The Nora Project"
date: "2006-11-28"
categories: 
  - "culturalinformatics"
---

The [Nora Project](http://www.noraproject.org/description.php) aims at putting together a big pool of digital texts in the **humanities** in order to develop and test **data mining techniques specific to this domain**. Various collaborations with other institutions have provided them already a testbed of about **10,000 literary texts** in English, from the 19th century, or about 5 GB of marked-up text. Started by the University of Illinois' Graduate School of Library and Information Science, it relies on several years of software development work that has been done at the University of Illinois' National Center for Supercomputing Applications (NCSA), developing the D2K (Data to Knowledge) software, in Michael Welge's [Automated Learning Group](http://alg.ncsa.uiuc.edu/do/index). As they explain:

> \[...\] the goal of data-mining (including text-mining) is to **produce new knowledge by exposing unanticipated similarities or differences, clustering or dispersal, co-occurrence and trends**. Over the last decade, many millions of dollars have been invested in creating digital library collections: at this point, terabytes of full-text humanities resources are publicly available on the web. The goal of the nora project is to produce software for discovering, visualizing, and exploring significant patterns across large collections of full-text humanities resources in existing digital libraries.

I tried the [online Nora Vis demo](http://www.noraproject.org/nora_demo.php), on the letters of Emily Dickinson, through the Java Web start:

[![Picture 22.png](/media/static/blog_img/Picture%2022.png)](http://people.kmi.open.ac.uk/mikele/blog/wp-content/uploads/2006/11/Picture%2022.png "Picture 22.png")

Didn't take too long to launch (well.. tx to KMi's super fast connection), and it automatically loads a text and some metadata we don't see initially. From the online guide I gathered that I have to browse the docs, and r**ate them** according to how much they represent a specific content (in the example, "erotic"...) [![Picture 31.png](/media/static/blog_img/Picture%2031.png)](http://people.kmi.open.ac.uk/mikele/blog/wp-content/uploads/2006/11/Picture%2031.png "Picture 31.png")

Different visualizations of the text are possible: [![Picture 41.png](/media/static/blog_img/Picture%2041.png)](http://people.kmi.open.ac.uk/mikele/blog/wp-content/uploads/2006/11/Picture%2041.png "Picture 41.png")

Metadata apparently associated with the documents - **not very 'semantic'**, are they? Maybe I'm leaving out something.... [![Picture 5.png](/media/static/blog_img/Picture%205.png)](http://people.kmi.open.ac.uk/mikele/blog/wp-content/uploads/2006/11/Picture%205.png "Picture 5.png")

The idea is to **provide a training corpus**, through the ranking on the right-bottom part of the page. Then to benefit from it by using it as a **"pattern" to match other documents**... at first sight, the result is a sort of linguistic similarity among literary texts. [![Picture 6.png](/media/static/blog_img/Picture%206.png)](http://people.kmi.open.ac.uk/mikele/blog/wp-content/uploads/2006/11/Picture%206.png "Picture 6.png")

So I set off to perform the analysis bit, but something got wrong, and it crashed... more on next episode!

[![Picture 7.png](/media/static/blog_img/Picture%207.png)](http://people.kmi.open.ac.uk/mikele/blog/wp-content/uploads/2006/11/Picture%207.png "Picture 7.png")
