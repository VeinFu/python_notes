from distutils.core import setup, Extension

cos_module = Extension('cos_module', sources=['cos_func.c'])

setup(ext_modules=[cos_module])
