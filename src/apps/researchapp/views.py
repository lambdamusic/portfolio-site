#!/usr/bin/env python
# encoding: utf-8

from django.shortcuts import render, redirect, get_object_or_404
from django.utils.http import urlquote
from django.http import HttpResponse, HttpResponseNotFound
from django.db.models import Q

from time import strftime

from render_block import render_block_to_string
from .models import *


def home(request):
    """
    landing page

    """

    val = request.GET.get("val", None)

    context = {
        'query': val,
    }

    return render(request, 'researchapp/home.html', context)
