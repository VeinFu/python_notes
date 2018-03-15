#!/usr/bin/env python
# *-* coding : utf-8 *-*

import os

def list_file(xpath):
	for subPath in os.listdir(xpath):
		subPath=os.path.join(xpath, subPath)
		if os.path.isdir(subPath):
			list_file(subPath)
		else:
			file_name=subPath
			print file_name

if __name__ == "__main__":
	list_file("/home/Work_Station/python/c_in_python")
