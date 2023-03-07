import sys
import pygame
import statemachine
import re
from obj import sprite

walkSpeed = 0.4

pygame.init()
screen = pygame.display.set_mode((700, 700))

duck = sprite("sprites/and.png", walkSpeed)

clock = pygame.time.Clock()

while True:
    dt = clock.tick(60)

    event = pygame.event.get()
    dinmor = [{"type": x.type, "key": x.dict["key"]} for x in event if "key" in x.dict]
    [sys.exit() for x in event if x.type == pygame.QUIT]

    duck.move(dinmor, dt)

    screen.fill((255, 0, 0))
    duck.blit(screen)
    pygame.display.flip()
