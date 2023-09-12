class Hero:
    heroes = {
        'Christian': lambda x: (x + 1),
        'Xsi': lambda x: (x - 1),
        'Ryland': lambda x: (x + 2),
        'Tamika': lambda x: (x - 2),
        'Astral': lambda x: (x + 3),
        'Octavia': lambda x: (x - 3),
        'Solmyr': lambda x: (x + 4),
        'Marius': lambda x: (x - 4),
        'Shiva': lambda x: (x + 5),
        'Jeddite': lambda x: (x - 5),
        'Crag Hack': lambda x: (x + 6),
        'Isra': lambda x: (x - 6),
        'Sir Mulich': lambda x: (x + 7),
        'Sandro': lambda x: (x - 7),
        'Dracon': lambda x: (x + 8),
        'Mutare': lambda x: (x - 8),
        'Roland': lambda x: (x + 9),
        'Xeron': lambda x: (x - 9),
        'Kilgor': lambda x: (x + 10),
        'Mutare Drake': lambda x: (x - 10)
    }

    def __init__(self, index: int):
        self._index = index

    def get_hero(self) -> str:
        return list(Hero.heroes)[self._index]