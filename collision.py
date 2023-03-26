import pygame
import sys
from obj import Event, linje

pygame.init()
screen = pygame.display.set_mode((1000, 1000))

event = Event()

col = linje((500, 333), (500, 666))
test = linje((600, 600), (600, 900))

while True:
    event.update()
    if event.quit():
        sys.exit()


    screen.fill((0, 255, 208))
    col.draw(screen)
    test.draw(screen)
    pygame.draw.circle(screen, (255, 0, 0), (700, 750), 3)
    col.colLine((test.A, test.B), screen, (700, 750))
    pygame.display.flip()
