import json
import pygame
import sys
from obj import Event

pygame.init()
pygame.font.init()

print(sys.argv[1])
img = pygame.image.load(sys.argv[1])
imgRect = img.get_rect()
buttons = pygame.Rect(imgRect.w, 0, 200, imgRect.h)
screen = pygame.display.set_mode((imgRect.w + buttons.w, imgRect.h))
paddingx = 10
paddingy = 10
buttonsInfo = [["lav linje",], ["gem",]]
button = pygame.Rect(buttons.x + paddingx, 0, buttons.w - paddingx * 2, buttons.h / len(buttonsInfo) - paddingy * 2)

buttonText = pygame.font.Font("Consolas-Regular.ttf", 20)
buttonTextRect = pygame.Rect(0, 0, 0, 0)

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
    for i, butt in enumerate(buttonsInfo):
        button.y = paddingy + ((paddingy + button.h) * i)
        print(button.y)
        screen.fill((235, 52, 88), button)
    screen.blit(buttonText.render("din mor", True, (255, 0, 0)), buttonTextRect)
    pygame.display.flip()
