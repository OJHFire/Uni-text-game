class Weapon():

    def __init__(self, name, rarity, damage, speed, material):
        self.name = name
        self.rarity = rarity
        self.damage = damage
        self.speed = speed
        self.material = material

class Armour():

    def __init__(self, name, rarity, resistance, durability):
        self.name = name
        self.rarity = rarity
        self.resistance = resistance
        self.durability = durability