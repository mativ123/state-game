import pygame
import sys
import math
from obj import Event, Player, Ai, World

pygame.init()
screen = pygame.display.set_mode((1000, 1000))

event = Event()
world = World("sprites/map 2.png", screen)
world.genMen(3)
world.bgBlit(screen)
world.genLines("map2")

player = Player("sprites/and.png", 0.65, screen)

# enemy = Ai("sprites/mand.png")

clock = pygame.time.Clock()

while True:
    dt = clock.tick(60)

    event.update()
    if event.quit():
        sys.exit()

    for i, inp in enumerate(player.input):
        player.event(i, event.checkInput(pygame.KEYDOWN, inp[0]), pygame.KEYDOWN)
        player.event(i, event.checkInput(pygame.KEYUP, inp[0]), pygame.KEYUP)

    player.move(dt)
    player.collision(world.lines, screen)
    world.moveMen(player.rect.center, dt, screen)
    world.punchMen(player.rect.center, event.checkInput(pygame.KEYDOWN, pygame.K_e), screen)

    world.drawAll(player, screen)
