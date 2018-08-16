#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import print_function
import datetime

f=open("C:\\today.txt","w+")
print (datetime.datetime.today(),file=f)
f.close()
