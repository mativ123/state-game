import pygame
import json
import time
import random
import math

class Event:
    def __init__(self):
        self.events = pygame.event.get()

    def quit(self):
        if True in [True for x in self.events if x.type == pygame.QUIT]:
            return True

    def checkInput(self, action: int, key: int):
        eventDict = self.__getDict()

        if [x for x in eventDict if x.get(str(action)) == key]:
            return True
        else:
            return False

    def checkMouse(self, action: int, mButton: int):
        ifType = action in self.__getTypes()
        ifButton = pygame.mouse.get_pressed()[mButton]
        return ifType and ifButton

    def update(self):
        self.events = pygame.event.get()

    def __getDict(self):
        return [{str(x.type): x.dict["key"]} for x in self.events if x.dict.get("key")]
    
    def __getTypes(self):
        return [x.type for x in self.events]

class Player:
    def __init__(self, img: str, walkSpeed: int, screen: pygame.Surface):
        self.sprite = pygame.image.load(img)
        self.rect = self.sprite.get_rect()
        self.rect.x = screen.get_width() / 2 - self.rect.w / 2
        self.rect.y = screen.get_height() / 2 - self.rect.h / 2
        self.prevRect = pygame.Rect(self.rect)
        self.walkSpeed = walkSpeed
        self.speed = [0, 0]
        self.input = [
            [pygame.K_LEFT, 0, -1],
            [pygame.K_RIGHT, 0, 1],
            [pygame.K_UP, 1, -1],
            [pygame.K_DOWN, 1, 1],
        ]
        self.__genPoints()

    def move(self, dt):
        self.prevRect = self.rect
        self.rect = self.rect.move(self.speed[0] * dt, self.speed[1] * dt)
        if self.prevRect != self.rect:
            self.__genPoints()

    def event(self, index: int, click: bool, type: int):
        if not click:
            return 0
        elif type == pygame.KEYDOWN:
            self.speed[self.input[index][1]] = self.walkSpeed * self.input[index][2]
        elif type == pygame.KEYUP:
            self.speed[self.input[index][1]] = 0

    def blit(self, screen: pygame.Surface):
        screen.blit(self.sprite, self.rect)

    def scaleX(self, size: float):
        w = size
        h = self.sprite.get_height() * (size / self.sprite.get_width())
        self.sprite = pygame.transform.scale(self.sprite, (w,h))
        self.rect.update(self.rect.topleft, self.sprite.get_size())

    def scaleY(self, size: float):
        h = size
        w = self.sprite.get_width() * (size / self.sprite.get_height())
        self.sprite = pygame.transform.scale(self.sprite, (w,h))
        self.rect.update(self.rect.topleft, self.sprite.get_size())

    def collision(self, worldLine: list, screen: pygame.Surface):
        res = []
        for col in worldLine:
            res.extend([col.colPoint(x, screen, self.rect.center) for x in self.corners])
        for dif in res:
            if dif[0] != 0:
                self.speed[0] = 0
            if dif[1] != 0:
                self.speed[1] = 0

            self.rect = self.rect.move(dif)
        self.__genPoints()

    def __genPoints(self):
        self.corners = [self.rect.topleft, self.rect.topright, self.rect.bottomright, self.rect.bottomleft]

class linje:
    def __init__(self, A: tuple[int, int], B: tuple[int, int]):
        self.A = A
        self.B = B

    def draw(self, screen: pygame.Surface):
        pygame.draw.line(screen, (255, 0, 0), self.A, self.B, width=3)

    def colPoint(self, pos: tuple[int, int], screen: pygame.Surface, center: tuple[int, int]):
        dif = [0, 0]
        if pos[1] > self.A[1] and pos[1] < self.B[1]:
            dif[0] = self.__col(pos, screen, center[0], 0)
        elif pos[0] > self.A[0] and pos[0] < self.B[0]:
            dif[1] = self.__col(pos, screen, center[1], 1)

        return dif

    def __intersect(self, pos1: tuple[int, int], pos2: tuple[tuple[int, int], tuple[int, int]], xy: int):
        t = (pos1[xy] - pos2[0][xy]) / (pos2[1][xy] - pos2[0][xy])
        x = pos2[0][0] + (pos2[1][0] - pos2[0][0]) * t
        y = pos2[0][1] + (pos2[1][1] - pos2[0][1]) * t

        return [x, y]

    def __col(self, pos: tuple[int, int], screen: pygame.Surface, center: int, xy: int):
        color = (0, 0, 0)
        inter = 0
        inter = self.__intersect(pos, (self.A, self.B), 1 if xy == 0 else 0)
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

        # pygame.draw.line(screen, color, pos, inter, width=3)

        return dif

