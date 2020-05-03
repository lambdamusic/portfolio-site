#!/usr/bin/env python
# encoding: utf-8

from django.shortcuts import render, redirect, get_object_or_404
from django.utils.http import urlquote
from django.http import HttpResponse, HttpResponseNotFound

import os
from time import strftime
import time
import random

from render_block import render_block_to_string
from .models import *


APP = "new_researchapp"


def home(request):
	"""
	just an index of what's available  in /static for this app
	"""


	context = {
		'query': '',
	}

	return render(request, APP + '/home.html', context)


# ===========
# dynamic views
# ===========

# @TODO

