import pygame
import sys
from obj import Event, linje, Player

pygame.init()
screen = pygame.display.set_mode((1000, 1000))

event = Event()

col = linje((333, 500), (666, 500))

player = Player("sprites/svamp.png", 0.65, screen)

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

    screen.fill((0, 255, 208))
    col.draw(screen)
    player.blit(screen)
    player.collision([col,], screen)
    pygame.display.flip()
