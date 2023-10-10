import state
from gum_ball_machine import GumBallMachine

test_machine = GumBallMachine(5)

if __name__ == "__main__":
    print(test_machine)
    test_machine.insert_quarter()