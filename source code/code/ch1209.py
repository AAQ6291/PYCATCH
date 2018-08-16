#!C:\Python26\python
# -*- coding: utf8 -*-

import cgi
import cgitb
cgitb.enable()

print "Content-Type: text/html; charset=utf-8"

html = """
<html>
<head>
<title>Python CGI的環境-參數</title>
</head>
<body>
<h2>Python CGI的環境-參數</h2>
"""
print html

cgi.print_environ()

print """
</body>
</html>
"""
