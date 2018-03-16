#!/usr/bin/env python
# *-* coding: utf-8 *-*

import time, threading
from threading import Thread, Semaphore

semaphore = Semaphore(2)

def func():

	print '%s acquire semaphore ...' % threading.currentThread().getName()
	if semaphore.acquire():
		print '%s get semaphore ...' % threading.currentThread().getName()
		time.sleep(4)

		print '%s release semaphore ...' % threading.currentThread().getName()
		semaphore.release()

if __name__ == "__main__":
	t1 = Thread(target=func)
	t2 = Thread(target=func)
	t3 = Thread(target=func)
	t4 = Thread(target=func)

	t1.start()
	t2.start()
	t3.start()
	t4.start()

	time.sleep(2)
	print 'MainThread release semaphore without acquire'
	semaphore.release()
