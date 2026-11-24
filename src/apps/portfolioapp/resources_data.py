"""
What the Resources page lists (#22, prototype). Hand-kept for now: guides are
the interactive one-pagers in static/pages/, decks are talk slides.

A deck's `pdf` is a file on the support site, by default
public_slides/<thumb>.pdf (support.michelepasin.org repo, docs/public_slides/).
Set `hosted=False` on a new deck until its PDF is uploaded; with DRAFT on, the
page marks it. The decks that were on SlideShare were downloaded from there on
2026-11-24; the account's inventory CSV is in the researcher backlog,
plans/022-resources-page/slideshare/.
`pub` is the Publication id the deck belongs to, `post` a blog post that
presents it, `also` the ids of other talks that used the same deck (Events
links them to it too). Thumbnails are static/resources/decks/<thumb>.jpg.
"""

# Marks the decks not uploaded yet, and the match notes. Off when publishing.
DRAFT = False

SUPPORT = "https://lambdamusic.github.io/support.michelepasin.org/public_articles/"
# Where decks go by default. A few decks were on the support site before the
# Resources page, in public_articles/ with their papers; they keep those URLs.
SLIDES = "https://lambdamusic.github.io/support.michelepasin.org/public_slides/"

GUIDES = [
	{
		"title": "Quiver, don't Quake: a field guide",
		"url": "/media/static/pages/quiver-dont-quake-field-guide.html",
		"img": "blog_img/2026-11-13-quiver-dont-quake-field-guide.jpg",
		"post": "/blog/2026/11/13/quiver-dont-quake/",
		"meta": "2026 · themes, critics and quotes from Nadim Sadek's book",
	},
	{
		"title": "The Mom Test: a field guide",
		"url": "/media/static/pages/mom-test-field-guide.html",
		"img": "blog_img/2026-10-11-mom-test-field-guide.jpg",
		"post": "/blog/2026/10/11/the-mom-test/",
		"meta": "2026 · how to ask customers questions they can't lie about",
	},
	{
		"title": "Deep Work: a field guide",
		"url": "/media/static/pages/deep-work-field-guide.html",
		"img": "blog_img/2023-07-01-deep-work-field-guide.jpg",
		"post": "/blog/2023/07/01/deep-work/",
		"meta": "2023 · Cal Newport's rules for focused work",
	},
]


def _deck(date, title, event, thumb, pdf=None, hosted=True, pub=None, post=None,
		slideshare=None, note="", also=()):
	return {
		"date": date, "title": title, "event": event, "thumb": thumb,
		"pdf": pdf or SLIDES + thumb + ".pdf", "hosted": hosted,
		"pub": pub, "post": post, "slideshare": slideshare, "note": note,
		"also": also,
	}


