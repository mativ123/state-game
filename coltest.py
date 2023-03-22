import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((1000, 1000))

box = pygame.Rect(screen.get_width() / 2 - 50, 110, 100, 100)
ground = pygame.Rect(0, screen.get_height() - 30, screen.get_width(), 30)

clock = pygame.time.Clock()

fallSpeed = 0
flyspeed = 0

while True:
    dt = clock.tick(60)
    event = pygame.event.get()
    [sys.exit() for x in event if x.type == pygame.QUIT]

    dinmor = [{str(x.type): x.dict["key"]} for x in event if x.dict.get("key")]
    for inp in dinmor:
        if inp.get(str(pygame.KEYDOWN)) == pygame.K_DOWN:
            flyspeed = 1
        if inp.get(str(pygame.KEYUP)) == pygame.K_DOWN:
            flyspeed = 0
        if inp.get(str(pygame.KEYDOWN)) == pygame.K_UP:
            flyspeed = -1
        if inp.get(str(pygame.KEYUP)) == pygame.K_UP:
            flyspeed = 0

    if box.y + box.height > ground.y:
        box = box.move(0, ground.y - (box.y + box.height))
        flyspeed = 0
    else:
        box = box.move(0, flyspeed * dt)

    screen.fill((244, 0, 103))

    screen.fill((0, 165, 100), box)
    screen.fill((66, 135, 245), ground)

    pygame.display.flip()
