#!/usr/bin/env python
# *-* coding: utf-8 *-*

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zqxt_data_import.settings")

import django
django.setup()

def main1():
	from blog.models import Blog
	f = open('oldblog.txt')

	for line in f:
		title, content = line.split('****')
		Blog.objects.get_or_create(title=title, content=content)

	f.close()

def main2():
	from blog.models import Blog
	BlogList = []

	f = open('oldblog.txt')

	BlogList = [Blog(title=line.split('****')[0], content=line.split('****')[1]) for line in f]

	Blog.objects.bulk_create(BlogList)

if __name__ == "__main__":
#	main1()
	main2()
	print 'Done.'
	


