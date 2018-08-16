#!/usr/bin/python
# -*- coding: utf-8 -*-

import codecs

fobj = codecs.open("./ch205.txt", "r", "utf-8")
r = fobj.read()

print r
