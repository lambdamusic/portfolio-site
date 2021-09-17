---
title: "How to visualize a big taxonomy within a single webpage?"
date: "2014-08-22"
categories: 
  - "informationarchitecture"
tags: 
  - "taxonomy"
  - "visualization"
---

Here's a couple more experiments aimed at representing visually a large taxonomy.

Some time ago [I looked at ways to visualise a medium-large taxonomy](http://www.michelepasin.org/blog/2013/06/21/messing-around-wih-d3-js-and-hierarchical-data/) (3000 terms circa) using one of the many visualisation kits out there. It turned out that pretty much all of them can't handle that many terms, but there are other strategies that do come handy for that e.g. hide/reveal terms in the taxonomy based on what level you are looking at.

**Why can't I see the whole damn thing in one single page?** Because there are too many things to display - you'd think.

### So, step 1.

Here's the entire set of elements on a page (well sort of).

[![layout1](/media/static/blog_img/layout1-300x155.png)](http://hacks.michelepasin.org/subjectsviz/megaview?num=1)

Can't we do better than that, though?

At the end of the day, if you assume a (quite modest these days) resolution of 800x600 pixels, you should be able to fit more than 300 9point characters in there (assuming [9 points equal 12 pixels](http://www.translatorscafe.com/cafe/EN/units-converter/typography/5-7/character_(X)-pixel_(X)/)).

### Step 2.

Here's another way: a font-size: 7px; and IDs instead of taxon's labels make the visualisation much more compact.

And it does fit in a single window - hurray!

[![layout2](/media/static/blog_img/layout2-300x129.png)](http://hacks.michelepasin.org/subjectsviz/megaview?num=2)

One problem though. This is not very useful with all those meaningless numbers.

### Step 3.

So I tried to reduce the size a bit more so to fit the entire taxon label in there.

Also, adding a bit of interactivity so to reveal the hierarchy. The simple mechanism is this: when you click on an element of the taxonomy all of its ancestors get highlighted too. Just to remember this is not a plain list of things, but a tree.

[![layout3](/media/static/blog_img/layout3-300x150.png)](http://hacks.michelepasin.org/subjectsviz/megaview?num=3)

Kind of like this one :-)

### Possible next steps:

a) adding arrows to make the hierarchical relationships more evident b) some sort of summary below the subject term in focus c) sorting the terms by hierarchy-level rather than alphabetical order (will it make the taxonomy more intelligible?)

..to be continued..
