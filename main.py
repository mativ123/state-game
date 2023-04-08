import pygame
import sys
from statemachine import StateMachine, State
from obj import Event, World, Player

pygame.init()
screen = pygame.display.set_mode((1000, 1000))

world = World("sprites/map 3.png", screen)
world.bgBlit(screen)
world.genLines("map3")
world.genMen(5)
world.genMush(10)

duck = Player("sprites/and.png", 0.65, screen)

event = Event()

clock = pygame.time.Clock()

class duckState(StateMachine):
    pickup = State("pickup", initial=True)
    beatup = State("beatup")
    win = State("win")

    start = pickup.to(pickup)
    donePickup = pickup.to(beatup)
    doneBeatup = beatup.to(win)

    @donePickup.before
    def killShrooms(self):
        world.killShrooms(screen)

    @doneBeatup.after
    def exit(self):
        sys.exit()

stateMac = duckState()
stateMac.start()

while True:
    dt = clock.tick(60)
    event.update()
    if event.quit():
        sys.exit()

    for i, inp in enumerate(duck.input):
        duck.event(i, event.checkInput(pygame.KEYDOWN, inp[0]), pygame.KEYDOWN)
        duck.event(i, event.checkInput(pygame.KEYUP, inp[0]), pygame.KEYUP)

    duck.move(dt)
    duck.collision(world.lines, screen)
    if stateMac.current_state.id == "pickup":
        world.pickup(duck.rect.center, event.checkInput(pygame.KEYDOWN, pygame.K_e), screen)
    elif stateMac.current_state.id == "beatup":
        world.moveMen(duck.rect.center, dt, screen)
        world.punchMen(duck.rect.center, event.checkInput(pygame.KEYDOWN, pygame.K_e), screen)

    if world.shroomCount >= 5 and stateMac.current_state.id == "pickup":
        stateMac.donePickup()
    if world.killCount >= 3 and stateMac.current_state.id == "beatup":
        stateMac.doneBeatup()

    world.drawAll(duck, screen, stateMac.current_state.id == "pickup")
    world.drawScore(stateMac.current_state.id == "pickup", screen)



