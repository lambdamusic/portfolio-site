#!/usr/bin/env python
# encoding: utf-8

from django.shortcuts import render, redirect, get_object_or_404
from django.utils.http import urlquote
from django.http import HttpResponse, HttpResponseNotFound
from django.db.models import Q, Count

import json
import os
from time import strftime
import markdown
# import time
# import random

from render_block import render_block_to_string

from settings import STATICFILES_DIRS, BLOGS_ROOT, FLICKR_API_KEY, FLICKR_API_SECRET
from myutils.myutils import add_lazy_loading_to_images

from researchapp.models import *
from researchapp.topics import *
from researchapp.pub_locations import coords_for

from researchapp.management.commands.do_blogs_reindex import parse_markdown
from . import seo
from .proto import current_layout, current_project_layout, current_sounds_layout

APP = "portfolioapp"


# ===========
# views with single landing page
# ===========


def home(request):
	"""
	the homepage is the projects grid, served at / (not redirected) so the
	homepage keeps its own URL; its canonical is / too (see pages/projects.html)

	Layout prototype C (proto.py) swaps it for a front page instead: recent
	writing, talks and sounds above a short selection of projects.
	"""
	if current_layout(request) == "c":
		return home_hub(request)
	return projects(request)


def home_hub(request):
	"""prototype C's homepage; the full grid stays at /projects/"""
	talks = PubType.objects.get(pk=12)
	pubs = Publication.objects.exclude(review=True)
	sounds = Item.objects.exclude(review=True).exclude(urlstub="").exclude(id__in=[7, 34]).filter(
		Q(atype__name__iexact="livecoding") | Q(atype__name__iexact="performance")
		| Q(atype__name__iexact="music")).order_by("-date")
	projects = Project.objects.exclude(review=True).order_by("-datefrom")
	context = {
		'latest_words': pubs.exclude(pubtype=talks).order_by('-pubdate')[:6],
		'latest_talks': pubs.filter(isspeaking=True).order_by('-pubdate')[:4],
		'latest_sounds': sounds[:4],
		'projects': projects[:8],
		'project_count': projects.count(),
		'canonical_path': '/',
	}
	context.update(seo.seo_context(nodes=[seo.website(), seo.person(full=True)], og_title="Michele Pasin"))
	return render(request, APP + '/pages/home-hub.html', context)



def about(request):
	"""
	bio page
	"""
	context = seo.seo_context(nodes=[seo.profile_page(), seo.person(full=True)], og_title="About | Michele Pasin")
	return render(request, APP + '/pages/about-bio.html', context)



def contact(request):
	"""
	bio page
	"""
	context = {}
	return render(request, APP + '/pages/about-contact.html', context)



def photos(request):
	"""
	photos page
	"""

	import flickrapi
	api_key = FLICKR_API_KEY
	secret = FLICKR_API_SECRET
	flickr = flickrapi.FlickrAPI(api_key, secret, cache=True)
	sets = flickr.photosets_getList(user_id='76186999@N00')
	sets_list = []

	for s in sets.find('photosets').findall('photoset'):
		# tip: inspect the s object to see what methods are available
		url = "https://www.flickr.com/photos/mikele/sets/%s/" % s.get(
			'id')
		d = (s[0].text, url, s.get('photos'))  # title, id and count
		sets_list += [d]
	context = {
		'sets_list' : sets_list
	}

	return render(request, APP + '/pages/photos.html', context)



