# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from django.http import HttpResponse
#from django.views.decorators.csrf import csrf_exempt
#from rest_framework.renderers import JSONRenderer
#from rest_framework.parsers import JSONParser
from models import Snippet
from serializers import SnippetSerializer

# Create your views here.
#class JSONResponse(HttpResponse):
#	def __init__(self, data, **kwargs):
#		content = JSONRenderer().render(data)
#		kwargs['content_type'] = 'application/json'
#		super(JSONResponse, self).__init__(content, **kwargs)

#@csrf_exempt
@api_view(['GET', 'PUT'])
def snippet_list(request, format=None):

	if request.method == 'GET':
		snippets = Snippet.objects.all()
		serializer = SnippetSerializer(snippets, many=True)

		#return JSONResponse(serializer.data)
		return Response(serializer.data)

	elif request.method == "POST":
		#data = JSONParser().parser(request)
		serializer = SnippetSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()
			#return JSONResponse(serializer.data, status=201)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		#return JSONResponse(serializer.errors, status=400)
		return Response(serializer.errors, status=status.HTTP_400_REQUEST)

#@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request,pk,format=None):

	try:
		snippet = Snippet.objects.get(pk=int(pk))
	except Snippet.DoesNotExist:
		#return HttpResponse(status=404)
		return Response(status=status.HTTP_404_NOT_FOUND)
		
		
	if request.method == 'GET':
		serializer = SnippetSerializer(snippet)
		#return JSONResponse(serializer.data)
		return Response(serializer.data)

	elif request.method == "POST":
		#data = JSONParser().parser(request)
		serializer = SnippetSerializer(snippet, data=request.data)

		if serializer.is_valid():
			serializer.save()
			#return JSONResponse(serializer.data, status=201)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		#return JSONResponse(serializer.errors, status=400)
		return Response(serializer.errors, status=status.HTTP_400_REQUEST)
	elif reuqest.method == 'DELETE':
		snippet.delete()
		#return HttpResponse(status=204)
		return Response(status=status.HTTP_204_NO_CONTENT)
