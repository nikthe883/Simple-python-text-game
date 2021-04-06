# Simple text based adventure game


import random
import time
from Items import *
from enemy import *

# enemy stats

goblin = Goblin(100, name="Goblin", attack=47)
elf = Elf(100, name="Elf", attack=50)
orc = Orc(100, name="Orc", attack=55)
villager = Villager(100, name="Villager", attack=47)

# Items

potion = Potion("HP Potion", amount=0, value=2, hpup=50, description="Healing you")
sword = Sword("Sword", 0, 20, 20, "When equiped adding 20 dmg")
goblin_head = Goblin_head(name="Goblin Head", amount=0, value=20, description="Gross Goblin head")
elf_head = Elf_head(name="Elf Head   ", amount=0, value=20, description="Gross ELf head")
orc_head = Orc_head(name="Orc Head   ", amount=0, value=20, description="Gross Orc head")
shield = Shield(name="Shield", amount=0, value=100, description="The good old shield.Gives you 10 defence", defence=5)
Head_armor = Head_armor(name="Helmet", amount=0, value=100, description="Helmet.Gives you 5 defence", defence=5)
Chest_armor = Chest_armor(name="Chestplate", amount=0, value=100, description="Chestplate. Gives you 12 defence",
                          defence=12)
Leg_armor = Leg_armor(name="Leggings  ", amount=0, value=100, description="Leggings. Give you 10 defence", defence=10)
lockpick = Lockpick(name="Lockpick    ", amount=0, value=25, description="A simple lockpick..Used to pick locks")

# shows if items are equipped
Shield_equip = "unequip"
Head_armor_equip = "unequip"
Chest_armor_equip = "unequip"
Leg_armor_equip = "unequip"
Sword_equip = "unequip"
items_in_inventory = False

global name


# player class

class Player:
    def __init__(self, name):
        self.hp = 100
        self.attack = 20
        self.defence = 12
        self.armor = 12
        self.name = str(name)
        self.thievery = 10
        self.lockpicking = 10

    def hp(self, hp):
        self.hp = hp + 100

    def attack(self):
        self.attack = 20

    def defence(self):
        self.defence = 15

    def name(self):
        self.name = {}

    def armor(self):
        self.armor = 12

    def thievery(self):
        self.thievery = 10

    def lockpicking(self):
        self.lockpicking = 10

    def __repr__(self):
        return "Name    : % s\nHealth  : % s\nAttack  : % s\nDefence : % s\nArmor   : % s\nThievery : % s\n" % (
            self.name, self.hp, self.attack, self.defence, self.armor, self.thievery,)


# inventory for player

class Inventory_Player:
    def __init__(self):
        self.balance = 100
        self.items = {}

    def add_item(self, item):
        self.items[item.name] = item

    def loose_gold(self, amount):
        self.balance -= amount

    def add_gold(self, amount):
        self.balance += amount

    def loose_item(self):
        self.items.pop("HP Potion")

    def __str__(self):
        print("your inventory\n"
              "================\n"
              "You have: " + str(self.balance) + " Gold\n"
                                                 "==================\n"
                                                 "Items : \n"
                                                 "====================")
        out1 = '\t'.join(['Amount      ', 'Name   ', "Value", "Description"])
        for item in self.items.values():
            out1 += '  \n' + '   \t'.join([str(x) for x in [item.amount, item.name, item.value, item.description]])
        return out1


inventory = Inventory_Player()


# rooms

class Forest:

    def __init__(self):
        print("You are in a deep dark forest\n"
              "")
        time.sleep(2)
        print("You saw in the distance a figure..\n"
              " ")
        time.sleep(2)
        forest_choose = input("Lets kill him..  y/n\n"
                              "")
        if forest_choose == "y":
            attack()
        elif forest_choose == "n":
            ops = random.randint(1, 2)
            if ops == 1:
                print("Neither that you didn't want to kill him...\n"
                      "")
                time.sleep(2)
                print("You couldn't deny your blood thirst instincts and attacked..\n"
                      "")
                attack()
            elif ops == 2:
                print("You sneaked around the figure and continued on your way\n"
                      "")
                time.sleep(2)


