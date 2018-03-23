# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return render(request, 'index.html')

def add(request):
	a = int(request.GET['a'])
	b = int(request.GET['b'])

	return HttpResponse(str(a+b))
