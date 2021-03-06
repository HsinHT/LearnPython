import pygame
import sys
from pygame.locals import *
from tkinter import *

root = Tk()

# 初始化 Pygame
pygame.init()

# 設定視窗大小常量
constW800 = 800
constH600 = 600

# 設定視窗大小
width = constW800
height = constH600

speed = [-2, 1]
bg = (255, 255, 255)

# 全屏初始值
fullscreen = False

# 創建指定大小的視窗
screen = pygame.display.set_mode((width, height), RESIZABLE)

# 設置視窗標題
pygame.display.set_caption('初次見面，請大家多多關照！')

# 加載圖片
turtle = pygame.image.load('imgs/turtle.png')

# 獲得圖片的位置矩形
position = turtle.get_rect()

first_location = [width / 2, height / 2]

# 頭向左
l_head = turtle
# 頭向右
r_head = pygame.transform.flip(turtle, True, False)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # 鍵盤方向鍵控制移動
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                turtle = l_head
                speed = [-1, 0]
            if event.key == K_RIGHT:
                turtle = r_head
                speed = [1, 0]
            if event.key == K_UP:
                speed = [0, -1]
            if event.key == K_DOWN:
                speed = [0, 1]

            # 全屏 (F11)
            if event.key == K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    width = root.winfo_screenwidth()
                    height = root.winfo_screenheight()
                    screen = pygame.display.set_mode((width, height), FULLSCREEN | HWSURFACE)
                else:
                    width = constW800
                    height = constH600
                    screen = pygame.display.set_mode((width, height))

                    # 重置加載圖片位置
                    position.center = first_location

        # 用戶調整視窗大小
        if event.type == VIDEORESIZE:
            size = event.size
            width, height = size
            print(size)
            screen = pygame.display.set_mode((width, height), RESIZABLE)

            # 重置加載圖片位置
            first_location = [width / 2, height / 2]
            position.center = first_location


    # 移動圖片
    position = position.move(speed)

    if position.left < 0 or position.right > width:
        # 翻轉圖片
        turtle = pygame.transform.flip(turtle, True, False)

        # 反方向移動
        speed[0] = -speed[0]

    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]

    # 填充背景
    screen.fill(bg)

    # 更新圖片
    screen.blit(turtle, position)

    # 更新畫面
    pygame.display.flip()

    # 延遲 10 毫秒
    pygame.time.delay(10)
