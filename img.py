from PIL import Image
import numpy as np
import copy
import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 1000))

image = Image.open("sprites/map 1.png").convert('L')
image.save("garry.png")
