#!/usr/bin/env python
# -*- coding: cp950 -*-

import pygame
import sys

# 初始化
pygame.init()

# 設定視窗大小
width, height = 300, 300
size = width, height

# 設定視窗大小
screen = pygame.display.set_mode(size)

# loop執行程式
while True:

   # 判斷是否有按下視窗結束按鈕
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         sys.exit()

   # 更新顯示畫面的 面（Surface）
   pygame.display.flip()
   
