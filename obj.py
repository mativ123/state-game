import pygame
import numpy as np

class sprite:
    def __init__(self, path: str, walkSpeed: float):
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.walkSpeed = walkSpeed
        self.speed = [0, 0]
        self.pos = [0, 0]

    def blit(self, screen: pygame.Surface):
        screen.blit(self.image, self.rect)
        screen.fill((255, 0, 0, 100), self.rect)

    def move(self, input: list[dict], dt: float, screen):
        keyup = [x for x in input if x["type"] == pygame.KEYUP]
        keydown = [x for x in input if x["type"] == pygame.KEYDOWN]
        for event in keydown:
            if event["key"] == pygame.K_LEFT:
                self.speed[0] = -self.walkSpeed
            if event["key"] == pygame.K_RIGHT:
                self.speed[0] = self.walkSpeed
            if event["key"] == pygame.K_DOWN:
                self.speed[1] = self.walkSpeed
            if event["key"] == pygame.K_UP:
                self.speed[1] = -self.walkSpeed
        
        for event in keyup:
            if event["key"] == pygame.K_LEFT:
                self.speed[0] = 0
            if event["key"] == pygame.K_RIGHT:
                self.speed[0] = 0
            if event["key"] == pygame.K_DOWN:
                self.speed[1] = 0
            if event["key"] == pygame.K_UP:
                self.speed[1] = 0

        self.pos[0] -= self.speed[0] * dt
        self.pos[1] -= self.speed[1] * dt

    def center(self, screen):
        self.rect.x = -(self.rect.w / 2 - screen.get_width() / 2)
        self.rect.y = -(self.rect.h / 2 - screen.get_height() / 2)

    def scaleX(self, size: float):
        w = size
        h = self.image.get_height() * (size / self.image.get_width())
        self.image = pygame.transform.scale(self.image, (w,h))
        self.rect = self.image.get_rect()

    def scaleY(self, size: float):
        h = size
        w = self.image.get_width() * (size / self.image.get_height())
        self.image = pygame.transform.scale(self.image, (w,h))

    def adjust(self, dist: int):
        if dist < 0:
            self.pos[0] += dist

class Map:
    def __init__(self, path: str, col: str, screen):
        self.image = pygame.image.load(path)
        self.colImg = pygame.image.load(col)
        self.collider = pygame.Surface((screen.get_width(), screen.get_height()))
        self.rect = self.image.get_rect()

    def center(self, screen):
        self.rect.x = -(self.rect.w / 2 - screen.get_width() / 2)
        self.rect.y = -(self.rect.h / 2 - screen.get_height() / 2)

    def move(self, x: int, y: int, screen):
        self.rect.x = x - (self.rect.w / 2 - screen.get_width() / 2)
        self.rect.y = y - (self.rect.h / 2 - screen.get_height() / 2)

    def blit(self, screen):
        screen.blit(self.colImg, self.rect)

    def colCheck(self, player: pygame.Rect, screen: pygame.Surface):
        self.collider.blit(self.colImg, self.rect)
        if np.mean(self.collider.get_at((player.x, player.y))[:3]) < 10:
            print("collision")
       #  x = player.x + round(player.width / 2)
       #  y = player.y
       #  while np.mean(self.collider.get_at((x, y))[:3]) > 10 and x > 0:
       #      x -= 1
       #  return player.x - x
        return 1
