#!C:\Python26\python
# -*- coding: cp950 -*-

from distutils.core import setup, Extension
 
myMoudle = Extension('fib', sources = ['ch1405.c'])
 
setup (name = '費氏數列模組',
        version = '1.0',
        description = '費氏數列模組',
        ext_modules = [myMoudle])