class Path:

    def __init__(self, ):
        self.name = name
        path_encounter = random.randint(1, 3)
        if path_encounter == 1:
            print("While you where walking down the road you saw something on the road side..\n"
                  "")
            time.sleep(2)
            chest_loot()
        if path_encounter == 2:
            print("While you where walking down the road, you suddenly heard behind you ... \n"
                  "")
            time.sleep(2)
            print("STOP I WILL TAKE THAT GOLD\n"
                  "")
            attack()
        if path_encounter == 3:
            print("You continued on your way..nothing interesting happened\n"
                  "")


class Village:
    global enemy

    def __init__(self, name):
        self.name = name
        print("You walked into a small village\n"
              "")
        time.sleep(2)
        print("But it was abandoned. You look inside the houses to see if there is anything useful for you\n"
              "")
        time.sleep(2)
        village_loot = random.randint(1, 5)
        if village_loot == 1:
            chest_loot()
        global enemy
        if village_loot == 2:
            print("You thought that the village was abandoned and was REALLY surprised when a villager attacked you\n"
                  "")
            enemy = villager
            attack()
        else:
            print("You could not find anything useful in the village\n"
                  "")
            time.sleep(2)


class Town:
    def __init__(self):
        self.name = None

        print("You walked into the TOWN\n"
              "")
        time.sleep(2)
        print("You looked around but the only things you could see were a couple of houses, a shop, an armory and Inn\n"
              "")
        time.sleep(1)
        print("1. Weapon smith\n"
              "2. House\n"
              "3. Shop\n"
              "4. Inn\n"
              "5. Xiburg's house")

        go = input("Where do you wanna go\n"
                   "===================\n"
                   "\n")
        if go == "1":
            Blacksmith()
        elif go == "2":
            House()
        elif go == "3":
            Shop()
        elif go == "4":
            Inn()
        elif go == "5":
            Xiburg_House()


class Blacksmith:
    def __init__(self):
        print("You have walked in the armory shop. You like anything  ?\n"
              "")
        time.sleep(2)
        trading()


class House:
    def __init__(self):
        self.name = name
        print("You looked at one of the houses that were in the Town..\n"
              "")
        time.sleep(2)
        print("You tried to get in however it was locked...\n"
              "")


class Shop:
    def __init__(self):
        self.name = name
        print("You walked into the shop. Look what the shop has to offer you: \n"
              "\n")
        time.sleep(1)
        trading()


class Inn:
    def __init__(self):
        self.name = name
        print("You walked into the Inn\n"
              "")
        time.sleep(1)
        print("The innkeeper looked at you and asked with grumpy voice..\n"
              "")
        time.sleep(2)
        print("Hey you do you want a room ? It will cost you 30 gold coins\n"
              "")
        time.sleep(2)
        print("But if you don't have money I will beat you till you don't move\n"
              "")
        want_room = input("y/n")
        if want_room == 'y':
            if inventory.balance < 29:
                time.sleep(3)
                print("The innkeeper understood that you don't have money and beat your sissy ass..\n"
                      "")
                time.sleep(2)
                print("HP -  50\n"
                      "")
                time.sleep(1)
                print("NEXT TIME BRING MONEY YOU BROKE BASTARD -   ")
                print("shouted the innkeeper while throwing you out of the Inn\n"
                      "")
                player.hp -= 50
                print(player)
            if inventory.balance > 30:
                print("The innkeeper showed your room and left you alone\n"
                      "")
                time.sleep(1)
                print("There wasn't anything special in it but the sweet, sweet bed in front of you\n"
                      "")
                sleeping()
        if want_room == "n":
            time.sleep(1)
            print("I do not have any work for you now GET OUT\n"
                  "")


