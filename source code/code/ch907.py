#!/usr/bin/env python
# -*- coding: cp950 -*-

# ���JConfigParser�Ҳ�
import ConfigParser

# �إ�config instance
config = ConfigParser.ConfigParser()

# Ū��ini��
config.read("./my-large.ini")

# �R��new section����abc�Ѽ�
config.remove_option("new", "abc")

# �R��new section
config.remove_section("new")

# �ϥ�open()��ƥhŪ��ini��, �ѼƳ]�w�� "r+"
config_file = open("./my-large.ini", "r+")

# �Nini�ɼg�J, �o�Ӱʧ@�|�ק���e�ڭ̳]�w�����e.
config.write(config_file)

# ����ini��
config_file.close()
