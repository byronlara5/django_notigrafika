# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from post.models import Post, Category, Tag
from ads.models import Ads
from django.db.models import Q

from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def Home(request):
	entries = Post.objects.filter(status='published').order_by('-publication_date')
	breakingnews = Post.objects.filter(breaking_news=True, status='published')[:5]
	categories = Category.objects.all()

	#revs
	revs = Ads.objects.filter(spot='index')
	revscenter = Ads.objects.filter(spot='center')

	query = request.GET.get("q")

	if query:
		entries = entries.filter(
			Q(title__icontains=query)|
			Q(content__icontains=query)
			).distinct()

	# Pagination
	paginator = Paginator(entries, 6)
	page = request.GET.get('page')

	try:
		entriesp = paginator.page(page)
	except PageNotAnInteger:
		entriesp = paginator.page(1)
	except EmptyPage:
		entriesp = paginator.page(paginator.num_pages)


	template = loader.get_template('index.html')
	context = {
		'breakingnews' : breakingnews,
		'categories' : categories,
		'entriesp': entriesp,
		'revs' : revs,
		'revscenter' : revscenter

	}
	
	return HttpResponse(template.render(context, request))


def Categories(request, category_slug):
	categories = Category.objects.all()
	entries = Post.objects.filter(status='published')

	#revs
	revs = Ads.objects.filter(spot='section')

	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		entries = entries.filter(category=category)

	# Pagination
	paginator_sections = Paginator(entries, 4)
	page = request.GET.get('page')

	try:
		entriess = paginator_sections.page(page)
	except PageNotAnInteger:
		entriess = paginator_sections.page(1)
	except EmptyPage:
		entriess = paginator_sections.page(paginator_sections.num_pages)


	template = loader.get_template('sections.html')
	context = {
		'categories' : categories,
		'category' : category,
		'entriess' : entriess,
		'revs' : revs
	}

	return HttpResponse(template.render(context, request))

def Entry_detail(request, slug):
	entries = get_object_or_404(Post, slug=slug)
	categories = Category.objects.all()

	#revs
	revs = Ads.objects.filter(spot='detail')

	template = loader.get_template('entry_detail.html')
	context = {
		'entries' : entries,
		'categories' : categories,
		'revs' : revs
	}

	return HttpResponse(template.render(context, request))


def Tags(request, tag_slug):
	tags = Tag.objects.all()
	entries = Post.objects.filter(status='published')
	categories = Category.objects.all()

	if tag_slug:
		tag = get_object_or_404(Tag, slug=tag_slug)
		entries = entries.filter(tags=tag)


	# Pagination
	paginator = Paginator(entries, 4)
	page = request.GET.get('page')

	try:
		entriest = paginator.page(page)
	except PageNotAnInteger:
		entriest = paginator.page(1)
	except EmptyPage:
		entriest = paginator.page(paginator.num_pages)


	template = loader.get_template('tags.html')
	context = {
		'tags' : tags,
		'tag' : tag,
		'categories' : categories,
		'entriest' : entriest
	}

	return HttpResponse(template.render(context, request))