#!/usr/bin/env python
# *-* coding: utf-8 *-*
from itertools import islice

class func(object):

	def __init__(self, maxinum):
		self.maxinum = maxinum
		self.a = 0
		self.b = 1

	def __iter__(self):
		return self

	def next(self):
		fib = self.a

		if fib > self.maxinum:
			return StopIteration

		self.a, self.b = self.b, self.a+self.b

		return fib
