from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return render(request, 'home.html')

def add(request):
	a = request.GET['a']  # a=request.GET.get('a',0)
	b = request.GET['b']
	c = int(a) + int(b)
	return HttpResponse(str(c))

def add1(request, a, b):
	c = int(a) + int(b)
	return HttpResponse(str(c))
	
