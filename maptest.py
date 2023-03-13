import pygame
import sys

class linje:
    def __init__(self, A: tuple[int, int], B: tuple[int, int]):
        self.A = A
        self.B = B

    "public"
    def draw(self, screen: pygame.Surface):
        pygame.draw.line(screen, (255, 0, 0), self.A, self.B, width=3)

    def drawLerp(self, pos: tuple[int, int], screen: pygame.Surface, center: tuple[int, int]):
        dif = [0, 0]
        if pos[1] > self.A[1] and pos[1] < self.B[1]:
            dif[0] = self.__col(pos, screen, center[0], 0)
        elif pos[0] > self.A[0] and pos[0] < self.B[0]:
            dif[1] = self.__col(pos, screen, center[1], 1)

        return dif

    "private"
    def __intersect(self, pos: tuple[int, int], xy: int):
        t = (pos[xy] - self.A[xy]) / (self.B[xy] - self.A[xy])
        x = self.A[0] + (self.B[0] - self.A[0]) * t
        y = self.A[1] + (self.B[1] - self.A[1]) * t

        return [x, y]

    def __col(self, pos: tuple[int, int], screen: pygame.Surface, center: int, xy: int):
        color = (0, 0, 0)
        inter = self.__intersect(pos, 1 if xy == 0 else 0)
        dif = 0
        if not (center > pos[xy] and center > inter[xy]) and not (center < pos[xy] and center < inter[xy]):
            return 0
        elif pos[xy] > center and pos[xy] > inter[xy]:
            color = (255, 0, 0)
            dif = inter[xy] - pos[xy]
        elif pos[xy] < center and pos[xy] < inter[xy]:
            color = (255, 0, 0)
            dif = inter[xy] - pos[xy]
        else:
            color = (0, 255, 0)

        pygame.draw.line(screen, color, pos, inter, width=3)

        return dif

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

dinfar = linje((333, 0), (333, 1000))
dinmor = linje((666, 0), (666, 1000))
dinbror = linje((0, 333), (1000, 333))
spasmager = linje((0, 666), (1000, 666))

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
    dinbror.draw(screen)
    spasmager.draw(screen)
    screen.fill((79, 227 ,153), player)

    corners = [player.topleft, player.bottomleft, player.bottomright, player.topright]

    for corner in corners:
        dimbo = dinfar.drawLerp(corner, screen, player.center)
        diblo = dinmor.drawLerp(corner, screen, player.center)
        broder = dinbror.drawLerp(corner, screen, player.center)
        bozo = spasmager.drawLerp(corner, screen, player.center)
        player = player.move(dimbo[0], dimbo[1])
        player = player.move(diblo[0], diblo[1])
        player = player.move(broder[0], broder[1])
        player = player.move(bozo[0], bozo[1])
        if dimbo[0]:
            speed[0] = 0
            break
        if diblo[0]:
            speed[0] = 0
            break
        if broder[1]:
            speed[1] = 0
            break
        if bozo[1]:
            speed[1] = 0
            break

    pygame.display.flip()

