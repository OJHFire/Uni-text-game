class Room():

    def __init__(self, name, rarity, loot_chance, loot_strength, enemy_chance, enemy_strength, nesw, exit_bool):
        #initialises all properties of the room
        self.name = name
        self.rarity = rarity
        self.loot_chance = loot_chance
        self.loot_strength = loot_strength
        self.enemy_chance = enemy_chance
        self.enemy_strength = enemy_strength
        self.nesw = nesw
        self.exit = exit_bool
        self.north = False
        self.east = False
        self.south = False
        self.west = False
        #figures out which directions of the room are available to have other rooms branch off
        for char in self.nesw:
            if char == "n":
                self.north = True
            elif char == "e":
                self.east = True
            elif char == "s":
                self.south = True
            elif char == "w":
                self.west = True