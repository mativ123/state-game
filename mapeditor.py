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
    cancelLinje = linje.to(standard)

    @tolinje.on
    def on_tolinje(self):
        print("tegn en linje")

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

while True:
    inp.update()
    if inp.quit():
        sys.exit()

    for i, butt in enumerate(buttonsInfo):
        color = (0,0,0)
        button.y = paddingy + ((paddingy + button.h) * i)
        if not button.collidepoint(pygame.mouse.get_pos()):
            color = (235, 52, 88)
        elif not pygame.mouse.get_pressed(num_buttons=3)[0]:
            color = (179, 41, 69)
        elif menu.current_state.id != "linje":
            menu.tolinje()

        if menu.current_state.id == "linje":
            color = (179, 41, 69)

        screen.fill(color, button)
        screen.blit(buttonText.render(buttonsInfo[i][0], True, (0, 255, 140)), (button.left, button.centery))
        pygame.display.update(button)
