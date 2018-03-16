#!/usr/bin/env python
# *-* coding: utf-8 *-*

import time
from threading import Thread, Lock

lock = Lock()

def print_hello():
	time.sleep(2)
	lock.acquire()
	print 'hello'
	lock.release()

def print_world():
	time.sleep(2)
	lock.acquire()
	print 'world'
	lock.release()

if __name__ == "__main__":
	threads = []
	for func in [print_hello, print_world]:
		threads.append(Thread(target=func))
		threads[-1].start()

	for thread in threads:
		thread.join()
