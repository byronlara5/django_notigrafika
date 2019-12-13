# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


SPOT_CHOICES = (
	('center', 'Centro'),
	('index', 'Inicio'),
	('detail', 'Articulos'),
	('section', 'Secciones'),
	('hidden', 'Oculta')
)

class Ads(models.Model):
	title = models.CharField(max_length=100, verbose_name ='Titulo')
	spot = models.CharField(max_length=100, choices=SPOT_CHOICES, default='hidden')
	picture = models.ImageField(upload_to='ads/', null=True, blank=True, verbose_name ='Imagen')
	content = RichTextUploadingField(verbose_name ='Contenido', blank=True, null=True)
	site_url = models.CharField(max_length=900, verbose_name ='Link', default='#')
	
	class Meta:
		verbose_name = 'Anuncio'
		verbose_name_plural = 'Anuncios'

	def __unicode__(self):
		return self.title