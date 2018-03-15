#!/usr/bin/env python3
# *-* coding: utf-8 *-*

class Countdown(object):

	def __init__(self, start):
			self.start  = start

	def __iter__(self):
			n = 0
			while n < self.start:
				yield n
				n += 1
for i in Countdown(10):
	print(i)
