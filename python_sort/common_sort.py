#!/usr/bin/env python
# *-* coding: utf-8 *-*

def insert_sort(sel_list):
	length = len(sel_list)
	for i in range(1, length):
		j = i - 1
		val = sel_list[i]
		while j >= 0:
			if sel_list[j] > val:
				sel_list[j], sel_list[j+1] = sel_list[j+1], sel_list[j]
			j-=1
		print sel_list

	return sel_list

def buddle_sort(sel_list):
	length = len(sel_list)
	val = length -1
	while val > 0:
		for i in range(0, val):
				if sel_list[i] > sel_list[i+1]:
					sel_list[i], sel_list[i+1] = sel_list[i+1], sel_list[i]
		val-=1
		print sel_list

	return sel_list

def select_sort(sel_list):
	length = len(sel_list)
	for i in range(0, length-1):
		for j in range(i+1, length):
			if sel_list[i] > sel_list[j]:
				sel_list[i], sel_list[j] = sel_list[j], sel_list[i]
		print sel_list
	return sel_list

def fast_sort(sel_list):
	if len(sel_list) <= 1:
		return sel_list

	pivot = sel_list[0]
	return fast_sort([x for x in sel_list[1:] if x < pivot]) + [pivot] + \
			fast_sort([x for x in sel_list[1:] if x >= pivot])

if __name__ == "__main__":
	demo_list = [9, 12, 2, 6, 4, 8, 17, 3, 12]
	#new_list = insert_sort(demo_list)
	#new_list = buddle_sort(demo_list)
	#new_list = select_sort(demo_list)
	new_list = fast_sort(demo_list)
	print new_list
				
