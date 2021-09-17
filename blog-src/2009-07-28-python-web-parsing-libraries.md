---
title: "Python web-parsing libraries"
date: "2009-07-28"
categories: 
  - "techlife"
tags: 
  - "html"
  - "parsing"
  - "python"
  - "scraping"
  - "web"
---

While continuing the interminable search for the ideal python editor, I run into three really useful libraries for scraping information off webpages:

- [mechanize](http://wwwsearch.sourceforge.net/mechanize/):  Stateful programmatic web browsing in Python, after Andy Lester's Perl module [`WWW::Mechanize`](http://search.cpan.org/dist/WWW-Mechanize/)
- [scrape](http://zesty.ca/python/scrape.html):  Python module for web browsing and scraping
- [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/): a Python HTML/XML parser designed for quick turnaround projects like screen-scraping

I had a quick play with the last one, BeautifulSoup, following one of the examples. Here I'm fetching the ICC Commercial Crime Services weekly piracy report, parsing it with Beautiful Soup, and pulling out the piracy incidents:

from BeautifulSoup import BeautifulSoup
import urllib2

page \= urllib2.urlopen("http://www.icc\-ccs.org/index.php?
            option\=com\_fabrik&view\=table&tableid\=70&calculations\=0&Itemid\=82")
soup \= BeautifulSoup(page)

for incident in soup('td',
         {"class" : "fabrik\_row\_\_\_jos\_fabrik\_icc-ccs-piracymap2009\_testing\_\_\_narrations"}):
    print "nAn incident :"
    print incident.next.renderContents()
    print incident.next.next.next.next.next.renderContents()

And the result is the following:

```

An incident :
21.07.2009: 0030 LT: Posn: 01:17.94N – 104:09.24E, Off Tanjong Stapa, Malaysia.
Six robbers armed with long knives in a boat came alongside and boarded a product tanker at anchor.
The robbers tied up the Master and crew members. They stole ship’s and crew properties.
During the incident the Malaysian Marine Police boarded the product tanker and arrested five robbers.
One robber jumped overboard and escaped.

An incident :
12.07.2009: 0330 LT: Posn: 10:16.2N - 107:04.6E, Vungtau outer anchorage, Vietnam.
Robbers boarded a container ship at anchor. They stole ship's stores and properties and escaped.

An incident :
12.07.2009: 0200 LT: Posn: 01:08.91N – 105:45.11E, Off Raffles lighthouse, Singapore Straits.
Five pirates armed with long knives and swords in a five meter long wooden boat approached a tug
towing a barge. Four pirates boarded the tug, and tied up the crew. They stole ship’s properties,
crew personal belongings and cash and escaped. No injuries to crew. VTIS and coast guard Singapore informed.
[Task exited status=0]
```

Nice and easy uh?
