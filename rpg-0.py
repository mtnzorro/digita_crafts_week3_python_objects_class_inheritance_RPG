"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
class Character(object):
    def __init__(self, name, health, power, species):
        self.name = name
        self.health = health
        self.power = power
        self.species = species

    def alive(self):
        return self.health > 0

    def print_status(self):
        print "%s, the %s has %d health and %d power." % (self.name, self.species, self.health, self.power)

    def attack(self, victim):
        victim.health -= self.power
        print "%s the %s does %d damage to %s the %s." % (self.name, self.species, self.power, victim.name, victim.species)
        if not victim.alive():
            print "%s the %s is dead." % (victim.name, victim.species)


class Zombie(Character):
    def alive(self):
        return True


hero = Character("Jim", 10, 5, "hero")
enemy = Character("Bodi", 6, 2, "goblin")
#Zombie("Zed", 1, 1, "zombie")
#Goblin Character
#goblin= Character("Bodi", 6, 2, "goblin")


while enemy.alive() and hero.alive():

    hero.print_status()
    enemy.print_status()
    print "What do you want to do?"
    print "1. fight enemy"
    print "2. do nothing"
    print "3. flee"
    print "> ",
    input = raw_input()
    if input == "1":
        # Hero attacks enemy
        hero.attack(enemy)
    elif input == "2":
        pass
    elif input == "3":
        print "Goodbye."
        break
    else:
        print "Invalid input %r" % input

    if enemy.alive():
        # Enemy attacks hero
        enemy.attack(hero)
