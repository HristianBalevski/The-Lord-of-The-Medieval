from random import randint
from abc import ABC, abstractmethod
from project.game.player import Player


def increase_power():
    return randint(1, 10)


class MagicBook(ABC):
    @abstractmethod
    def do_magic(self):
        pass


class Prayer(MagicBook):
    def __init__(self, player: Player):
        self.player = player
        self.name = 'Prayer'
        self.increase = increase_power()

    def do_magic(self) -> str:
        self.player.stats[0] += self.increase
        return f'{self.player.name} did {self.name} and increase {self.player.warrior} attack with {self.increase}.'


class Bless(MagicBook):
    def __init__(self, player: Player):
        self.player = player
        self.name = 'Bless'
        self.increase = 3

    def do_magic(self) -> str:
        self.player.stats[2] += self.increase
        return f'{self.player.name} did {self.name} and increase {self.player.warrior} damage with {self.increase}.'


class Shield(MagicBook):
    def __init__(self, player: Player):
        self.player = player
        self.name = 'Shield'
        self.increase = 3

    def do_magic(self) -> str:
        self.player.stats[1] += self.increase
        return f'{self.player.name} did {self.name} and increase {self.player.warrior} defence with {self.increase}.'


class Resurrection(MagicBook):
    def __init__(self, player: Player):
        self.player = player
        self.name = 'Resurrection'
        self.increase = increase_power()

    def do_magic(self) -> str:
        self.player.stats[4] += self.increase
        return f'{self.player.name} did {self.name} and added {self.increase} {self.player.warrior} to his army.'


class Haste(MagicBook):
    def __init__(self, player: Player):
        self.player = player
        self.name = 'Haste'
        self.increase = increase_power()

    def do_magic(self) -> str:
        self.player.stats[3] += self.increase
        return f'{self.player.name} did {self.name} and increase {self.player.warrior} health with {self.increase}.'
