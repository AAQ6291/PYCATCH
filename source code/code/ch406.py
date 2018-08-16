#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

f = open("./ch406.html", "r")
context = f.read()

p = re.compile(\
   "(<a\shref=\"mailto:((\w+@\w+\.\w+)|(\w+@\w+\.\w+.\w+))\">)"\
   )

m = p.findall(context)

for x in m:
   print x[1]

f.close()
