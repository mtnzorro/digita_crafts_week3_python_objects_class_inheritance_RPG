"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health whereas a sword will add 2 power.
"""
import random
import time

class Character(object):
    def __init__(self):
        self.name = '<undefined>'
        self.health = 10
        self.power = 5
        self.coins = 20

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.alive():
            return
        print "%s attacks %s" % (self.name, enemy.name)
        enemy.receive_damage(self.power)
        time.sleep(1.5)

    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if not self.alive():
            print "%s is dead." % self.name

    def print_status(self):
        print "%s has %d health and %d power." % (self.name, self.health, self.power)


class Hero(Character):
    def __init__(self):
        self.name = 'hero'
        self.health = 10
        self.power = 5
        self.armor = 0
        self.coins = 20
        self.sleeping = False

    def restore(self):
        self.health = 10
        print "Hero's heath is restored to %d!" % self.health
        time.sleep(1)

    def buy(self, item):
        self.coins -= item.cost
        item.apply(hero)

    def attack(self, enemy):
        if self.sleeping:
            print "%s is asleep and cannot attack this round" % self.name
        else:
            double_damage = random.random() < 0.2
            if double_damage:
                print "%s deals double damage to %s during attack!!!" % (self.name, enemy.name)
                self.power = self.power * 2
            super(Hero, self).attack(enemy)
            if double_damage:
                self.power = self.power / 2

    def receive_damage(self, points):
        if self.armor >= points:
            super(Hero, self).receive_damage(0)
        else:
            super(Hero, self).receive_damage(points - self.armor)

    def loot(self, enemy):
        self.coins += enemy.coins
        print "%s loots the dead %s for %d coins" % (self.name, enemy.name, enemy.coins)



class Goblin(Character):
    def __init__(self):
        self.name = 'goblin'
        self.health = 6
        self.power = 2
        self.coins = 5

class Demogorgon(Character):
    def __init__(self):
        self.name = 'demogorgon'
        self.health = 40
        self.power = random.randint(5,10)
        self.coins = 100

class Jigglypuff(Character):
    def __init__(self):
        self.name = 'Jigglypuff'
        self.health = 11
        self.power = 1
        self.coins = 7

    def attack(self, enemy):
        if hero.sleeping:
            hero.sleeping = False
            print "%s wakes up" % hero.name
        print "%s is singing!" % self.name
        print "JIIIIIIGUHLYY PUFFFFF LA LA LA LA"
        sleep_attack = random.random() < .7
        if sleep_attack:
            print "%s has been lulled to sleep for this turn!" % hero.name
            hero.sleeping = True
        else:
            print "The sweet tune has no effect"
            pass
        super(Jigglypuff, self).attack(enemy)

class Medic(Character):
    def __init__(self):
        self.name = 'medic'
        self.health = 12
        self.power = 2
        self.coins = 6

    def receive_damage(self, points):
        super(Medic, self).receive_damage(points)
        recuperate = random.random() < .2
        if recuperate:
            print "%s recovers 2 health points!" % self.name
            self.health += 2

class Shadow(Character):
    def __init__(self):
        self.name = 'shadow'
        self.health = 1
        self.power = 1
        self.coins = 10

    def receive_damage(self, points):
        gets_hit = random.random() < .1
        if gets_hit:
            super(Shadow, self).receive_damage(points)
        else:
            print "%s evades attack." % self.name

class Wizard(Character):
    def __init__(self):
        self.name = 'wizard'
        self.health = 8
        self.power = 1
        self.coins = 9

    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print "%s swaps power with %s during attack" % (self.name, enemy.name)
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power

class Zombie(Character):
    def __init__(self):
        self.name = 'zombie'
        self.health = 8
        self.power = 1
        self.coins = 15

    def alive(self):
        return True

class Battle(object):
    def do_battle(self, hero, enemy):
        print "====================="
        print "Hero faces the %s" % enemy.name
        print "====================="
        if hero.sleeping:
            hero.sleeping = False
        while hero.alive() and enemy.alive():
            hero.print_status()
            enemy.print_status()
            time.sleep(1.5)
            print "-----------------------"
            print "What do you want to do?"
            print "1. fight %s" % enemy.name
            print "2. do nothing"
            print "3. flee"
            print "> ",
            input = int(raw_input())
            if input == 1:
                hero.attack(enemy)
            elif input == 2:
                pass
            elif input == 3:
                print "Goodbye."
                exit(0)
            else:
                print "Invalid input %r" % input
                continue
            # this statement is necessary to keep Jigglypuff from singing post-mortem
            if enemy.alive():
                enemy.attack(hero)
        if hero.alive():
            print "You defeated the %s" % enemy.name
            hero.loot(enemy)
            return True
        else:
            print "YOU LOSE!"
            return False

class Tonic(object):
    cost = 5
    name = 'tonic'
    def apply(self, hero):
        hero.health += 2
        print "%s's health increased to %d." % (hero.name, hero.health)

class SuperTonic(object):
    cost = 20
    name = 'super-tonic'
    def apply(self, hero):
        hero.health += 10
        print "%s's health increased to %d." % (hero.name, hero.health)

class Sword(object):
    cost = 10
    name = 'sword'
    def apply(self, hero):
        hero.power += 2
        print "%s's power increased to %d." % (hero.name, hero.power)

class Armor(object):
    cost = 10
    name = 'armor'
    def apply(self, hero):
        hero.armor += 2
        print "%s's armor increased to %d." % (hero.name, hero.armor)



class Store(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Tonic, SuperTonic, Sword, Armor]
    def do_shopping(self, hero):
        while True:
            print "====================="
            print "Welcome to the store!"
            print "====================="
            print "You have %d coins." % hero.coins
            print "What do you want to do?"
            for i in xrange(len(Store.items)):
                item = Store.items[i]
                print "%d. buy %s (%d)" % (i + 1, item.name, item.cost)
            print "10. leave"
            input = int(raw_input("> "))
            if input == 10:
                break
            else:
                ItemToBuy = Store.items[input - 1]
                item = ItemToBuy()
                if hero.coins >= item.cost:
                    hero.buy(item)
                else:
                    print "Not enough coins to purchase %s" % item.name
                time.sleep(1.5)
hero = Hero()
enemies = [Goblin(), Medic(), Wizard(), Shadow(), Zombie(), Demogorgon()]
battle_engine = Battle()
shopping_engine = Store()

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print "YOU LOSE!"
        exit(0)
    shopping_engine.do_shopping(hero)

print "YOU WIN!"
