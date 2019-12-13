# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from ads.models import Ads

from django.template import loader
from django.http import HttpResponse
# Create your views here.

"""
def HomeRevs(request):
	revs = Ads.objects.filter(spot='index')

	template = loader.get_template('index.html')
	context = {
		'revs' : revs,
	}

	return HttpResponse(template.render(context, request))


def DetailRevs(request):
	revs = Ads.objects.filter(spot='detail')

	template = loader.get_template('entry_detail.html')
	context = {
		'revs' : revs,
	}

	return HttpResponse(template.render(context, request))


def SectionRevs(request):
	revs = Ads.objects.filter(spot='section')

	template = loader.get_template('entry_detail.html')
	context = {
		'revs' : revs,
	}

	return HttpResponse(template.render(context, request))


def CenterRevs(request):
	revs = Ads.objects.filter(spot='center')

	template = loader.get_template('index.html')
	context = {
		'revs' : revs,
	}

	return HttpResponse(template.render(context, request))"""