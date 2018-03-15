#!/usr/bin/env python
# *-* coding: utf-8 *-*

def log(text):
	def decorator(func):
		def wrapper(*args, **kwargs):
			func(*args, **kwargs)
			print '%s %s' % (text, func.__name__)
		print '%s %s' % ('start', func.__name__)
		return wrapper
									
	return decorator

@log('end')
def now(str):
	print '%s: 2016-11-10' % str

now('welcome')
