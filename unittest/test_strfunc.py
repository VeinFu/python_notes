#!/usr/bin/env python
# *-* coding: utf-8 *-*

import unittest

class TestStrFunc(unittest.TestCase):

	def test_upper(self):
		self.assertEqual("foo".upper(), "FOO")
		self.assertEqual("WELCOME", 'WelCome'.upper())

	def test_lower(self):
		self.assertEqual('schEDul'.lower(), 'schedul')
		self.assertEqual('spring', 'SPRinG'.lower())
