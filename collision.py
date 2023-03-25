import pygame
import sys
from obj import Event, World, Player

pygame.init()

screen = pygame.display.set_mode((1000, 1000))

world = World("sprites/map 2.png", screen)
event = Event()

duck = Player("sprites/and.png", 0.65)
duck.scaleY(100)

world.bgBlit(screen)

clock = pygame.time.Clock()

world.genLines("din")

while True:
    dt = clock.tick(60)
    event.update()
    if event.quit():
        sys.exit()

    for i, inp in enumerate(duck.input):
        duck.event(i, event.checkInput(pygame.KEYDOWN, inp[0]), pygame.KEYDOWN)
        duck.event(i, event.checkInput(pygame.KEYUP, inp[0]), pygame.KEYUP)

    duck.move(dt)
    world.blitPlayer(duck, screen)
