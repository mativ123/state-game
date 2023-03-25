import pygame
import sys
from obj import linje, Event

pygame.init()

screen = pygame.display.set_mode((1000, 1000))

rlinje = linje((333, 0), (333, 1000))
llinje = linje((666, 0), (666, 1000))
tlinje = linje((0, 333), (1000, 333))
blinje = linje((0, 666), (1000, 666))

player = pygame.Rect(450, 450, 100, 100)
speed = [0, 0]

event = Event()

clock = pygame.time.Clock()
walkSpeed = 1

while True:
    dt = clock.tick(60)
    event.update()

    if event.quit():
        sys.exit()

    if event.checkInput(pygame.KEYDOWN, pygame.K_LEFT):
        speed[0] = -walkSpeed
    if event.checkInput(pygame.KEYDOWN, pygame.K_RIGHT):
        speed[0] = walkSpeed
    if event.checkInput(pygame.KEYDOWN, pygame.K_UP):
        speed[1] = -walkSpeed
    if event.checkInput(pygame.KEYDOWN, pygame.K_DOWN):
        speed[1] = walkSpeed

    if event.checkInput(pygame.KEYUP, pygame.K_LEFT):
        speed[0] = 0
    if event.checkInput(pygame.KEYUP, pygame.K_RIGHT):
        speed[0] = 0
    if event.checkInput(pygame.KEYUP, pygame.K_UP):
        speed[1] = 0
    if event.checkInput(pygame.KEYUP, pygame.K_DOWN):
        speed[1] = 0

    player = player.move(speed[0] * dt, speed[1] * dt)
    screen.fill((177, 240, 115))

    rlinje.draw(screen)
    llinje.draw(screen)
    tlinje.draw(screen)
    blinje.draw(screen)
    screen.fill((79, 227 ,153), player)

    corners = [player.topleft, player.bottomleft, player.bottomright, player.topright, (player.left, player.centery), (player.right, player.centery), (player.centerx, player.top), (player.centerx, player.bottom)]

    for corner in corners:
        rdif = rlinje.drawLerp(corner, screen, player.center)
        ldif = llinje.drawLerp(corner, screen, player.center)
        tdif = tlinje.drawLerp(corner, screen, player.center)
        bdif = blinje.drawLerp(corner, screen, player.center)
        player = player.move(rdif[0], rdif[1])
        player = player.move(ldif[0], ldif[1])
        player = player.move(tdif[0], tdif[1])
        player = player.move(bdif[0], bdif[1])
        if rdif[0]:
            speed[0] = 0
            break
        if ldif[0]:
            speed[0] = 0
            break
        if tdif[1]:
            speed[1] = 0
            break
        if bdif[1]:
            speed[1] = 0
            break

    print(clock.get_fps())

    pygame.display.flip()

