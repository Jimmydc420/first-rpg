import random


class Character:
    health = 100
    level = 1
    mod = None
    target = None
    stats = None
    race = None
    clas = None

    def __init__(self):
        name = input("Choose a name: ")
        print('____________________________________')
        self.name = name
        print("Hi", self.name)
        print('____________________________________')
        self.ability_score()
        self.get_race()
        self.print_stats()
        self.get_class()

    def main_roll(self, mod, target):
        self.mod = mod
        self.target = target
        return random.randint(1, 20) + self.mod < self.target

    def ability_score(self):
        accept_stats = False
        while not accept_stats:
            print("Rolling Stats:")
            print('________________________________')
            stre = random.randint(1, 6) * 3
            dex = random.randint(1, 6) * 3
            con = random.randint(1, 6) * 3
            intel = random.randint(1, 6) * 3
            wis = random.randint(1, 6) * 3
            cha = random.randint(1, 6) * 3
            self.stats = {'str': stre, 'dex': dex, 'con': con,
                          'int': intel, 'wis': wis, 'cha': cha}
            self.print_stats()
            if input('Do you accept this roll? Yes/No:') == 'Yes':
                return self.stats
            else:
                continue

    def print_stats(self):
        for k, v in self.stats.items():
            print(k, ':', v)

    def get_race(self):
        races = ['Human', 'Dwarf', 'Elf', 'Gnome', 'Halfling', 'Half-Elf', 'Half-Orc']
        while self.race is None:
            print("Races")
            print('_____________________________')
            for i in races:
                print(i)
            self.race = input('Choose a Race:')
            print('_____________________________')
            if self.race not in races:
                self.race = None
                print('Try again')
            else:
                print("You have chosen", self.race)
                return self.race

    def get_class(self):
        classes = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk',
                   'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Wizard']
        while self.clas is None:
            for i in classes:
                print(i)
            self.clas = input('Choose a Class:')
            print('_______________________________')
            if self.clas not in classes:
                self.clas = None
            else:
                print('You have chosen', self.clas)
                return self.clas


player = Character()
