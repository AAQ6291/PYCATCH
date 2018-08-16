#!/usr/bin/env python
# -*- coding: cp950 -*-

"""���Joptparse�Ҳ�"""
import optparse

"""
# ch901.py --help �� ch901.py -help

Usage: ch901.py [options] arg1 arg2

Options:
  -h, --help            show this help message and exit
  -s SERVER, -S SERVER, --server=SERVER
                        �w�q�D��IP��}
  -p PORT, -P PORT, --port=PORT
                        �w�q�D�����s�uPort number
"""

"""
�ŧiusage�ܼ�, �o��usage�ܼƬO�n�ǤJOptionParser()��Ƥ�,
�D�n�ηN�|�N�o���r��ܦbch901.py --help���e��

"""
usage = "usage: %prog [options] arg1 arg2"

"""�إ�parser instance"""
parser = optparse.OptionParser(usage=usage)

"""
�ϥ�add_option()��ƥ[�J�ﶵ�޼�, �o�̫����޼ƬOcommand-line���޼�,
�Ҧp-s��ch901.py -s, --server��ch901.py --server
��dest="server"�O��parse_args()��Ƥ������ަW��,
help�O�]�w��ܦb--help�T��������r.
"""
parser.add_option("-s", "-S", "--server", type="string",dest="server",
                  help=u"�w�q�D��IP��}")


parser.add_option("-p", "-P", "--port", type="string", dest="port",
               help=u"�w�q�D�����s�uPort number")

"""
�N�ұ������޼ƭȶǻ���(options, args),
�o�ɭԱN�|���ͤ@�Ӧr�嫬�A,�Ҧp�G
{'port': '1010', 'server': '123.123.123.123'}
"""
(options, args) = parser.parse_args()

if options.server == None and options.port == None:
    parser.error("�����T�����O�Шϥ� ch901.py --help �[�ݸԲӫ��O�Ϊk")

print "server = ", options.server
print "port = ", options.port

