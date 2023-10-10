from abc import ABC, abstractmethod


class Duck(ABC):

    _flyBehavior = None
    _quackBehavior = None

    def display(self):
        pass

    def performFly(self):
        self._flyBehavior.fly()

    def peformQuack(self):
        self._quackBehavior.quack()

    @staticmethod
    def swim():
        print("All ducks float, even decoys!")

    def setFlyBehavior(self, fb):
        self._flyBehavior = fb

    def setQuackBehavior(self, qb):
        self._quackBehavior = qb


class FlyBehavior(ABC):
    """This is FlyInterface"""

    @abstractmethod
    def fly(self):
        pass


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I'm flying")


class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I can't fly")


class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print("I'm flying with a rocket!")


class QuackBehavior(ABC):
    """This is QuackInterface"""

    @abstractmethod
    def quack(self):
        pass


class Quack(QuackBehavior):
    def quack(self):
        print("Quack")


class MuteQuack(QuackBehavior):
    def quack(self):
        print("<< Silence >>")


class Squeak(QuackBehavior):
    def quack(self):
        print("Squeak")


class MalardDuck(Duck):
    _quackBehavior = Quack()
    _flyBehavior = FlyWithWings()

    def display(self):
        print("I'm a real Mallard Duck")


class ModelDuck(Duck):
    _quackBehavior = Quack()
    _flyBehavior = FlyNoWay()

    def display(self):
        print("I'm a model duck")


class Manok:
    def __init__(self):
        self.pattern = Quack()

    def make_sound(self):
        print(f"Sounds like")
        self.pattern.quack()


mallard = MalardDuck()
mallard.peformQuack()
mallard.performFly()

model = ModelDuck()
model2 = ModelDuck()
model.performFly()
model.setFlyBehavior(FlyRocketPowered())
model.performFly()
mallard.performFly()

model2.performFly()

new_toy = Manok()
new_toy.make_sound()
#
# some_duck = Duck()
# some_duck.peformQuack()
