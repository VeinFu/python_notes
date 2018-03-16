#!/usr/bin/env python
# *-* coding: utf-8 *-*

import time, threading
from threading import Thread, Event

event = Event()

def func():

	print '%s wait for event ...' % threading.currentThread().getName()
	event.wait()

	print '%s recv event.' % threading.currentThread().getName()

for i in xrange(2):
	Thread(target=func).start()

time.sleep(2)

print 'MainThread set event.'
event.set()
