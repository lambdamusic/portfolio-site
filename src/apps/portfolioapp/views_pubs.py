#!/usr/bin/env python
# encoding: utf-8

from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.http import urlquote
from django.http import HttpResponse, HttpResponseNotFound
from django.db.models import Q

import os
from time import strftime
import markdown
# import time
# import random

from render_block import render_block_to_string

from settings import STATICFILES_DIRS, BLOGS_ROOT
from myutils.myutils import printDebug

from researchapp.models import *
from researchapp.topics import *

from researchapp.management.commands.do_blogs_reindex import parse_markdown

APP = "portfolioapp"




def words(request):
	"""
	papers + blogs mega index LIST page
	"""
	context = {}

	query = request.GET.get('query', 'date')
	ttype = request.GET.get('type', 'all')
	tag = request.GET.get('tag', None)
	format = request.GET.get('format', 'html')
	
	if request.user.is_superuser:
		admin_change_url = True
	else:
		admin_change_url = False

	if format == 'bibtex':
		ttype = "papers" # show only research // PS filtered also in template!
		templatee = "papers.bibtex.txt"

	elif format == 'txt':
		ttype = "papers" # show only research 
		templatee = "papers.txt"

	else:
		templatee = "words.html"

	if ttype == 'tags':
		return_items = None
		tags = get_tags()
	else:
		return_items = get_pubs(query, ttype, tag)
		tags = None
	
	
	context = {
		'return_items': return_items,
		'urlname': "papers",
		'query': query,
		'ttype': ttype,
		'tag': tag,
		'admin_change_url': admin_change_url,
		'tags': tags,
	}
	
	return render(request, APP + '/pages/' + templatee, context)





def paper_detail(request, year="", month="", day="", namedetail=""):
	"""
	papers page
	"""
	context = {}

	permalink = f"""{year}/{month}/{day}/{namedetail}"""
	# PAPERS DETAILs

	return_item = get_object_or_404(Publication, permalink=permalink)

	try:  # bugfix after changing logic for speaking events
		pubtypegroup = return_item.pubtype.groupfk.name
	except:
		pubtypegroup = ""

	if request.user.is_superuser:
		admin_change_url = return_item.get_admin_url()
	else:
		admin_change_url = None

	# MUST NOT BE A BLOG
	if return_item.pubtype.pk == 13:  
		return Http404
	
	context = {
		'return_item' : return_item,
		'admin_change_url' : admin_change_url,
		'itemtitle': return_item.title,
		'itempubdate': return_item.pubdate,
		'summary': return_item.pub_summary(),
		'abstract': return_item.abstract,
		'year': return_item.pubdate.year,
		'all_urls': return_item.all_urls(),
		'type': pubtypegroup,
		'itemembed1': return_item.embedcode1,
		'all_papers_list' : get_related_pubs(return_item),
		# 'all_papers_list' : get_pubs('date')
	}

	templatee = "detail-papers.html"

	return render(request, APP + '/pages/' + templatee, context)




def blog_detail(request, year="", month="", day="", namedetail=""):
	"""
	blog detail page
	"""
	context = {}

	permalink = f"""{year}/{month}/{day}/{namedetail}"""
	# PAPERS DETAILs

	return_item = get_object_or_404(Publication, permalink=permalink)

	try:  # bugfix after changing logic for speaking events
		pubtypegroup = return_item.pubtype.groupfk.name
	except:
		pubtypegroup = ""

	if request.user.is_superuser:
		admin_change_url = return_item.get_admin_url()
	else:
		admin_change_url = None

	# MUST BE OF TYPE BLOG / MARKDOWN
	if not return_item.pubtype.pk == 13:  
		return Http404

	#
	# get the contents from the source MD files 
	blog_source_file = BLOGS_ROOT + return_item.md_file
	TITLE, DATE, REVIEW, CATS, TAGS, PURE_MARKDOWN = parse_markdown(blog_source_file)

	html_blog_entry = markdown.markdown(PURE_MARKDOWN, extensions=['fenced_code', 'codehilite'])

	context = {
		'return_item' : return_item,
		'admin_change_url' : admin_change_url,
		'itemtitle': return_item.title,
		'itempubdate': return_item.pubdate,
		'blog_source_file': blog_source_file,
		'blog_entry': html_blog_entry,
		'year': return_item.pubdate.year,
		'all_urls': return_item.all_urls(),
		'type': pubtypegroup,
		'all_papers_list' : get_related_pubs(return_item),
	}

	templatee = "detail-blogs.html"

	return render(request, APP + '/pages/' + templatee, context)






