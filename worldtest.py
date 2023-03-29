import pygame
import sys
from obj import Event, World, Player, linje

pygame.init()

screen = pygame.display.set_mode((1000, 1000))

world = World("sprites/map 1.png", screen)
event = Event()

duck = Player("sprites/and.png", 0.65, screen)
duck.scaleY(100)

world.bgBlit(screen)

clock = pygame.time.Clock()

world.genLines("map1", screen)

while True:
    dt = clock.tick(60)
    event.update()
    if event.quit():
        sys.exit()

    for i, inp in enumerate(duck.input):
        duck.event(i, event.checkInput(pygame.KEYDOWN, inp[0]), pygame.KEYDOWN)
        duck.event(i, event.checkInput(pygame.KEYUP, inp[0]), pygame.KEYUP)

    duck.move(dt)
    duck.collision(world.lines, screen)
    world.blitPlayer(duck, screen)
    pygame.display.flip()
