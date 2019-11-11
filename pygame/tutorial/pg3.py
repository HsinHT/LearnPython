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

bg = (255, 255, 255)

# 全屏初始值
fullscreen = False

# 創建指定大小的視窗
screen = pygame.display.set_mode((width, height), RESIZABLE)

# 設置視窗標題
pygame.display.set_caption('初次見面，請大家多多關照！')

# 設置放大縮小的比率
ratio = 1.0

# 加載圖片
origin_turtle = pygame.image.load('imgs/turtle.png')
turtle = origin_turtle

# 獲得圖片的位置矩形
origin_turtle_rect = origin_turtle.get_rect()
position = turtle_rect = origin_turtle_rect

first_location = [width / 2, height / 2]

# 頭向左
l_head = turtle
# 頭向右
r_head = pygame.transform.flip(turtle, True, False)

speed = [5, 0]
turtle_right = pygame.transform.rotate(turtle, 90)
turtle_top = pygame.transform.rotate(turtle, 180)
turtle_left = pygame.transform.rotate(turtle, 270)
turtle_bottom = turtle
turtle = turtle_top

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # 鍵盤方向鍵控制移動
        if event.type == KEYDOWN:
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

            # 放大、縮小烏龜 (=, -)，空格恢復原始大小
            if event.key == K_EQUALS or event.key == K_MINUS or event.key == K_SPACE:
                # 最大只能放大 50%，縮小 50%
                if event.key == K_EQUALS and ratio < 2:
                    ratio += 0.1
                if event.key == K_MINUS and ratio > 0.5:
                    ratio -= 0.1
                if event.key == K_SPACE:
                    ratio = 1.0

                turtle = pygame.transform.smoothscale(origin_turtle, \
                                            (int(origin_turtle_rect.width * ratio), \
                                            int(origin_turtle_rect.height * ratio)))

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

    if position.right > width:
        turtle = turtle_right
        position = turtle_rect = turtle.get_rect()
        position.left = width - turtle_rect.width
        speed = [0, 5]

    if position.bottom > height:
        turtle = turtle_bottom
        position = turtle_rect = turtle.get_rect()
        position.left = width - turtle_rect.width
        position.top = height - turtle_rect.height
        speed = [-5, 0]

    if position.left < 0:
        turtle = turtle_left
        position = turtle_rect = turtle.get_rect()
        position.top = height - turtle_rect.height
        speed = [0, -5]

    if position.top < 0:
        turtle = turtle_top
        position = turtle_rect = turtle.get_rect()
        speed = [5, 0]

    # 填充背景
    screen.fill(bg)

    # 更新圖片
    screen.blit(turtle, position)

    # 更新畫面
    pygame.display.flip()

    # 延遲 10 毫秒
    pygame.time.delay(10)
