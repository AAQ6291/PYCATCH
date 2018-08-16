#!/usr/bin/env python
#coding=utf-8

from __future__ import print_function

def a(x):
   x += 1
   return x

def b(x):
   x += 1
   return x

## a(1) is b(1)為True，因為它們之間的值是一樣的。
print(a(1) is b(1))

## a(1) is b(2)為False，因為它們之間存在記憶體的位置不一樣。
print("a(1) is b(2)", id(a(1)), id(b(2)), a(1) is b(2))

## type(a(1)) is type(b(1))為True，因為它們之間的型態是一樣的。
print(type(a(1)) is type(b(1)))

x = [1, 2, 3]
y = [3, 2, 1]

## x is y為False，不相等。
print(x is y)

## is not用法
print(x is not y)

## type(x) is type(y)為True，因為它們之間的型態是一樣的。
print(type(x) is type(y))

## x[1] is y[1]為True，因為它們的物件位置是一樣的。
print("x[1] is y[1]", id(x[1]), id(y[1]), type(id(x[1])) is type(id(y[1])))
