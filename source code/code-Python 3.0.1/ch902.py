#!/usr/bin/env python
# -*- coding: cp950 -*-

"""���Joptparse�Ҳ�"""
import optparse

usage = "usage: %prog [options] arg1 arg2"

"""�إ�parser instance"""
parser = optparse.OptionParser(usage=usage)

parser.add_option("-s", "-S", "--server", type="string",dest="server",
                  default="123.123.12.1", help="�w�q�D��IP��}")


parser.add_option("-p", "-P", "--port", type="string", dest="port",
               default=1010, help="�w�q�D�����s�uPort number")

(options, args) = parser.parse_args()

if options.server == None and options.port == None:
    parser.error("�����T�����O�Шϥ� ch902.py --help �[�ݸԲӫ��O�Ϊk")

print("server = ", options.server)
print("port = ", options.port)

