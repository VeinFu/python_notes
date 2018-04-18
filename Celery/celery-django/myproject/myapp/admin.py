# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Blog

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
	list_display = ('caption',)

admin.site.register(Blog, BlogAdmin)
