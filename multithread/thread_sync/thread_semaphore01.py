#!/usr/bin/env python
# *-* coding: utf-8 *-*

import time
import random
from threading import Thread, Semaphore, BoundedSemaphore

max_items = 5
#semaphore = BoundedSemaphore(max_items)
semaphore = Semaphore(max_items)

def producer(nloops):
	for i in xrange(nloops):
		time.sleep(random.randrange(2, 5))
		print "%s:" % time.ctime()
		try:
			semaphore.release()
			print 'Produced an item.'
		except:
		 	print 'Full, skipping.'

def consumer(nloops):
	for i in xrange(nloops):
		time.sleep(random.randrange(2, 5))
		print "%s:" % time.ctime()
		if semaphore.acquire():
			print 'Consumed an item.'
		else:
		 	print 'Empty, skipping.'

threads = []
nloops = random.randrange(3, 6)
print 'loops: %d' % nloops

threads.append(Thread(target=producer, args=(nloops,)))
threads.append(Thread(target=consumer, args=(random.randrange(nloops, nloops+max_items+2),)))

for thread in threads:
	thread.start()

for thread in threads:
	thread.join()

print 'All Done.'

