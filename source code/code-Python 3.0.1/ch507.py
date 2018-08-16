#!/usr/bin/env python
#coding=utf-8

def who(**details):
    for detail in details:
        print("%s: %s" % (detail, details[detail]))

who(name="王小明", age="21", sex="男", email="abc@gmail.com")
who(name="李大同", age="21", sex="男", email="def@gmail.com")

