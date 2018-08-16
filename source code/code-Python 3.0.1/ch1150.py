#!/usr/bin/env python
#coding=cp950

# ���Jtextwrap�Ҳ�
import textwrap

# �w�p�n�]�˰_�Ӫ�text��r�ܼ�
text = """Python is a dynamic object-oriented programming language
that can be used for many kinds of software development.
It offers strong support for integration with other languages and tools,
comes with extensive standard libraries, and can be learned in a few days.
Many Python programmers report substantial productivity gains and feel the
language encourages the development of higher quality, more maintainable code.
"""

# �ϥ�textwrap.wrap()��Ʊa�Jtext�ܼƻP�]�w�e��30
myWrap = textwrap.wrap(text=text, width=30)

print("textwrap.wrap")
print("*" * 30)

# ��X�]�˫᪺��r
for line in myWrap:
   print(line)
print("*" * 30)

print("textwrap.fill")
print("*" * 30)

# �ϥ�textwrap.fill()��Ʊa�Jtext�ܼƻP�]�w�e��30
myWrap = textwrap.fill(text=text, width=30)

# ��X�]�˫᪺��r
print(myWrap)
print("*" * 30)

print("textwrap.wrap")
print("*" * 30)

# �o���ǤJ����r���O��r
myWrap = textwrap.wrap(text="a"*120, width=30)

# ��X�]�˫᪺��r
for line in myWrap:
   print(line)
print("*" * 30)
