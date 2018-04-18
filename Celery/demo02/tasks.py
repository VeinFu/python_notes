#!/usr/bin/env python
# *-* coding: utf-8 *-*

from celery import Celery
from celery.utils.log import get_task_logger

#app = Celery('tasks', backend='amqp', broker='pyamqp://')
#app = Celery('tasks', broker='pyamqp://guest@localhost//')
app = Celery('tasks', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')

logger = get_task_logger(__name__)
@app.task(bind=True)
def add(self, x, y):
	logger.info(self.request.__dict__)
	return x + y
