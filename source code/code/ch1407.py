#!C:\Python26\python
# -*- coding: cp950 -*-

import fib

n = raw_input("��X�n�p��O��ƦC�e�X��:")
if n:
   print(fib.fib(int(n)))

# ��X��ƻ���
print ("fib.fib.__doc__ = %s" % (fib.fib.__doc__))
