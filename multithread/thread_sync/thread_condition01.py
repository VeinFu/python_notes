#!/usr/bin/env python
# *-* coding: utf-8 *-*

import time, random
#import threading
from threading import Thread, Condition

condition = Condition()
product = 0

def producer():
	global product
	for i in xrange(5):
		time.sleep(random.randrange(2, 5))
		condition.acquire()
		product = random.randint(1, 10)
		print 'Produce %d' % product
		condition.notify()
		condition.release()

def consumer():
	global product
	for i in xrange(5):
		condition.acquire()
		condition.wait()

		print '%s -- Consume: %d' % (time.ctime(), product)
		#condition.notify()
		condition.release()

if __name__ == "__main__":
	threads = []
	for func in [producer, consumer]:
		threads.append(Thread(target=func))
		threads[-1].start()

	for thread in threads:
		thread.join()

	print 'All Done.'

