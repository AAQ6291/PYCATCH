#!/usr/bin/env python
#coding=cp950

# 載入textwrap模組
import textwrap

# 預計要包裝起來的text文字變數
text = """Python is a dynamic object-oriented programming language
that can be used for many kinds of software development.
It offers strong support for integration with other languages and tools,
comes with extensive standard libraries, and can be learned in a few days.
Many Python programmers report substantial productivity gains and feel the
language encourages the development of higher quality, more maintainable code.
"""

# 使用textwrap.wrap()函數帶入text變數與設定寬度30
myWrap = textwrap.wrap(text=text, width=30)

print("textwrap.wrap")
print("*" * 30)

# 輸出包裝後的文字
for line in myWrap:
   print(line)
print("*" * 30)

print("textwrap.fill")
print("*" * 30)

# 使用textwrap.fill()函數帶入text變數與設定寬度30
myWrap = textwrap.fill(text=text, width=30)

# 輸出包裝後的文字
print(myWrap)
print("*" * 30)

print("textwrap.wrap")
print("*" * 30)

# 這次傳入的文字不是單字
myWrap = textwrap.wrap(text="a"*120, width=30)

# 輸出包裝後的文字
for line in myWrap:
   print(line)
print("*" * 30)
