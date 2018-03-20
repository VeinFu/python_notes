from django.http import HttpResponse

def add(request):
	a = request.GET['a']  # a=request.GET.get('a',0)
	b = request.GET['b']
	c = int(a) + int(b)
	return HttpResponse(str(c))

def add1(request, a, b):
	c = int(a) + int(b)
	return HttpResponse(str(c))
	
