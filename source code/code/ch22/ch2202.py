#!/usr/bin/env python
# -*- coding: cp950 -*-

"""載入optparse模組"""
import optparse

"""
# ch901.py --help 或 ch901.py -help

Usage: ch901.py [options] arg1 arg2

Options:
  -h, --help            show this help message and exit
  -s SERVER, -S SERVER, --server=SERVER
                        定義主機IP位址
  -p PORT, -P PORT, --port=PORT
                        定義主機的連線Port number
"""

"""
宣告usage變數, 這個usage變數是要傳入OptionParser()函數內,
主要用意會將這行文字顯示在ch901.py --help內容裡

"""
usage = "usage: %prog [options] arg1 arg2"

"""建立parser instance"""
parser = optparse.OptionParser(usage=usage)

"""
使用add_option()函數加入選項引數, 這裡指的引數是command-line的引數,
例如-s為ch901.py -s, --server為ch901.py --server
而dest="server"是指parse_args()函數內的索引名稱,
help是設定顯示在--help訊息內的文字.
"""
parser.add_option("-s", "-S", "--server", type="string",dest="server",
                  help=u"定義主機IP位址")


parser.add_option("-p", "-P", "--port", type="string", dest="port",
               help=u"定義主機的連線Port number")

"""
將所接收的引數值傳遞給(options, args),
這時候將會產生一個字典型態,例如：
{'port': '1010', 'server': '123.123.123.123'}
"""
(options, args) = parser.parse_args()

if options.server == None and options.port == None:
    parser.error("不正確的指令請使用 ch901.py --help 觀看詳細指令用法")

print "server = ", options.server
print "port = ", options.port

