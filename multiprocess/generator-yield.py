#!/usr/bin/env python
# *-* coding: utf-8 *-*


def func():
	a=1
	b=2
	yield a
	yield b
	while True:
		a,b=b,a*b
		yield b

i=0
g=func()
while i < 10:
	i=i+1
	print g.next()
