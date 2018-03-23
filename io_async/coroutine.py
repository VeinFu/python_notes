#!/usr/bin/env python
# *-* coding: utf-8 *-*

def consumer():
	r = ''
	while True:
		n = yield r
		if not n:
			return
		print '[Consumer]: consuming %s ...' % n
		r = '200 OK'

def producer(c):
	c.send(None)

	m = 0
	while m < 5:
		m += 1
		print '[Producer]: producing %s ...' % m
		s = c.send(m)
		print '[Producer]: Consumer return %s' % s
	c.close()

x = consumer()
producer(x)
