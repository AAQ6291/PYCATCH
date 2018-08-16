#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 載入compileall模組
import compileall

"""
指定要compile的資料夾,
如果force為True表示會對這個資料夾內的.py重新compiler
"""
compileall.compile_dir("./dir/", force=True)


