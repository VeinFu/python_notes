#!/usr/bin/env python
# *-* coding: utf-8 *-*

from threading import Lock, Thread

g = 0
lock = Lock()

def add_one():
	global g
	lock.acquire()
	g+=1
	lock.release()

def add_two():
	global g
	lock.acquire()
	g+=2
	lock.release()

if __name__ == "__main__":
	threads = []
	for func in [add_one, add_two]:
		threads.append(Thread(target=func))
		threads[-1].start()

	for thread in threads:
		thread.join()

	print g