# ===========
# SUPPORT FUNCTIONS
# ===========


def get_pubs(query, ttype, tag):
	""" retrieves pubs info 
	
	query: the ordering parameter eg date or pubtype
	ttype: the (simplified) type filter  // September 3, 2021
	tag: a blog tag, default: 'all'

	pubType 12 = "Invited Talk"
	pubType 13 = "Blog"
	See http://127.0.0.1:8000/admin/researchapp/pubtype/

	"""

	type_talks = PubType.objects.get(pk=12)  # used to exclude 'INVITED TALKS' from articles list
	type_blogs = PubType.objects.get(pk=13) 

	QSET = Publication.objects.exclude(review=True)

	# SORT BY PUBTYPE eg Book, Article, Invited Talk etc..
	if query == 'type':
		# exclude talks and blog 'types'
		pubtypegroups_list = PubType.objects.exclude(pk=12).exclude(pk=13).values_list(
			'groupfk__name').order_by('groupfk__order').distinct()
		# eg [(u'Books',), (u'Journal Articles & Book Chapters',), (u'Articles in Peer-Reviewed Conference or Proceedings',), (u'White papers, Reports, etc.',)]
		# NOTE talks are excluded as they don't have any groupfk (meta pubtype)
		return_items = []
		for x in pubtypegroups_list:
			return_items.append(
				(x[0], QSET.exclude(pubtype=type_talks).filter(
					pubtype__groupfk__name=x[0])))
		return return_items

	# SORT BY PROJECT
	elif query == 'project':
		valid_projects = list(
			set([
				x[0] for x in QSET.exclude(
					pubtype=type_talks).values_list('project__title') if x[0]
			]))
		return_items = []
		for x in valid_projects:
			return_items.append((x, QSET.exclude(
				pubtype=type_talks).filter(project__title=x)))
		return_items.sort()  # sort by alpha
		# return_items.append(('Misc',
		# 					 QSET.filter(project=None)))
		return return_items


	# SORT BY DATE, with an optional filter for type
	else:
		# ==>  query == 'date':  
		# ==>  always fallback here

		# For the following options, ensure names are same as in http://127.0.0.1:8000/admin/researchapp/pubtypegroup/

		if ttype == "blogs":
			printDebug("ttype == blogs")
			printDebug(str(QSET.count()))
			ddset = QSET.filter(pubtype__groupfk__pk=6)
			printDebug(str(ddset.count()))

		elif ttype == "papers":

			ddset = QSET.exclude(pubtype=type_talks).exclude(pubtype__groupfk__pk=6).exclude(pubtype__groupfk__pk=3)

		elif ttype == "misc":

			ddset = QSET.filter(pubtype__groupfk__pk=3)

		elif ttype == "review":
			# SHOW ANYTHING IN REVIEW
			ddset = Publication.objects.filter(review=True)

		elif tag:
			# SHOW ANYTHING IN REVIEW
			ddset = Publication.objects.exclude(
				review=True).filter(tags__name=tag)


		else:

			ddset = QSET.exclude(pubtype=type_talks)

		valid_years = list(
			set([
				x[0].year for x in ddset.values_list('pubdate').distinct()
			]))
		return_items = []
		valid_years.sort(reverse=True)
		# print valid_years
		for x in valid_years:
			return_items.append((x, ddset.filter(pubdate__year=x)))
		return return_items





def get_related_pubs(a_pub):
	""" retrieves pubs info - with similar title"""

	talks = PubType.objects.get(
		pk=12)  # used to exclude 'INVITED TALKS' from articles list

	words = a_pub.title.split()
	words = [x for x in words if len(x) > 3]

	q = Q()
	for word in words:
		q |= Q(title__icontains = word)
	pubs = Publication.objects.exclude(
				pubtype=talks).exclude(
				review=True).filter(q)

	valid_years = list(
		set([
			x[0].year for x in pubs.values_list('pubdate').distinct()
		]))
	return_items = []
	valid_years.sort(reverse=True)
	# print valid_years
	for x in valid_years:
		return_items.append((x, pubs.filter(pubdate__year=x)))
	return return_items





def get_tags():
	""" retrieves tags info for the cloud viz
	
	The filtering is done in the template
	IE {% if tag.1 > 1 %}
	"""

	tagcloud_pubs = Tag.objects.values_list('name').distinct().annotate(cc=Count('publications'))

	return tagcloud_pubs
