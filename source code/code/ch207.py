#!/usr/bin/python
# -*- coding: utf-8 -*-

x = u'Python對中文支援'

print "repr() ==>", repr(x), type(repr(x))
print x, type(x)
print x.encode('big5'), type(x.encode('big5'))

y = x.encode('big5')

## 如果將編碼轉為gbk的結果。所對應的文字會不對。
print y.decode('gbk'), type(y.decode('big5'))
print y.decode('big5'), type(y.decode('big5'))
