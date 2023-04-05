import pygame
import sys
import math
from obj import Event, Player, Ai

pygame.init()
screen = pygame.display.set_mode((1000, 1000))

event = Event()

player = Player("sprites/and.png", 0.65, screen)

enemy = Ai("sprites/mand.png")

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
    enemy.move(player.rect.center, dt, screen.get_size())

    screen.fill((227, 127, 150))
    player.blit(screen)
    screen.blit(enemy.sprite, enemy.rect)
    pygame.display.flip()