class Xiburg_House:
    def __init__(self):
        time.sleep(2)
        print("You went south out of the TOWN and saw Xiburg's house.\n"
              ""
              "You walked to the front door and knocked...")
        time.sleep(2)
        print("'Come in...' - you heard a voice from the inside..and pushed the door\n"
              "")
        time.sleep(2)
        print("The house was with only one room...however with a large fireplace - Xiburg was there\n"
              ""
              "You approached him...\n"
              "")
        time.sleep(3)
        quest_items = input("TEll me now " + name + " have you brought my goblin heads ? y/n\n"
                                                    "")
        if quest_items == "y" and goblin_head.amount >= 3:
            print("'Very well my friend...' - Xiburg mumbled under his nose and turned around\n"
                  "")
            time.sleep(3)
            print("While you were waiting for him to say something suddenly Xiburg turned towards you\n"
                  "")
            time.sleep(2)
            print("You saw a dagger in his hand but it was too late..\n"
                  ""
                  "")
            time.sleep(1)
            print("He stabbed you in the stomach and pulled the dagger..\n"
                  ""
                  "")
            time.sleep(1)
            print("You fell on your knees and bled to death\n"
                  "")
            time.sleep(3)
            print("Xiburg looked at your body with disgust and said to himself\n"
                  "")
            time.sleep(1)
            print("'Those pathetic outer world creatures'\n"
                  "")
            time.sleep(3)
            end_game()

        if quest_items == "y" and goblin_head.amount < 3:
            print("Xiburg looked into your eyes and said:\n")
            time.sleep(2)
            print("DON'T LIE TO ME\n")

        if quest_items == "n":
            print("So what are you waiting bring me 3 Goblin heads..\n")


# movement logic
def move():
    time.sleep(1)
    print("\n"
          "====================\n"
          "What do you want to do ?\n"
          "====================\n"
          "\n"
          "1.Head east\n"
          "2.Head west\n"
          "3.Head south\n"
          "4.Head north\n"
          "5.Flee back to TOWN\n"
          "6.Open inventory\n"
          "7.Show stats\n"
          "8.Equip Items\n")

    where = input("Press 1,2,3,4,5,6,7,8\n"
                  "\n"
                  "==================")

    if where == "1":
        room()

    elif where == "2":
        room()

    elif where == "3":
        room()

    elif where == "4":
        room()

    elif where == "5":
        Town()

    elif where == "6":
        print(inventory)

    elif where == "7":
        print(player)
        equipped_items()

    elif where == "8":
        equip()

    elif where == "9":
        Blacksmith()

    else:
        print("Choose options")


# equip items
def equipped_items():
    if Shield_equip == "equip":
        print("\nShield is equipped\n"
              "")

    if Shield_equip == "unequip":
        print("\nShield is not equipped\n"
              "")

    if Head_armor_equip == "equip":
        print("Helmet is equipped\n"
              "")

    if Head_armor_equip == "unequip":
        print("Helmet is not equipped\n"
              "")

    if Chest_armor_equip == "equip":
        print("Chestplate is equipped\n"
              "")

    if Chest_armor_equip == "unequip":
        print("Chestplate is not equipped\n"
              "")

    if Leg_armor_equip == "equip":
        print("Leggings is equipped\n"
              "")

    if Leg_armor_equip == "unequip":
        print("Leggings is not equipped\n"
              "")

    if Sword_equip == "equip":
        print("Swords is equipped\n"
              "")

    if Sword_equip == "unequip":
        print("Sword is not equipped")


