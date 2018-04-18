#!/usr/bin/env python
# *-* coding: utf-8 *-*

from celery import *

#app = Celery('tasks', backend='amqp', broker='pyamqp://')
#app = Celery('tasks', broker='pyamqp://guest@localhost//')
app = Celery('tasks', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')

class mytask(Task):
	
	def on_success(self, retval, task_id, args, kwargs):
		print "task done: {0}".format(retval)
		return super(mytask, self).on_success(retval, task_id, args, kwargs)

	def on_failure(self, exc, task_id, args, kwargs, einfo):
		print "task fai,reason: {0}".format(exc)
		return super(mytask, self).on_failure(exc, task_id, args, kwargs, einfo)
	

@app.task(base=mytask)
def add(x, y):
	#raise KeyError   #打开用于测试on_failure方法
	return x + y
