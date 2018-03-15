#!/usr/bin/env python3
# *-* coding: utf-8 *-*

import time

def consumer_work(len):
	print('writer:')
	w = ''

	while True:
		w = yield w
		print('[CONSUMER] Consuming %s...>> ', w)
		w *= len
		time.sleep(0.1)

def consumer(coro):
	yield from coro

def produce(c):
	c.send(None)
	for i in range(1, 5):
		print('[PROCUCE] Producing %s---- ', i)
		w = c.send(i)
		print('[PRODUCE] Receive %s---- ', w)

	c.close()

c1=consumer_work(100)
produce(consumer(c1))
