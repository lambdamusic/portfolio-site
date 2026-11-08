#!/usr/bin/env python
# encoding: utf-8

"""
Structured data (JSON-LD) and Open Graph values for the page templates.

Views put `seo_context(...)` into their context; components/base.html prints
`jsonld` in a <script type="application/ld+json"> and `og_*` in the meta tags.
Every URL is absolute and built from SITE_URL, since the pages are rendered on
127.0.0.1 and mirrored with wget.
"""

import json
import os
import re
from urllib.parse import unquote

from django.conf import settings
from django.templatetags.static import static


PERSON_ID = settings.SITE_URL + "/#person"
WEBSITE_ID = settings.SITE_URL + "/#website"

DEFAULT_IMAGE = "legacy/me_cartoon.jpg"  # static path; the portrait on /about/

# the same profiles the site links to (components/outlinks.html, in the footer)
SAME_AS = [
	"https://orcid.org/0000-0001-8909-7766",
	"https://github.com/lambdamusic",
	"https://scholar.google.com/citations?user=zj-99x0AAAAJ",
	"https://www.linkedin.com/pub/michele-pasin/1/223/a0",
	"https://x.com/lambdaman",
	"https://soundcloud.com/magicrebirth",
	"https://www.youtube.com/channel/UCanqSICbxzRNEZGMlu8qfyw",
]

# Publication.pubtype name -> schema.org type. Talks, slides and "Other" get
# no item of their own, only breadcrumbs.
PUBTYPE_SCHEMA = {
	"Journal Article": "ScholarlyArticle",
	"Conference article (peer-reviewed)": "ScholarlyArticle",
	"Workshop article (peer-reviewed)": "ScholarlyArticle",
	"Book Chapter": "ScholarlyArticle",
	"Poster": "ScholarlyArticle",
	"Book": "Book",
	"Thesis": "Thesis",
}

# project tags that name a programming language
LANGUAGE_TAGS = {"python": "Python", "lisp": "Lisp", "javascript": "JavaScript", "scheme": "Scheme"}


def absolute(url):
	"""absolute URL for a root-relative path; full URLs are returned as they are"""
	if not url:
		return ""
	return url if url.startswith(("http://", "https://")) else settings.SITE_URL + url


def static_url(path):
	return absolute(static(path))


def jsonld(*nodes):
	"""serialise schema.org nodes as one @graph, safe to print inside <script>"""
	data = {"@context": "https://schema.org", "@graph": [n for n in nodes if n]}
	return json.dumps(data, ensure_ascii=False, indent=1).replace("</", "<\\/")


def seo_context(nodes=(), og_type="website", og_title="", og_image="", citation_meta=()):
	return {
		'jsonld': jsonld(*nodes) if nodes else "",
		'og_type': og_type,
		'og_title': og_title,
		'og_image': og_image,
		'citation_meta': citation_meta,
	}


# ===========
# NODES
# ===========


def person(full=False):
	"""Michele: the full node for the homepage and /about/, a reference elsewhere"""
	node = {"@type": "Person", "@id": PERSON_ID, "name": "Michele Pasin", "url": settings.SITE_URL + "/"}
	if full:
		node.update({
			"jobTitle": "Ontology engineer",
			"image": static_url(DEFAULT_IMAGE),
			"mainEntityOfPage": settings.SITE_URL + "/about/",
			"identifier": {"@type": "PropertyValue", "propertyID": "ORCID", "value": "0000-0001-8909-7766"},
			"knowsAbout": ["Ontology engineering", "Knowledge graphs", "Artificial intelligence",
				"Data architecture", "Digital humanities", "Research analytics", "Livecoding"],
			"sameAs": SAME_AS,
		})
	return node


def website():
	return {
		"@type": "WebSite",
		"@id": WEBSITE_ID,
		"url": settings.SITE_URL + "/",
		"name": "Michele Pasin",
		"inLanguage": "en",
		"publisher": {"@id": PERSON_ID},
	}


def profile_page():
	return {
		"@type": "ProfilePage",
		"url": settings.SITE_URL + "/about/",
		"name": "About | Michele Pasin",
		"mainEntity": {"@id": PERSON_ID},
		"isPartOf": {"@id": WEBSITE_ID},
	}


def breadcrumbs(*crumbs):
	"""crumbs: (name, path) pairs; the last one is the page itself (path may be None)"""
	items = []
	for i, (name, path) in enumerate(crumbs, start=1):
		item = {"@type": "ListItem", "position": i, "name": name}
		if path:
			item["item"] = absolute(path)
		items.append(item)
	return {"@type": "BreadcrumbList", "itemListElement": items}


def blog_posting(pub, description, image=""):
	url = absolute(pub.get_absolute_url())
	node = {
		"@type": "BlogPosting",
		"@id": url + "#post",
		"mainEntityOfPage": url,
		"url": url,
		"headline": pub.title,
		"description": description,
		"datePublished": pub.pubdate.isoformat(),
		"inLanguage": "en",
		"author": {"@id": PERSON_ID},
		"publisher": {"@id": PERSON_ID},
		"isPartOf": {"@id": WEBSITE_ID},
		"keywords": [t.name for t in pub.tags.all()],
	}
	if image:
		node["image"] = image
	return node


