class Player:
    def __init__(self, name: str, town: str, army: dict):
        self.name = name
        self.town = town
        self.mana = 0
        self.army = army
        self.warrior = None
        self.stats = None

    def __repr__(self):
        return f'Attack: {self.stats[0]}\n' + \
               f'Defence: {self.stats[1]}\n' + \
               f'Damage: {self.stats[2]}\n' + \
               f'Health: {self.stats[3]}\n' + \
               f'Quantity: {self.stats[4]}'

    def __str__(self):
        return f'The Battle Finish.\n' + \
               f'The Winner is {self.name} with {self.town}!'




