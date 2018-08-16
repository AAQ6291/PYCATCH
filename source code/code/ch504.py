#!/usr/bin/env python
#coding=utf-8

name = "John"

def change():
    global name
    name = "Jack"
    print "change name", name

print "outside function", name
change()
print "outside function", name
