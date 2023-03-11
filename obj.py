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

    def adjust(self, dist: list[int]):
        # print(dist[1] - self.pos[0] - self.rect.width)
        self.pos[0] += dist[0] - self.pos[0]
        self.pos[0] -= dist[1] - self.pos[0]

class Map:
    def __init__(self, path: str, col: str, screen):
        self.image = pygame.image.load(path)
        self.colImg = pygame.image.load(col)
        self.collider = pygame.Surface((screen.get_width(), screen.get_height()))
        self.rect = self.image.get_rect()
        self.colX = [0,0,0,0]

    def center(self, screen):
        self.rect.x = -(self.rect.w / 2 - screen.get_width() / 2)
        self.rect.y = -(self.rect.h / 2 - screen.get_height() / 2)

    def move(self, x: int, y: int, screen):
        self.rect.x = x - (self.rect.w / 2 - screen.get_width() / 2)
        self.rect.y = y - (self.rect.h / 2 - screen.get_height() / 2)

    def blit(self, screen):
        screen.blit(self.image, self.rect)

    def colCheck(self, player: sprite, screen: pygame.Surface):
        self.collider.blit(self.colImg, self.rect)
        checkPos = [
            {"x": player.rect.x, "y": player.rect.y, "pos": player.pos[0]},
            {"x": player.rect.x + player.rect.width, "y": player.rect.y, "pos": player.pos[0] - player.rect.width},
        ]
        for index, pos in enumerate(checkPos):
            if self.__checkAt(pos["x"], pos["y"]):
                continue
            else:
                self.colX[index] = pos["pos"]
        dist = [self.colX[0] if self.__checkAt(x["x"], x["y"]) else x["pos"] for x in checkPos]
        return dist
       #  if self.__checkAt(player.rect.x, player.rect.y):
       #      return self.colX
       #  else:
       #      self.colX = player.pos[0]
       #  return player.pos[0]

    def __checkAt(self, x: int, y: int):
        if np.mean(self.collider.get_at((x, y))[:3]) < 10:
            return True
        else:
            return False
