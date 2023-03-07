import pygame

class sprite:
    def __init__(self, path: str, walkSpeed: float):
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.walkSpeed = walkSpeed
        self.speed = [0, 0]

    def blit(self, screen):
        screen.blit(self.image, self.rect)

    def move(self, input: list[dict], dt: float):
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

        self.rect = self.rect.move(self.speed[0] * dt, self.speed[1] * dt)

    def scaleY(self, size: float):
        h = size
        w = self.image.get_width() * (size[1] / self.image.get_height())
        pygame.transform.scale(self.image, (w,h))

    def scaleY(self, size: float):
        h = size
        w = self.image.get_width() * (size[1] / self.image.get_height())
        pygame.transform.scale(self.image, (w,h))



