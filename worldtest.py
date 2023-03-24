import pygame
import sys
from obj import Event, Player, World

pygame.init()
pygame.font.init()

fps = pygame.font.SysFont("Arial", 20)
fpsrect = pygame.Rect(0, 0, 30, 30)

screen = pygame.display.set_mode((1000, 1000))

event = Event()
world = World("sprites/map 1.png", screen)

screen.fill((0, 0, 0))
pygame.display.flip()

duck = Player("sprites/and.png", 1)

clock = pygame.time.Clock()

world.bgBlit(screen)

while True:
    dt = clock.tick(60)
    print(clock.get_fps())
    pygame.display.update(fpsrect)

    event.update()
    if event.quit():
        sys.exit()

    for i, key in enumerate(duck.input):
        if event.checkInput(pygame.KEYDOWN, key[0]):
            duck.event(i, True, pygame.KEYDOWN)
        if event.checkInput(pygame.KEYUP, key[0]):
            duck.event(i, True, pygame.KEYUP)

    duck.move(dt)
    world.blitPlayer(duck, screen)
