#!C:\Python26\python
# -*- coding: utf8 -*-

import cgitb
cgitb.enable()

print "Content-Type: text/html; charset=utf-8"

html = """
<html>
<head>
<title>我的CGI程式</title>
</head>
<body>
<h2>%d</h2>
</body>
</html>
""" % (1, 2)

print html
