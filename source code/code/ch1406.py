#!C:\Python26\python
# -*- coding: cp950 -*-

from distutils.core import setup, Extension
 
myMoudle = Extension('fib', sources = ['ch1405.c'])
 
setup (name = '�O��ƦC�Ҳ�',
        version = '1.0',
        description = '�O��ƦC�Ҳ�',
        ext_modules = [myMoudle])
