"""
What the Resources page lists besides the database (#22). Guides are the
interactive one-pagers in static/pages/.

Talk slides live in the database: a Publication's `slides_url` (a PDF on the
support site, usually public_slides/) puts it on the Resources page, on Events
and on its own talk or paper page. EXTRA_DECKS is only for the few decks that
have no talk or paper record. A deck's thumbnail is
static/resources/decks/<PDF file name without .pdf>.jpg, see deck_thumb().

The decks that were on SlideShare were downloaded from there on 2026-11-24;
the account's inventory CSV is in the researcher backlog,
plans/022-resources-page/slideshare/.
"""

import os
from urllib.parse import urlparse

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


def deck_thumb(pdf_url):
	"""The thumbnail's name: the PDF's file name without .pdf."""
	return os.path.splitext(os.path.basename(urlparse(pdf_url).path))[0]


def _deck(date, title, event, name, post="", slideshare=""):
	pdf = SLIDES + name + ".pdf"
	return {
		"date": date, "year": date[:4], "title": title, "event": event,
		"pdf": pdf, "thumb": deck_thumb(pdf), "pub_url": "", "pub_label": "",
		"post": post, "slideshare": slideshare,
	}


# Decks with no talk or paper record, newest first.
EXTRA_DECKS = [
	_deck("2023-07", "Designing great dashboards: tips from data visualization and information architecture",
		"A slide deck for dashboard developers", "2023-07-designing-great-dashboards",
		post="/blog/2023/07/06/designing-great-dashboards/",
		slideshare="https://www.slideshare.net/slideshow/designing-great-dashboards-a-slidedeck-for-dashboard-developers/259009125"),
	_deck("2021-11", "The Dimensions APIs: harness the full power of Dimensions data",
		"API training for the US National Institutes of Health (NIH)",
		"2021-11-nih-dimensions-api-training"),
]
