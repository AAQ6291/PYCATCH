#!/usr/bin/env python

# �}���ɮרèϥ�w+�Ҧ�
f = open("./sample-new.txt", "w+")

for line in range(100):
   print(">> %s" % (line))

   # �g�J
   f.writelines(">> %s \n" % (str(line)))

# ����
f.close()
