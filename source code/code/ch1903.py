#!/usr/bin/env python
# -*- coding: cp950 -*-

import pygame
import sys

# 初始化
pygame.init()

# 設定視窗大小
width, height = 300, 300
size = width, height

# 設定背景顏色
black = 0, 0, 0

# 設定移動速度
speed = [1, 1]

# 設定視窗大小
screen = pygame.display.set_mode(size)

blowfish = pygame.image.load("C:\\ch1903.bmp")

# 取的圖片大小（矩形大小）
blowfish_rect = blowfish.get_rect()

# loop執行程式
while True:

   # 判斷是否有按下視窗結束按鈕
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         sys.exit()

   # 設定圖片移動
   blowfish_rect = blowfish_rect.move(speed)

   # 延遲秒數單位為"微秒"
   pygame.time.delay(50)

   # 判斷物件移動的範圍以不超過視窗的寬度
   if blowfish_rect.left < 0 or blowfish_rect.right > width:
      speed[0] = - speed[0]

   # 判斷物件移動的範圍以不超過視窗的高度
   if blowfish_rect.top < 0 or blowfish_rect.bottom > height:
      speed[1] = - speed[1]

   # 設定背景色
   screen.fill(black)

   # 繪圖 面（Surface）
   screen.blit(blowfish, blowfish_rect)

   # 更新顯示畫面的 面（Surface）
   pygame.display.flip()
   
