import pygame
import sys
from obj import World, Event, Player

pygame.init()

screen = pygame.display.set_mode((1000, 1000))

world = World("sprites/map 1.png", screen)
world.bgBlit(screen)
world.genMush(1)

event = Event()

player = Player("sprites/and.png", 0.65, screen)

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
    world.pickup(player.rect.center)

    world.blitMush(screen)
    world.blitPlayer(player, screen)
