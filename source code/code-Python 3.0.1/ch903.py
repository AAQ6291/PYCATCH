#!/usr/bin/env python
# -*- coding: cp950 -*-

# ���JConfigParser�Ҳ�
import configparser

# �إ�config instance
config = configparser.ConfigParser()

# Ū��ini file
config.read("./my-large.ini")

# �C�X�Ҧ���section
print(config.sections())
