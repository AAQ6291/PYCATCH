#!/usr/bin/env python
#coding=utf-8

import locale

def number_format(num, places=0):
   return locale.format("%.*f", (places, num), True)

if __name__ == '__main__':
   locale.setlocale(locale.LC_NUMERIC, '')
   print(number_format(123457890.6789, 2))
   print(number_format(-123457890.6789, 2))
