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

rlinje = linje((333, 0), (333, 1000))
llinje = linje((666, 0), (666, 1000))
tlinje = linje((0, 333), (1000, 333))
blinje = linje((0, 666), (1000, 666))

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

    rlinje.draw(screen)
    llinje.draw(screen)
    tlinje.draw(screen)
    blinje.draw(screen)
    screen.fill((79, 227 ,153), player)

    corners = [player.topleft, player.bottomleft, player.bottomright, player.topright, (player.left, player.centery), (player.right, player.centery), (player.centerx, player.top), (player.centerx, player.bottom)]

    for corner in corners:
        rdif = rlinje.drawLerp(corner, screen, player.center)
        ldif = llinje.drawLerp(corner, screen, player.center)
        tdif = tlinje.drawLerp(corner, screen, player.center)
        bdif = blinje.drawLerp(corner, screen, player.center)
        player = player.move(rdif[0], rdif[1])
        player = player.move(ldif[0], ldif[1])
        player = player.move(tdif[0], tdif[1])
        player = player.move(bdif[0], bdif[1])
        if rdif[0]:
            speed[0] = 0
            break
        if ldif[0]:
            speed[0] = 0
            break
        if tdif[1]:
            speed[1] = 0
            break
        if bdif[1]:
            speed[1] = 0
            break

    print(clock.get_fps())

    pygame.display.flip()

