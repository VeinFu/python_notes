#!/usr/bin/env python
# *-* coding: utf-8 *-*

import os,sys
import time
from multiprocessing import Pool

def copy_file(index):
	target_file="/tmp/tmp"+str(index)+".txt"
	print "Run task %d %s ..." % (index,os.getpid())
	start=time.time()
	exec_cmd="dd if=/tmp/tmp.txt of=%s" % target_file
	os.system(exec_cmd)
	end=time.time()
	print "Task %d runs %0.2f seconds" % (index,end-start)


if __name__ == "__main__":
	children=[]
	print "Parent process %s ..." % os.getpid()
	p=Pool()
	for i in range(2):
#		pid=os.fork()
#		if pid:
#			children.append(pid)
#		else:
#			copy_file(i)
#			os._exit(0)

#	for i in range(1):
#		os.waitpid(children[i],0)
			
		p.apply_async(copy_file,args=(i,))
	print "Wait all subprocess done ..."
	p.close()
	p.join()
	print "All subprocess done!"
