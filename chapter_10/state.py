from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gum_ball_machine import GumBallMachine


class State(ABC):

    @abstractmethod
    def insert_quarter(self):
        pass

    @abstractmethod
    def eject_quarter(self):
        pass

    @abstractmethod
    def turn_crank(self):
        pass

    @abstractmethod
    def dispense(self):
        pass


class NoQuarterState(State):

    def __init__(self, gum_ball_machine: "GumBallMachine"):
        self.gum_ball_machine = gum_ball_machine

    def insert_quarter(self):
        print("You inserted a quarter")
        self.gum_ball_machine.set_state(self.gum_ball_machine.get_has_quarter_state())

    def eject_quarter(self):
        print("You haven't inserted a quarter")

    def turn_crank(self):
        print("You turned, but there's no quarter")

    def dispense(self):
        print("You need to pay first")


class HasQuarterState(State):

    def __init__(self, gum_ball_machine):
        self.gum_ball_machine = gum_ball_machine

    def insert_quarter(self):
        print("You can't insert another quarter")

    def eject_quarter(self):
        print("Quarter returned")
        self.gum_ball_machine.set_state(self.gum_ball_machine.get_no_quarter_state())

    def turn_crank(self):
        print("You turned...")
        self.gum_ball_machine.set_state(self.gum_ball_machine.get_sold_state())

    def dispense(self):
        print("No gumball dispensed")


class SoldState(State):

    def __init__(self, gum_ball_machine):
        self.gum_ball_machine = gum_ball_machine

    def insert_quarter(self):
        print("Wait for ball")

    def eject_quarter(self):
        print("You already turned crank")

    def turn_crank(self):
        print("Even if you turn twice you got one ball")
        self.gum_ball_machine.set_state(self.gum_ball_machine.get_sold_state())

    def dispense(self):
        self.gum_ball_machine.release_ball()
        if self.gum_ball_machine.get_count() > 0:
            self.gum_ball_machine.set_state(self.gum_ball_machine.get_no_quarter_state())
        else:
            self.gum_ball_machine.set_state(self.gum_ball_machine.get_sold_out_state())


class SoldOutState(State):

    def __init__(self, gum_ball_machine):
        self.gum_ball_machine = gum_ball_machine

    def insert_quarter(self):
        print("You can't insert a quarter, the machine is sold out")

    def eject_quarter(self):
        print("You haven't inserted a quarter")

    def turn_crank(self):
        print("You turned, but there is no gumballs")

    def dispense(self):
        print("No gumball dispensed")
