#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
自訂模組
"""

__all__ = ['myfun1','Foo', 'Bar']

def myfun1():
   """Introduction myfun1() function"""
   print "myfun1"

def myfun2():
   """Introduction myfun2() function"""
   print "myfun2"

class Foo:
   """Introduction class Foo"""
   def __init__(self, name):
      """Initialize foo..."""
      self.name = name

   def foo_fun1(self):
      """Introduction foo_fun1() function"""
      print "foo_fun1"

class Bar:
   """Introduction class Bar"""
   def __init__(self, name):
      """Initialize bar..."""
      self.id = id

   def bar_fun1(self):
      """Introduction bar_fun1() function"""
      print "bar_fun1"

   def bar_fun2(self):
      """Introduction bar_fun2() function"""
      print "bar_fun2"


class Test:
   """Introduction class Test"""
   def __init__(self, name):
      """Initialize test..."""
      self.id = id

   def test_fun1(self):
      """Introduction test_fun1() function"""
      print "test_fun1"
