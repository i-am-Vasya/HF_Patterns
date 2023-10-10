from abc import ABC, abstractmethod


class Command(ABC):

    @abstractmethod
    def execute(self) -> None:
        pass


class Light:

    def on(self) -> None:
        print('Light is on')

    def off(self) -> None:
        print('Light is off')


class GarageDoor:

    def up(self) -> None:
        print('Garage door moving up')

    def down(self) -> None:
        print('Garage door ,oving down')

    def stop(self) -> None:
        print('Garage door stopped')

    def lights_on(self) -> None:
        print('Garage lights is on')

    def lights_off(self) -> None:
        print('Garage lights is off')


class LightOnCommand(Command):

    def __init__(self, light: Light):
        self.light = light

    def execute(self) -> None:
        self.light.on()


class GarageDoorOpenCommand(Command):

    def __init__(self, garage_door: GarageDoor):
        self.garage_door = garage_door

    def execute(self) -> None:
        self.garage_door.up()


class SimpleRemoteControl:
    slot: Command

    def set_command(self, command: Command):
        self.slot = command

    def button_was_pressed(self):
        self.slot.execute()


class RemoteControlTest:

    def __init__(self):
        self.remote: SimpleRemoteControl = SimpleRemoteControl()
        self.light: Light = Light()
        self.garage_door: GarageDoor = GarageDoor()
        self.light_on_command: LightOnCommand = LightOnCommand(self.light)
        self.garage_door_open_command: GarageDoorOpenCommand = GarageDoorOpenCommand(self.garage_door)


if __name__ == '__main__':
    test = RemoteControlTest()
    test.remote.set_command(test.light_on_command)
    test.remote.button_was_pressed()
    test.remote.set_command(test.garage_door_open_command)
    test.remote.button_was_pressed()