def events(request):
	"""
	events page

	Alongside the list, emit the data for the world map: one entry per talk
	that has a known location, keyed by the same index the template puts on
	each list row so hovering either side can highlight the other.

	Unmapped places (a `pubplace` string with no entry in PUB_LOCATIONS)
	are simply skipped - the talk still lists, it just gets no dot. See
	researchapp/pub_locations.py, and `tools/geocode-pub-places`.
	"""

	return_items = Publication.objects.filter(
		isspeaking=True).order_by('-pubdate')

	map_points = []
	for i, pub in enumerate(return_items):
		latlon = coords_for(pub.pubplace)
		if not latlon:
			continue
		map_points.append({
			'i': i,
			'lat': latlon[0],
			'lon': latlon[1],
			'place': pub.pubplace.strip(),
			'year': pub.pubdate.year,
			'title': pub.title,
			'url': pub.get_absolute_url(),
		})

	context = {
		'return_items': return_items,
		'map_points_json': json.dumps(map_points),
		'mapped_count': len(map_points),
		'mapped_places': len({(p['lat'], p['lon']) for p in map_points}),
	}

	return render(request, APP + '/pages/events.html', context)



# ===========
# views with details pages 
# ===========


def projects(request, namedetail=""):
	"""
	projects page
	"""
	context = {}

	if not namedetail:

		# PROJECTS LIST PAGE

		_format = request.GET.get('format', 'html')
		_active_tag = request.GET.get('k', 'all')
		# print active_tag

		if _format == 'txt':
			tags = []
			projects = Project.objects.all()
			templatee = 'projects.txt'

		else:
			tags = Project.all_used_tags()
			if _active_tag not in tags:
				_active_tag = "all"
				projects = Project.objects.all().order_by("-datefrom")
			else:
				projects = Project.objects.filter(tags__name=_active_tag).order_by("-datefrom")
			templatee = 'projects.html'


		context = {
			'projects': projects,
			'tags': tags,
			'active_tag': _active_tag,
			'canonical_path': '/',  # / and /projects/ are the same page
		}
		# the grid is the homepage (canonical /): declare the site and its author
		context.update(seo.seo_context(nodes=[seo.website(), seo.person(full=True)], og_title="Michele Pasin"))


	else:

		# PROJECTS DETAIL PAGE 

		return_item = get_object_or_404(Project, urlstub=namedetail)

		projects = list(Project.objects.all())
		this_index = projects.index(return_item)

		# next = projects[this_index + 1] if len(projects) > (
		# 	this_index + 1) else projects[0]  # recursive
		# prev = projects[this_index - 1] if (this_index - 1) >= 0 else None

		# load images from manually managed folder

		project_images_names = []
		THUMBS_FILES = ["thumb.png", "thumb.jpg"]  # the grid thumbnail, not part of the gallery

		project_images_dir = STATICFILES_DIRS[
			0] + "/manual_img/" + return_item.urlstub
		if os.path.exists(project_images_dir):
			for f in os.listdir(project_images_dir):
				if os.path.isfile(os.path.join(project_images_dir, f)):
					if not f.startswith(".") and f not in THUMBS_FILES:
						project_images_names += [f]

		if request.user.is_superuser:
			admin_change_url = return_item.get_admin_url()
		else:
			admin_change_url = None


		html_description = markdown.markdown(return_item.description, extensions=['fenced_code', 'codehilite'])
		html_description = add_lazy_loading_to_images(html_description)

		context = {
			'admin_change_url': admin_change_url,
			'return_item': return_item,
			'return_item_desc': html_description,
			'project_images_names': sorted(project_images_names),
			# posts link here via their `project:` front matter, papers via the admin
			'project_writing': Publication.objects.filter(project=return_item).exclude(review=True).order_by('-pubdate'),
			'ALL_PROJECTS': Project.objects.all().order_by("-datefrom")
		}
		context.update(seo.seo_context(
			nodes=[seo.project(return_item), seo.person(),
				seo.breadcrumbs(("Home", "/"), (return_item.title, None))],
			og_title=return_item.title, og_image=seo.project_image(return_item)))

		templatee = "detail-projects.html"

		if current_project_layout(request):
			context.update(project_proto_context(return_item))
			templatee = "detail-projects-proto.html"


	return render(request, APP + '/pages/' + templatee, context)





