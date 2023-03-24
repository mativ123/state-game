import sys
import pygame
import statemachine
import json
from obj import Event, Player, linje

pygame.init()

screen = pygame.display.set_mode((1000, 1000))
bg = pygame.image.load("sprites/map 1.png")
rec = bg.get_rect()
rec.x = screen.get_width() / 2 - rec.w / 2
rec.y = screen.get_height() / 2 - rec.h / 2

event = Event()
duck = Player("sprites/and.png", 1)

clock = pygame.time.Clock()

# screen.fill((0, 0, 0))
# screen.blit(bg, rec)
# pygame.display.flip()

while True:
    event.update()

    if event.quit():
        sys.exit()

    dt = clock.tick(60)

    for i, key in enumerate(duck.input):
        if event.checkInput(pygame.KEYDOWN, key[0]):
            duck.event(i, True, pygame.KEYDOWN)
        if event.checkInput(pygame.KEYUP, key[0]):
            duck.event(i, True, pygame.KEYUP)

    # screen.blit(bg, rec)
    duck.move(dt)
    screen.fill((0, 0, 0))
    duck.blit(screen)
    pygame.display.flip()

