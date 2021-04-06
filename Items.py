# Game items



class Gold():
    def __init__(self, name, value, amount, description):
        self.name = name
        self.value = value
        self.amount = 1
        self.description = description

    def __str__(self):
        return "Item : {} Amount: {}\n".format(self.name, self.amount)


class Potion():
    def __init__(self, name, value, amount, description, hpup):
        self.name = name
        self.description = description
        self.value = value
        self.amount = amount
        self.hpup = 50

    def amount(self, amount):
        self.amount = 1

    def __str__(self):
        return "Item : {} Value: {}\n".format(self.name, self.value, )


class Sword():

    def __init__(self, name, amount, value, dmg, description):
        self.name = name
        self.amount = 1
        self.value = 20
        self.dmg = 20
        self.description = description

    def dmg(self):
        self.dmg = 20

    def __str__(self):
        return "Item : {} Value: {}\n".format(self.name, self.value)


class Orc_head():

    def __init__(self, name, amount, value, description):
        self.name = name
        self.amount = 1
        self.value = 20
        self.dmg = 0
        self.description = description

    def __str__(self):
        return "Item : {} Value: {}\n".format(self.name, self.value)


class Elf_head():

    def __init__(self, name, amount, value, description):
        self.name = name
        self.amount = 1
        self.value = 20
        self.dmg = 0
        self.description = description

    def __str__(self):
        return "Item : {} Value: {}\n".format(self.name, self.value)


class Goblin_head():

    def __init__(self, name, amount, value, description):
        self.name = name
        self.amount = 1
        self.value = 20
        self.dmg = 0
        self.description = description

    def __str__(self):
        return "Item : {} Value: {}\n".format(self.name, self.value)


class Book_of_thievery():
    def __init__(self, name, value, amount, description, thievery):
        self.name = name
        self.description = description
        self.value = value
        self.amount = amount
        self.hpup = 10

    def amount(self, amount):
        self.amount = 1


class Book_of_attack():
    def __init__(self, name, value, amount, description, attack):
        self.name = name
        self.description = description
        self.value = value
        self.amount = amount
        self.attack = 12

    def amount(self, amount):
        self.amount = 1


class Book_of_bargain():
    def __init__(self, name, value, amount, description, bargain):
        self.name = name
        self.description = description
        self.value = value
        self.amount = amount
        self.bargain = 15

    def amount(self, amount):
        self.amount = 1


class Book_of_lockpicking():
    def __init__(self, name, value, amount, description, lockpicking):
        self.name = name
        self.description = description
        self.value = value
        self.amount = amount
        self.lockpicking = 30

    def amount(self, amount):
        self.amount = 1


class Lockpick():
    def __init__(self, name, value, amount, description):
        self.name = name
        self.description = description
        self.value = value
        self.amount = amount

    def amount(self, amount):
        self.amount = 1


class Shield():
    def __init__(self, name, value, amount, description, defence):
        self.name = name
        self.description = description
        self.value = value
        self.amount = amount
        self.defence = defence

    def amount(self, amount):
        self.amount = 1


class Head_armor():
    def __init__(self, name, value, amount, description, defence):
        self.name = name
        self.description = description
        self.value = value
        self.amount = amount
        self.defence = defence

        def amount(self, amount):
            self.amount = 1


class Chest_armor():
    def __init__(self, name, value, amount, description, defence):
        self.name = name
        self.description = description
        self.value = value
        self.amount = amount
        self.defence = defence

        def amount(self, amount):
            self.amount = 1


class Leg_armor():
    def __init__(self, name, value, amount, description, defence):
        self.name = name
        self.description = description
        self.value = value
        self.amount = amount
        self.defence = defence

        def amount(self, amount):
            self.amount = 1
