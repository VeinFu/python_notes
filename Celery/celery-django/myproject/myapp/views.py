# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from models import Blog
import json,time
from tasks import sendmail

def home(request):
	sendmail.delay('chunfu@celestica.com')

	data = list(Blog.objects.values('caption'))
	return HttpResponse(json.dumps(data), content_type='application/json')