def sounds_proto(request):
	"""
	Prototype Sounds landing page (pages/sounds-proto.html): everything on one
	page. The pieces are blog posts with a `video:` front matter line, shown as
	YouTube thumbnails linking to the post (which has the player); the two
	albums as covers, singles as a list.
	"""
	import re

	pieces = list(Publication.objects.filter(pubtype__pk=13).exclude(review=True)
		.exclude(video="").order_by('-pubdate'))
	for pub in pieces:
		# "Livecoding: Xanadu" -> "Xanadu": the section heading already says it
		pub.display_title = re.sub(r"^(Livecoding|Event):\s*", "", pub.title)

	# Kryos and Rebirth Fever only have their ?k= pages; Rebirth has no cover
	albums = [
		(Item.objects.get(pk=7), "?k=kryos", "blog_img/Kryos-Noise-Cover.jpg"),
		(Item.objects.get(pk=34), "?k=rebirth", ""),
	]
	singles = Item.objects.exclude(review=True).exclude(id__in=[7, 34]).filter(
		atype__name__iexact="music").order_by('-date')

	context = {
		'pieces': pieces,
		'albums': albums,
		'singles': singles,
	}
	return render(request, APP + '/pages/sounds-proto.html', context)


def project_proto_context(return_item):
	"""
	Extras for the project page prototypes (pages/detail-projects-proto.html):
	links labelled by their site when they have no name, the writing linked
	to the project, and a few neighbours by shared tags for the footer.
	"""
	from urllib.parse import urlparse

	links = []
	for url, name in return_item.all_urls():
		host = urlparse(url).netloc
		if not name or name.startswith("http"):  # some names are just the URL again
			name = host[4:] if host.startswith("www.") else host
		links.append((url, name))

	writing = Publication.objects.filter(project=return_item).exclude(review=True).order_by('-pubdate')

	others = Project.objects.exclude(pk=return_item.pk)
	related = list(others.filter(tags__in=return_item.tags.all())
		.annotate(shared=Count('tags')).order_by('-shared', '-datefrom')[:4])
	if len(related) < 4:
		taken = [p.pk for p in related]
		related += list(others.exclude(pk__in=taken).order_by('-datefrom')[:4 - len(related)])

	return {
		'project_links': links,
		'project_writing': writing,
		'related_projects': related,
		'project_count': Project.objects.count(),
	}


def sounds(request, namedetail=""):
	"""
	new sounds page
	"""

	_subpage = request.GET.get('k', 'livecoding')
	context = {}
	if not namedetail:

		if _subpage == "livecoding" and current_sounds_layout(request):

			return sounds_proto(request)

		if _subpage == "livecoding":

			items = Item.objects.exclude(review=True).filter(
				Q(atype__name__iexact="livecoding")
				| Q(atype__name__iexact="performance"))

			templatee = "sounds-livecoding.html"

		elif _subpage == "kryos":

			items = Item.objects.filter(pk=7)

			templatee = "sounds-kryos.html"

		elif _subpage == "rebirth":

			items = Item.objects.filter(pk=34)

			templatee = "sounds-rebirth.html"

		elif _subpage == "singles":

			items = Item.objects.exclude(review=True).exclude(id__in=[7, 34]).filter(
			Q(atype__name__iexact="music"))

			templatee = "sounds-singles.html"

		else:

			return HttpResponseNotFound

		context = {
			'sounds_subpage' : _subpage,
			'items' : items,
		}
		if _subpage != "livecoding":
			# a real page behind ?k=, which the static site only has as wget's
			# index.html%3Fk=… file: make that file the canonical
			context['canonical_path'] = f"/sounds/index.html%3Fk={_subpage}.html"

	else:

		# the sounds pages link with urlstub|lower, e.g. ATMevent -> atmevent
		return_item = get_object_or_404(Item, urlstub__iexact=namedetail)
		next = None
		prev = None


		if request.user.is_superuser:
			admin_change_url = return_item.get_admin_url()
		else:
			admin_change_url = None

		context = {
			'return_item': return_item,  # 2021-08-31 pass full object
			'itemtitle': return_item.title,
			'admin_change_url' : admin_change_url,
			'itemdesc': return_item.description,
			'itemembed1': return_item.embedcode1,
			'itemembed2': return_item.embedcode2,
			'datefrom': return_item.date,
			'all_urls': return_item.all_urls(),
			# the sounds pages link here without the trailing slash, so wget
			# saves sounds/<stub>.html and the static site serves /sounds/<stub>
			'canonical_path': f"/sounds/{return_item.urlstub.lower()}",
		}
		templatee = "detail-sounds.html"

	return render(request, APP + '/pages/' + templatee, context)



