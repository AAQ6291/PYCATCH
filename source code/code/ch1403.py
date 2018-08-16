#!C:\Python26\python
# -*- coding: cp950 -*-

from distutils.core import setup, Extension
 
myMoudle = Extension('my', sources = ['ch1402.c'])
 
setup (name = '測試模組',
        version = '1.0',
        description = '這是我使用C語言撰寫的第一個模組',
        ext_modules = [myMoudle])
