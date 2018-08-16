#!/usr/bin/env python
# -*- coding: cp950 -*-

import pygame
import sys
import math
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
   color = (255,255,255)

   # �]�w��������
   angle = (3*math.pi)/4
   
   # �ϥ�arc()���ø�s����
   pygame.draw.arc(screen, color, (5,5,280,280), 0, angle)

   # ��s��ܵe���� ���]Surface�^
   pygame.display.flip()
   
