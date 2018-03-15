#!/usr/bin/env python
# *-* coding: utf-8 *-*

def mergelist(a, b):
	c = []
	i = 0
	j = 0

	while i < len(a) and j < len(b):
		if a[i] < b[j]:
			c.append(a[i])
			i+=1
		else:
			c.append(b[j])
			j+=1

	if i < len(a):
		c = c + a[i:]
	if j < len(b):
		c = c + b[j:]

	return c

def merge_sort(sel_list):
	if len(sel_list) <= 1:
		return sel_list
	middle = len(sel_list) / 2
	left = merge_sort(sel_list[:middle])
	right = merge_sort(sel_list[middle:])

	return mergelist(left, right)

if __name__ == "__main__":
	demolist = [9,12,2,3,8,10,17,5,4,20]
	print merge_sort(demolist)
