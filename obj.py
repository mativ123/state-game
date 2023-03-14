import pygame

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

class Player:
    def __init__(self, img: str, walkSpeed: int):
        self.sprite = pygame.image.load(img)
        self.rect = self.sprite.get_rect()
        self.walkSpeed = walkSpeed
        self.speed = [0, 0]
        self.input = [
            [pygame.K_LEFT, 0, -1],
            [pygame.K_RIGHT, 0, 1],
            [pygame.K_UP, 1, -1],
            [pygame.K_DOWN, 1, 1],
        ]

    def move(self, dt):
        self.rect = self.rect.move(self.speed[0] * dt, self.speed[1] * dt)

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
        self.rect = self.sprite.get_rect()

    def scaleY(self, size: float):
        h = size
        w = self.sprite.get_width() * (size / self.sprite.get_height())
        self.sprite = pygame.transform.scale(self.sprite, (w,h))

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

