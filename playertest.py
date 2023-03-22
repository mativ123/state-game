import json
import pygame
import sys
from obj import Event, Player

pygame.init()
screen = pygame.display.set_mode((1000, 1000))

inp = Event()
dinmor = Player("sprites/svamp.png", 1)

clock = pygame.time.Clock()

while True:
    dt = clock.tick(60)
    inp.update()
    if inp.quit():
        sys.exit()

    for i, key in enumerate(dinmor.input):
        if inp.checkInput(pygame.KEYDOWN, key[0]):
            dinmor.event(i, True, pygame.KEYDOWN)
        if inp.checkInput(pygame.KEYUP, key[0]):
            dinmor.event(i, True, pygame.KEYUP)

    dinmor.move(dt)

    screen.fill((0, 255, 174))

    dinmor.blit(screen)

    pygame.display.flip()
