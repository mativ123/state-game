import pygame
import sys
from obj import Event, Player, World, linje

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((1000, 1000))

event = Event()
world = World("sprites/map 2.png", screen)

duck = Player("sprites/and.png", 1)

clock = pygame.time.Clock()

world.bgBlit(screen)

world.genLines("din")
for line in world.lines:
    print(line.A)
    line.draw(screen)

pygame.display.flip()

while True:
    dt = clock.tick(60)
    print(clock.get_fps())

    event.update()
    if event.quit():
        sys.exit()

   #  for i, key in enumerate(duck.input):
   #      duck.event(i, event.checkInput(pygame.KEYDOWN, key[0]), pygame.KEYDOWN)
   #      duck.event(i, event.checkInput(pygame.KEYUP, key[0]), pygame.KEYUP)

   #  duck.move(dt)
   #  world.blitPlayer(duck, screen)
