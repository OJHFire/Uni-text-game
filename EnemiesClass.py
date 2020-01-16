from random import randint

class Zombie():

    name = "Zombie"
    speed = 1
    damage = 3
    health = 50


    def attack(self):
        multiplier = 1
        num = randint(0, 10)
        if num > 4:
            multiplier = 2
        return self.damage * multiplier
    
class Ogre():

    name = "Ogre"
    speed = 0.5
    damage = 40
    health = 200

    def attack(self):
        multiplier = 1
        num = randint(0, 10)
        if num > 5:
            multiplier = 0.5
        return self.damage * multiplier

class Troll():

    name = "Troll"
    speed = 0.75
    damage = 40
    health = 150

    def attack(self):
        multiplier = 1
        num = randint(0, 10)
        if num > 3:
            multiplier = 0.5
        return self.damage * multiplier

class knight():

    name = "Knight"
    speed = 1
    damage = 15
    health = 150

    def attack(self):
        multiplier = 1
        num = randint(0, 10)
        if num > 8:
            multiplier = 2
        return self.damage * multiplier

class Imp():

    name = "Imp"
    speed = 2
    damage = 10
    health = 100
    
    def attack(self):
        multiplier = 1
        num = randint(0, 10)
        if num > 8:
            multiplier = 2
        return self.damage * multiplier

class Succubus():
    
    name = "Succubus"
    speed = 2
    damage = 5
    health = 50
    
    def attack(self):
        multiplier = 1
        num = randint(0, 10)
        if num > 8:
            multiplier = 2
        return self.damage * multiplier