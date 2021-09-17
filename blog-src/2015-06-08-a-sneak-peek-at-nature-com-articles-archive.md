---
title: "A sneak peek at Nature.com articles' archive"
date: "2015-06-08"
categories: 
  - "justblogging"
  - "semantic-web"
tags: 
  - "d3"
  - "nature"
  - "publishing"
  - "visualization"
---

We're getting closer to releasing the full set of metadata covering over one million articles published by Nature Publishing Group since 1845. So here's a sneak peek at this dataset, in the form of a simple d3.js visual summary of what soon will be available to download and reuse.

In the last months I've been working with my colleagues at Macmillan Science and Education on an [open data portal](http://www.nature.com/ontologies/) that makes available to the public many of the taxonomies and ontologies we use internally for organising the content we publish.

This is part of our ongoing involvement with linked data and semantic technologies, aimed both at leveraging these tools to the end of transforming the publishing workflow into a [more dynamic platform](http://www.quora.com/What-is-dynamic-semantic-publishing), and at contributing to the evolving [web of open data](http://linkeddata.org/) with a rich dataset of scientific articles metadata.

The articles dataset includes metadata about all articles published by the [Nature](http://en.wikipedia.org/wiki/Nature_%28journal%29) journal, of course. But not only: the [Scientific American](http://www.scientificamerican.com/), [Nature Medicine](http://www.nature.com/nm/index.html), [Nature Genetics](http://www.nature.com/ng/index.html) and many other titles are also part of it (note: the full list can be downloaded as raw data [here](http://www.nature.com/ontologies/models/journals/)).

[![Screen Shot 2015 06 08 at 22 24 15](/media/static/blog_img/Screen-Shot-2015-06-08-at-22.24.15.png)](http://bl.ocks.org/lambdamusic/raw/bfcaa40fa350778883fe/)

The first diagram shows how many articles have been published each year since [1845](http://www.nature.com/search?year_range=1845) (the start year of Scientific American). Nature began only a few years later in [1869](http://www.nature.com/search?year_range=1869); the curve getting steeper in the 90s instead corresponds to the exponential increase in publications due to the progressive specialisation of scientific journals (e.g. all the nature-branded titles).

The second diagram instead shows the increase in publication volumes on an incremental scale. We've now reached the **1M articles and counting**!

[![Screen Shot 2015 06 08 at 22 25 09](/media/static/blog_img/Screen-Shot-2015-06-08-at-22.25.09.png)](http://bl.ocks.org/lambdamusic/raw/bfcaa40fa350778883fe/)

In order to create the charts I played around with a nifty example from Mike Bostock ([http://bl.ocks.org/mbostock/3902569](http://bl.ocks.org/mbostock/3902569)) and added a couple of extra things to it.

The full source code is on [Github](http://bl.ocks.org/lambdamusic/bfcaa40fa350778883fe).

Finally, worth mentioning that this metadata had already been made available a [few of years ago](http://www.nature.com/press_releases/ldp.html) under the CC0 license: you can still access it [here](http://www.nature.com/ontologies/releases/archive/). **This upcoming release** though makes it available in the context of a much more **precise and stable** set of ontologies. Meaning that the semantics of the dataset is more clearly laid out and **consistent**.

So stay tuned for more! ..and if you plan/would like to reuse these datasets please do get in touch, either here of by emailing [developers@nature.com](mailto:developers@nature.com).
