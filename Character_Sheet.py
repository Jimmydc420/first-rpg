import random


class Character:
    health = 100
    level = 1
    mod = None
    target = None
    stats = None
    race = None
    clas = None
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
        self.adjust_ability_score()
        self.print_stats()

    def main_roll(self, mod, target):
        self.mod = mod
        self.target = target
        return random.randint(1, 20) + self.mod < self.target

    def ability_score(self):
        accept_stats = False
        while not accept_stats:
            print(self.line)
            print("Rolling Stats:")
            stre = random.randint(1, 6) * 3
            dex = random.randint(1, 6) * 3
            con = random.randint(1, 6) * 3
            intel = random.randint(1, 6) * 3
            wis = random.randint(1, 6) * 3
            cha = random.randint(1, 6) * 3
            self.stats = {'str': stre, 'dex': dex, 'con': con,
                          'int': intel, 'wis': wis, 'cha': cha}
            self.print_stats()
            print(self.line)
            if input('Do you accept this roll? Yes/No:') == 'Yes':
                return self.stats
                print(self.line)
            else:
                continue

    def adjust_ability_score(self):
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
        while self.clas is None:
            for i in classes:
                print(i)
            print(self.line)
            self.clas = input('Choose a Class:')
            print(self.line)
            if self.clas not in classes:
                self.clas = None
                print('Try Again')
            else:
                print('You have chosen', self.clas)
                return self.clas


player = Character()
