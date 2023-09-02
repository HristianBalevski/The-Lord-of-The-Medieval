from abc import ABC, abstractmethod
from random import randint


class Town(ABC):
    def __init__(self):
        self.name = ''

    @abstractmethod
    def get_name(self):
        pass

    @staticmethod
    @abstractmethod
    def get_army():
        pass


class Castle(Town):
    def __init__(self):
        super().__init__()
        self.name = 'Castle'

    def get_name(self):
        return self.name

    @staticmethod
    def get_army():
        return {
            'HALBERDIER': [6, 5, randint(2, 3), 10, randint(810, 1610)],
            'MARKSMAN': [6, 3, randint(4, 6), 10, randint(710, 1410)],
            'ROYAL GRIFFIN': [10, 9, randint(3, 6), 25, randint(610, 1210)],
            'CRUSADER': [12, 12, randint(14, 20), 35, randint(510, 1010)],
            'ZEALOT': [12, 10, randint(10, 12), 30, randint(410, 810)],
            'CHAMPION': [16, 16, randint(20, 25), 100, randint(310, 610)],
            'ARCHANGEL': [30, 30, 50, 250, randint(200, 400)]
        }


class Rampart(Town):
    def __init__(self):
        super().__init__()
        self.name = 'Rampart'

    def get_name(self):
        return self.name

    @staticmethod
    def get_army():
        return {
            'CENTAUR CAPTAIN': [6, 3, randint(2, 3), 10, randint(800, 1600)],
            'BATTLE DWARF': [7, 7, randint(2, 4), 20, randint(700, 1400)],
            'GRAND ELF': [9, 5, randint(6, 10), 15, randint(600, 1200)],
            'SILVER PEGASUS': [9, 10, randint(5, 9), 30, randint(500, 1000)],
            'DENDROID SOLDIER': [9, 12, randint(10, 14), 65, randint(400, 800)],
            'WAR UNICORN': [15, 14, randint(18, 22), 110, randint(300, 600)],
            'GOLD DRAGON': [27, 30, randint(40, 50), 250, randint(200, 400)]
        }


class Tower(Town):
    def __init__(self):
        super().__init__()
        self.name = 'Tower'

    def get_name(self):
        return self.name

    @staticmethod
    def get_army():
        return {
            'MASTER GREMLIN': [4, 4, randint(1, 2), 4, randint(800, 1600)],
            'OBSIDIAN GARGOYLE': [7, 7, randint(2, 3), 16, randint(700, 1400)],
            'IRON GOLEM': [9, 10, randint(4, 5), 35, randint(600, 1200)],
            'ARCH MAGE': [12, 9, randint(7, 9), 30, randint(500, 1000)],
            'MASTER GENIE': [12, 12, randint(13, 16), 40, randint(400, 800)],
            'NAGA QUEEN': [16, 13, 30, 120, randint(300, 600)],
            'TITAN': [24, 24, randint(40, 60), 310, randint(200, 400)]
        }


class Inferno(Town):
    def __init__(self):
        super().__init__()
        self.name = 'Inferno'

    def get_name(self):
        return self.name

    @staticmethod
    def get_army():
        return {
            'FAMILIAR': [4, 4, randint(1, 2), 4, randint(800, 1600)],
            'MAGOG': [7, 4, randint(2, 4), 13, randint(700, 1400)],
            'CERBERUS': [10, 8, randint(2, 7), 27, randint(600, 1200)],
            'HORNED DEMON': [10, 10, randint(7, 9), 40, randint(500, 1000)],
            'PIT LORD': [13, 13, randint(13, 17), 45, randint(400, 800)],
            'EFREET SULTAN': [16, 14, randint(16, 24), 90, randint(300, 600)],
            'ARCH DEVIL': [26, 28, randint(30, 40), 220, randint(200, 400)]
        }


