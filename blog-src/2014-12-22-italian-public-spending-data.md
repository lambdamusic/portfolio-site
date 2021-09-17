---
title: "Italian public spending data: a review"
date: "2014-12-22"
categories: 
  - "informationarchitecture"
  - "semantic-web"
tags: 
  - "italy"
  - "open-data"
  - "open-democracy"
  - "transparency"
---

The Italian government recently announced a new portal containing data on public spending: [http://soldipubblici.gov.it](http://soldipubblici.gov.it). This is obviously great news; the website is still in beta though so in what follows I'd like to put forward a few (hopefully constructive) comments and desires for how it could/should be developed further.

Incidentally, I recently ran into [Ian Makgill](https://twitter.com/ianmakgill) from [spendnetwork.com/](http://spendnetwork.com/), a London startup funded by the [Open Data Institute](http://opendatainstitute.org/start-ups/spend-network) which looks at using _open public data to create the first comprehensive and publicly available repository for government transaction data_.

<iframe src="//player.vimeo.com/video/101522232" width="500" height="281" frameborder="0" webkitallowfullscreen mozallowfullscreen="" allowfullscreen=""></iframe>

We ended up chatting about the situation with **open government data in Italy**. To be honest I'm no expert on the matter but a couple of names quickly came to mind.

**First**, the excellent [OpenPolis](http://www.openpolis.it/eng/) association. Their mission is _to enable free access to public information on political candidates, elected representatives, and legislative activity thus promoting [transparency](http://blog.openpolis.it/2014/09/29/foia-4-italy-ricordiamo-renzi-gli-impegni-preso-diritto-accesso/#more-2981) and the democratic participation of Italian citizens_.

One of their most successful projects is [Open Parliament](http://parlamento.openpolis.it/) (similar in scope to [theyworkforyou.com](http://www.theyworkforyou.com/) in the UK). More recently the [Open Bilanci](http://www.openbilanci.it/) platform was created so to allow citizens to search&compare the budgets and expenses of municipalities (local boroughs) in Italy.

[![Screen Shot 2014 12 22 at 22 44 34](/media/static/blog_img/Screen-Shot-2014-12-22-at-22.44.34.png)](http://michelepasin.org/blog/wp-content/uploads/2014/12/Screen-Shot-2014-12-22-at-22.44.34.png)

[![Screen Shot 2014 12 23 at 10 52 45](/media/static/blog_img/Screen-Shot-2014-12-23-at-10.52.45.png)](http://michelepasin.org/blog/wp-content/uploads/2014/12/Screen-Shot-2014-12-23-at-10.52.45.png)

**Second**, the ongoing work done by the [Open Knowledge Foundation](https://okfn.org/), which also has an [Italian charter](http://it.okfn.org/). For example one of its long-standing projects, [openspending.org](https://openspending.org), contains references to several [datasets about Italy's public spending](https://openspending.org/search?q=italy).

Another useful resource is the [Italia open data census](http://it-city.census.okfn.org/), a community driven initiative to _compare the progress made by different cities and local areas in releasing Open Data_.

[![Screen Shot 2014 12 22 at 22 42 47](/media/static/blog_img/Screen-Shot-2014-12-22-at-22.42.47.png)](http://michelepasin.org/blog/wp-content/uploads/2014/12/Screen-Shot-2014-12-22-at-22.42.47.png)

### Soldipubblici.gov.it: a first look

It should be clear by now that the people behind [soldipubblici.gov.it](http://soldipubblici.gov.it/it/home) are not the only ones looking at increasing transparency and democracy by releasing open data.

What's **not clear at all** though, is whether these different groups are **talking to each other** - which would seem the most obvious thing to do before embarking on a new enterprise like this. Especially since soldipubblici.gov.it is strikingly **similar** (in scope) to the aforementioned [Open Bilanci](http://www.openbilanci.it/) portal. I'm sure that both the folks at the OKFN and openpolis.org would be interested in getting their hands on these data so to integrate them with their existing services.

Nonetheless, it's great to hear that more is happening in this space. Even more so because it's the Italian government who's taking responsibility for it this (as it should be).

[![Screen Shot 2014 12 23 at 11 14 52](/media/static/blog_img/Screen-Shot-2014-12-23-at-11.14.52.png)](http://michelepasin.org/blog/wp-content/uploads/2014/12/Screen-Shot-2014-12-23-at-11.14.52.png)

That's the good news. The bad news is that, from a data perspective, **there isn't much you can do with the [soldipubblici.gov.it](http://soldipubblici.gov.it/)** in this beta release. If one wants to put these data to use there are various key elements missing I believe. Here's a few ideas:

- **There is no way to browse/review the data**. Search is good, but if you have no idea what to search for (e.g. simply because you don't know what's it called), then you're fundamentally stuck. The system actually features a more advanced 'semantic' search, which essentially augments the scope of the keywords you put in via synonyms and related terms. That's nice, but that's also no substitute for a good old days yellow-pages-like categories browser. You know, just to get the hang of what's in the box before opening it.

- **You can't download the data**. To be fair, the FAQs clearly state that this feature is still being worked on. Fine - I guess they're talking about some nifty mechanism to select-collect-&-download specific datasets one is interested in. However I do wonder why one cannot download the entire dataset already. At the end of the day, that data is **A)** already made available via the current user interface; **B)** public and (in theory) already available on a different website called [SIOPE](https://www.siope.it/opendata/siopeopendata.htm) (available is a big word though - I should probably say [buried](http://blog.openpolis.it/2014/06/06/opensiope-cogliamo-unopportunita-non-puo-essere-sprecata/)).

- **The visualisation app is nice but very limited**. Data doesn't become information unless you give it some meaningful context. This tool is a great idea but it'd be enormously more useful if you could decide yourself what to plot on the graph (e.g. which years, of which data sets) depending on your research questions i.e. your context. Moreover, you want to be able to make comparisons between different datasets etc etc.. All things that [Open Bilanci does already pretty well](http://www.openbilanci.it/confronti/milano-comune-mi/napoli-comune-na/entrate/consuntivo-entrate-cassa-imposte-e-tasse).

- **There's no data about the beneficiaries of the public expenses**. Not sure what the challenges are here, or whether this is feasible at all. But it'd be great to have this extra piece of information, for transparency's sake. For example, on spendnetwork.com you can easily see which are the list of [suppliers for the London Borough Council of Ealing expenses](https://spendnetwork.com/entity_spend/E5036_ELBC_gov).

### Conclusion: how serious do you want to be about open data?

This is an inspiring start and I can't wait to see it being developed further. Especially if it gets developed with real end-users in mind! To that end, it's useful to bring up what the OKFN has declared to be the key features of [data openness](https://okfn.org/opendata/):

> - **Availability and access**: the data must be available as a whole and at no more than a reasonable reproduction cost, preferably by downloading over the internet. The data must also be available in a convenient and modifiable form.
> - **Reuse and redistribution**: the data must be provided under terms that permit reuse and redistribution including the intermixing with other datasets. The data must be machine-readable.
> - **Universal participation**: everyone must be able to use, reuse and redistribute — there should be no discrimination against fields of endeavour or against persons or groups. For example, ‘non-commercial’ restrictions that would prevent ‘commercial’ use, or restrictions of use for certain purposes (e.g. only in education), are not allowed.

Personally, I can't stress strongly enough how useful it'd be being able to access the **raw data**. Excel, CSV, a [REST API](http://en.wikipedia.org/wiki/Representational_state_transfer) or even better a [Linked Data API](http://linkeddata.org/guides-and-tutorials). A data-level access point would turn this nice-looking but essentially [siloed website](http://en.wikipedia.org/wiki/Information_silo) into an open resource which thousands of [data journalists](http://en.wikipedia.org/wiki/Data_journalism) or data scientists (of [any kind](http://www.oreilly.com/data/free/)) could build upon.

Are you looking forward to see this happen? I do!
