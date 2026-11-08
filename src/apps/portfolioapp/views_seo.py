#!/usr/bin/env python
# encoding: utf-8

"""
robots.txt, sitemap.xml and the section-root redirects. All are fetched
explicitly by tools/site-dump, since wget only mirrors what pages link to.
"""

from django.conf import settings
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

from researchapp.models import Publication, Project, Item


def section_redirect(request, target="/"):
	"""a section root with no page of its own, e.g. /blog/ -> /words/"""
	return render(request, 'portfolioapp/pages/section-redirect.html', {'target': target})


def robots_txt(request):
	lines = [
		"User-agent: *",
		"Allow: /",
		"",
		f"Sitemap: {settings.SITE_URL}/sitemap.xml",
	]
	return HttpResponse("\n".join(lines) + "\n", content_type="text/plain")


def sitemap_xml(request):
	"""
	Every indexable page, as its canonical URL (see components/base.html):
	https, trailing slash, no index.html, no query strings except the sounds
	sub-pages, which only exist as wget's index.html%3Fk=… files. The sounds
	detail pages are the exception to the trailing slash.
	"""
	urls = []  # (path, lastmod date or None)

	# /contact/ is a redirect to the end of /about/ since 2026-11-08
	for name in ['home', 'words', 'music', 'events', 'about']:
		urls.append((reverse('portfolioapp:' + name), None))
	# the singles tab is part of the Sounds page since 2026-11-08
	for k in ['kryos', 'rebirth']:
		urls.append((f"/sounds/index.html%3Fk={k}.html", None))

	for p in Project.objects.exclude(review=True).order_by("-datefrom"):
		urls.append((p.get_absolute_url(), p.updated_at.date() if p.updated_at else None))

	# blogs are re-created on every reindex, so updated_at says nothing: use pubdate
	# talks are left out of the Words lists and only linked from /events/, which
	# shows the isspeaking ones: the rest are never mirrored (see views.events)
	pubs = Publication.objects.exclude(review=True).exclude(permalink="").exclude(permalink__isnull=True)
	pubs = pubs.exclude(pubtype__pk=12, isspeaking=False)
	for p in pubs.order_by("-pubdate"):
		urls.append((p.get_absolute_url(), p.pubdate))

	# the singles on the Sounds page (see views.sounds_page). They link to
	# their detail pages without the trailing slash, so that is the URL served.
	# Kryos and Rebirth (7, 34) have their own ?k= pages instead; livecoding
	# pieces are blog posts now, already listed above, and their old item
	# pages are redirects.
	items = Item.objects.exclude(review=True).exclude(urlstub="").exclude(id__in=[7, 34]).filter(
		atype__name__iexact="music")
	for i in items:
		urls.append((f"/sounds/{i.urlstub.lower()}", i.date))

	context = {'urls': [(settings.SITE_URL + path, lastmod) for path, lastmod in urls]}
	return render(request, 'portfolioapp/sitemap.xml', context, content_type="application/xml")
