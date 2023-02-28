import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))

duck = pygame.image.load("sprites/and.png")
duck = pygame.transform.scale(duck, (duck.get_width() / 2, duck.get_height() / 2))
duckrect = duck.get_rect();

speed = [0, 0]
walkSpeed = 700

t = 0
prev_t = 0

while True:
    prev_t = t
    t = pygame.time.get_ticks()
    dt = (t - prev_t) / 1000
    print(t)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                speed[0] = walkSpeed
            if event.key == pygame.K_LEFT:
                speed[0] = -walkSpeed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                speed[0] = 0
            if event.key == pygame.K_LEFT:
                speed[0] = 0

    duckrect = duckrect.move(speed[0] * dt, speed[1] * dt)

    screen.fill((255, 0, 0))
    screen.blit(duck, duckrect)
    pygame.display.flip()
