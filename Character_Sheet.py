import random


class Character:
    health = 100
    level = 1
    mod = None
    target = None
    str = None
    dex = None
    con = None
    intel = None
    wis = None
    cha = None
    stats = None
    races = ['Human', 'Dwarf', 'Elf', 'Gnome', 'Halfling', 'Half-Elf', 'Half-Orc']
    race = None

    def __init__(self):
        name = input("Choose a name: ")
        print('____________________________________')
        self.name = name
        print("Hi", self.name)
        print('____________________________________')
        self.ability_score()
        self.get_race()
        print("You have chosen", self.race)
        self.print_stats()

    def main_roll(self, mod, target):
        self.mod = mod
        self.target = target
        return random.randint(1, 20) + self.mod < self.target

    def ability_score(self):
        accept_stats = False
        while not accept_stats:
            print("Rolling Stats:")
            print('________________________________')
            self.str = random.randint(1, 6) * 3
            self.dex = random.randint(1, 6) * 3
            self.con = random.randint(1, 6) * 3
            self.intel = random.randint(1, 6) * 3
            self.wis = random.randint(1, 6) * 3
            self.cha = random.randint(1, 6) * 3
            self.stats = {'str': self.str, 'dex': self.dex, 'con': self.con,
                          'int': self.intel, 'wis': self.wis, 'cha': self.cha}
            self.print_stats()
            if input('Do you accept this roll? Yes/No:') == 'Yes':
                return self.stats
            else:
                continue

    def print_stats(self):
        for k, v in self.stats.items():
            print(k, ':', v)

    def get_race(self):
        while self.race is None:
            print("Races")
            print('_____________________________')
            for i in self.races:
                print(i)
            self.race = input('Choose a Race:')
            print('_____________________________')
            if self.race not in self.races:
                self.race = None
                print('Try again')
            else:
                return self.race

    def get_class(self):
        pass


player = Character()
