from random import randint
from unittest import TestCase, main
from project.game.hero import Hero
from project.game.magic_book import Prayer, increase_power, Bless, Shield, Resurrection, Haste
from project.game.player import Player
from project.game.towns import Stronghold


class TestMagicBook(TestCase):
    def test_class_prayer_initialization(self):
        name = Hero(18).get_hero()
        town = Stronghold().get_name()
        army = Stronghold.get_army()
        self.player = Player(name, town, army)

        self.prayer = Prayer(self.player)

        self.assertEqual('Prayer', self.prayer.name)
        self.assertEqual(self.prayer.player, self.player)

    def test_class_prayer_do_magic(self):
        name = Hero(18).get_hero()
        town = Stronghold().get_name()
        army = Stronghold.get_army()
        self.player = Player(name, town, army)
        self.player.warrior = 'ANCIENT BEHEMOTH'
        self.player.stats = [34, 19, randint(30, 50), 300, randint(200, 400)]

        self.prayer = Prayer(self.player)
        self.prayer.increase = increase_power()
        expected_result = 34 + self.prayer.increase
        self.player.stats[0] += self.prayer.increase
        expected_message = f'Kilgor did Prayer and increase ANCIENT BEHEMOTH attack with {self.prayer.increase}.'

        self.assertEqual(self.player.stats[0], expected_result)
        self.assertEqual(self.prayer.do_magic(), expected_message)

    def test_class_bless_initialization(self):
        name = Hero(18).get_hero()
        town = Stronghold().get_name()
        army = Stronghold.get_army()
        self.player = Player(name, town, army)

        self.bless = Bless(self.player)

        self.assertEqual(self.bless.player, self.player)
        self.assertEqual('Bless', self.bless.name)

    def test_class_bless_do_magic(self):
        name = Hero(18).get_hero()
        town = Stronghold().get_name()
        army = Stronghold.get_army()
        self.player = Player(name, town, army)
        self.player.warrior = 'ANCIENT BEHEMOTH'
        self.player.stats = [34, 19, randint(30, 50), 300, randint(200, 400)]

        self.bless = Bless(self.player)
        self.bless.increase = 3
        damage = self.player.stats[2]
        do_magic = self.bless.do_magic()

        result = self.player.stats[2] - damage
        expected_message = f'Kilgor did Bless and increase ANCIENT BEHEMOTH damage with 3.'

        self.assertEqual(3, result)
        self.assertEqual(do_magic, expected_message)

    def test_class_shield_initialization(self):
        name = Hero(18).get_hero()
        town = Stronghold().get_name()
        army = Stronghold.get_army()
        self.player = Player(name, town, army)

        self.shield = Shield(self.player)

        self.assertEqual(self.shield.player, self.player)
        self.assertEqual('Shield', self.shield.name)

    def test_class_shield_do_magic(self):
        name = Hero(18).get_hero()
        town = Stronghold().get_name()
        army = Stronghold.get_army()
        self.player = Player(name, town, army)
        self.player.warrior = 'ANCIENT BEHEMOTH'
        self.player.stats = [34, 19, randint(30, 50), 300, randint(200, 400)]

        self.shield = Shield(self.player)
        do_magic = self.shield.do_magic()

        expected_message = f'Kilgor did Shield and increase ANCIENT BEHEMOTH defence with 3.'

        self.assertEqual(self.player.stats[1], 22)
        self.assertEqual(do_magic, expected_message)

    def test_class_resurrection_initialization(self):
        name = Hero(18).get_hero()
        town = Stronghold().get_name()
        army = Stronghold.get_army()
        self.player = Player(name, town, army)

        self.resurrection = Resurrection(self.player)

        self.assertEqual('Resurrection', self.resurrection.name)
        self.assertEqual(self.resurrection.player, self.player)

    def test_class_resurrection_do_magic(self):
        name = Hero(18).get_hero()
        town = Stronghold().get_name()
        army = Stronghold.get_army()
        self.player = Player(name, town, army)
        self.player.warrior = 'ANCIENT BEHEMOTH'
        self.player.stats = [34, 19, randint(30, 50), 300, randint(200, 400)]

        self.resurrection = Resurrection(self.player)
        self.resurrection.increase = increase_power()
        previous_quantity = self.player.stats[4]
        self.player.stats[4] += self.resurrection.increase
        expected_result = self.player.stats[4] - previous_quantity
        expected_message = f'Kilgor did Resurrection and added {self.resurrection.increase} ANCIENT BEHEMOTH to his army.'

        self.assertEqual(expected_result, self.resurrection.increase)
        self.assertEqual(self.resurrection.do_magic(), expected_message)

    def test_class_haste_initialization(self):
        name = Hero(18).get_hero()
        town = Stronghold().get_name()
        army = Stronghold.get_army()
        self.player = Player(name, town, army)

        self.haste = Haste(self.player)

        self.assertEqual(self.haste.player, self.player)
        self.assertEqual('Haste', self.haste.name)

    def test_class_haste_do_magic(self):
        name = Hero(18).get_hero()
        town = Stronghold().get_name()
        army = Stronghold.get_army()
        self.player = Player(name, town, army)
        self.player.warrior = 'ANCIENT BEHEMOTH'
        self.player.stats = [34, 19, randint(30, 50), 300, randint(200, 400)]

        self.haste = Haste(self.player)
        self.haste.increase = increase_power()
        previous_health = self.player.stats[3]
        do_magic = self.haste.do_magic()
        current_health = self.player.stats[3]

        result = current_health - previous_health
        expected_message = f'Kilgor did Haste and increase ANCIENT BEHEMOTH health with {self.haste.increase}.'

        self.assertEqual(self.haste.increase, result)
        self.assertEqual(do_magic, expected_message)


if '__name__' == '__main__':
    main()
