#!/usr/bni/env python
# *-* coding: utf-8 *-*

import threading, time
from threading import Thread, RLock

rlock = RLock()
val = 0

def func():
	global val

	print "%s acquire lock ..." % threading.currentThread().getName()
	if rlock.acquire():
		print "%s get the lock ..." % threading.currentThread().getName()
		val+=1		
		time.sleep(2)
		print 'val: %d' % val

		print "%s acquire lock again..." % threading.currentThread().getName()
		if rlock.acquire():
			print "%s get the lock ..." % threading.currentThread().getName()
			val+=2
			time.sleep(2)
			print 'val: %d' % val

		print "%s release lock ..." % threading.currentThread().getName()
		rlock.release()
		time.sleep(2)

		print "%s release lock again..." % threading.currentThread().getName()
		rlock.release()

if __name__ == "__main__":
	for i in xrange(3):
		Thread(target=func).start()
