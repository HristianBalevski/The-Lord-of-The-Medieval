from random import randint
from unittest import TestCase, main

from project.game.hero import Hero
from project.game.player import Player
from project.game.towns import Stronghold


class TestPlayer(TestCase):
    def test_initialization(self):
        name = Hero(18).get_hero()
        town = Stronghold().get_name()
        army = Stronghold.get_army()
        self.player = Player(name, town, army)

        expected_army = {
            'HOBGOBLIN': [3, 3, randint(1, 2), 5, randint(800, 1600)],
            'WOLF RIDER': [8, 5, randint(6, 8), 10, randint(700, 1400)],
            'ORC CHIEFTAIN': [8, 4, randint(2, 5), 22, randint(600, 1200)],
            'OGRE MAGE': [14, 7, randint(6, 12), 60, randint(500, 1000)],
            'THUNDERBIRD': [14, 11, randint(11, 15), 60, randint(400, 800)],
            'CYCLOPS KING': [19, 13, randint(16, 20), 70, randint(300, 600)],
            'ANCIENT BEHEMOTH': [34, 19, randint(30, 50), 300, randint(200, 400)]
        }

        self.assertEqual(self.player.name, 'Kilgor')
        self.assertEqual(self.player.town, 'Stronghold')
        self.assertEqual(self.player.army.keys(), expected_army.keys())
        self.assertEqual(self.player.mana, 0)
        self.assertEqual(self.player.warrior, None)
        self.assertEqual(self.player.stats, None)

    def test_repr_returns_the_correct_message(self):
        name = Hero(18).get_hero()
        town = Stronghold().get_name()
        army = Stronghold.get_army()
        self.player = Player(name, town, army)
        self.player.warrior = 'HOBGOBLIN'
        self.player.stats = self.player.army['HOBGOBLIN']

        attack = 3
        defence = 3
        damage = self.player.stats[2]
        health = 5
        quantity = self.player.stats[4]

        expected_message = f'Attack: {attack}\n' + \
                           f'Defence: {defence}\n' + \
                           f'Damage: {damage}\n' + \
                           f'Health: {health}\n' + \
                           f'Quantity: {quantity}'

        self.assertEqual(expected_message, repr(self.player))

    def test_str_returns_correct_message(self):
        name = Hero(18).get_hero()
        town = Stronghold().get_name()
        army = Stronghold.get_army()
        self.player = Player(name, town, army)

        expected_message = f'The Battle Finish.\n' + \
                           f'The Winner is Kilgor with Stronghold!'

        self.assertEqual(str(self.player), expected_message)


if '__name__' == '__main__':
    main()
