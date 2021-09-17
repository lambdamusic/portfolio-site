---
title: "Creating useful classifications with taxonomies (part 1)"
date: "2013-07-25"
categories: 
  - "informationarchitecture"
tags: 
  - "modeling"
  - "taxonomy"
---

Taxonomies and other classification schemes are omnipresent in Information Architecture. In this post I've tried to gather a few ideas on the topic, with the aim of clarifying the issue a little, and maybe help constructing more useful taxonomies. Comments and suggestions are welcome as usual!

It recently occurred to me though that there is a great deal of confusion with regards to what a taxonomy is, and how it should be designed, constructed, and managed. Often this is simply because people have different backgrounds and intents when dealing with taxonomies, so they end up overseeing a great deal of scientific work that already exists on this area.

### What are taxonomies?

Let's start by looking at a simple taxonomy. Here's one that I could use in order to sort out the junk I have accumulated in my backyard:

```
- hardware
--- pc tower cases [2]
--- pc accessories  [4]
- toys
--- construction toys 
------ meccano [1]
--- dolls [3]
- kitchen stuff
--- plates [10]
--- old cutleries [14] 
```

So what is a taxonomy? In general the aim of a taxonomy is to **organise things into groups, according to some perceived similarities** (e.g. structure, role, behaviour, purpose etc.). Not surprisingly this is what the Greek root 'taxis' means: putting things into order.

If you want a fancier definition, a taxonomy can be defined as a **conceptual tool for classification**. It's a way to bring order to a domain of interest that can be composed by objects of any kind (e.g. physical or abstract, real or invented). A taxonomy normally plays the same role of an **inventory** or a list, for it describes what kind of things are available in a certain context and thus lets us carry out some _task_ more efficiently within that context. For example, _finding_ objects of interest, or _comparing_ objects with similar characteristics.

I just said that a taxonomy is similar to a list or inventory of things; actually, that's not correct. **A taxonomy is much more than a list of concepts**, in fact its key feature is that is organizes the concepts within a hierarchical structure. This is called the **taxonomical tree**.

```
root node
-- sub-concept-1
-- -- sub-concept 1-1 (leaf node)
-- sub concept 2
-- -- sub-concept 2-1 (leaf node)
```

The taxonomical tree is composed by **nodes** and **links**. In particular, the links are very important here as they offer a (more or less) explicit definition of the _relationships_ among the categories that describe your 'stuff'. In other words, a taxonomy acts a little bit like a **map**: it tells you what kind of things exists, and also how they can be meaningfully organized into a coherent framework.

So for example in biology we could have a taxonomy that organizes cell entities based on a (spatial) **whole-part relationship**:

```
Cell (Eukaryotic)
--Membrane
--Cytoplasm
----Mitochondria
----Nucleus
------Chromosomes
------Nucleolus
```

Consider now the case of a music magazine; here it might be more appropriate to construct a taxonomy based on a (thing-kind) **sub-genre relationship**:

```
rock
--blues rock
--hard rock
--heavy metal
---- speed metal
---- progressive metal
```

Finally, we can think of a mountaineering club that keeps an organized list of the instances of expeditions done by its members, by means of an **instance-of relationship** (or 'example'):

```
Mountain
--Mount Everest
--Mount Kilimanjaro
Canyon
--Samaria Gorge
--Grand Canyon
```

So, in general, there can be many variations of 'taxonomical maps': spatial maps, thing-kind ones, thing-example ones etc.. And here's the good news: the key to understanding how taxonomies work (and hence how to design them successfully) is to be able to identify and evaluate the implications of these variations.

### The taxonomical relationship

I think it's clear by now that the rationale for the hierarchical structure used by a taxonomy is not always entirely transparent. The meaning of the links that makes up the main taxonomical tree (the _taxonomical relationship_) is somehow left **implicit**. In fact, unless we have some accompanying documentation that defines the intended meaning of the relationship between one node and its parent(s) and children, it is up to us to interpret its sense.

This is often not a problem. If you look at the examples above, it is likely that you'd immediately understand what the taxonomical relationship stands for: e.g. part-of, type-of, broader-topic-than, instance-of etc..

However **if your taxonomy has been growing over time, the situation could be rather different**. An increasing number of relationships may have been used to construct a single tree, making it difficult for new users to make sense of the taxonomy, or for expert ones to update it without generating conflicts.

**It is good practice** then (especially if the taxonomy aims at being reused) to **use a single relationship consistently throughout the taxonomical tree**; also, to identify explicitly what the meaning of the taxonomical link is. As we will see in the next part of this post, this will make your work much more extendable and reusable.
