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

   # 取得按鍵事件
   pressed_keys = pygame.key.get_pressed()

   # 如果按下的是左鍵, 就將物件往左移
   if pressed_keys[K_LEFT]:
      fish_pos[0] = fish_pos[0] - 1

   # 如果按下的是右鍵, 就將物件往右移
   if pressed_keys[K_RIGHT]:
      fish_pos[0] = fish_pos[0] + 1

   # 如果按下的是上鍵, 就將物件往上移
   if pressed_keys[K_UP]:
      fish_pos[1] = fish_pos[1] - 1

   # 如果按下的是下鍵, 就將物件往下移
   if pressed_keys[K_DOWN]:
      fish_pos[1] = fish_pos[1] + 1

   # 當按下空白鍵就旋轉物件
   if pressed_keys[K_SPACE]:
      fish_angle -= 1
      
   # 顯示背景
   screen.blit(background, (0,0))
   
   # 設定要旋轉的物件
   rotate = pygame.transform.rotate(fish, fish_angle)
   
   # 顯示魚
   screen.blit(rotate, fish_pos)
   
   # 更新畫面
   pygame.display.update()

   
