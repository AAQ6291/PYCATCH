#!C:\Python26\python
# -*- coding: cp950 -*-

from distutils.core import setup, Extension
 
myMoudle = Extension('my', sources = ['ch1402.c'])
 
setup (name = '���ռҲ�',
        version = '1.0',
        description = '�o�O�ڨϥ�C�y�����g���Ĥ@�ӼҲ�',
        ext_modules = [myMoudle])
