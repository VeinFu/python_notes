#!/usr/bin/env python
# *-* coding: utf-8 *-*

from celery import Celery

#app = Celery('tasks', backend='amqp', broker='pyamqp://')
#app = Celery('tasks', broker='pyamqp://guest@localhost//')
app = Celery('tasks', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')

@app.task
def add(x, y):
	return x + y
