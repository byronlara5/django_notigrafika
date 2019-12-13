# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.utils.text import slugify
from django.core.urlresolvers import reverse

# 3rd parties
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

STATUS_CHOICES = (
	('draft', 'Draft'),
	('published', 'Publicada'),
)


class Category(models.Model):
	title = models.CharField(max_length=100, verbose_name ='Titulo')
	slug = models.SlugField(max_length=100, unique=True)
	icon = models.CharField(max_length=100, verbose_name ='Icono')

	class Meta:
		verbose_name = 'Categoria'
		verbose_name_plural = 'Categorias'

	def get_absolute_url(self):
		return reverse('categories', args=[self.slug])

	def __unicode__(self):
		return self.title



class Tag(models.Model):
	title = models.CharField(max_length=50, verbose_name ='Tag')
	slug = models.SlugField(max_length=255, unique=True)

	class Meta:
		verbose_name = 'Tag'
		verbose_name_plural = 'Tags'

	def get_absolute_url(self):
		return reverse('tags', args=[self.slug])

	def __unicode__(self):
		return self.title


class Post(models.Model):
	title = models.CharField(max_length=255, verbose_name ='Titulo')
	slug = models.SlugField(max_length=255, unique=True)
	status = models.CharField(choices=STATUS_CHOICES, default='draft', max_length=10, verbose_name ='Estatus')
	breaking_news = models.BooleanField(default=False, verbose_name='Destacado')
	publication_date = models.DateTimeField(verbose_name ='Fecha')
	category = models.ForeignKey(Category, verbose_name ='Categoria')
	picture = models.ImageField(upload_to='uploads/%Y/%m/%d', null=True, blank=True, verbose_name ='Imagen')
	content = RichTextUploadingField(verbose_name ='Contenido')
	gallery_content = models.BooleanField(default=False, verbose_name='Galeria')
	tags = models.ManyToManyField(Tag)
	

	class Meta:
		verbose_name = 'Publicacion'
		verbose_name_plural = 'Publicaciones'

	def get_absolute_url(self):
		return reverse('entry_detail', args=[self.slug])


	def __unicode__(self):
		return self.title








