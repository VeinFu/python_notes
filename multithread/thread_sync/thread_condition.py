#!/usr/bin/env python
# *-* coding: utf-8 *-*

from threading import Condition, Thread
import time, sys

product = None
con = Condition()

def produce():
	global product
	if con.acquire():
		for i in xrange(5):
			if product == None:
				print 'producing ...'
				product = 'anything'


				con.notify()
			
			con.wait()
			time.sleep(2)

def consume():
	global product
	if con.acquire():
		for i in xrange(5):
			if product != None:
				print 'consuming ...'
				product = None

				con.notify()

			con.wait()
			time.sleep(2)

if __name__ == "__main__":
	threads = []
	for func in [produce, consume]:
		threads.append(Thread(target=func))
		threads[-1].start()

	for thread in threads:
		thread.join()
