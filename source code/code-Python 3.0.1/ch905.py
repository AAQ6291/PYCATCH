#!/usr/bin/env python
# -*- coding: cp950 -*-

# ���JConfigParser�Ҳ�
import configparser

# �إ�config instance
config = configparser.ConfigParser()

# Ū��ini��
config.read("./my-large.ini")

"""
�ϥ�set(section, option, value)��ƥh�ק�ini�ɸ̭������e:
section�O��section�W��
option�O���Ѽƪ��W��
value�O���Ѽƭ�
"""
config.set("mysqld", "key_buffer", "128M")
config.set("client", "port", "3636")
config.set("mysqldump", "max_allowed_packet", "64M")

# �s�W�@��section, �å[�J�@�ӰѼƦW��abc = 123
config.add_section("new")
config.set("new", "abc", "123")
           
# �ϥ�open()��ƥhŪ��ini��, �ѼƳ]�w�� "r+"
config_file = open("./my-large.ini", "r+")

# �Nini�ɼg�J, �o�Ӱʧ@�|�ק���e�ڭ̳]�w�����e.
config.write(config_file)

# ����ini��
config_file.close()
