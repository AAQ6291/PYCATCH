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
   color = (0,0,100)

   # �ϥ�circle()���ø�s���
   pygame.draw.circle(screen, color, (width/2, height/2),100, 5)

   # ��s��ܵe���� ���]Surface�^
   pygame.display.flip()
   
