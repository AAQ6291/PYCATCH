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
      
   # 設定線條顏色
   color = (0,100,100)

   pointlist = [(149,74), (220,125), (181,203), (96,168), (96,106)]
   # 使用polygon()函數繪製多邊形
   pygame.draw.polygon(screen, color, pointlist)

   # 更新顯示畫面的 面（Surface）
   pygame.display.flip()
   
