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

    def __init__(self):
        name = input("Choose a name: ")
        self.name = name
        print("Hi", self.name)

    def main_roll(self, mod, target):
        self.mod = mod
        self.target = target
        return random.randint(1, 20) + self.mod < self.target

    def ability_score(self):
        self.str = random.randint(1, 6) * 3
        self.dex = random.randint(1, 6) * 3
        self.con = random.randint(1, 6) * 3
        self.intel = random.randint(1, 6) * 3
        self.wis = random.randint(1, 6) * 3
        self.cha = random.randint(1, 6) * 3
        self.stats = {'str': self.str, 'dex': self.dex, 'con': self.con,
                      'intel': self.intel, 'wis': self.wis, 'cha': self.cha}
        return self.stats

    def print_stats(self):
        pass

    def get_race(self):
        pass

    def get_class(self):
        pass

    def level_up(self):
        pass


player = Character()
player.ability_score()
print(player.stats)
