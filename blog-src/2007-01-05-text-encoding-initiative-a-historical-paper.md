---
title: "Text Encoding Initiative - a historical paper"
date: "2007-01-05"
categories: 
  - "culturalinformatics"
  - "justblogging"
  - "semantic-web"
---

[![](/media/static/blog_img/jaco001d.gif)](http://www.tei-c.org/P4X/index.html)

I read this interesting paper from Allen Renear, met at [SoSornet-06](http://sosornet.dcs.kcl.ac.uk/) a few weeks ago in London.

[**Theory and Metatheory in the Development of Text Encoding, Allen Renear, Scholarly Technology Group, Brown University November 3, 1995.**](http://www.philo.at/mii/pesp.dir9511/msg00004.html)

I just managed to put my hands on an old working draft, but it seems complete. It's a seminal paper worth reading, if you work on text annotation and markup... think it was published on The Monist's' Philosophy and Electronic Publishing electronic conference, in 1996.

It is a clear description of where the traditional philosopical work becomes handy, with respect to the text encoding work.. (and, more generally, how well established philosophical methods of enquiry are re-used in software design and ontological engineering). Some extracts follow:

> #2.0.2 I am particularly interested in how, as practical questions give rise to theoretical enquiry, the views of textuality offered by practitioners of text encoding recapitulate an interesting and familiar evolution from a kind of platonistic essentialism, to a less platonic and less essentialist, but still realist, pluralism, to positions that seem more pragmatic, constructivist, and antirealist. Although the domain is a practical one, and the theorizing is presumably directed at resolving practical problems, the discourse which carries this theoretical evolution contains many argumentative strategies familiar to philosophers. These include arguments from hypothetical variation (to discover essential properties), existential instantiation (to display ontological commitment), conceptual involvement (to detect conceptual priority) and others. Ultimately this story reveals that theories about the nature of texts appear inevitably and inextricably intertwined with theories about the nature of theories and the distinction scientific inquiry and philosophical argument is in practice very hard to make out.

And a good review of the text-processors evolution, from old typesetting machines ...

> #3.0.2 By the 1960s text encoding systems were widely used commercially to support computer text processing and computer typesetting. At that time a compositor or author would prepare a data file consisting of "markup" (computer codes specifying formatting information) and "content" (codes specifying the linguistic items of the text, such as alphabetic characters and punctuation). This file would then be processed by formatting software, creating another data file which would then be transferred to a printer or typesetting machine to produce printed pages of text.

...... to the first discussions on content-based text encoding:

> #4.0.2 The earliest endorsement of this approach was by software engineers who were, of course, not trying to make an ontological point, but rather to promote a particular set of techniques and practices as being more efficient and functional than the competing alternatives. To promote their approach and discourage others they offered a theoretical backing which both explained and predicted these efficiencies (Reid 1981, Goldfarb 1981). But in the course of the discussion, some partisans of content-based text processing inevitably claimed more directly that the alternative representational practices were inefficient because they were based on a "false model" of text and that their many disadvantages and inadequacies ultimately flowed directly from that flawed conception. (Coombs et al 1987, DeRose et al 1990).

And the emergence of a dedicated working group in 1987:

> #4.2.13 The principal vehicle for the development and standardization of descriptive markup for the humanities is the \*Text Encoding Initiative\*. The TEI, founded in 1987, is an international effort to specify a common interchange format for machine readable texts; it has developed an SGML-conformant language, known as "TEI" which is in common use, particularly among scholars in the humanities and social sciences.

Very interesting also the second section....

> #5.0.1 In this section I attempt to fit the progress of theorizing about texts (and eventually, theorizing about theorizing about texts) into three stages: Platonism, Pluralism, and Antirealism.

Here he describes the inevitable presence of various coexisting world-views (pluralism) on the same text, initially thought to be the instantiation of a single hierarchical model (platonism).

> #5.2.1 When researchers from the literary and linguistic communities began using SGML in their work, the implicit assumption in SGML that every document could be represented as a single logical hierarchical structure quickly created real practical problems for text encoding projects (Barnard et al. 1987). Briefly the difficulty is that while the SGML world assumed that text encoders would always represent the logical structure of a text as a single hierarchical structure, there in fact turned out to be many hierarchical structures that had reasonable claims to be 'logical'. A verse drama for instance contains dialogue lines, metrical lines, and sentences. But these do not fit in a single hierarchy of non-overlapping objects: sentences and metrical lines obviously overlap (enjambment) and when a character finishes another character's sentence or metrical line then dialogue lines overlap with sentences and metrical lines.

And the final development of the pluralistic perspective, towards a post-modern antirealism:

> #5.3.2 Pluralistic realism allowed that there are many perspectives on a text, but assumes that texts have the structures they have independently of our interests, our theories, and our beliefs about them. The antirealist trend in text encoding, which is consistent with post-modern epistemologies such as constructivism and neo-pragmatism, rejects this view, seeing texts as in some sense the product of the theories and analytical tools we deploy when we transcribe, edit, analyze, or encode them. It is interesting that just as Landow (1992), Bolter (1991), and Lanham (1993) have claimed that electronic textuality, and particularly hypertext, confirms certain tenets of post- modernism, Pichler and others are suggesting that text encoding and the creation of electronic editions also confirms a post-modern view of texts: texts do not exist independently and objectively, but are constructed by us.
