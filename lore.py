import pygame
from obj import Event

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((500, 1000))

event = Event()

font = pygame.font.Font("CASTELAR.ttf", 30)
rect = pygame.Rect(0, 0, screen.get_width(), font.get_height())

screen.fill((0, 0, 0))

with open("lore.txt", "r") as f:
    for line in f.readlines():
        screen.blit(font.render(line.strip(), True, (255, 0, 0)), rect)
        rect.y += rect.h

pygame.display.flip()

event.update()
while not event.quit():
    event.update()
