#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bz2

text = """
Python在近年來已經成為現今成長速度最快的程式語言...
"""
compress_text = bz2.compress(text)
print "壓縮內容: \n", compress_text

decompress_text = bz2.decompress(compress_text)
print "解壓後的內容: \n", decompress_text
