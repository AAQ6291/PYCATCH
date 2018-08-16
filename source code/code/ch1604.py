# -*- coding: cp950 -*-

# ���Jjava.util�Pjava.lang�M��
from java.util import Random
from java.lang import Math

# �w�q�@��subclass
class myRand(Random):
    #__init__()��ƴN�OJava���غc��ơ]Constructor�^
    def __init__(self, multiplier=100):
        self.multiplier = multiplier

    #�@�и��]Override�^
    def nextInt(self):
        return Math.random() * self.multiplier

# �إ߹��
r = myRand(100)

for i in range(10):
    print r.nextInt()

