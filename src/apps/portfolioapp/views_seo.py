#!/usr/bin/env python
# encoding: utf-8

"""
robots.txt and sitemap.xml. Both are fetched explicitly by tools/site-dump,
since wget only mirrors what pages link to.
"""

from django.conf import settings
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

from researchapp.models import Publication, Project, Item


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
	sub-pages, which only exist as wget's index.html%3Fk=… files.
	"""
	urls = []  # (path, lastmod date or None)

	for name in ['home', 'words', 'music', 'events', 'about', 'contact']:
		urls.append((reverse('portfolioapp:' + name), None))
	for k in ['kryos', 'rebirth', 'singles']:
		urls.append((f"/sounds/index.html%3Fk={k}.html", None))

	for p in Project.objects.exclude(review=True).order_by("-datefrom"):
		urls.append((p.get_absolute_url(), p.updated_at.date() if p.updated_at else None))

	# blogs are re-created on every reindex, so updated_at says nothing: use pubdate
	for p in Publication.objects.exclude(review=True).exclude(permalink="").exclude(permalink__isnull=True).order_by("-pubdate"):
		urls.append((p.get_absolute_url(), p.pubdate))

	# the items listed on the sounds pages (see views.sounds)
	items = Item.objects.exclude(review=True).exclude(urlstub="").filter(
		Q(atype__name__iexact="livecoding") | Q(atype__name__iexact="performance")
		| Q(atype__name__iexact="music"))
	for i in items:
		urls.append((reverse('portfolioapp:music-detail', args=[i.urlstub]), i.date))

	context = {'urls': [(settings.SITE_URL + path, lastmod) for path, lastmod in urls]}
	return render(request, 'portfolioapp/sitemap.xml', context, content_type="application/xml")
