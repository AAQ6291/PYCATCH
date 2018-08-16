#!/usr/bin/env python
# -*- coding: cp950 -*-

# ���JConfigParser�Ҳ�
import ConfigParser

# �إ�config instance
config = ConfigParser.ConfigParser()

# Ū��ini file
config.read("./my-large.ini")

"""
�]�wŪ��mysqld section�̭����Ҧ��ѼƦW��,
�`�N, �o�̥u�|�^��section�W��, �Ҧp�G

key_buffer

�Ӥ��O�@���:

key_buffer = 256M

���㪺options���e���G

['query_cache_size',
'key_buffer',
'socket',
'sort_buffer_size',
'read_rnd_buffer_size',
'myisam_sort_buffer_size',
'table_cache',
'thread_concurrency',
'max_allowed_packet',
'thread_cache_size',
'port',
'read_buffer_size']
"""
options = config.options("mysqld")

# ���ۧQ��get()��ƥhŪ���ӰѼƪ���
for option in options:
   print option, "=", config.get("mysqld", option)
