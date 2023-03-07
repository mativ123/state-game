from statemachine import StateMachine, State

class andValhalla(StateMachine):
    "duck trip"
    besked = ""
    svamp = State("svamp", initial=True)
    bank = State("bank")

    start = svamp.to(svamp)
    trip = svamp.to(bank)
    
    @start.on
    def on_svamp(self):
        print("din mor er grim")

    @trip.before
    def before_bank(self):
        self.besked = "din far er grim"

    @trip.on
    def on_bank(self):
        print(self.besked)

din = andValhalla()

din.start()
din.trip()

if din.current_state.id == "svamp":
    print("din mor")
elif din.current_state.id == "bank":
    print("din far")
