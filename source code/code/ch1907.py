#!/usr/bin/env python
# -*- coding: cp950 -*-

import pygame
import sys

# ��l��
pygame.init()

# �]�w�����j�p
width, height = 300, 300
size = width, height

# �]�w�����j�p
screen = pygame.display.set_mode(size)

# loop����{��
while True:

   # �P�_�O�_�����U�����������s
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         sys.exit()
      
   # �]�w�u���C��
   color = (0,100,100)

   pointlist = [(149,74), (220,125), (181,203), (96,168), (96,106)]
   # �ϥ�polygon()���ø�s�h���
   pygame.draw.polygon(screen, color, pointlist)

   # ��s��ܵe���� ���]Surface�^
   pygame.display.flip()
   
