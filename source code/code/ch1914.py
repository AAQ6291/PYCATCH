#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import sys
import os
# 初始化
pygame.init()

# 設定視窗大小
width, height = 500, 375
size = width, height
title = "按鍵操作"
background = pygame.image.load("ocean.jpg")
fish = pygame.image.load("ch1903.bmp")
fish_pos = [150,150]
fish_angle = 0

# 設定隱藏滑數指標
pygame.mouse.set_visible(0)

# 設定視窗大小
screen = pygame.display.set_mode(size)

# 設定視窗標籤
pygame.display.set_caption(title)

# loop執行程式
while True:

   # 判斷是否有按下視窗結束按鈕
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         sys.exit()

   # 當按下滑鼠左鍵時就將角度遞減
   if pygame.mouse.get_pressed() == (1,0,0):
      fish_angle -= 1

   # 當按下滑鼠右鍵時就將角度遞增
   if pygame.mouse.get_pressed() == (0,0,1):
      fish_angle += 1
      
   # 顯示背景
   screen.blit(background, (0,0))

   # 取得滑數的座標
   x, y = pygame.mouse.get_pos()
   x -= fish.get_width() / 2
   y -= fish.get_height() / 2

   # 設定要旋轉的物件
   rotate = pygame.transform.rotate(fish, fish_angle)

   # 顯示魚
   screen.blit(rotate, (x,y))
   
   # 更新畫面
   pygame.display.update()

   
