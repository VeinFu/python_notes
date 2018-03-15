#!/usr/bin/env python
# *-* coding: utf-8 *-*

import unittest
from  test_mathfunc import TestMathFunc

if __name__ == "__main__":
	suite=unittest.TestSuite()

	tests=[TestMathFunc("test_multi"), TestMathFunc("test_minus"), TestMathFunc("test_add")]
	suite.addTests(tests)

	#suite1 = test_mathfunc.TheTestSuite()
	#suite1 = test_strfunc.TheTestSuite()
	
	#suite1.AddTest(test_mathfunc.TestMathFunc('test_add'))
	#suite2.AddTest(test_strfunc.TestStrFunc('test_lower'))
	#suite=unittest.TestSuite(suite1, suite2)

	runner = unittest.TextTestRunner(verbosity=2)

	runner.run(suite)
