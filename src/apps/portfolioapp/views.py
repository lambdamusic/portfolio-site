#!/usr/bin/env python
# encoding: utf-8

from django.shortcuts import render, redirect, get_object_or_404
from django.utils.http import urlquote
from django.http import HttpResponse, HttpResponseNotFound
from django.db.models import Q

import os
from time import strftime
import time
import random

from settings import STATICFILES_DIRS

from render_block import render_block_to_string

from researchapp.models import *
from researchapp.topics import *

APP = "portfolioapp"


# ===========
# views with single landing page
# ===========


def home(request):
	"""
	just an index of what's available  in /static for this app
	"""

	context = {
		'top_topics' :	top_topics,
		'topics_links' :	topics_links,
		'topics_unique' :	topics_unique,
	}

	return render(request, APP + '/home.html', context)


def about(request):
	"""
	about page
	"""
	context = {
		'top_topics' :	top_topics,
		'topics_links' :	topics_links,
		'topics_unique' :	topics_unique,
	}

	return render(request, APP + '/pages/about.html', context)


def contact(request):
	"""
	contact page
	"""

	context = {
	}

	return render(request, APP + '/pages/contact.html', context)




def photos(request):
	"""
	photos page
	"""

	import flickrapi
	api_key = "6b36d6a49a7abb07d8f156bbe5562380"
	secret = "920639143ba2cd27"
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
	"""

	return_items = Publication.objects.filter(
		isspeaking=True).order_by('-pubdate')

	context = {
		'return_items': return_items,
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
		}


	else:

		# PROJECTS DETAIL PAGE 

		return_item = get_object_or_404(Project, urlstub=namedetail)

		projects = list(Project.objects.all())
		this_index = projects.index(return_item)

		next = projects[this_index + 1] if len(projects) > (
			this_index + 1) else projects[0]  # recursive
		prev = projects[this_index - 1] if (this_index - 1) >= 0 else None

		# load images from manually managed folder

		project_images_names = []
		THUMBS_FILE = "thumb.png"

		project_images_dir = STATICFILES_DIRS[
			0] + "/manual_img/" + return_item.urlstub
		if os.path.exists(project_images_dir):
			for f in os.listdir(project_images_dir):
				if os.path.isfile(os.path.join(project_images_dir, f)):
					if not f.startswith(".") and f != THUMBS_FILE:
						project_images_names += [f]

		context = {
			'next': next,
			'prev': prev,
			'project': return_item,
			'project_images_names': sorted(project_images_names),
		}

		templatee = "detail-projects.html"


	return render(request, APP + '/pages/' + templatee, context)




def papers(request, namedetail=""):
	"""
	papers page
	"""
	context = {}

	if not namedetail:

		# PUBLICATIONS LIST  PAGE

		query = request.GET.get('query', 'date')
		format = request.GET.get('format', 'html')
		return_items = get_pubs(query)
		context = {
			'return_items': return_items,
			'urlname': "papers",
		}
		if format == 'bibtex':
			templatee = "papers.bibtex.txt"

		elif format == 'txt':
			templatee = "papers.txt"

		else:
			templatee = "papers.html"



	else:

		# PAPERS DETAILs

		return_item = get_object_or_404(Publication, id=namedetail)
		if return_item.pubtype.id == 12:
			# used to exclude 'INVITED TALKS' from articles list
			next, prev = None, None
		else:
			next, prev = return_item.next_prev_pubs()

		try:  # bugfix after changing logic for speaking events
			pubtypegroup = return_item.pubtype.groupfk.name
		except:
			pubtypegroup = ""

		context = {
			'itemtitle': return_item.title,
			'itempubdate': return_item.pubdate,
			'summary': return_item.pub_summary(),
			'abstract': return_item.abstract,
			'year': return_item.pubdate.year,
			'all_urls': return_item.all_urls(),
			'type': pubtypegroup,
			'itemembed1': return_item.embedcode1,
			'prev': prev,
			'next': next,
		}

		templatee = "detail-papers.html"

	return render(request, APP + '/pages/' + templatee, context)



def ontologies(request, namedetail=""):
	"""
	ontologies page
	"""


	if not namedetail:

		items = Item.objects.exclude(review=True).filter(
			Q(atype__name__iexact="ontology"))

		context = {
			'items' : items
		}
		templatee = "ontologies.html"

	else:

		return_item = get_object_or_404(Item, urlstub=namedetail)
		next = None
		prev = None

		context = {
			'itemtitle': return_item.title,
			'itemdesc': return_item.description,
			'itemembed1': return_item.embedcode1,
			'itemembed2': return_item.embedcode2,
			'datefrom': return_item.date,
			'all_urls': return_item.all_urls(),
			'next': next,
			'prev': prev,
		}
		templatee = "detail-ontologies.html"

	return render(request, APP + '/pages/' + templatee, context)


def livecoding(request, namedetail=""):
	"""
	livecoding page
	"""

	if not namedetail:

		items = Item.objects.exclude(review=True).filter(
			Q(atype__name__iexact="livecoding")
			| Q(atype__name__iexact="performance"))

		context = {
			'items' : items
		}

		templatee = "livecoding.html"
	
	else:

		return_item = get_object_or_404(Item, urlstub=namedetail)
		next = None
		prev = None

		context = {
			'itemtitle': return_item.title,
			'itemdesc': return_item.description,
			'itemembed1': return_item.embedcode1,
			'itemembed2': return_item.embedcode2,
			'datefrom': return_item.date,
			'all_urls': return_item.all_urls(),
			'next': next,
			'prev': prev,
		}
		templatee = "detail-livecoding.html"

	return render(request, APP + '/pages/' + templatee, context)




def music(request, namedetail=""):
	"""
	music page
	"""

	if not namedetail:

		items = Item.objects.exclude(review=True).filter(
			Q(atype__name__iexact="music"))

		context = {
			'items' : items
		}

		templatee = "music.html"

	else:

		return_item = get_object_or_404(Item, urlstub=namedetail)
		next = None
		prev = None

		context = {
			'itemtitle': return_item.title,
			'itemdesc': return_item.description,
			'itemembed1': return_item.embedcode1,
			'itemembed2': return_item.embedcode2,
			'datefrom': return_item.date,
			'all_urls': return_item.all_urls(),
			'next': next,
			'prev': prev,
		}
		templatee = "detail-music.html"

	return render(request, APP + '/pages/' + templatee, context)



# ===========
# SUPPORT FUNCTIONS
# ===========


def get_pubs(query):
	""" retrieves pubs info """

	talks = PubType.objects.get(
		pk=12)  # used to exclude 'INVITED TALKS' from articles list

	if query == 'type':
		pubtypegroups_list = PubType.objects.exclude(pk=12).values_list(
			'groupfk__name').order_by('groupfk__order').distinct()
		# eg [(u'Books',), (u'Journal Articles & Book Chapters',), (u'Articles in Peer-Reviewed Conference or Proceedings',), (u'White papers, Reports, etc.',)]
		# NOTE talks are excluded as they don't have any groupfk (meta pubtype)
		return_items = []
		for x in pubtypegroups_list:
			return_items.append(
				(x[0], Publication.objects.exclude(pubtype=talks).filter(
					pubtype__groupfk__name=x[0])))
		return return_items

	elif query == 'date':
		valid_years = list(
			set([
				x[0].year for x in Publication.objects.exclude(
					pubtype=talks).values_list('pubdate').distinct()
			]))
		return_items = []
		valid_years.sort(reverse=True)
		# print valid_years
		for x in valid_years:
			return_items.append((x, Publication.objects.exclude(
				pubtype=talks).filter(pubdate__year=x)))
		return return_items

	elif query == 'project':
		valid_projects = list(
			set([
				x[0] for x in Publication.objects.exclude(
					pubtype=talks).values_list('project__title') if x[0]
			]))
		return_items = []
		for x in valid_projects:
			return_items.append((x, Publication.objects.exclude(
				pubtype=talks).filter(project__title=x)))
		return_items.sort()  # sort by alpha
		return_items.append(('Miscellaneous',
							 Publication.objects.filter(project=None)))
		return return_items

	else:
		return None





