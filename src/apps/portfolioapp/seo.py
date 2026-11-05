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
import re

from django.conf import settings
from django.templatetags.static import static


PERSON_ID = settings.SITE_URL + "/#person"
WEBSITE_ID = settings.SITE_URL + "/#website"

DEFAULT_IMAGE = "legacy/me_cartoon.jpg"  # static path; the portrait on /about/

# the same profiles the site links to (components/site-rail.html)
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


def seo_context(nodes=(), og_type="website", og_title="", og_image=""):
	return {
		'jsonld': jsonld(*nodes) if nodes else "",
		'og_type': og_type,
		'og_title': og_title,
		'og_image': og_image,
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


def _authors(pub):
	"""the publication's authors in order, Michele as the shared Person node"""
	people = []
	for a in pub.authorship_set.all().order_by("order", "id"):
		name = " ".join(x for x in [a.person.name, a.person.surname] if x)
		if name == "Michele Pasin":
			people.append({"@id": PERSON_ID})
		elif name:
			people.append({"@type": "Person", "name": name})
	return people or [{"@id": PERSON_ID}]


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
	links = [u for u in [pub.pdf_url, pub.url1, pub.url2, pub.url3] if u]
	dois = [u for u in links if "doi.org/" in u]
	if dois:
		node["identifier"] = {"@type": "PropertyValue", "propertyID": "DOI", "value": dois[0].split("doi.org/", 1)[1]}
		node["sameAs"] = dois
	if pub.pdf_url:
		node["encoding"] = {"@type": "MediaObject", "contentUrl": pub.pdf_url, "encodingFormat": "application/pdf"}
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
	"""absolute URL of the first <img> in some rendered HTML, or an empty string"""
	m = re.search(r'<img[^>]+src="([^"]+)"', html or "")
	return absolute(m.group(1)) if m else ""
