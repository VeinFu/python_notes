#!/usr/bin/env python
# *-* coding: utf-8 *-*

class Chain(object):

	def __init__(self, path=''):
		self._path = path

	def __getattr__(self, path):
		print path
		return Chain('%s/%s' % (self._path, path))

	def users(self, value):
		return Chain('%s/%s' % (self._path, value))

	def __str__(self):
		return self._path

	__repr__ = __str__

print Chain().status.user.timeline.list
print Chain().users('Jackon').repo
