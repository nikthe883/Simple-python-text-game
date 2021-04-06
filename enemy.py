


class Goblin():
    def __init__(self, hp, name, attack):
        self.hp = hp
        self.attack = attack
        self.defence = 25
        self.name = name
        self.armor = 0

    def __repr__(self):
        return "Name    : % s\nHealth  : % s\nAttack  : % s\nDefence : % s\nArmor   : % s" % (
        self.name, self.hp, self.attack, self.defence, self.armor)


class Orc():
    def __init__(self, hp, name, attack):
        self.hp = hp
        self.attack = attack
        self.defence = 35
        self.name = name
        self.armor = 0

    def __repr__(self):
        return "Name    : % s\nHealth  : % s\nAttack  : % s\nDefence : % s\nArmor   : % s" % (
        self.name, self.hp, self.attack, self.defence, self.armor)


class Elf():
    def __init__(self, hp, name, attack):
        self.hp = hp
        self.attack = attack
        self.defence = 35
        self.name = name
        self.armor = 0

    def __repr__(self):
        return "Name    : % s\nHealth  : % s\nAttack  : % s\nDefence : % s\nArmor   : % s" % (
        self.name, self.hp, self.attack, self.defence, self.armor)


class Villager():
    def __init__(self, hp, name, attack):
        self.hp = hp
        self.attack = attack
        self.defence = 35
        self.name = name
        self.armor = 0

    def __repr__(self):
        return "Name    : % s\nHealth  : % s\nAttack  : % s\nDefence : % s\nArmor   : % s" % (
        self.name, self.hp, self.attack, self.defence, self.armor)