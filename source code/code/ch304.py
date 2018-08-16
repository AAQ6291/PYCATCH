#!/usr/bin/env python
#coding=utf-8

from __future__ import print_function

import random

animals = [
   ['cheetah'],
   ['lion'],
   ['giraffe'],
   ['jackal'],
   [''],
   ]

if len(animals) > 0:
   print("A number of animal toys, pick up:")
   x = random.choice(animals)[0]
   if x:
      print("you got", x)
