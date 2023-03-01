import sys
import pygame
from statemachine import StateMachine, state
from funk import aspect_scale, andInp

pygame.init()
screen = pygame.display.set_mode((500, 500))

duck = pygame.image.load("sprites/and.png")
# duck = pygame.transform.scale(duck, (duck.get_width() / 2, duck.get_height() / 2))
duck = aspect_scale(duck, [50, 0])
duckrect = duck.get_rect();

speed = [0, 0]
walkSpeed = 700

t = 0
prev_t = 0

while True:
    prev_t = t
    t = pygame.time.get_ticks()
    dt = (t - prev_t) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        speed = andInp(event, walkSpeed)
    duckrect = duckrect.move(speed[0] * dt, speed[1] * dt)

    screen.fill((255, 0, 0))
    screen.blit(duck, duckrect)
    pygame.display.flip()
