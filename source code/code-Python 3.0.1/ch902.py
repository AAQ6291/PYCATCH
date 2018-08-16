#!/usr/bin/env python
# -*- coding: cp950 -*-

"""載入optparse模組"""
import optparse

usage = "usage: %prog [options] arg1 arg2"

"""建立parser instance"""
parser = optparse.OptionParser(usage=usage)

parser.add_option("-s", "-S", "--server", type="string",dest="server",
                  default="123.123.12.1", help="定義主機IP位址")


parser.add_option("-p", "-P", "--port", type="string", dest="port",
               default=1010, help="定義主機的連線Port number")

(options, args) = parser.parse_args()

if options.server == None and options.port == None:
    parser.error("不正確的指令請使用 ch902.py --help 觀看詳細指令用法")

print("server = ", options.server)
print("port = ", options.port)

