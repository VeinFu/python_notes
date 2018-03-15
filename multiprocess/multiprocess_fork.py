#!/usr/bin/env python
# *-* coding: utf-8 *-*

import os,sys
import time
from multiprocessing import Pool
from multiprocessing import Process

def func(index):
	print "Run task %d %s ..." % (index,os.getpid())
	start=time.time()
	time.sleep(10)
	print index*index
	end=time.time()
	print "Task %d runs %0.2f seconds" % (index,end-start)


if __name__ == "__main__":
	print "Parent process %s ..." % os.getpid()
	children=[]
	for i in range(3):
		pid=os.fork()
		if pid:
			children.append(pid)
		else:
			func(i)
			os._exit(0)
	for i in range(3):
		os.waitpid(children[i],0)
		
	
	
