#!/usr/bin/python
# -*- coding: utf-8 -*-

x = 'Python對中文支援'

print("repr() ==> %s %s" % (repr(x), type(repr(x))))
print(x, type(x))
print(x.encode('big5'), type(x.encode('big5')))

y = x.encode('big5')

## 如果將編碼轉為gbk的結果。所對應的文字會不對。
print(str(y, 'gbk'), type(str(y, 'gbk')))
print(str(y, 'big5'), type(str(y, 'big5')))
