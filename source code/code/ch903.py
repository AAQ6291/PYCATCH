#!/usr/bin/env python
# -*- coding: cp950 -*-

# ���JConfigParser�Ҳ�
import ConfigParser

# �إ�config instance
config = ConfigParser.ConfigParser()

# Ū��ini file
config.read("./my-large.ini")

# �C�X�Ҧ���section
print config.sections()
