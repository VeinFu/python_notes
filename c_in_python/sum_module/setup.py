from distutils.core import setup, Extension

sum_module = Extension("mysum", sources=['my_sum.c'])

setup(name = "mysum",
	version = '1.0',
	description = 'This is a math package',
	ext_modules= [sum_module])
