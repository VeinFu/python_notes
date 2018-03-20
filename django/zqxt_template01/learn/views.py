# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def show_str(request):
	string = 'Welcome to Django world.'
	return render(request, 'string.html', {'string': string})

def show_list(request):
	TutorialList = ['HTML', 'CSS', 'JavaScript', 'Python', 'Django']
	return render(request, 'list.html', {"TutorialList": TutorialList})

def show_dict(request):
	dict_info = {"site":"ziqiangxuetang", "content":"all kinds of IT Tutorials"}
	return render(request, 'dict.html', {"dict_info": dict_info})
	
