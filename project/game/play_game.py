from math import ceil
from project.game.hero import Hero
from project.game.magic_book import Prayer, Bless, Shield, Haste, Resurrection
from project.game.player import Player
from project.game.towns import Castle, Rampart, Tower, Inferno, Necropolis, Dungeon, Stronghold, Fortress, Conflux
from random import randint, choice

line = '-' * 35

castles = [Castle(), Rampart(), Tower(), Inferno(), Necropolis(), Dungeon(), Stronghold(), Fortress(), Conflux()]
magics = [Prayer, Bless, Shield, Haste, Resurrection]


def player_choice(hero_name: str):
    while True:
        try:
            index = int(input(f'{hero_name} choose a number between 1 and {len(castles)}: '))
            if 1 <= index <= len(castles):
                return index - 1
            else:
                print('Please enter a valid number!')
        except ValueError:
            print('Invalid values, try again!')


def attacker_do_magic(user: Player):
    while True:
        try:
            magic_number = int(input(f"{user.name} to perform magic. Choose a number between 1 and {len(magics)}: "))

            if 1 <= magic_number <= len(magics):
                magic_number -= 1
                print(magics[magic_number](user).do_magic())
                break
            else:
                print('Please enter a valid number!')
        except ValueError:
            print('Invalid values, try again...')


def calculate_damage(player: Player) -> int:
    return (player.stats[0] + player.stats[2]) * player.stats[4]


def calculate_defence(player: Player) -> int:
    return player.stats[1] * player.stats[4]


def calculate_dead_creatures(dmg: float, defn: float, health: int, current_quantity: int) -> int:
    dead_units = ceil((dmg - defn) / health)
    if dead_units <= 0:
        return 1

    elif dead_units >= current_quantity:
        return current_quantity

    return dead_units


def fight(first_player: Player, second_player: Player, dead_units: int):
    if first_player.mana >= 10:
        attacker_do_magic(first_player)
        first_player.mana -= 10

    second_player.stats[4] -= dead_units


def generate_index():
    index = randint(0, len(Hero.heroes) - 1)

    return index


def generate_hero():
    # Here I use random generated number to pick a hero from the Hero class.
    hero = Hero(generate_index()).get_hero()

    return hero


def generate_town(player):
    town = castles[player].get_name()

    return town


def generate_army(current_player_town):
    army = [a.get_army() for a in castles if current_player_town == a.name][0]

    return army


# Every user starts with a random hero because of their special abilities
# that can be advantage or disadvantage in the battle.
player_hero = generate_hero()
computer_hero = generate_hero()

# Here I force the user to choose a number then I use that number to pick a town and army for him.
current_player_choice = player_choice(player_hero)
player_town = generate_town(current_player_choice)
player_army = generate_army(player_town)

second_player_choice = player_choice(computer_hero)
computer_town = generate_town(second_player_choice)
computer_army = generate_army(computer_town)

human = Player(player_hero, player_town, player_army)
computer = Player(computer_hero, computer_town, computer_army)

print()
print(f'{human.name} with {human.town} vs {computer.name} with {computer.town}.')

iteration = 0

while True:
    attacker = human if iteration % 2 == 0 else computer
    defender = human if iteration % 2 != 0 else computer

    # Here on every iteration I take different warrior for the users.
    # Every warrior has own parameters and I use them in the battle.
    attacker.warrior, attacker.stats = choice(list(attacker.army.items()))
    defender.warrior, defender.stats = choice(list(defender.army.items()))

    # Every hero has special ability(check file hero for more clarification).
    # The hero can use his ability only on the first iteration and this is what I check here.
    if iteration == 0:
        # len(attacker.stats) and len(defender.stats) are always equal so there is no matter what stats we will iterate
        for i in range(len(attacker.stats)):
            attacker.stats[i] = Hero.heroes[attacker.name](attacker.stats[i])
            attacker.stats[i] = max(1, attacker.stats[i])

            defender.stats[i] = Hero.heroes[defender.name](defender.stats[i])
            defender.stats[i] = max(1, defender.stats[i])

    print(line)
    print()
    print(f'Round {iteration + 1}. {attacker.name} plays with {attacker.warrior}:')
    print(repr(attacker))
    print(line)
    print(f'Round {iteration + 1}. {defender.name} plays with {defender.warrior}:')
    print(repr(defender))

    # damage = attack of the creature + damage to the enemy * creature quantity
    damage = calculate_damage(attacker)

    # defence = defence of the creature * creature quantity
    defence = calculate_defence(defender)

    # dead_creatures = ceil((damage - defence) / health of the defensive creature)
    dead_creatures = calculate_dead_creatures(damage, defence, defender.stats[3], defender.stats[4])

    fight(attacker, defender, dead_creatures)

    if defender.stats[4] == 0:
        del defender.army[defender.warrior]

    print(line)
    print(f'{attacker.name} killed {dead_creatures} {defender.warrior}.')

    if len(defender.army) == 0:
        print(line)
        print(attacker)
        break

    attacker.mana += randint(1, 7)
    defender.mana += randint(1, 7)
    iteration += 1
