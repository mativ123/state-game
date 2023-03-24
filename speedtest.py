import time
import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 1000))

image = pygame.image.load("sprites/map 1.png")
rect = image.get_rect()

clip = pygame.Rect(0, 0, 100, 100)
screen.set_clip(clip)

t0 = time.time()
screen.blit(image, rect)
pygame.display.update(clip)
print(f"dif: {time.time() - t0}")
