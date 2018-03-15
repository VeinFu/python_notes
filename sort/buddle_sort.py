#!/usr/bin/env python
# *-* coding: utf-8 *-*

def buddle_sort(sel_list):
	length = len(sel_list)
	val = length -1
	while val > 0:
		for i in range(0, val):
				if sel_list[i] > sel_list[i+1]:
					sel_list[i], sel_list[i+1] = sel_list[i+1], sel_list[i]
		val-=1

	return sel_list

if __name__ == "__main__":
	demo_list = [9, 12, 2, 6, 4, 8, 17, 3, 12]
	new_list = buddle_sort(demo_list)
	print new_list
	
