#!/usr/bin/env python
# -*- coding: cp950 -*-

import pygame
import sys

# ��l��
pygame.init()

# �]�w�����j�p
width, height = 300, 300
size = width, height

# �]�w�I���C��
black = 0, 0, 0

# �]�w���ʳt��
speed = [1, 1]

# �]�w�����j�p
screen = pygame.display.set_mode(size)

blowfish = pygame.image.load("C:\\ch1903.bmp")

# �����Ϥ��j�p�]�x�Τj�p�^
blowfish_rect = blowfish.get_rect()

# loop����{��
while True:

   # �P�_�O�_�����U�����������s
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         sys.exit()

   # �]�w�Ϥ�����
   blowfish_rect = blowfish_rect.move(speed)

   # �����Ƴ�쬰"�L��"
   pygame.time.delay(50)

   # �P�_���󲾰ʪ��d��H���W�L�������e��
   if blowfish_rect.left < 0 or blowfish_rect.right > width:
      speed[0] = - speed[0]

   # �P�_���󲾰ʪ��d��H���W�L����������
   if blowfish_rect.top < 0 or blowfish_rect.bottom > height:
      speed[1] = - speed[1]

   # �]�w�I����
   screen.fill(black)

   # ø�� ���]Surface�^
   screen.blit(blowfish, blowfish_rect)

   # ��s��ܵe���� ���]Surface�^
   pygame.display.flip()
   
