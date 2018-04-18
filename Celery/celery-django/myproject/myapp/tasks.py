# *-* coding: utf-8 *-*

#from myproject import celery_app
from celery.task.schedules import crontab
from datetime import timedelta
from celery.decorators import periodic_task
from myproject.celery import app
import time

@app.task
def sendmail(mail):
	print 'start sending email to %s' % mail
	time.sleep(5)
	print 'success'
	return True

#@periodic_task(run_every=10)
#periodic_task(run_every=timedelta(seconds=10))
@periodic_task(run_every=crontab(hour='15', day_of_week='2'))
def some_task():
	print 'periodic task test!!!!!'
	time.sleep(5)
	print 'success'
	return True
