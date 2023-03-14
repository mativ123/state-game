import json
import pygame
import sys
from obj import Event

pygame.init()
print(sys.argv[1])
img = pygame.image.load(sys.argv[1])
imgRect = img.get_rect()
buttons = pygame.Rect(imgRect.w, 0, 200, imgRect.h)
screen = pygame.display.set_mode((imgRect.w + buttons.w, imgRect.h))
button = pygame.Rect()

inp = Event()

dinmor = {
    "din": "mor"
}

with open("data.json", "w") as fp:
    json.dump(dinmor, fp)

while True:
    inp.update()
    if inp.quit():
        sys.exit()

    screen.fill((255, 255, 255))
    screen.blit(img, imgRect)
    screen.fill((3, 252, 115), buttons)
    pygame.display.flip()