class Editor:
    def __init__(self):
        self.lines = []
        self.rects = []

    def addLine(self, coor: tuple[tuple[int, int], tuple[int, int]]):
        self.lines.append(coor)
        self.__genRect(coor)

    def save(self, name: str):
        info = [{"A": x[0], "B": x[1]} for x in self.lines]

        with open(f"{name}.json", "w") as fp:
            json.dump(info, fp, indent=4)

    def drawPoints(self, screen: pygame.Surface):
        perc = lambda t, s : (t[0] * (s.get_width() - 200), t[1] * (s.get_height()))
        for line in self.lines:
            pygame.draw.circle(screen, (255, 0, 0), perc(line[0], screen), 3, width=0)
            pygame.draw.circle(screen, (255, 0, 0), perc(line[1], screen), 3, width=0)
        pygame.display.flip()

    def __genRect(self, line: tuple[tuple[int, int], tuple[int, int]]):
        x = 0
        y = 0
        w = 0
        h = 0
        if line[0][0] < line[1][0]:
            x = line[0][0]
            w = line[1][0] - x
        elif line[0][0] > line[1][0]: 
            x = line[1][0]
            w = line[0][0] - x

        if line[0][1] < line[1][1]:
            y = line[0][1]
            h = line[1][1] - y
        elif line[0][0] > line[1][0]: 
            y = line[1][1]
            h = line[0][1] - y

        self.rects.append(pygame.Rect(x, y, w, h))

class World:
    def __init__(self, img: str, screen: pygame.Surface):
        self.bg = pygame.image.load(img)
        self.bgrect = self.bg.get_rect()
        self.bgrect.x = screen.get_width() / 2 - self.bgrect.w / 2
        self.bgrect.y = screen.get_height() / 2 - self.bgrect.h / 2
        self.lines = []
        self.mush = []
        self.mushOutline = []
        self.shroomCount = 0
        self.men = []
        self.killCount = 0
        self.blood = []

    def bgBlit(self, screen: pygame.Surface):
        screen.set_clip()
        screen.blit(self.bg, self.bgrect)
        pygame.display.flip()

    def blitPlayer(self, player: Player, screen: pygame.Surface):
        screen.set_clip(player.prevRect)
        screen.blit(self.bg, self.bgrect)
        screen.set_clip(player.rect)
        screen.blit(player.sprite, player.rect)
        pygame.display.update([player.rect, player.prevRect])

    def genLines(self, fName: str):
        f = open(f"{fName}.json", "r")
        data = json.load(f)
        for entry in data:
            self.lines.append(linje(self.__lineOffset(entry["A"]), self.__lineOffset(entry["B"])))

    def blitMush(self, screen: pygame.Surface):
        screen.set_clip()
        self.__drawMushs(screen)
        pygame.display.update([shroom.rect for shroom in self.mush])

    def drawAll(self, player: Player, screen: pygame.Surface):
        screen.set_clip(player.prevRect)
        screen.blit(self.bg, self.bgrect)
        self.__drawMushs(screen)
        screen.set_clip(player.rect)
        self.__drawMushs(screen)
        self.__drawMen(screen)
        screen.blit(player.sprite, player.rect)
        pygame.display.update([player.rect, player.prevRect])

    def moveMen(self, target: tuple[int, int], dt: float, screen: pygame.Surface):
        for man in self.men:
            if man.dead:
                continue
            man.move(target, dt, self.lines, screen)

    def punchMen(self, player: tuple[int, int], click: bool, screen: pygame.Surface):
        for i, man in enumerate(self.men):
            if man.dead:
                continue
            if man.checkPunch(player) and click:
                man.hp -= 1
            if man.hp == 0:
                self.__eraseMan(screen, i)
                man.kill()
                self.killCount += 1

    
    def genMush(self, n: int):
        for i in range(n):
            temp = collectable("sprites/svamp.png", self.__randomPos())
            temp.scaleX(70)
            self.mush.append(temp)
            self.mushOutline.append(False)

    def pickup(self, player: tuple[int, int], click: bool, screen: pygame.Surface):
        for i, shroom in enumerate(self.mush):
            if shroom.checkPickup(player) and click:
                self.shroomCount += 1
                print(self.shroomCount)
                self.mush.pop(i)
                self.mushOutline.pop(i)
                screen.set_clip(shroom.rect)
                screen.blit(self.bg, self.bgrect)
                pygame.display.update(shroom.rect)

            elif shroom.checkPickup(player):
                self.mushOutline[i] = True
                self.__drawMush(screen, i)
            else:
                self.mushOutline[i] = False
                self.__drawMush(screen, i)

    def genMen(self, n: int):
        for i in range(n):
            self.men.append(Ai("sprites/mand.png", self.__randomPos()))

    def drawScore(self, shrooms: bool, screen: pygame.Surface):
        color = (255, 0, 0)
        text = str(self.shroomCount if shrooms else self.killCount)
        if not pygame.font.get_init():
            pygame.font.init()
        scoreF = pygame.font.Font("Consolas-Regular.ttf", 40)
        rectF = pygame.Rect((0, 0), scoreF.size(text))
        rectF.x = screen.get_width() - rectF.w
        screen.set_clip(rectF)
        screen.blit(self.bg, self.bgrect)
        screen.set_clip()
        screen.blit(scoreF.render(text, True, color), rectF)
        pygame.display.update(rectF)

    def __randomPos(self):
        x = random.randint(self.bgrect.x, self.bgrect.x + self.bgrect.w)
        y = random.randint(self.bgrect.y, self.bgrect.y + self.bgrect.h)
        return (x, y)

    def __lineOffset(self, point: tuple[int, int]):
        return (point[0] * self.bg.get_width() + self.bgrect.x, point[1] * self.bg.get_height() + self.bgrect.y)

    def __drawMush(self, screen: pygame.Surface, n: int):
        screen.set_clip(self.mush[n])
        screen.blit(self.bg, self.bgrect)
        screen.blit(self.mush[n].sprite, self.mush[n].rect)
        if self.mushOutline[n]:
            self.mush[n].drawOutline(screen)
        pygame.display.update(self.mush[n].rect)

    def __drawMushs(self, screen: pygame.Surface):
        screen.blits((shroom.sprite, shroom.rect) for shroom in self.mush)
        for i, shroom in enumerate(self.mush):
            if self.mushOutline[i]:
                shroom.drawOutline(screen)

    def __drawMen(self, screen: pygame.Surface):
        for man in self.men:
            screen.set_clip(man.prevRect)
            screen.blit(self.bg, self.bgrect)
            screen.set_clip(man.rect)
            screen.blit(self.bg, self.bgrect)
        screen.set_clip()
        screen.blits([(man.sprite, man.rect) for man in self.men])
        rects = [man.rect for man in self.men] 
        rects.extend([man.prevRect for man in self.men])
        pygame.display.update(rects)

    def __eraseMan(self, screen: pygame.Surface, n: int):
        screen.set_clip(self.men[n].prevRect)
        screen.blit(self.bg, self.bgrect)
        screen.set_clip(self.men[n].rect)
        screen.blit(self.bg, self.bgrect)
        pygame.display.update([self.men[n].rect, self.men[n].prevRect])
        screen.set_clip()

