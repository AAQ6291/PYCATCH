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

# 設定字型
font = pygame.font.SysFont("Arial", 24)

# 取得文字高度
font_height = font.get_linesize()

# loop執行程式
while True:

   # 判斷是否有按下視窗結束按鈕
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         sys.exit()
      
   # 設定背景色
   screen.fill(black)

   # 取得鍵盤按鈕是否有按下
   pressed_keys = pygame.key.get_pressed()
   
   # 高度
   line = font_height

   # 逐步輸出按下的按鈕資訓
   for key_constant, pressed in enumerate(pressed_keys):
      if pressed:
         key_name = pygame.key.name(key_constant)
         text_surface = font.render("Key %s pressed" % (key_name), True, (255,255,255))
         screen.blit(text_surface, (50, line))
         line += font_height
   
   # 更新畫面
   pygame.display.update()

   
