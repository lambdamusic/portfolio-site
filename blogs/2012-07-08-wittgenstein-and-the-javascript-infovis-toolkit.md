---
title: "Wittgenstein Tractatus and the JavaScript InfoVis Toolkit"
date: "2012-07-08"
categories: 
  - "culturalinformatics"
tags: 
  - "philosophy"
  - "text"
  - "visualization"
  - "wittgenstein"
---

What do the [JavaScript InfoVis Toolkit](http://thejit.org/) and the Austrian philosopher [Ludwig Wittgenstein](http://en.wikipedia.org/wiki/Ludwig_Wittgenstein) have in common? Definitely not much, at first sight. But the moment you realise that Wittgenstein was so fascinated with logic that he wanted to organise his masterwork in the form of a tree structure, well, you may change your mind.

The javaScript [InfoVis Toolkit](http://thejit.org/) includes a number of pretty cool libraries that work in the browser and can be customised to your own needs. Some of these visualisations are specifically designed for trees and graphs, so I always wondered how a dynamic tree-rendering of Wittgenstein's Tractatus would look like.

> The [Tractatus Logico-Philosophicus](http://en.wikipedia.org/wiki/Tractatus_Logico-Philosophicus) (Latin for "Logical-Philosophical Treatise") is the only book-length philosophical work published by the Austrian philosopher Ludwig Wittgenstein in his lifetime. It was an ambitious project: to identify the relationship between language and reality and to define the limits of science. It is recognized as a significant philosophical work of the twentieth century. \[…\] The Tractatus employs a notoriously austere and succinct literary style. The work contains almost no arguments as such, but rather declarative statements which are meant to be self-evident. The statements are hierarchically numbered, with seven basic propositions at the primary level (numbered 1–7), with each sub-level being a comment on or elaboration of the statement at the next higher level (e.g., 1, 1.1, 1.11, 1.12).

The final result is available here (warning: it's been tested only on Chrome and Firefox): [http://hacks.michelepasin.org/witt/spacetree](http://hacks.michelepasin.org/witt/spacetree)

[![SpaceTree Tractatus app](/media/static/blog_img/7487681310_255f7caca4.jpg)](http://hacks.michelepasin.org/witt/spacetree)

### Some more details

I've played around a little with one of the visualisation libraries the JavaScript InfoVis Toolkit makes available, the [Radial Graph](http://thejit.org/static/v20/Docs/files/Visualizations/RGraph-js.html), to the purpose of transforming the Tractatus text into a more interactive platform. The [Radial Graph](http://en.wikipedia.org/wiki/Radar_chart) is essentially a tree-rendering library built over a circular area (hence called also _space-tree_).

I liked the idea of making the tree-like structure of the text explorable one step at a time, within a framework that suggests a predefined order of the text-units but also allows for _lateral_ steps or quick _jumps_ to other sections. However I'm still trying to figure out what the advantages of looking at the text this way can be, once you go past the initial excitement of playing with it as if it was some sort of toy!

Some of the **pros** seem to be:- By zooming in and out of the tree, you can see immediately where one sentence is located and how it (structurally) relates to the other ones
- The tree visualisation makes more transparent the importance of some sentences, and thus implicitly conveys some aspects of the argument Wittgenstein is making.
On the other hand, here are some **cons**:- We lose the the diachronic, linear sense of the text (assuming the Tractatus has one - which is something not all scholars would agree with)
- The animations may become distracting..

I wonder how all of this could be developed further and/or transformed into a useful tool.. if you have any comment or suggestion please do get in touch ! I'm also planning to release the source code for the whole app as soon as a I clean it up a little; for the moment, here is the javascript bit that renders the graph:

<script src="https://gist.github.com/3096854.js?file=Tractatus-rgraph.js"></script>
