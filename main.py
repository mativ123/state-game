import sys
import pygame
import statemachine
import re
from obj import sprite, Map

walkSpeed = 0.4

pygame.init()
screen = pygame.display.set_mode((700, 700))

duck = sprite("sprites/and.png", walkSpeed)
duck.scaleX(100)
duck.center(screen)

first_map = Map("sprites/map 1.png", "sprites/map 1 - col.png", screen)
first_map.center(screen)

clock = pygame.time.Clock()

while True:
    dt = clock.tick(60)

    event = pygame.event.get()
    dinmor = [{"type": x.type, "key": x.dict["key"]} for x in event if "key" in x.dict]
    [sys.exit() for x in event if x.type == pygame.QUIT]

    duck.move(dinmor, dt, screen)
    first_map.move(duck.pos[0], duck.pos[1], screen)
    duck.adjust(first_map.colCheck(duck.rect, screen))

    screen.fill((0, 0, 0))
    first_map.blit(screen)
    duck.blit(screen)
    pygame.display.flip()