# # ===========
# # SUPPORT FUNCTIONS
# # ===========


# def get_pubs(query, ttype):
# 	""" retrieves pubs info 
	
# 	query: the ordering parameter eg date or pubtype
# 	ttype: the (simplified) type filter  // September 3, 2021

# 	"""

# 	talks = PubType.objects.get(
# 		pk=12)  # used to exclude 'INVITED TALKS' from articles list

# 	QSET = Publication.objects.exclude(review=True)

# 	if query == 'type':
# 		# exclude talks and blog
# 		pubtypegroups_list = PubType.objects.exclude(pk=12).exclude(pk=13).values_list(
# 			'groupfk__name').order_by('groupfk__order').distinct()
# 		# eg [(u'Books',), (u'Journal Articles & Book Chapters',), (u'Articles in Peer-Reviewed Conference or Proceedings',), (u'White papers, Reports, etc.',)]
# 		# NOTE talks are excluded as they don't have any groupfk (meta pubtype)
# 		return_items = []
# 		for x in pubtypegroups_list:
# 			return_items.append(
# 				(x[0], QSET.exclude(pubtype=talks).filter(
# 					pubtype__groupfk__name=x[0])))
# 		return return_items


# 	elif query == 'project':
# 		valid_projects = list(
# 			set([
# 				x[0] for x in QSET.exclude(
# 					pubtype=talks).values_list('project__title') if x[0]
# 			]))
# 		return_items = []
# 		for x in valid_projects:
# 			return_items.append((x, QSET.exclude(
# 				pubtype=talks).filter(project__title=x)))
# 		return_items.sort()  # sort by alpha
# 		return_items.append(('Miscellaneous',
# 							 QSET.filter(project=None)))
# 		return return_items


# 	else:
# 		#  query == 'date':  ==>  always fallback here

# 		# http://127.0.0.1:8000/admin/researchapp/pubtypegroup/

# 		if ttype == "blogs":

# 			ddset = QSET.filter(pubtype__groupfk__pk=6)

# 		elif ttype == "papers":

# 			ddset = QSET.exclude(pubtype=talks).exclude(pubtype__groupfk__pk=6).exclude(pubtype__groupfk__pk=3)

# 		elif ttype == "misc":

# 			ddset = QSET.filter(pubtype__groupfk__pk=3)

# 		else:

# 			ddset = QSET.exclude(pubtype=talks)

# 		valid_years = list(
# 			set([
# 				x[0].year for x in ddset.values_list('pubdate').distinct()
# 			]))
# 		return_items = []
# 		valid_years.sort(reverse=True)
# 		# print valid_years
# 		for x in valid_years:
# 			return_items.append((x, ddset.filter(pubdate__year=x)))
# 		return return_items





# def get_related_pubs(a_pub):
# 	""" retrieves pubs info - with similar title"""

# 	talks = PubType.objects.get(
# 		pk=12)  # used to exclude 'INVITED TALKS' from articles list

# 	words = a_pub.title.split()
# 	words = [x for x in words if len(x) > 3]

# 	q = Q()
# 	for word in words:
# 		q |= Q(title__icontains = word)
# 	pubs = Publication.objects.exclude(
# 				pubtype=talks).exclude(
# 				review=True).filter(q)

# 	valid_years = list(
# 		set([
# 			x[0].year for x in pubs.values_list('pubdate').distinct()
# 		]))
# 	return_items = []
# 	valid_years.sort(reverse=True)
# 	# print valid_years
# 	for x in valid_years:
# 		return_items.append((x, pubs.filter(pubdate__year=x)))
# 	return return_items





