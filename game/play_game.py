from math import ceil
from game.hero import Hero

from game.player import Player
from game.towns import Castle, Rampart, Tower, Inferno, Necropolis, Dungeon, Stronghold, Fortress, Conflux
from random import randint, choice
from game.magic_book import magics

line = '-' * 35
castles = [Castle(), Rampart(), Tower(), Inferno(), Necropolis(), Dungeon(), Stronghold(), Fortress(), Conflux()]


def player_choice(hero_name: str):
    while True:
        try:
            person = int(input(f'{hero_name} choose a number between 1 and {len(castles)}: '))
            if 1 <= person <= len(castles):
                return person - 1
            else:
                print('Please enter a valid number!')
        except ValueError:
            print('Invalid values, try again!')


def attacker_do_magic(user: Player):
    while True:
        try:
            magic_number = int(input(f'{user.name} to do a magic choose a number between 1 and {len(magics)}: '))

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


def calculate_defence(player: Player):
    return player.stats[1] * player.stats[4]


def calculate_dead_creatures(dmg: float, defn: float, health: int) -> int:
    if defn > dmg:
        return 1

    return ceil((dmg - defn) / health)


# Here I generate a random number

player_index = randint(0, len(Hero.heroes) - 1)
computer_index = randint(0, len(Hero.heroes) - 1)

# Here I use the random generated number to pick a hero from the Hero class.
# Every user starts with a random hero because of their special abilities
# that can be advantage or disadvantage in the battle.
player_hero = Hero(player_index).get_hero()
computer_hero = Hero(computer_index).get_hero()

# Here I force the user to choose a number then I use that number to pick a town and army for him.
current_player_choice = player_choice(player_hero)
player_town = castles[current_player_choice].get_name()
player_army = [a.get_army() for a in castles if player_town == a.name][0]

second_player_choice = player_choice(computer_hero)
computer_town = castles[second_player_choice].get_name()
computer_army = [a.get_army() for a in castles if computer_town == a.name][0]

human = Player(player_hero, player_town, player_army)
computer = Player(computer_hero, computer_town, computer_army)

print()
print(f'{human.name} with {human.town} vs {computer.name} with {computer.town}.')

iteration = 0

while True:
    # Here on every iteration I take different warrior for the users.
    # Every warrior has own parameters and I use them in the battle.
    human.warrior, human.stats = choice(list(human.army.items()))
    computer.warrior, computer.stats = choice(list(computer.army.items()))

    # Every hero has special ability(check file hero for more clarification).
    # The hero can use his ability only on the first iteration and this is what I check here.
    if iteration == 0:
        for i in range(len(human.stats)):
            human.stats[i] = Hero.heroes[human.name](human.stats[i])
            if human.stats[i] < 1:
                human.stats[i] = 1

        for i in range(len(computer.stats)):
            computer.stats[i] = Hero.heroes[computer.name](computer.stats[i])
            if computer.stats[i] < 1:
                computer.stats[i] = 1

    print(line)
    print()
    print(f'Round {iteration + 1}. {human.name} plays with {human.warrior}:')
    print(repr(human))
    print(line)
    print(f'Round {iteration + 1}. {computer.name} plays with {computer.warrior}:')
    print(repr(computer))

    # damage = attack of the creature + damage to the enemy * creature quantity
    damage = calculate_damage(human) if iteration % 2 == 0 else calculate_damage(computer)

    # defence = defence of the creature * creature quantity
    defence = calculate_defence(computer) if iteration % 2 == 0 else calculate_defence(human)

    # dead_creatures = ceil((damage - defence) / health of the defensive creature)
    dead_creatures = calculate_dead_creatures(damage, defence, computer.stats[3]) if iteration % 2 == 0 else (
        calculate_dead_creatures(damage, defence, human.stats[3]))

    if iteration % 2 == 0:
        if human.mana >= 10:
            attacker_do_magic(human)
            human.mana -= 10

        if dead_creatures > computer.stats[4]:
            dead_creatures = computer.stats[4]

        computer.stats[4] -= dead_creatures

        # if the quantity of the current warrior is 0 I remove the warrior from the battle.
        if computer.stats[4] == 0:
            del computer.army[computer.warrior]

        print(line)
        print(f'{human.name} killed {dead_creatures} {computer.warrior}.')
        # If all computer's warriors are dead the battle finish and the user is winner.
        if len(computer.army) == 0:
            print(line)
            print(human)
            break
    else:
        if computer.mana >= 10:
            attacker_do_magic(computer)
            computer.mana -= 10

        if dead_creatures > human.stats[4]:
            dead_creatures = human.stats[4]

        human.stats[4] -= dead_creatures

        # if the quantity of the current warrior is 0 I remove the warrior from the battle.
        if human.stats[4] == 0:
            del human.army[human.warrior]

        print(line)
        print(f'{computer.name} killed {dead_creatures} {human.warrior}.')
        # If all user's warriors are dead the battle finish and the computer is winner.
        if len(human.army) == 0:
            print(line)
            print(computer)
            break

    human.mana += randint(1, 7)
    computer.mana += randint(1, 7)
    iteration += 1
