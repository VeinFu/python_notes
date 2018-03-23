#!/usr/bin/env python
# *-* coding: utf-8 *-*
from itertools import islice

def func(index):
	if index == 1 or index == 2:
		return 1
	if index >= 3:
		return func(index-1)+func(index-2)

def func1(): # A generator
	a, b = 0, 1
	while True:
		yield b
		a, b = b, a+b

new_list = map(func, [i for i in xrange(1,10)])
print new_list

f = func1() # a generator object
print list(islice(f, 0, 10))
