from django.shortcuts import render

def hello(request):
	context = {}
	context['hello'] = 'Welcome to Django world'
	return render(request, 'hello.html', {"context": context})
