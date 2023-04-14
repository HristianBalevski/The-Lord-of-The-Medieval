from random import randint, choice
from math import floor

line = '-' * 35
# List with all towns that you can choose from.
towns = ['Castle', 'Rampart', 'Tower', 'Inferno', 'Necropolis', 'Dungeon', 'Stronghold', 'Fortress', 'Conflux']
# List with all heroes that you can choose from.
get_hero = ['Christian', 'Xsi', 'Ryland', 'Tamika', 'Astral', 'Octavia', 'Solmyr', 'Marius', 'Shiva', 'Jeddite',
            'Crag Hack', 'Isra', 'Sir Mulich', 'Sandro', 'Dracon', 'Mutare', 'Roland', 'Xeron', 'Kilgor', 'Mutare Drake']


# Castle generate more army than the others because their special creature ARCHANGEL
# has the ability to resurrect army during the battle.
castle = {
    'HALBERDIER': [6, 5, randint(2, 3), 10, randint(810, 1610)],
    'MARKSMAN': [6, 3, randint(4, 6), 10, randint(710, 1410)],
    'ROYAL GRIFFIN': [10, 9, randint(3, 6), 25, randint(610, 1210)],
    'CRUSADER': [12, 12, randint(14, 20), 35, randint(510, 1010)],
    'ZEALOT': [12, 10, randint(10, 12), 30, randint(410, 810)],
    'CHAMPION': [16, 16, randint(20, 25), 100, randint(310, 610)],
    'ARCHANGEL': [30, 30, 50, 250, randint(200, 400)]
}

rampart = {
    'CENTAUR CAPTAIN': [6, 3, randint(2, 3), 10, randint(800, 1600)],
    'BATTLE DWARF': [7, 7, randint(2, 4), 20, randint(700, 1400)],
    'GRAND ELF': [9, 5, randint(6, 10), 15, randint(600, 1200)],
    'SILVER PEGASUS': [9, 10, randint(5, 9), 30, randint(500, 1000)],
    'DENDROID SOLDIER': [9, 12, randint(10, 14), 65, randint(400, 800)],
    'WAR UNICORN': [15, 14, randint(18, 22), 110, randint(300, 600)],
    'GOLD DRAGON': [27, 30, randint(40, 50), 250, randint(200, 400)]
}

tower = {
    'MASTER GREMLIN': [4, 4, randint(1, 2), 4, randint(800, 1600)],
    'OBSIDIAN GARGOYLE': [7, 7, randint(2, 3), 16, randint(700, 1400)],
    'IRON GOLEM': [9, 10, randint(4, 5), 35, randint(600, 1200)],
    'ARCH MAGE': [12, 9, randint(7, 9), 30, randint(500, 1000)],
    'MASTER GENIE': [12, 12, randint(13, 16), 40, randint(400, 800)],
    'NAGA QUEEN': [16, 13, 30, 120, randint(300, 600)],
    'TITAN': [24, 24, randint(40, 60), 310, randint(200, 400)]
}

inferno = {
    'FAMILIAR': [4, 4, randint(1, 2), 4, randint(800, 1600)],
    'MAGOG': [7, 4, randint(2, 4), 13, randint(700, 1400)],
    'CERBERUS': [10, 8, randint(2, 7), 27, randint(600, 1200)],
    'HORNED DEMON': [10, 10, randint(7, 9), 40, randint(500, 1000)],
    'PIT LORD': [13, 13, randint(13, 17), 45, randint(400, 800)],
    'EFREET SULTAN': [16, 14, randint(16, 24), 90, randint(300, 600)],
    'ARCH DEVIL': [26, 28, randint(30, 40), 220, randint(200, 400)]
}

necropolis = {
    'SKELETON WARRIOR': [6, 6, randint(1, 3), 6, randint(800, 1600)],
    'ZOMBIE': [5, 5, randint(2, 3), 20, randint(700, 1400)],
    'WRAITH': [7, 7, randint(3, 5), 19, randint(600, 1200)],
    'VAMPIRE LORD': [10, 12, randint(5, 8), 45, randint(500, 1000)],
    'POWER LICH': [13, 10, randint(13, 17), 40, randint(400, 800)],
    'DREAD KNIGHT': [18, 18, randint(20, 35), 120, randint(300, 600)],
    'GHOST DRAGON': [19, 17, randint(35, 50), 200, randint(200, 400)]
}

