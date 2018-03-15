#!/usr/bin/env python
# *-* coding: utf-8 *-*

import os,sys
import time
from multiprocessing import Pool
from multiprocessing import Process

def func(index):
	print "Run task %d %s ..." % (index,os.getpid())
	start=time.time()
	time.sleep(5)
	print index * index
	end=time.time()
	print "Task %d runs %0.2f seconds" % (index,end-start)


if __name__ == "__main__":
	prolist=[]
	print "Parent process %s ..." % os.getpid()
	for i in range(1,10):
		p=Process(target=func,args=(i,))
		p.start()
		prolist.append(p)
	for p in prolist:
		p.join()
	
	
