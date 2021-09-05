---
title: "Zero Hunger Hack Day: surfacing research about the Sustainable Development Goals program"
date: "2019-02-11"
categories: 
  - "informationarchitecture"
  - "justblogging"
---

This post is about a little dashboard idea that aims at helping policy makers discover research relevant to the '[zero hunger](https://en.wikipedia.org/wiki/Sustainable_Development_Goals#Goal_2:_Zero_hunger)' topic, one of the themes of the [Sustainable Development Goals](https://sustainabledevelopment.un.org/sdgs) program.

> [The 2030 Agenda for Sustainable Development,](https://sustainabledevelopment.un.org/post2015/transformingourworld) adopted by all United Nations Member States in 2015, provides a shared blueprint for peace and prosperity for people and the planet, now and into the future. At its heart are the 17 Sustainable Development Goals (SDGs), which are an urgent call for action by all countries - developed and developing - in a global partnership. They recognize that ending poverty and other deprivations must go hand-in-hand with strategies that improve health and education, reduce inequality, and spur economic growth – all while tackling climate change and working to preserve our oceans and forests.

For more background about this project, see also its wikipedia page [https://en.wikipedia.org/wiki/Sustainable\_Development\_Goals](https://en.wikipedia.org/wiki/Sustainable_Development_Goals)

[![Screenshot 2019-02-19 at 21.18.42.png](/media/static/blog_img/Screenshot-2019-02-19-at-21.18.42.png)](https://sustainabledevelopment.un.org/sdgs)

[Springer Nature](https://www.springernature.com) is among the many organizations who are taking [an active role](https://grandchallenges.springernature.com/) in developing scenarios and solutions to tackle these global challenges. A couple of months ago Springer Nature organized a hack day which brought together people with different backgrounds and expertise in order to come up with ideas and prototypes that could lead to further research. In particular, the focus of the hack day was on the ['zero hunger'](https://en.wikipedia.org/wiki/Sustainable_Development_Goals#Goal_2:_Zero_hunger) theme.

The team I was working with developed a **concept** around the idea of an easy-to-use **dashboard-like tool** which could be **used by busy policy makers** in order to quickly gather infos about researchers or institutions they'd want to consult with.

[_![](/media/static/blog_img/Screenshot 2019-02-19 at 21.46.02.jpg)_](http://www.michelepasin.org/blog/wp-content/uploads/2019/02/Screenshot-2019-02-19-at-21.46.02.jpg)

In order to make this idea more tangible I ended up building a little [prototype,](http://hacks2019.michelepasin.org/zerohunger/) which allows to scan scholarly documents in order to pull out information (potentially) related to the 'zero hunger' topic and sub-topics, essentially following the keywords-structure specified in the Sustainable Development Goals document.

> The prototype is available here: [http://hacks2019.michelepasin.org/zerohunger/](http://hacks2019.michelepasin.org/zerohunger/)

 

[![Screen Shot 2018-11-02 at 16.22.42](/media/static/blog_img/Screen-Shot-2018-11-02-at-16.22.42.png)](http://www.michelepasin.org/blog/wp-content/uploads/2019/02/Screen-Shot-2018-11-02-at-16.22.42.png)

 

[![Screen Shot 2018-11-02 at 16.22.51](/media/static/blog_img/Screen-Shot-2018-11-02-at-16.22.51.png)](http://www.michelepasin.org/blog/wp-content/uploads/2019/02/Screen-Shot-2018-11-02-at-16.22.51.png)

 

This experiment also gave me an opportunity to learn about the **Dimensions.ai API**, a domain specific language (DSL) which allows to query the [Dimensions database,](https://www.dimensions.ai/) a state-of-the-art scholarly platform containing  millions of linked metadata records about publications, grants, patents, clinical trials and policy documents (for more background about Dimensions, see this [blog post](https://www.digital-science.com/press-releases/digital-science-launches-dimensions-next-generation-research-discovery-platform-linking-124-million-documents-providing-free-search-citation-data-across-86-million-articles/) and this [white paper](http://www.library.spbu.ru/blog/wp-content/uploads/2018/01/Guide-to-Dimensions-Data-Approach-2018.pdf)).

[![Screenshot 2019-02-19 at 21.50.33.jpg](/media/static/blog_img/Screenshot-2019-02-19-at-21.50.33.jpg)](https://www.dimensions.ai/)

The API itself is being a paywall, but if you are curious about it, the [documentation is available online](https://docs.dimensions.ai/dsl/index.html).

It's a fantastic resource, intuitive and easy to use yet powerful and features-rich, so I am pretty sure I'll be writing more about it.

Stay tuned for more!