dungeon = {
    'INFERNAL TROGLODYTE': [5, 5, randint(1, 3), 6, randint(800, 1600)],
    'HARPY HAG': [6, 6, randint(1, 4), 20, randint(700, 1400)],
    'EVIL EYE': [10, 8, randint(3, 5), 22, randint(600, 1200)],
    'MEDUSA QUEEN': [10, 10, randint(7, 9), 30, randint(500, 1000)],
    'MINOTAUR KING': [16, 15, randint(12, 20), 50, randint(400, 800)],
    'SCORPICORE': [17, 15, randint(15, 20), 80, randint(300, 600)],
    'BLACK DRAGON': [25, 30, randint(40, 50), 300, randint(200, 400)]
}

stronghold = {
    'HOBGOBLIN': [3, 3, randint(1, 2), 5, randint(800, 1600)],
    'WOLF RIDER': [8, 5, randint(6, 8), 10, randint(700, 1400)],
    'ORC CHIEFTAIN': [8, 4, randint(2, 5), 22, randint(600, 1200)],
    'OGRE MAGE': [14, 7, randint(6, 12), 60, randint(500, 1000)],
    'THUNDERBIRD': [14, 11, randint(11, 15), 60, randint(400, 800)],
    'CYCLOPS KING': [19, 13, randint(16, 20), 70, randint(300, 600)],
    'ANCIENT BEHEMOTH': [34, 19, randint(30, 50), 300, randint(200, 400)]
}

fortress = {
    'GNOLL MARAUDER': [4, 6, randint(2, 3), 6, randint(800, 1600)],
    'LIZARD WARRIOR': [6, 8, randint(2, 5), 17, randint(700, 1400)],
    'DRAGON FLY': [10, 10, randint(2, 5), 20, randint(600, 1200)],
    'GREATER BASILISK': [12, 12, randint(7, 10), 40, randint(500, 1000)],
    'MYGHTY GORGON': [13, 16, randint(15, 18), 70, randint(400, 800)],
    'WYVERN MONARCH': [14, 14, randint(20, 22), 70, randint(300, 600)],
    'CHAOS HYDRA': [18, 25, randint(35, 45), 250, randint(200, 400)]
}

conflux = {
    'SPRITE': [2, 3, randint(1, 3), 6, randint(800, 1600)],
    'STORM ELEMENTAL': [9, 10, randint(2, 8), 26, randint(700, 1400)],
    'ICE ELEMENTAL': [8, 10, randint(3, 7), 35, randint(600, 1200)],
    'ENERGY ELEMENTAL': [12, 8, randint(4, 6), 40, randint(500, 1000)],
    'MAGMA ELEMENTAL': [11, 11, randint(6, 10), 50, randint(400, 800)],
    'MAGIC ELEMENTAL': [17, 13, randint(20, 25), 100, randint(300, 600)],
    'PHOENIX': [25, 18, randint(30, 40), 250, randint(200, 400)]
}

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

magic_book = {
    'Bloodlust': lambda a: (a + 5),
    'Bless': lambda a: (a + 5),
    'Curse': lambda a: (a - 5),
    'Shield': lambda a: (a + 5),
    'Resurrection': lambda a: (a + randint(1, magic_number * 10)),
    'Magic Arrow': lambda a: (a - randint(1, 30)),
    'Dispel': lambda a: (a * 0),
    'Haste': lambda a: (a + 5),
    'Chain Lightning': lambda a: (a - 2),
    'Prayer': lambda a: (a + 2)
}


def print_info(town, fighter):
    town_dictionary = ''

    if town == 'Castle':
        town_dictionary = castle
    elif town == 'Stronghold':
        town_dictionary = stronghold
    elif town == 'Rampart':
        town_dictionary = rampart
    elif town == 'Tower':
        town_dictionary = tower
    elif town == 'Inferno':
        town_dictionary = inferno
    elif town == 'Necropolis':
        town_dictionary = necropolis
    elif town == 'Dungeon':
        town_dictionary = dungeon
    elif town == 'Fortress':
        town_dictionary = fortress
    elif town == 'Conflux':
        town_dictionary = conflux

    info = []
    for soldier, value in town_dictionary.items():
        if soldier == fighter:
            info.append(f'Attack: {value[0]}')
            info.append(f'Defence: {value[1]}')
            info.append(f'Damage: {value[2]}')
            info.append(f'Health: {value[3]}')
            info.append(f'Quantity: {value[4]}')
    return '\n'.join(info)


def get_army(town):
    current_army = ''

    if town == 'Castle':
        current_army = castle
    elif town == 'Stronghold':
        current_army = stronghold
    elif town == 'Rampart':
        current_army = rampart
    elif town == 'Tower':
        current_army = tower
    elif town == 'Inferno':
        current_army = inferno
    elif town == 'Necropolis':
        current_army = necropolis
    elif town == 'Dungeon':
        current_army = dungeon
    elif town == 'Fortress':
        current_army = fortress
    elif town == 'Conflux':
        current_army = conflux
    return current_army