# trading system
def trading():
    global items_in_inventory

    amount1 = 10
    name1 = "HP Potion"
    value1 = 50
    description1 = "Heals you"

    amount2 = 10
    name2 = "Sword"
    value2 = 500
    description2 = "Do I need to explain what is sword"

    # topshelf = print(" amount ", '    Name    ', '  Value', "   Description")
    traders_items1 = "   " + str(amount1) + "       " + name1 + "        " + str(value1) + "     " + str(description1)
    traders_items2 = "   " + str(amount2) + "       " + name2 + "        " + str(value2) + "     " + str(description2)

    # need to work on trader and so on amount
    print("Still in development")

    trade = input("Do you want to trade ? y/n \n")

    # trader_add_items()
    if trade == "y":

        buy_sell = input("Do you want to buy or to sell | b or s")
        if buy_sell == "b":
            print(" amount ", '    Name    ', '  Value', "   Description")
            print(traders_items1)
            print(traders_items2)

            name_item = input("What do you want to buy")
            if name_item == "hp potion":
                if inventory.balance < 49:
                    print("You do not have enough money to buy this item")

                elif inventory.balance >= 50:
                    print("You have added to your inventory 1 " + name1)
                    potion.amount += 1
                    inventory.add_item(potion)
                    items_in_inventory = True
                    inventory.loose_gold(50)

            if name_item == "sword":
                if inventory.balance < 499:
                    print("You do not have enough money to buy this item")
                elif inventory.balance >= 500:
                    print("You have added to your inventory 1 " + name2)
                    sword.amount += 1
                    inventory.add_item(sword)
                    items_in_inventory = True
                    inventory.loose_gold(500)

            else:
                print("Choose an option")

        if buy_sell == "s":

            print("what do you want to sell ?")
            print(inventory)
            sell_item = input("Write item's name to sell it")
            if sell_item == "HP Potion":
                if potion.amount < 1:
                    print("You have 0 amount from this item")
                else:
                    confirm_sell = input("Do you want to sell HP Potion for 10 gold ? y/n")
                    if confirm_sell == "y":
                        inventory.add_gold(10)
                        potion.amount -= 1
                    if confirm_sell == "n":
                        print("Have a nice day")

                    else:
                        print("Choose an option")

            if sell_item == "Sword":
                if sword.amount < 1:
                    print("You have 0 amount from this item")
                else:
                    confirm_sell = input("Do you want to sell Sword for 20 gold ? y/n")
                    if confirm_sell == "y":
                        inventory.add_gold(20)
                        sword.amount -= 1
                    if confirm_sell == "n":
                        print("Have a nice day")

                    else:
                        print("Choose an option")

            else:
                print("Choose an option")

        else:
            print("Choose an option")


# shows end game
def end_game():
    print("Congratulations you finished the game...\n"
          "")
    time.sleep(3)
    print("For now...")
    time.sleep(2)
    exit()


# sleeping
def sleeping():
    sleep = input("Do you want to sleep y/n\n"
                  "")
    if sleep == "y":
        print("You were very tired, lied on the bed and closed your eyes\n"
              "")
        if player.hp < 100:
            player.hp = 100
        time.sleep(5)
        print("You woke up. IT IS TIME TO ACT\n"
              ""
              "")
        time.sleep(1)
    if sleep == "n":
        print("Sleep is healthy\n"
              "")
        time.sleep(2)
        print("BUT REAL MEN DON'T NEED SLEEP\n"
              ""
              "")
        time.sleep(1)
    else:
        print("Choose option\n"
              "")


# calculate defence parameters and how it influences player stats
def defence():
    if Head_armor_equip == "equip":
        enemy.attack -= Head_armor.defence
    if Chest_armor_equip == "equip":
        enemy.attack -= Chest_armor.defence
    if Leg_armor_equip == "equip":
        enemy.attack -= Leg_armor.defence


# battle system for game
def attack():
    print("You have encountered " + enemy.name + "\n"
                                                 "")
    if spawn_enemy() is True:
        while player.hp >= 0:
            # goblin.attack = 20
            # elf.attack = 50
            # orc.attack
            reset_enemy()
            print(str(player))
            print("===================\n")
            print(str(enemy))
            print("===================\n")
            attack_or_heal = input("Press a to attack or q to heal\n"
                                   ""
                                   )
            if attack_or_heal == "a":

                defence()
                enemy.hp -= player.attack

                print(enemy.name + " is left with " + str(enemy.hp) + " HP\n"
                                                                      "")
                if Shield_equip == "equip":

                    reflect = input("You have a shield. Press r to  try to reflect damage\n"
                                    ""
                                    )
                    if reflect == "r":
                        chance_of_reflect = random.randint(1, 3)
                        if chance_of_reflect == 1:
                            player.hp -= (enemy.attack - 20)
                            print("You have successfully reflected 20 dmg\n"
                                  ""
                                  )
                        if chance_of_reflect == 2:
                            player.hp -= (enemy.attack - 10)
                            print("You have partially reflected enemy attack\n"
                                  ""
                                  )
                        if chance_of_reflect == 3:
                            player.hp -= enemy.attack
                            print("You didn't do anything with the shield. Learn to use it noob\n"
                                  ""
                                  )

                    else:
                        print("Choose an option noob..\n"
                              "")

                if Shield_equip == "unequip":
                    player.hp -= enemy.attack
                    print("You are left with : " + str(player.hp) + " HP\n"
                                                                    "")

                if player.hp <= 0:
                    print("You loose\n"
                          "")
                    global running
                    strat()
                    player.hp = 100
                    enemy.hp = 100
                    global items_in_inventory
                    inventory.loose_gold(50)
                    items_in_inventory = False
                    player.attack = 20

                    break

                if enemy.hp <= 0:
                    input("You won lets continue press enter\n"
                          "")
                    enemy.hp = 100
                    enemy.attack = 100
                    mob_drop()

                    break

            if attack_or_heal == "q":
                heal()
    else:
        print("But when you saw him you got scared  and ran like a the little COWARD you are..\n"
              "")


