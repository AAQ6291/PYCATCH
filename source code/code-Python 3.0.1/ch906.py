#!/usr/bin/env python
# -*- coding: cp950 -*-

# ���JConfigParser�Ҳ�
import configparser

# �إ�config instance
config = configparser.ConfigParser()

config.add_section("login")

config.set("login", "user", "root")
config.set("login", "passwd", "12345")

# �ϥ�open()��ƥhŪ��ini��, �ѼƳ]�w�� "r+"
config_file = open("./new.ini", "w")

# �Nini�ɼg�J, �o�Ӱʧ@�|�ק���e�ڭ̳]�w�����e.
config.write(config_file)

# ����ini��
config_file.close()