def player_make_magic(magic_number, mana):

    if magic_number == 1:
        p_stats[0] = magic_book['Bloodlust'](p_stats[0])
        return f'{player} has {player_mana} mana and increase {player_warrior} attack with 5.'

    elif magic_number == 2:
        p_stats[2] = magic_book['Bless'](p_stats[2])
        return f'{player} has {player_mana} mana and increase {player_warrior} damage with 5.'

    elif magic_number == 3:
        c_stats[0] = magic_book['Curse'](c_stats[0])
        if c_stats[0] < 0:
            c_stats[0] = 0
        return f'{player} has {player_mana} mana and reduce {computer_warrior} attack with 5.'

    elif magic_number == 4:
        p_stats[1] = magic_book['Shield'](p_stats[1])
        return f'{player} has {player_mana} mana and increase {player_warrior} defence with 5.'

    elif magic_number == 5:
        old_army = p_stats[4]
        p_stats[4] = magic_book['Resurrection'](p_stats[4])
        add_army = p_stats[4] - old_army
        return f'{player} has {player_mana} mana and added {add_army} new {player_warrior} to his army.'

    elif magic_number == 6:
        old_army = c_stats[4]
        c_stats[4] = magic_book['Magic Arrow'](c_stats[4])
        if c_stats[4] < 0:
            c_stats[4] = 0
        dead_army = old_army - c_stats[4]
        return f'{player} has {player_mana} mana and kill {dead_army} {computer_warrior} with Magic Arrow.'

    elif magic_number == 7:
        mana = magic_book['Dispel'](mana)
        return f'{player} has {player_mana} mana and reduce {computer} mana to {mana}.'

    elif magic_number == 8:
        p_stats[3] = magic_book['Haste'](p_stats[3])
        return f'{player} has {player_mana} mana and increase {player_warrior} health with 5.'

    elif magic_number == 9:
        for j in range(len(c_stats)):
            c_stats[j] = magic_book['Chain Lightning'](c_stats[j])
            if c_stats[j] < 0:
                c_stats[j] = 0
        return f'{player} has {player_mana} mana and reduce all {computer_warrior} parameters with 2.'

    elif magic_number == 10:
        for j in range(len(p_stats)):
            p_stats[j] = magic_book['Prayer'](p_stats[j])
        return f'{player} has {player_mana} mana and increase all {player_warrior} parameters with 2.'


def computer_make_magic(magic_number, mana):
    if magic_number == 1:
        c_stats[0] = magic_book['Bloodlust'](c_stats[0])
        return f'{computer} has {computer_mana} mana and increase {computer_warrior} attack with 5.'

    elif magic_number == 2:
        c_stats[2] = magic_book['Bless'](c_stats[2])
        return f'{computer} has {computer_mana} mana and increase {computer_warrior} damage with 5.'

    elif magic_number == 3:
        p_stats[0] = magic_book['Curse'](p_stats[0])
        if p_stats[0] < 0:
            p_stats[0] = 0
        return f'{computer} has {computer_mana} mana and reduce {player_warrior} attack with 5.'

    elif magic_number == 4:
        c_stats[1] = magic_book['Shield'](c_stats[1])
        return f'{computer} has {computer_mana} mana and increase {computer_warrior} defence with 5.'

    elif magic_number == 5:
        old_army = c_stats[4]
        c_stats[4] = magic_book['Resurrection'](c_stats[4])
        add_army = c_stats[4] - old_army
        return f'{computer} has {computer_mana} mana and added {add_army} new {computer_warrior} to his army.'

    elif magic_number == 6:
        old_army = p_stats[4]
        p_stats[4] = magic_book['Magic Arrow'](p_stats[4])
        if p_stats[4] < 0:
            p_stats[4] = 0
        dead_army = old_army - p_stats[4]
        return f'{computer} has {computer_mana} mana and kill {dead_army} {player_warrior} with Magic Arrow.'

    elif magic_number == 7:
        mana = magic_book['Dispel'](mana)
        return f'{computer} has {computer_mana} mana and reduce {player} mana to {mana}.'

    elif magic_number == 8:
        c_stats[3] = magic_book['Haste'](c_stats[3])
        return f'{computer} has {computer_mana} mana and increase {computer_warrior} health with 5.'

    elif magic_number == 9:
        for j in range(len(p_stats)):
            p_stats[j] = magic_book['Chain Lightning'](p_stats[j])
            if p_stats[j] < 0:
                p_stats[j] = 0
        return f'{computer} has {computer_mana} mana and reduce all {player_warrior} parameters with 2.'

    elif magic_number == 10:
        for j in range(len(c_stats)):
            c_stats[j] = magic_book['Prayer'](c_stats[j])
        return f'{computer} has {computer_mana} mana and increase all {computer_warrior} parameters with 2.'


