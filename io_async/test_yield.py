#!/usr/bin/env python3
# *-* coding: utf-8 *-*

def gen_one():
	subgen = range(10)
	yield from subgen

def gen_two():
	subgen = range(10)
	for item in subgen:
		yield item
