#!/usr/bin/env python
# *-* coding: utf-8 *-*

def search2(sel_list, val):
	low = 0
	high = len(sel_list) - 1

	while low <= high:
		mid = (low + high) / 2
		if sel_list[mid] < val:
			low = mid + 1
		elif sel_list[mid] > val:
			high = mid - 1
		else:
			for k,v in enumerate(sel_list[:mid]):
				if v == val:
					pos1 = k
					break
			for m,n in enumerate(sel_list[mid:]):
				if n == val:
					continue
				else:
					pos2 = m+mid-1
					break
			return (pos1, pos2)

	print 'Not found %d' % val
	return -1

if __name__ == "__main__":
	demo_list = [1,3,3,5,5,5,7,7,7,7]
	if search2(demo_list, 1) != -1:
		set0 = search2(demo_list, 1)
		print set0
		
		
