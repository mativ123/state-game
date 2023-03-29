import pygame
import sys
from obj import Event, linje, Player, World

pygame.init()
screen = pygame.display.set_mode((1000, 1000))

event = Event()

# col = linje((333, 500), (666, 500))
world = World("sprites/map 1.png", screen)
world.genLines("map1")

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
    for line in world.lines:
        line.draw(screen)
    # col.draw(screen)
    player.blit(screen)
    for line in player.lines:
        pygame.draw.line(screen, (200, 50, 50), line[0], line[1], 3)
    player.collision(world.lines, screen)
    pygame.display.flip()
