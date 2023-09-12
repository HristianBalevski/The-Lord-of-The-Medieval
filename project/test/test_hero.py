from unittest import TestCase, main
from project.game.hero import Hero


class TestClassHero(TestCase):

    def test_initialization(self):
        self.hero = Hero(4)
        self._index = self.hero._index

        self.assertEqual(self._index, 4)

    def test_get_hero_returns_the_right_hero(self):
        self.hero = Hero(4)
        expected_hero = 'Astral'

        self.assertEqual(expected_hero, self.hero.get_hero())

        self.hero = Hero(18)
        expected_hero = 'Kilgor'

        self.assertEqual(expected_hero, self.hero.get_hero())


if '__name__' == '__main__':
    main()