def _author_names(pub):
	"""(first names, surname) of the publication's authors, in order"""
	people = [(a.person.name or "", a.person.surname or "")
		for a in pub.authorship_set.all().order_by("order", "id")]
	return [p for p in people if any(p)] or [("Michele", "Pasin")]


def _authors(pub):
	"""the publication's authors in order, Michele as the shared Person node"""
	people = []
	for first, last in _author_names(pub):
		name = " ".join(x for x in [first, last] if x)
		people.append({"@id": PERSON_ID} if name == "Michele Pasin" else {"@type": "Person", "name": name})
	return people


def _doi(pub):
	for u in [pub.pdf_url, pub.url1, pub.url2, pub.url3]:
		if u and "doi.org/" in u:
			return u.split("doi.org/", 1)[1]
	return ""


def _pdf_url(pub):
	u = pub.pdf_url or ""
	return u if u.startswith(("http://", "https://")) else ""


# Publication.pubtype name -> the Google Scholar tag for its venue
VENUE_TAG = {
	"Journal Article": "citation_journal_title",
	"Conference article (peer-reviewed)": "citation_conference_title",
	"Workshop article (peer-reviewed)": "citation_conference_title",
	"Poster": "citation_conference_title",
	"Book Chapter": "citation_inbook_title",
}


def citation_meta(pub):
	"""Google Scholar <meta name="citation_*"> tags for a paper, as (name, value)
	pairs; none for talks and slides. https://scholar.google.com/intl/en/scholar/inclusion.html"""
	if pub.pubtype.name not in PUBTYPE_SCHEMA:
		return []
	tags = [("citation_title", pub.title)]
	tags += [("citation_author", ", ".join(x for x in [last, first] if x)) for first, last in _author_names(pub)]
	tags.append(("citation_publication_date", pub.pubdate.strftime("%Y/%m/%d")))
	venue = pub.journal or pub.conference
	if pub.pubtype.name in VENUE_TAG and venue:
		tags.append((VENUE_TAG[pub.pubtype.name], venue))
	if pub.pubtype.name == "Thesis" and pub.pubplace:
		tags.append(("citation_dissertation_institution", pub.pubplace))
	if _doi(pub):
		tags.append(("citation_doi", _doi(pub)))
	if _pdf_url(pub):
		tags.append(("citation_pdf_url", _pdf_url(pub)))
	tags.append(("citation_abstract_html_url", absolute(pub.get_absolute_url())))
	return tags


def publication(pub):
	"""ScholarlyArticle / Book / Thesis for a paper; None for talks and slides"""
	schema_type = PUBTYPE_SCHEMA.get(pub.pubtype.name)
	if not schema_type:
		return None
	url = absolute(pub.get_absolute_url())
	node = {
		"@type": schema_type,
		"@id": url + "#work",
		"mainEntityOfPage": url,
		"url": url,
		"headline": pub.title,
		"name": pub.title,
		"author": _authors(pub),
		"datePublished": pub.pubdate.isoformat(),
		"inLanguage": "en",
	}
	if pub.abstract:
		node["abstract"] = re.sub(r"<[^>]+>", "", pub.abstract).strip()
	venue = pub.journal or pub.conference
	if venue:
		node["isPartOf"] = {"@type": "Periodical" if pub.journal else "CreativeWork", "name": venue}
	if _doi(pub):
		node["identifier"] = {"@type": "PropertyValue", "propertyID": "DOI", "value": _doi(pub)}
		node["sameAs"] = "https://doi.org/" + _doi(pub)
	if _pdf_url(pub):
		node["encoding"] = {"@type": "MediaObject", "contentUrl": _pdf_url(pub), "encodingFormat": "application/pdf"}
	return node


def project(p):
	"""SoftwareSourceCode when the project links to a GitHub repo, else CreativeWork"""
	from myutils.modelextra.mymodels import meta_description
	url = absolute(p.get_absolute_url())
	repos = [u for u, _ in p.all_urls() if "github.com/" in u]
	node = {
		"@type": "SoftwareSourceCode" if repos else "CreativeWork",
		"@id": url + "#project",
		"mainEntityOfPage": url,
		"url": url,
		"name": p.title,
		"description": meta_description(p.description, p.short_title),
		"author": {"@id": PERSON_ID},
		"isPartOf": {"@id": WEBSITE_ID},
		"image": project_image(p),
		"keywords": [t.name for t in p.tags.all()],
	}
	if p.datefrom:
		node["dateCreated"] = p.datefrom.isoformat()
	if repos:
		node["codeRepository"] = repos[0]
		languages = [LANGUAGE_TAGS[t] for t in node["keywords"] if t in LANGUAGE_TAGS]
		if languages:
			node["programmingLanguage"] = languages
	return node


# ===========
# IMAGES
# ===========


def project_image(p):
	# the PNG source, not the grid's thumb.jpg: bigger, and fine for a social card
	return static_url("manual_img/%s/thumb.png" % p.urlstub.lower())


def first_image(html):
	"""absolute URL of the first <img> in some rendered HTML that exists, or an
	empty string. Old posts link some images that were never copied over (#8):
	skip those rather than put a broken image on the social card."""
	for src in re.findall(r'<img[^>]+src="([^"]+)"', html or ""):
		if src.startswith(settings.STATIC_URL):
			path = os.path.join(settings.STATICFILES_DIRS[0], unquote(src[len(settings.STATIC_URL):]))
			if not os.path.isfile(path):
				continue
		return absolute(src)
	return ""
