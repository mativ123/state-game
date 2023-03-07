from PIL import Image
import numpy as np
import copy
import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 1000))

image = Image.open("sprites/map 1.png").convert('L')
data = list(image.getdata())

new_data = [1 if x > 0 else 0 for x in data]

x = 1
res = []
temp = []
for value in new_data:
    if x % image.size[0] == 0:
        x = 1
        res.append(copy.copy(temp))
        temp.clear()
    else:
        x += 1
        temp.append(value)

draw_box = pygame.Rect(0, 0, 1, 1)

while True:
    screen.fill((0,0,0))
    for i in range(len(new_data)):
        white = False
        if (draw_box.x + 1) % image.size[0]:
            draw_box.x = 0
            draw_box.y += 1
            print(f"x: {draw_box.x}, y: {draw_box}")
            if res[draw_box.x][draw_box.y] == 0:
                white = False
            else:
                white = True
        else:
            draw_box.x += 1
        if white:
            screen.fill((255, 255, 255), draw_box)
        else:
            screen.fill((0, 0, 0), draw_box)
