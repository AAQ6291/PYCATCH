#!/usr/bin/env python
#coding=utf-8

from __future__ import print_function

match = []

strs = """
abcdefghijklmnopqrstuvwxyz
abcdefghijklmnopqrstuvwxyz
abcdefghijklmno
"""
current_match = strs.find("o")

while current_match != -1:
   match.append(current_match)
   current_match = strs.find("o", current_match + 1)

print("match = ",match, sep="")
