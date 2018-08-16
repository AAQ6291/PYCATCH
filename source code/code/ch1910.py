#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import sys
import os
# 初始化
pygame.init()

# 設定視窗大小
width, height = 300, 300
size = width, height
title = "視窗文字"

# 設定背景顏色
black = 0, 0, 0

# 設定視窗大小
screen = pygame.display.set_mode(size)

# 設定視窗標籤
pygame.display.set_caption(title)

# 設定細明體字型
font = pygame.font.Font(os.environ['SYSTEMROOT'] + "\\Fonts\\mingliu.ttc", 12)

# 顯示中文字
text = font.render(u"Pygame顯示中文字", True, (255, 255, 255))
text1 = font.render(u"Hi, 你好~", True, (255, 255, 255))

# loop執行程式
while True:

   # 判斷是否有按下視窗結束按鈕
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         sys.exit()
      
   # 設定背景色
   screen.fill(black)

   # 繪圖文字
   screen.blit(text, (10, 10))
   screen.blit(text1, (10, 30))

   # 更新畫面
   pygame.display.update()

   
