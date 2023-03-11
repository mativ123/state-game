import pygame
import sys

class linje:
    def __init__(self, A: tuple[int, int], B: tuple[int, int]):
        self.A = A
        self.B = B

    "public"
    def draw(self, screen: pygame.Surface):
        pygame.draw.line(screen, (255, 0, 0), self.A, self.B, width=3)

    def drawLerp(self, pos: tuple[int, int], screen: pygame.Surface, centerx: int):
        color = (0, 0, 0)
        inter = self.__intersect(pos)
        dif = 0
        
        if not (centerx > pos[0] and centerx > inter[0]) and not (centerx < pos[0] and centerx < inter[0]):
            return 0
        elif pos[0] > centerx and pos[0] > inter[0]:
            color = (255, 0, 0)
            dif = inter[0] - pos[0]
        elif pos[0] < centerx and pos[0] < inter[0]:
            color = (255, 0, 0)
            dif = inter[0] - pos[0]
        else:
            color = (0, 255, 0)

        if pos[1] > self.A[1] and pos[1] < self.B[1]:
            pygame.draw.line(screen, color, pos, inter, width=3)

        return dif

    "private"
    def __intersect(self, pos: tuple[int, int]):
        t = (pos[1] - self.A[1]) / (self.B[1] - self.A[1])
        x = self.A[0] + (self.B[0] - self.A[0]) * t
        y = self.A[1] + (self.B[1] - self.A[1]) * t

        return [x, y]

class Event:
    def __init__(self):
        self.events = pygame.event.get()

    "public"
    def quit(self):
        if True in [True for x in self.events if x.type == pygame.QUIT]:
            return True

    def checkInput(self, action: int, key: int):
        eventDict = self.__getDict()

        if [x for x in eventDict if x.get(str(action)) == key]:
            return True
        else:
            return False

    def update(self):
        self.events = pygame.event.get()

    "private"
    def __getDict(self):
        return [{str(x.type): x.dict["key"]} for x in self.events if x.dict.get("key")]

pygame.init()

screen = pygame.display.set_mode((1000, 1000))

dinfar = linje((333, 10), (333, 990))
dinmor = linje((666, 10), (666, 990))

player = pygame.Rect(450, 450, 100, 100)
speed = [0, 0]

event = Event()

clock = pygame.time.Clock()
walkSpeed = 1

while True:
    dt = clock.tick(60)
    event.update()

    if event.quit():
        sys.exit()

    if event.checkInput(pygame.KEYDOWN, pygame.K_LEFT):
        speed[0] = -walkSpeed
    if event.checkInput(pygame.KEYDOWN, pygame.K_RIGHT):
        speed[0] = walkSpeed
    if event.checkInput(pygame.KEYDOWN, pygame.K_UP):
        speed[1] = -walkSpeed
    if event.checkInput(pygame.KEYDOWN, pygame.K_DOWN):
        speed[1] = walkSpeed

    if event.checkInput(pygame.KEYUP, pygame.K_LEFT):
        speed[0] = 0
    if event.checkInput(pygame.KEYUP, pygame.K_RIGHT):
        speed[0] = 0
    if event.checkInput(pygame.KEYUP, pygame.K_UP):
        speed[1] = 0
    if event.checkInput(pygame.KEYUP, pygame.K_DOWN):
        speed[1] = 0

    player = player.move(speed[0] * dt, speed[1] * dt)
    screen.fill((177, 240, 115))

    dinfar.draw(screen)
    dinmor.draw(screen)
    screen.fill((79, 227 ,153), player)

    corners = [player.topleft, player.bottomleft, player.bottomright, player.topright]

    for corner in corners:
        dimbo = dinfar.drawLerp(corner, screen, player.centerx)
        diblo = dinmor.drawLerp(corner, screen, player.centerx)
        if dimbo:
            player = player.move(dimbo, 0)
        if diblo:
            player = player.move(diblo, 0)

    pygame.display.flip()

