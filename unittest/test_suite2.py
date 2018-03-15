#!/usr/bin/env python
# *-* coding: utf-8 *-*

import unittest
from  test_strfunc import TestStrFunc

def suite_test_str_func():
	suite=unittest.TestSuite()

	tests=[TestStrFunc("test_upper")]
	suite.addTests(tests)

	#suite1 = test_mathfunc.TheTestSuite()
	#suite1 = test_strfunc.TheTestSuite()
	
	#suite1.AddTest(test_mathfunc.TestMathFunc('test_add'))
	#suite2.AddTest(test_strfunc.TestStrFunc('test_lower'))
	#suite=unittest.TestSuite(suite1, suite2)

	#runner = unittest.TextTestRunner(verbosity=2)

	#runner.run(suite)
	return suite