# mob drop


def mob_drop():
    gold_loot = random.randint(2, 17)
    drop = random.randint(1, 5)
    inventory.add_gold(gold_loot)
    print("You got " + str(
        gold_loot) + " gold from killing " + enemy.name + ". Tell me is it worth it ? Are you happy ?\n"
                                                          "")
    if drop == 1:

        if enemy == goblin:
            loot()
        elif enemy == elf:
            loot()
        elif enemy == orc:
            loot()
        elif enemy == villager:
            loot()

    else:
        print(" You could not get any loot from the body..Noob\n"
              "")


# resets enemy attack
def reset_enemy():
    goblin.attack = 50
    elf.attack = 50
    orc.attack = 60


# random generation

def spawn_enemy():
    fight = random.randint(1, 2)
    if fight == 1:
        return True
    if fight == 2:
        return False


# random generated rooms


def room():
    while True:

        gen1 = random.randint(1, 3)
        if gen1 == 1:
            Forest()
        elif gen1 == 2:
            Village("Village")
        elif gen1 == 3:
            Path()

        input("Lets continue...press Enter\n"
              "")
        break


# loot in chest
def chest_loot():
    global items_in_inventory
    print("Wohooo, you have found a chest with loot.\n"
          "")
    chestloot = random.randint(1, 2)
    if chestloot == 1:
        if lockpick.amount >= 1:
            print("You are trying to open the chest with the lockpicks you have\n"
                  "")
            time.sleep(1)
            open_chest_tries = random.randint(1, 3)
            if open_chest_tries == 1:
                print("You have successfully opened the chest\n"
                      "")
                time.sleep(1)
                win = random.randint(15, 50)  # random value for gold
                inventory.add_gold(win)
                loot()
                print("You have added to your inventory: " + str(win) + " Gold \n"
                                                                        "")
                lockpick.amount -= 1
            else:
                print("Lockpick broke\n"
                      "")
        if lockpick.amount < 1:
            print("You do not have any lockpicks\n"
                  "")
    elif chestloot == 2:
        print("Someone shouted THIEF\n"
              "")
        time.sleep(1)
        print("You got spotted while trying to open the chest....\n"
              "")
        attack()


# random loot generation


def loot():
    global items_in_inventory
    loot = random.choice(
        [potion, sword, goblin_head, elf_head, orc_head, shield, Head_armor, Chest_armor, Leg_armor, lockpick])
    items_in_inventory = True
    loot.amount = + 1
    inventory.add_item(loot)
    print("You have added to your inventory 1 " + loot.name
          + "\n"
            "")


# heal player

def heal():
    if potion.amount < 0:
        print("You do not have any potions to heal\n"
              "")

    elif potion.amount > 0:
        q = input("Press q to heal\n"
                  "")
        if q == "q" and player.hp < 100:
            if player.hp <= 50:
                potion.amount -= 1
                player.hp += potion.hpup
                print("You have healed yourself with " + str(potion.hpup) + "HP .You are lef with " + str(
                    potion.amount) + " HP potions\n"
                                     "")
                time.sleep(2)
            elif player.hp > 50:
                potion.amount -= 1
                player.hp = 100
                print("You have healed yourself with " + str(potion.hpup) + "HP .You are lef with " + str(
                    potion.amount) + " HH potionss\n"
                                     "")
            time.sleep(2)

        elif player.hp >= 100 and q == "q":
            print("You have reached your maximum health. You can not heal anymore.\n")
            time.sleep(2)
    else:
        print("You do not have any potions\n")
        time.sleep(2)
    # shows player stats