class Necropolis(Town):
    def __init__(self):
        super().__init__()
        self.name = 'Necropolis'

    def get_name(self):
        return self.name

    @staticmethod
    def get_army():
        return {
            'SKELETON WARRIOR': [6, 6, randint(1, 3), 6, randint(800, 1600)],
            'ZOMBIE': [5, 5, randint(2, 3), 20, randint(700, 1400)],
            'WRAITH': [7, 7, randint(3, 5), 19, randint(600, 1200)],
            'VAMPIRE LORD': [10, 12, randint(5, 8), 45, randint(500, 1000)],
            'POWER LICH': [13, 10, randint(13, 17), 40, randint(400, 800)],
            'DREAD KNIGHT': [18, 18, randint(20, 35), 120, randint(300, 600)],
            'GHOST DRAGON': [19, 17, randint(35, 50), 200, randint(200, 400)]
        }


class Dungeon(Town):
    def __init__(self):
        super().__init__()
        self.name = 'Dungeon'

    def get_name(self):
        return self.name

    @staticmethod
    def get_army():
        return {
            'INFERNAL TROGLODYTE': [5, 5, randint(1, 3), 6, randint(800, 1600)],
            'HARPY HAG': [6, 6, randint(1, 4), 20, randint(700, 1400)],
            'EVIL EYE': [10, 8, randint(3, 5), 22, randint(600, 1200)],
            'MEDUSA QUEEN': [10, 10, randint(7, 9), 30, randint(500, 1000)],
            'MINOTAUR KING': [16, 15, randint(12, 20), 50, randint(400, 800)],
            'SCORPICORE': [17, 15, randint(15, 20), 80, randint(300, 600)],
            'BLACK DRAGON': [25, 30, randint(40, 50), 300, randint(200, 400)]
        }


class Stronghold(Town):
    def __init__(self):
        super().__init__()
        self.name = 'Stronghold'

    def get_name(self):
        return self.name

    @staticmethod
    def get_army():
        return {
            'HOBGOBLIN': [3, 3, randint(1, 2), 5, randint(800, 1600)],
            'WOLF RIDER': [8, 5, randint(6, 8), 10, randint(700, 1400)],
            'ORC CHIEFTAIN': [8, 4, randint(2, 5), 22, randint(600, 1200)],
            'OGRE MAGE': [14, 7, randint(6, 12), 60, randint(500, 1000)],
            'THUNDERBIRD': [14, 11, randint(11, 15), 60, randint(400, 800)],
            'CYCLOPS KING': [19, 13, randint(16, 20), 70, randint(300, 600)],
            'ANCIENT BEHEMOTH': [34, 19, randint(30, 50), 300, randint(200, 400)]
        }


class Fortress(Town):
    def __init__(self):
        super().__init__()
        self.name = 'Fortress'

    def get_name(self):
        return self.name

    @staticmethod
    def get_army():
        return {
            'GNOLL MARAUDER': [4, 6, randint(2, 3), 6, randint(800, 1600)],
            'LIZARD WARRIOR': [6, 8, randint(2, 5), 17, randint(700, 1400)],
            'DRAGON FLY': [10, 10, randint(2, 5), 20, randint(600, 1200)],
            'GREATER BASILISK': [12, 12, randint(7, 10), 40, randint(500, 1000)],
            'MYGHTY GORGON': [13, 16, randint(15, 18), 70, randint(400, 800)],
            'WYVERN MONARCH': [14, 14, randint(20, 22), 70, randint(300, 600)],
            'CHAOS HYDRA': [18, 25, randint(35, 45), 250, randint(200, 400)]
        }


class Conflux(Town):
    def __init__(self) -> None:
        super().__init__()
        self.name = 'Conflux'

    def get_name(self) -> str:
        return self.name

    @staticmethod
    def get_army() -> dict:
        return {
            'SPRITE': [2, 3, randint(1, 3), 6, randint(800, 1600)],
            'STORM ELEMENTAL': [9, 10, randint(2, 8), 26, randint(700, 1400)],
            'ICE ELEMENTAL': [8, 10, randint(3, 7), 35, randint(600, 1200)],
            'ENERGY ELEMENTAL': [12, 8, randint(4, 6), 40, randint(500, 1000)],
            'MAGMA ELEMENTAL': [11, 11, randint(6, 10), 50, randint(400, 800)],
            'MAGIC ELEMENTAL': [17, 13, randint(20, 25), 100, randint(300, 600)],
            'PHOENIX': [25, 18, randint(30, 40), 250, randint(200, 400)]
        }