from state import State, NoQuarterState, HasQuarterState, SoldState, SoldOutState


class GumBallMachine:
    count = 0

    def __init__(self, balls: int):
        self.no_quarter_state: 'State' = NoQuarterState(self)
        self.has_quarter_state: State = HasQuarterState(self)
        self.sold_state: State = SoldState(self)
        self.sold_out_state: State = SoldOutState(self)
        self.count: int = balls
        if self.count > 0:
            self.state: State = self.no_quarter_state
        else:
            self.state: State = self.sold_out_state


    def insert_quarter(self):
        self.state.insert_quarter()

    def eject_quarter(self):
        self.state.eject_quarter()

    def turn_crunk(self):
        self.state.turn_crank()

    def set_state(self, state):
        self.state = state

    def release_ball(self):
        print("A gumball comes rolling out the slot...")
        if self.count > 0:
            self.count -= 1

    def get_count(self):
        return self.count

    def get_has_quarter_state(self):
        return self.has_quarter_state

    def get_no_quarter_state(self):
        return self.no_quarter_state

    def get_sold_state(self):
        return self.sold_state

    def get_sold_out_state(self):
        return self.sold_out_state
