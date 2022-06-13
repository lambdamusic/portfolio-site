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

# from researchapp.management.commands.do_blogs_reindex import parse_markdown

APP = "portfolioapp"

QUOTES_SOURCE_DIR = "/Users/michele.pasin/Dropbox/Apps/NVALT/003/"
# QUOTES_SOURCE_DIR = "/Users/michele.pasin/Desktop/003/"

import itertools
def quotes_all(request):
	"""
	TODO
	"""
	context = {}

	query = request.GET.get('query', 'date')
	tag = request.GET.get('tag', None)
	format = request.GET.get('format', 'html')
	
	if request.user.is_superuser:
		admin_change_url = True
	else:
		admin_change_url = False

	templatee = "quotes.html"

	# return_items = get_quotes(query, tag)
	files_data = read_all_files_data(tag)
	
	tags = count_tags(files_data)
	print(f"\nTags total: {len(tags)}")
	tags = sorted(tags.items()) # turn into a list

	context = {
		'return_items': files_data,
		'admin_change_url': admin_change_url,
		'urlname': "quotes",
		'query': query,
		'tag': tag,
		'tags': tags,
	}
	
	return render(request, APP + '/pages/' + templatee, context)




def quote_detail(request, slug):
	"""
	TODO
	"""
	context = {}

	templatee = "detail-quotes.html"

	quote_source_file = QUOTES_SOURCE_DIR+slug+".md"
	TITLE, SOURCE, SOURCE_URL, DATE, MODIFIED, REVIEW, TAGS, PURE_MARKDOWN = parse_markdown(quote_source_file)
	html_quote_text = markdown.markdown(PURE_MARKDOWN, extensions=['fenced_code', 'codehilite'])

	print(f"Showing: \n\t=> {quote_source_file}\n")

	context = {
		'quote_text': html_quote_text,
		'quote_source_file': quote_source_file,
		'title': TITLE,
		'tags': TAGS,
		'source': SOURCE,
		'source_url': SOURCE_URL,
		'created': DATE,
		'modified': MODIFIED,
	}

	
	return render(request, APP + '/pages/' + templatee, context)





##################################
###
# Support Functions
###
##################################


def read_all_files_data(tag=""):
	"""
	Reads MD files
	Returns a list of dicts with the following keys:
		title
		filename
		tags
		review
	"""
	counter1, counter2, counter3 = 0, 0, 0
	files_data = []

	for filename in os.listdir(QUOTES_SOURCE_DIR):
		counter1 +=1
		if "-" in filename and filename.endswith(".md"):

			counter2 +=1
			quote =  {}

			TITLE, SOURCE, SOURCE_URL, DATE, MODIFIED, REVIEW, TAGS, PURE_MARKDOWN = parse_markdown(QUOTES_SOURCE_DIR+"/"+filename)

			quote['filename'] = filename
			quote['title'] = TITLE
			quote['tags'] = TAGS
			quote['review'] = REVIEW

			if tag and tag in TAGS:
				counter3 +=1
				files_data += [quote]
			elif not tag:
				counter3 +=1
				files_data += [quote]
			else:
				pass

	# finally

	printDebug(f"""\n# Files read: {counter1}\n# Records parsed: {counter2}\n# Records selected: {counter3}\n""", "bold")
	return(files_data)





def count_tags(files_data):
	"""
	Quick count of quotes per tags

	Return a dict EG
	 {'such-benefits': 1, 'relata': 1, 'notion-of-sign': 1, 'true-self': 1, 'recognition': 1}
	"""
	tags = {}
	for quote in files_data:
		for tag in quote['tags']:
			if str(tag) not in tags:
				tags[str(tag)] = 1
			else:
				tags[str(tag)] += 1
	return tags



def parse_markdown(full_file_path, verbose=False): 
	"""Parse the Obsidian markdown and return title and other metadata. 

	EG 
	```
---
template: quote.html
title: "Instance of a property"
source: "Cidoc-crm Version 4.2.4 - Reference Document"
url: http://www.google.co.uk/url?sa=t&rct=j&q=cidoc-crm%20version%204.2.4%20-%20reference%20document&source=web&cd=1&ved=0CEMQFjAA&url=http%3A%2F%2Fwww.cidoc-crm.org%2Fprevious_releases_cidoc.html&ei=xjnMT
date: 2013-02-26
modified: 2015-05-04
review: false
---
#properties #factual-relation #instances #relation #range #intension


	==This is where the markdown content starts..==
	```

	"""

	DEBUG_TAGS = False

	if verbose: printDebug("Parsing..: \n" + full_file_path)
	with open(full_file_path) as f:
		lines = f.readlines()
		text_begins_flag = tag_flag = 0
		TITLE, SOURCE, SOURCE_URL, PURE_MARKDOWN = "", "", "", ""
		REVIEW = False
		DATE, MODIFIED = None, None
		TAGS = []
		for l in lines:
			# printDebug(l)
			if tag_flag and text_begins_flag == 2:
				PURE_MARKDOWN += l
			elif l == "---\n":
				text_begins_flag += 1  # after second one, the header is over
			elif l.strip().startswith("#"):
				tag_flag = 1
				tags = [x.replace("#", "") for x in l.strip().split()]
				if DEBUG_TAGS: print(f"Tags: {tags}")
				TAGS = tags
			elif l.startswith("title: "):
				TITLE = l.replace("title: ", "")[1:-2] # remove quotes and newline char
			elif l.startswith("source: "):
				SOURCE = l.replace("source: ", "")[1:-2] # remove quotes and newline char
			elif l.startswith("url: "):
				SOURCE_URL = l.replace("url: ", "")[0:-1] # remove newline char
			elif l.startswith("review: "):
				if "true" in l:
					REVIEW = True
			elif l.startswith("date: "):
				DATE = l.replace("date: ", "") 
				if DATE[0] == "\"":
					DATE = DATE[1:-2] # remove quotes and newline char
				else:
					DATE = DATE[:-1] # remove newline char
				DATE = datetime.datetime.strptime(DATE, "%Y-%m-%d")
				DATE = DATE.replace(tzinfo=datetime.timezone.utc).date()
			elif l.startswith("modified: "):
				MODIFIED = l.replace("modified: ", "") 
				if MODIFIED[0] == "\"":
					MODIFIED = MODIFIED[1:-2] # remove quotes and newline char
				else:
					MODIFIED = MODIFIED[:-1] # remove newline char
				MODIFIED = datetime.datetime.strptime(MODIFIED, "%Y-%m-%d")
				MODIFIED = MODIFIED.replace(tzinfo=datetime.timezone.utc).date()
		
		return TITLE, SOURCE, SOURCE_URL, DATE, MODIFIED, REVIEW, TAGS, PURE_MARKDOWN
		