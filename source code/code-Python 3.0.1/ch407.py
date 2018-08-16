#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

f = open("./ch407.html", "r")
context = f.read()

p = re.compile(\
   '<a\shref="(http://[a-zA-Z0-9]+.[a-zA-Z0-9]+.[a-zA-Z0-9]+.*)">'\
   )
m = p.findall(context)

for x in m:
   print(x)

f.close()
