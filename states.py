import sys
from statemachine import StateMachine, State

class duckState(StateMachine):
    pickup = State("pickup", initial=True)
    beatup = State("beatup")
    win = State("win")

    start = pickup.to(pickup)
    donePickup = pickup.to(beatup)
    doneBeatup = beatup.to(win)

    @donePickup.before
    def killShrooms(self):
        print("din mor")

    @doneBeatup.after
    def exit(self):
        print("din far")
        sys.exit()