# Newest first. The KR seminar decks are dated by their title slides (June
# 2010, July for FRBR-OO); the Dropbox folder that holds them says 2011.
DECKS = [
	_deck("2026-04", "Dimensions as scientific data infrastructure: funding data, international flows, and open access",
		"CLACSO, Tracking research funding flows in the Global South, Buenos Aires",
		"2026-04-clacso-buenos-aires-dimensions-funding-data", pub=552,
		post="/blog/2026/04/21/funding-flows-global-south-clacso/"),
	_deck("2025-06", "Performing research analytics at scale using Dimensions and BigQuery",
		"Invited talk, NSLP 2025 workshop at ESWC, Portorož; also KMI, The Open University, May 2025",
		"2025-06-eswc-nslp-research-analytics-dimensions-bigquery", pub=541, also=(542,)),
	_deck("2023-07", "Designing great dashboards: tips from data visualization and information architecture",
		"A slide deck for dashboard developers", "2023-07-designing-great-dashboards",
		post="/blog/2023/07/06/designing-great-dashboards/",
		slideshare="https://www.slideshare.net/slideshow/designing-great-dashboards-a-slidedeck-for-dashboard-developers/259009125"),
	_deck("2022-09", "Generating large-scale network analyses of scientific landscapes in seconds using Dimensions on Google BigQuery",
		"STI 2022, Granada", "2022-09-sti-granada-network-analyses-dimensions",
		slideshare="https://www.slideshare.net/slideshow/sti-2022-generating-largescale-network-analyses-of-scientific-landscapes-in-seconds-using-dimensions-on-google-bigquery/252899991"),
	_deck("2021-11", "The Dimensions APIs: harness the full power of Dimensions data",
		"API training for the US National Institutes of Health (NIH)",
		"2021-11-nih-dimensions-api-training"),
	_deck("2020-07", "Prosopography and computer ontologies", "Prosopography summer school",
		"2020-07-prosopography-summer-school"),
	_deck("2019-06", "Modeling publications in SN SciGraph 2012–2019",
		"Workshop on Scholarly Digital Editions, Lausanne",
		"2019-06-lausanne-modeling-publications-scigraph",
		pdf=SUPPORT + "2019-Pasin-Lausanne.pdf", hosted=True, pub=69),
	_deck("2018-10", "Building business tools for scholarly publishing with LOD and the ELK stack",
		"The Getty Research Institute", "2018-10-getty-scigraph-lod-elk", pub=61),
	_deck("2017-12", "Building a linked open data knowledge graph",
		"London Info International; also Frankfurt Book Fair and the Japan Library Forum",
		"2017-12-lod-knowledge-graph-london-info",
		pdf=SUPPORT + "2017_Pasin_London_Info_International_Scigraph.pdf", hosted=True, pub=59),
	_deck("2016-11", "Linked open data at Springer Nature", "ODI Summit 2016, London",
		"2016-11-odi-summit-linked-open-data-springer-nature", pub=52,
		post="/blog/2016/10/21/open-data-summit-2016/",
		slideshare="https://www.slideshare.net/mpasin/linked-open-data-at-springer-nature"),
	_deck("2016-09", "Linked data experiences at Springer Nature", "SEMANTiCS 2016 keynote, Leipzig",
		"2016-09-semantics-leipzig-linked-data-springer-nature", pub=51,
		post="/blog/2016/10/25/leipzig-semantics-2016-conference/",
		slideshare="https://www.slideshare.net/mpasin/linked-data-experiences-at-springer-nature"),
	_deck("2015-10", "The nature.com ontologies portal", "Linked Science workshop, ISWC 2015, Bethlehem",
		"2015-10-linked-science-nature-ontologies-portal", pub=49,
		slideshare="https://www.slideshare.net/mpasin/the-naturecom-ontologies-portal-linked-science-2015"),
	_deck("2014-10", "Linked data experience at Macmillan", "ISWC 2014, Riva del Garda",
		"2014-10-iswc14-linked-data-macmillan", pub=47,
		post="/blog/2014/11/25/iswc14-paper-a-hybrid-semantic-publishing-architecture-combining-xml-and-rdf/",
		slideshare="https://www.slideshare.net/mpasin/linked-data-experience-at-macmillan-building-discovery-services-for-scientific-and-scholarly-content-on-top-of-a-semantic-data-model"),
	_deck("2013-04", "Exploring highly interconnected humanities data: are faceted browsers always the answer?",
		"Bliss Classification Association annual lecture", "2013-04-bliss-faceted-browsers-dh",
		pdf=SUPPORT + "2013-Pasin-BlissPresentation.pdf", hosted=True, pub=44,
		post="/blog/2013/04/27/annual-bliss-classification-association-lecture-using-faceted-browsers-in-the-dh/"),
	_deck("2011-11", "Semantic Web approaches in digital history: an introduction",
		"Digital history course, King's College London", "2011-10-ddh-semantic-web-digital-history",
		pub=39, slideshare="https://www.slideshare.net/mpasin/semantic-web-approaches-in-digital-history-an-introduciton"),
	_deck("2011-09", "Prosopography and computer ontologies: the 'factoid' model in CIDOC-CRM",
		"Representing Knowledge in the Digital Humanities, Kansas", "2011-09-kansas-prosopography-factoid",
		pub=34, slideshare="https://www.slideshare.net/mpasin/prosopography-and-computer-ontologies-towards-a-formal-representation-of-the-factoid-model-by-means-of-cidoccrm"),
	_deck("2011-07", "Introduction to the Impromptu livecoding environment",
		"Libre Software Meeting 2011, Strasbourg", "2011-07-livecoding-impromptu-strasbourg", pub=33,
		post="/blog/2011/07/11/workshop-on-live-coding-rmll-11/",
		slideshare="https://www.slideshare.net/mpasin/livecoding-with-impromptu"),
	_deck("2011-06", "An ontological view of canonical citations (with Matteo Romanello)",
		"Digital Humanities 2011, Stanford", "2011-06-dh11-canonical-citations", pub=29,
		post="/blog/2011/06/30/digital-humanities-conference-2011-a-short-review/",
		slideshare="https://www.slideshare.net/mpasin/an-ontological-view-of-canonical-citations-8597680"),
	_deck("2011-06", "Browsing interconnected humanities databases with multi-result faceted browsers",
		"Digital Humanities 2011, Stanford", "2011-06-dh11-faceted-browsers",
		post="/blog/2011/06/30/digital-humanities-conference-2011-a-short-review/",
		slideshare="https://www.slideshare.net/mpasin/dh11-browsing-highly-interconnected-humanities-databases-through-multiresult-faceted-browsers"),
	_deck("2011-03", "Using formal models in the humanities: challenges and misdirections",
		"Laboratory for Applied Ontology, Trento", "2011-03-loa-formal-models-humanities",
		pdf=SUPPORT + "2011-Pasin-LOA-Slides.pdf", hosted=True, pub=32),
	_deck("2011-02", "Research challenges in EMLoT: a digital humanities perspective",
		"Early Modern London Theatres, Globe Theatre", "2011-02-emlot-research-challenges",
		pdf=SUPPORT + "2011-Pasin-Slides-GlobeLondon.pdf", hosted=True, pub=27),
	_deck("2010-10", "How do philosophers think their own discipline?", "ECAP 2010, Munich",
		"2010-10-ecap10-how-philosophers-think-their-discipline", pub=20,
		slideshare="https://www.slideshare.net/mpasin/how-do-philosophers-think-their-own-disciplines"),
	_deck("2010-10", "Ontologies and the Semantic Web: an introduction", "Lecture, King's College London",
		"2010-10-cch-ontologies-lecture"),
	_deck("2010-07", "Knowledge representation seminar 3: introducing FRBR-OO",
		"Centre for Computing in the Humanities, King's College London",
		"2010-07-cch-kr-workshop-2-2-frbroo", post="/blog/2010/08/30/kr-workshop-2-introducing-cidoc-crm-and-frbr-oo/",
		slideshare="https://www.slideshare.net/mpasin/introducing-frbroo-cch-kr-workshop-22"),
	_deck("2010-06", "Knowledge representation seminar 2: introducing CIDOC-CRM",
		"Centre for Computing in the Humanities, King's College London",
		"2010-08-cch-kr-workshop-2-1-cidoc-crm", post="/blog/2010/08/30/kr-workshop-2-introducing-cidoc-crm-and-frbr-oo/",
		slideshare="https://www.slideshare.net/mpasin/cch-kr-workshop-22"),
	_deck("2010-06", "Knowledge representation seminar 1: ontologies",
		"Centre for Computing in the Humanities, King's College London",
		"2010-07-cch-kr-workshop-1-ontologies", post="/blog/2010/07/26/knowledge-representation-workshop-cch/",
		slideshare="https://www.slideshare.net/mpasin/kr-workshop-1-ontologies"),
	_deck("2010-06", "Data integration perspectives from the LTB project", "SDH-SEMI 2010, Montreal",
		"2010-06-sdh-semi-montreal"),
	_deck("2010-03", "Ontological requirements for the smart navigation of philosophical resources",
		"Mizoguchi Lab, Osaka University", "2010-03-mizoguchi-lab-philosophical-resources",
		pdf=SUPPORT + "2010-Pasin-MizoLab-Slides.pdf", hosted=True, pub=31),
	_deck("2009-06", "Laying the conceptual foundations for data integration in the humanities",
		"Digital Humanities 2009, Maryland", "2009-06-dh09-conceptual-foundations-data-integration",
		pub=1, slideshare="https://www.slideshare.net/mpasin/digital-humanities-2009-laying-out-the-conceptual-foundations-for-data-integration-in-the-humanities"),
]


def slides_by_pub():
	"""Publication id -> deck PDF URL: each deck's `pub`, and the talks in its `also`."""
	slides = {}
	for d in DECKS:
		for pub_id in ((d["pub"],) if d["pub"] else ()) + tuple(d["also"]):
			slides[pub_id] = d["pdf"]
	return slides
