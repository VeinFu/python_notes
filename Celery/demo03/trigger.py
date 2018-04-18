#!/usr/bin/env python
# *-* coding: utf-8 *-*

from tasks import test_mes
import sys

def pm(body):
	res = body.get('result')
	if body.get('status') == 'PROGRESS':
		sys.stdout.write('\rProgerss: {0}'.format(res.get('p')))
		sys.stdout.flush()
	else:
		print '\r'
		print res

r = test_mes.delay()
print r.get(on_message=pm, propagate=False)