def player_choice(user):
    while True:
        try:
            person = int(input(f'{user} choose a number between 1 and {len(towns)}: '))
            if 1 <= person <= len(towns):
                return person - 1
            else:
                print('Please enter a valid number!')
        except ValueError:
            print('Invalid values, try again!')


player = get_hero[randint(0, len(get_hero) - 1)]
computer = get_hero[randint(0, len(get_hero) - 1)]
print()
current_player_choice = player_choice(player)

player_town = towns[current_player_choice]
player_army = get_army(towns[current_player_choice])

computer_town = towns[randint(0, len(towns) - 1)]
computer_army = get_army(computer_town)

print()
print(f'{player} with {towns[current_player_choice]} vs {computer} with {computer_town}.')

iteration = 0
player_mana = 0
computer_mana = 0

while True:

    player_warrior, p_stats = choice(list(player_army.items()))
    computer_warrior, c_stats = choice(list(computer_army.items()))

    attacker = p_stats if iteration % 2 == 0 else c_stats
    defender = p_stats if iteration % 2 != 0 else c_stats
    hero_in_attack = player if iteration % 2 == 0 else computer
    dead_name = computer_warrior if iteration % 2 == 0 else player_warrior

    if iteration == 0:
        for i in range(len(p_stats)):
            p_stats[i] = heroes[player](p_stats[i])
            if p_stats[i] < 0:
                p_stats[i] = 0

        for i in range(len(c_stats)):
            c_stats[i] = heroes[computer](c_stats[i])
            if c_stats[i] < 0:
                c_stats[i] = 0

    print(line)
    print(f'Round {iteration + 1}. {player} plays with {player_warrior}:')
    print(print_info(player_town, player_warrior))
    print()

    if player_mana >= 10 and p_stats == attacker:
        while True:
            try:
                magic_number = int(input(f'{player} to make a magic choose a number between 1 and {len(magic_book)}: '))

                if 1 <= magic_number <= len(magic_book):
                    print(player_make_magic(magic_number, computer_mana))
                    if magic_number == 7:
                        computer_mana = 0
                    player_mana -= 10
                    print(f'Available mana after the magic {player_mana}.')
                    break
                else:
                    print('Please enter a valid number!')
            except ValueError:
                print('Invalid values, try again...')

    print(line)
    print(f'Round {iteration + 1}. {computer} plays with {computer_warrior}:')
    print(print_info(computer_town, computer_warrior))
    print()

    if computer_mana >= 10 and c_stats == attacker:

        magic_number = randint(1, len(magic_book))
        print(computer_make_magic(magic_number, player_mana))
        if magic_number == 7:
            player_mana = 0
        computer_mana -= 10
        print(f'Available mana after the magic {computer_mana}.')

    # damage = attack of the creature + damage to the creature * creature quantity
    damage = (attacker[0] + attacker[2]) * attacker[4]
    # defence = defence of the creature * creature quantity + health of creature
    defence = (defender[1] * defender[4]) + defender[3]

    if damage < defence:
        dead_creatures = 1
    else:
        # Here I calculate how many creatures are dead by the formula (damage / health of creature).
        dead_creatures = floor(damage / defender[3])
        if dead_creatures < 1:
            dead_creatures = 1
        if dead_creatures > defender[4]:
            dead_creatures = defender[4]
        defender[4] -= dead_creatures

    # Here the player and the computer gain random amount of mana.
    player_mana += randint(1, 10)
    computer_mana += randint(1, 10)
    print(line)
    print(f'{hero_in_attack} killed {dead_creatures} {dead_name}.')

    if defender[4] == 0:

        if defender == p_stats:
            del player_army[player_warrior]
        else:
            del computer_army[computer_warrior]

        if len(player_army) == 0 or len(computer_army) == 0:
            print()
            print('The Battle Finish!')

            if len(player_army) > 0:
                print('Available army after the battle.')
                for warrior in player_army:
                    print()
                    print(warrior)
                    print(print_info(player_town, warrior))
                print()
                print(f'{towns[current_player_choice]} beat {computer_town}!')
                print(f"{player} Won!")
            else:
                print(f'{computer_town} beat {towns[current_player_choice]}!')
                print(f"{computer} Won!")
            break

    iteration += 1
