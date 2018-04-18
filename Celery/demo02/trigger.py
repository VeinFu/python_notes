#!/usr/bin/env python
# *-* coding: utf-8 *-*

from tasks import add
import time

result = add.delay(4, 5)
while not result.ready():
	time.sleep(1)

print 'task done: {0}'.format(result.get())