# equips items
def equip():
    print(inventory)
    equipped_items()
    global Shield_equip
    global Head_armor_equip
    global Chest_armor_equip
    global Leg_armor_equip
    global Sword_equip

    if items_in_inventory is False:
        print("\nYou do not have any items to equip now\n"
              "")

    elif items_in_inventory is True:

        equip = input("Which item do you want to equip ?\n"
                      "")

        if equip == "sword":
            Sword_equip = "equip"
            player.attack += sword.dmg
            inventory.items.pop("Sword")
            print("Sword is equipped\n"
                  "")

        if equip == "shield":
            Shield_equip = "equip"
            inventory.items.pop("Shield")
            print("Shield is equipped\n"
                  "")

        if equip == "helmet":
            Head_armor_equip = "equip"
            inventory.items.pop("Helmet")
            print("Helmet is equipped\n"
                  "")

        if equip == "chestplate":
            Chest_armor_equip = "equip"
            inventory.items.pop("Chestplate")
            print("Chestplate is equipped\n"
                  "")
        if equip == "leggings":

            Leg_armor_equip = "equip"
            inventory.items.pop("Leggings")
            print("Leggings are equipped\n"
                  "")

        elif equip != "sword" or "helmet" or "chestplate" or "leggings":
            print("You can't equip that item\n")


# intro of game and 1st quest

def intro():
    global introo
    global running
    print("==================================")
    print("You woke up in a small town without having any idea how did you get there...\n")
    time.sleep(2)
    print("Upon a second glance you saw a strange figure approaching. You stood up and waved at the figure.\n")
    time.sleep(2)
    print("""The figure kept walking in your direction. As he came closely you saw that he was old, with long 
        gray hair and beard, dirty clothes and holding a rusty sword in his right hand...\n""")
    time.sleep(2)
    print("You looked around and saw a stick laying a couple of meters\n")
    print("==================================\n")
    time.sleep(2)
    option_intro = input("Do you want to fight and take the stick or you want to wait\n"
                         "\n"
                         " ==========================================================\n"
                         "\n"
                         " Press 1 to fight\n"
                         " Press 2 to wait\n "
                         "==========================================================\n")
    if option_intro == "1":
        print("You jumped forward took the stick and attacked the old man..... ")
        time.sleep(2)
        print("You manage to kill him , however you were heavily wounded by his sword")
        time.sleep(2)
        print("You fainted on the ground....")
        time.sleep(3)
        print("And Died....Try again")
        time.sleep(3)
        running = False
        strat()

    elif option_intro == "2":
        print("You decided to wait...\n")
        time.sleep(2)
        print("Tha man approach you and said : 'Hmmm, you finally arrived... ' \n")

        print("Very good " + name + "...")
        time.sleep(2)
        print("Now, my name is Xiburg, and you are in the TOWN...you can find me just outside the TOWN..\n"
              "There is a small house. I live there...\n")
        time.sleep(3)
        print("Now enough with the talking\n"
              "I need you to go outside the TOWN and bring me 3 Goblin "
              "head.Here are 4 HP potions for your adventures..")
        time.sleep(3)
        print("Hmmm , WAIT")
        time.sleep(1)
        print("On the other hand when I think about it...Here take those 5 lockpicks as well\n"
              "I hope you know how to use those\n")
        time.sleep(2)

        print(
            "===================\n"
            "Here check your stats:\n"
            "===================\n")

        print(player)
        equipped_items()
        inventory.add_item(potion)
        inventory.add_item(lockpick)
        potion.amount += 4
        lockpick.amount += 4
        introo = "stop"
    else:
        print("Chose an option\n")


# Play again
def strat():
    global running
    again = input("Game over.\n"
                  "Do you want to play again ? (y or n)\n")
    if again == "y":
        running = True

    elif again == "n":
        running = False
        print("NOOB.BYE")

    else:
        strat()


# asks for players name
def player_set_up():
    global name
    name = input("What is your name, adventurer: ")
    print("")
    time.sleep(2)


player_set_up()
player = Player(name)

# game loop


running = True
introo = "start"

while running:

    if introo == "start":

        intro()

    else:
        while True:
            enemy = random.choice([goblin, elf, orc, villager])
            move()

else:
    strat()
