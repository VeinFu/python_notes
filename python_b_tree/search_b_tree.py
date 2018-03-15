#!/usr/bin/env python
# *-* coding: utf-8 *-*

class Node(object):
	def __init__(self, elem=-1, lchild=None, rchild=None):
		self.elem = elem
		self.lchild = lchild
		self.rchild = rchild

class Tree(object):
	def __init__(self):
		self.root = Node()
		self.myqueue = []

	def add_elem(self, elem):
		node = Node(elem)
		if self.root.elem == -1:
			self.root = node
			self.myqueue.append(self.root)
		else:
			treeNode = self.myqueue[0]
			if treeNode.lchild == None:
				treeNode.lchild = node
				self.myqueue.append(treeNode.lchild)
			else:
				treeNode.rchild = node
				self.myqueue.append(treeNode.rchild)
				self.myqueue.pop(0)  #change myqueue[0] position

	def front_digui(self, root):
		if root == None:
			return
		print root.elem
		self.front_digui(root.lchild)
		self.front_digui(root.rchild)

	def middle_digui(self, root):
		if root == None:
			return
		self.middle_digui(root.lchild)
		print root.elem
		self.middle_digui(root.rchild)

	def later_digui(self, root):
		if root == None:
			return
		self.later_digui(root.lchild)
		self.later_digui(root.rchild)
		print root.elem

	def level_search(self, root):
		if root == None:
			return

		onequeue = []
		onequeue.append(root)

		while onequeue:
			node = onequeue.pop(0)
			print node.elem
			if node.lchild != None:
				onequeue.append(node.lchild)
			if node.rchild != None:
				onequeue.append(node.rchild)
	
	def front_stack(self, root):
		if root == None:
			return
		mystack = []
		node = root
		while node or mystack:
			while node:
				print node.elem
				mystack.append(node)
				node = node.lchild
			node = mystack.pop()
			node = node.rchild

	def middle_stack(self, root):
		if root == None:
			return	
		mystack = []
		node = root
		while node or mystack:
			while node:
				mystack.append(node)
				node = node.lchild
			node = mystack.pop()
			print node.elem
			node = node.rchild

	def later_stack(self, root):
		if root == None:
			return
		node = root
		mystack1 = []
		mystack2 = []
		mystack1.append(node)

		while mystack1:
			node = mystack1.pop()
			if node.lchild:
				mystack1.append(node.lchild)
			if node.rchild:
				mystack1.append(node.rchild)
			mystack2.append(node)
		while mystack2:
			print mystack2.pop().elem



if __name__ == "__main__":
	elems = range(10)
	tree = Tree()
	for elem in elems:
		tree.add_elem(elem)

	print 'level:'
	tree.level_search(tree.root)

	print 'front_digui:'
	tree.front_digui(tree.root)
	print 'front_stack:'
	tree.front_stack(tree.root)
	
	print 'middle_digui:'
	tree.middle_digui(tree.root)
	print 'middle_stack:'
	tree.middle_stack(tree.root)

	print 'later_digui:'
	tree.later_digui(tree.root)
	print 'later_stack:'
	tree.later_stack(tree.root)
