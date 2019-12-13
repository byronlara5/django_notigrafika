# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from post.models import Category, Tag, Post

# 3rd party
from import_export import resources
from import_export.admin import ImportExportMixin, ExportActionModelAdmin 


# Register your models here.

#admin for post
class PostResource(resources.ModelResource):

	class Meta:
		model = Post

class PostResAdmin(ImportExportMixin, admin.ModelAdmin):
	resource_class = PostResource
	list_display = ('title','breaking_news','status', 'publication_date', 'category')
	list_filter = ('status', 'category', 'tags')
	search_feidls = ('title', 'content')
	prepopulated_fields = {'slug': ('title',)}

#admin for categories
class CategoryResource(resources.ModelResource):

	class Meta:
		model = Category

class CategoryResAdmin(ImportExportMixin, admin.ModelAdmin):
	resource_class = CategoryResource
	prepopulated_fields = {'slug': ('title',)}


#admin for tags
class TagResource(resources.ModelResource):

	class Meta:
		model = Tag

class TagResAdmin(ImportExportMixin, admin.ModelAdmin):
	resource_class = TagResource
	prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryResAdmin)
admin.site.register(Tag, TagResAdmin)
admin.site.register(Post, PostResAdmin)