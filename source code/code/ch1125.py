# -*- coding: cp950 -*-
import urllib
import htmllib
import formatter

class SearchLinks(htmllib.HTMLParser):
   def __init__(self, formatter) :
      htmllib.HTMLParser.__init__(self, formatter)
      self.links = []

   # �и��]override�^�쥻��start_a�@method
   def start_a(self, attrs):
      if len(attrs) > 0:
         for attr in attrs:
            if attr[0] == "href":
               self.links.append(attr[1])

   def get_links(self):
      return self.links

# �إ�formatter.NullFormatter��ҡ]instance�^
f = formatter.NullFormatter()

# �إ�SearchLinks()��ҡ]instance�^
html_parser = SearchLinks(f)

# Ū������
data = urllib.urlopen("http://www.google.com")

# �N�������e�ǤJfeed()���
html_parser.feed(data.read())

# ����html_parser
html_parser.close()

# �j�M�������Ҧ�<a href="*">���}
links = htmlparser.get_links()

# ��X
i=0
for link in links:
   print i, link
   i+=1

