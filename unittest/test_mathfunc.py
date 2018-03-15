#!/usr/bin/env python
# *-* coding: utf-8 *-*

import unittest
from mathfunc import *

class TestMathFunc(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		print "This setUpClass() method only called once"

	@classmethod
	def tearDownClass(cls):
		print "This tearDownClass() method only called once too"

	#def setUp(self):
	#	print 'do something before test.Prepare environment'

	#def tearDown(self):
	#	print 'do something after test.cleanup'

	def test_add(self):
		print "add"
		self.assertEqual(4, add(1, 3))
		self.assertNotEqual(7, add(4, 5))

	@unittest.skip("I want to skip test_minus method")
	def test_minus(self):
		print "minus"
		self.assertEqual(3, minus(7, 4))
		self.assertEqual(-1, minus(5, 6))
		self.assertEqual(4, minus(7, 2))
		self.assertNotEqual(5, minus(8, 6))

	def test_multi(self):
		print "multi"
		self.assertEqual(24, multi(4, 6))
		self.assertNotEqual(35, multi(3, 10))

	def test_divide(self):
		print "divide"
		self.assertEqual(3, divide(9, 3))
		self.assertNotEqual(2.5, divide(5, 2))


#if __name__ == "__main__":
#	unittest.main(verbosity=2)
