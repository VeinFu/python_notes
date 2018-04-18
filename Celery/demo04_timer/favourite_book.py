#!/usr/bin/env python
# *-* coding: utf-8 *-*

from celery import Celery
import time

app = Celery('select_favourite_book', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')
app.config_from_object('celery_config')

@app.task
def select_favourite_book():
	print 'Start to select_favourite_book task at {0}'.format(time.ctime())
	time.sleep(2)
	print 'Success to select_favourite_book task at {0}'.format(time.ctime())
	return True