class collectable:
    def __init__(self, img: str, pos: tuple[int, int]):
        self.sprite = pygame.image.load(img)
        self.rect = self.sprite.get_rect()
        self.rect = self.rect.move(pos)

    def scaleX(self, size: float):
        w = size
        h = self.sprite.get_height() * (size / self.sprite.get_width())
        self.sprite = pygame.transform.scale(self.sprite, (w,h))
        self.rect.update(self.rect.topleft, self.sprite.get_size())

    def scaleY(self, size: float):
        h = size
        w = self.sprite.get_width() * (size / self.sprite.get_height())
        self.sprite = pygame.transform.scale(self.sprite, (w,h))
        self.rect.update(self.rect.topleft, self.sprite.get_size())

    def checkPickup(self, player: tuple[int, int]):
        x = pow(self.rect.centerx - player[0], 2)
        y = pow(self.rect.centery - player[1], 2)
        dist = math.sqrt(x + y)
        if dist < 140:
            return True
        else:
            return False

    def drawOutline(self, screen: pygame.Surface):
        mask = pygame.mask.from_surface(self.sprite)
        maskeOutline = mask.outline()
        for i, point in enumerate(maskeOutline):
            maskeOutline[i] = (point[0] + self.rect.x, point[1] + self.rect.y)
        pygame.draw.polygon(screen, (0, 255, 128), maskeOutline, 5)

class Ai:
    def __init__(self, img: str, pos: tuple[int, int]):
        self.sprite = pygame.image.load(img)
        self.deadSprite = pygame.image.load("sprites/mand_knust.png")
        self.rect = self.sprite.get_rect().move(pos)
        self.prevRect = self.rect
        self.speed = 0.2
        self.hp = 3
        self.dead = False
        self.__genPoints()

    def scaleX(self, size: float):
        w = size
        h = self.sprite.get_height() * (size / self.sprite.get_width())
        self.sprite = pygame.transform.scale(self.sprite, (w,h))
        self.rect.update(self.rect.topleft, self.sprite.get_size())

    def scaleY(self, size: float):
        h = size
        w = self.sprite.get_width() * (size / self.sprite.get_height())
        self.sprite = pygame.transform.scale(self.sprite, (w,h))
        self.rect.update(self.rect.topleft, self.sprite.get_size())

    def move(self, player: tuple[int, int], dt, lines: list, screen: pygame.Surface):
        self.prevRect = self.rect
        angle = math.atan2(player[1] - self.rect.centery, player[0] - self.rect.centerx)
        self.rect = self.rect.move(math.cos(angle) * -self.speed * dt, math.sin(angle) * -self.speed * dt)
        res = []
        for col in lines:
            res.extend([col.colPoint(x, screen, self.rect.center) for x in self.corners])
        for dif in res:
            self.rect = self.rect.move(dif)
        self.__genPoints()

    def checkPunch(self, player: tuple[int, int]):
        x = pow(self.rect.centerx - player[0], 2)
        y = pow(self.rect.centery - player[1], 2)
        dist = math.sqrt(x + y)
        if dist < 140:
            return True
        else:
            return False

    def kill(self):
        self.dead = True
        self.sprite = self.deadSprite

    def __genPoints(self):
        self.corners = [self.rect.topleft, self.rect.topright, self.rect.bottomright, self.rect.bottomleft]
