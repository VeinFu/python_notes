# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=20)
	mail = models.EmailField()

	def __unicode__(self):
		return self.name

class Entry(models.Model):
	STATUS_DRAFT = 'draft'
	STATUS_PUBLIC = 'public'
	STATUS_SET = ((STATUS_DRAFT, '草稿'),(STATUS_PUBLIC, '公开'))

	title = models.CharField(max_length=128)
	body = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	status = models.CharField(choices=STATUS_SET, default=STATUS_DRAFT, max_length=20)
	author = models.ForeignKey(User, related_name='entries')

	def __unicode__(self):
		return self.title
