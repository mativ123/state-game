import json
import pygame
import sys
from obj import Event
from statemachine import StateMachine, State

class Menu(StateMachine):
    standard = State("standard", initial=True)
    linje = State("linje")
    
    init = standard.to(standard)
    tolinje = standard.to(linje)
    endLinje = linje.to(standard)

    presses = 2

    @tolinje.on
    def on_tolinje(self):
        self.presses = 2

menu = Menu()
menu.init()

pygame.init()
pygame.font.init()

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

screen.fill((255, 255, 255))
screen.blit(img, imgRect)
screen.fill((3, 252, 115), buttons)
pygame.display.flip()

linecoor = [[0, 0], [0, 0]]

while True:
    inp.update()
    if inp.quit():
        sys.exit()

    if not menu.current_state.id == "linje":
        pass
    elif not menu.presses > 0:
        menu.endLinje()
        pygame.draw.line(screen, (255, 0, 0), linecoor[0], linecoor[1], width=3)
        pygame.display.update()
        linecoor = [0, 0]
    elif inp.checkMouse(pygame.MOUSEBUTTONDOWN, 0):
        print("klik")
        linecoor[menu.presses - 1] = list(pygame.mouse.get_pos())
        menu.presses -= 1

    for i, butt in enumerate(buttonsInfo):
        color = (0,0,0)
        button.y = paddingy + ((paddingy + button.h) * i)
        if not button.collidepoint(pygame.mouse.get_pos()):
            color = (235, 52, 88)
        elif not inp.checkMouse(pygame.MOUSEBUTTONDOWN, 0):
            color = (179, 41, 69)
        elif menu.current_state.id != "linje":
            menu.tolinje()
        if menu.current_state.id == "linje":
            screen.fill((3, 252, 115), buttons)
            pygame.display.update(buttons)
        else:
            screen.fill(color, button)
            screen.blit(buttonText.render(buttonsInfo[i][0], True, (0, 255, 140)), (button.left, button.centery))
            pygame.display.update(button)
