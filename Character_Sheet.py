import random


class Character:
    stats = None
    race = None
    character_class = None
    hit_dice = None
    line = '________________________________________'

    def __init__(self):
        print(self.line)
        name = input("Choose a name: ")
        print(self.line)
        self.name = name
        print("Hi", self.name)
        print(self.line)
        self.get_race()
        self.get_class()
        self.ability_score()
        self.race_stat_mod()
        self.print_stats()
        self.class_stat_mod()
        self.print_stats()

    @staticmethod
    def main_roll(mod, target):
        return random.randint(1, 20) + mod < target

    def ability_score(self):
        accept_stats = False
        while not accept_stats:
            print(self.line)
            print("Rolling Stats:")
            strength = random.randint(1, 6) * 3
            dexterity = random.randint(1, 6) * 3
            constitution = random.randint(1, 6) * 3
            intelligence = random.randint(1, 6) * 3
            wisdom = random.randint(1, 6) * 3
            charisma = random.randint(1, 6) * 3
            self.stats = {'str': strength, 'dex': dexterity, 'con': constitution,
                          'int': intelligence, 'wis': wisdom, 'cha': charisma}
            self.print_stats()
            print(self.line)
            if input('Do you accept this roll? Yes/No:') == 'Yes':
                return self.stats
            else:
                continue

    def race_stat_mod(self):
        if self.race == 'Dwarf':
            self.stats['con'] += 2
            self.stats['wis'] -= 2
        if self.race == 'Elf':
            self.stats['dex'] += 2
            self.stats['con'] -= 2
        if self.race == 'Gnome':
            self.stats['con'] += 2
            self.stats['str'] -= 2
        if self.race == 'Halfling':
            self.stats['dex'] += 2
            self.stats['str'] -= 2
        if self.race == 'Half-Orc':
            self.stats['str'] += 2
            self.stats['int'] -= 2
            self.stats['cha'] -= 2
            if self.stats['int'] < 3:
                self.stats['int'] = 3

    def class_stat_mod(self):
        if self.character_class == 'Barbarian':
            self.stats['str'] += 2
            self.stats['dex'] += 1
            self.stats['wis'] += 1
            self.stats['con'] += 1
        if self.character_class == 'Bard':
            self.stats['cha'] += 2
            self.stats['dex'] += 2
            self.stats['int'] += 1
        if self.character_class == 'Cleric':
            self.stats['wis'] += 3
            self.stats['con'] += 1
            self.stats['cha'] += 1
        if self.character_class == 'Druid':
            self.stats['wis'] += 4
            self.stats['dex'] += 1
        if self.character_class == 'Fighter':
            self.stats['str'] += 2
            self.stats['con'] += 2
            self.stats['dex'] += 1
        if self.character_class == 'Monk':
            self.stats['wis'] += 2
            self.stats['dex'] += 2
            self.stats['str'] += 1
        if self.character_class == 'Paladin':
            self.stats['cha'] += 2
            self.stats['str'] += 2
            self.stats['wis'] += 1
        if self.character_class == 'Ranger':
            self.stats['dex'] += 2
            self.stats['wis'] += 2
            self.stats['str'] += 1
        if self.character_class == 'Rogue':
            self.stats['dex'] += 2
            self.stats['int'] += 2
            self.stats['wis'] += 1
        if self.character_class == 'Sorcerer':
            self.stats['cha'] += 3
            self.stats['dex'] += 1
            self.stats['con'] += 1
        if self.character_class == 'Wizard':
            self.stats['int'] += 3
            self.stats['dex'] += 1
            self.stats['con'] += 1

    def print_stats(self):
        print(self.line)
        for k, v in self.stats.items():
            print(k, ':', v)

    def get_race(self):
        races = ['Human', 'Dwarf', 'Elf', 'Gnome', 'Halfling', 'Half-Elf', 'Half-Orc']
        while self.race is None:
            print("Races")
            print(self.line)
            for i in races:
                print(i)
            print(self.line)
            self.race = input('Choose a Race:')
            print(self.line)
            if self.race not in races:
                self.race = None
                print('Try again')
            else:
                print("You have chosen", self.race)
                print(self.line)
                return self.race

    def get_class(self):
        classes = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk',
                   'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Wizard']
        while self.character_class is None:
            for i in classes:
                print(i)
            print(self.line)
            self.character_class = input('Choose a Class:')
            print(self.line)
            if self.character_class not in classes:
                self.character_class = None
                print('Try Again')
            else:
                print('You have chosen', self.character_class)
                return self.character_class
