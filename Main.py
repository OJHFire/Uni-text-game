#importing all the other libraries and classes
from ItemsClass import Weapon
from ItemsClass import Armour
from RoomsClass import Room
from EnemiesClass import Enemy
from time import sleep
from os import system
from random import randint



def slow_print(string):
    for char in string + "\n":
        print(char, end="")
        sleep(0.01)

#global difficulty variable
difficulty = "Normal"

rooms = ["corridor_ns", "corridor_ew", "lcorridor_ne", "lcorridor_nw", "lcorridor_se", "lcorridor_sw", "armoury", "kitchen", "torture_chamber", "dining_hall"]

#define weapons using Weapon class
fist = Weapon("Fist", 0, 1, 3, "None")
iron_broadsword = Weapon("Iron Broadsword", 1, 10, 1.5, "Iron")
iron_dagger = Weapon("Iron Dagger", 1, 5, 3, "Iron")
steel_broadsword = Weapon("Steel Broadsword", 2, 20, 1.5, "Steel")
steel_dagger = Weapon("Steel Dagger", 2, 10, 3, "Steel")
iron_warhammer = Weapon("Iron Warhammer", 2, 50, 0.25, "Iron")
steel_warhammer = Weapon("Steel Warhammer", 3, 100, 0.25, "Steel")
iron_waraxe = Weapon("Iron War-Axe", 1, 7, 2, "Iron")
steel_waraxe = Weapon("Steel War-Axe", 2, 20, 2, "Steel")
iron_battleaxe = Weapon("Iron Battle Axe", 2, 30, 0.5, "Iron")
steel_battleaxe = Weapon("Steel Battle Axe", 3, 60, 0.5, "Steel")
shotgun = Weapon("Shotgun?", 4, 200, 3, "Steel")



#define enemy types using Enemy class
zombie = Enemy("Zombie", 1, 3, 50, 1)
ogre = Enemy("Ogre", 0.5, 40, 200, 3)
troll = Enemy("Troll", 0.75, 20, 150, 3)
possessed_knight = Enemy("Possessed Knight", 1,  15, 150, 2)
imp = Enemy("Imp", 2, 10, 100, 2)
succubus = Enemy("Succubus", 3, 3, 96, 2)

#function to call the menu
def menu():
    #print a welcome message to the user
    slow_print("Hello, welcome to the dungeon!")
    slow_print("I hope you enjoy your stay.\n")
    #show a little graphic to spruce up the menu(I am not very good at ascii art so I chose something simple)
    slow_print("""
         /\ 
        /  \ 
       |    |
       |    |
       |    |
       |    |
 ___|    |___
|___      ___| 
       |    |
       |__| """)
    #print out the players options
    slow_print("""
    Play
    Scores
    Quit
    """)
    
    #get an input from player to make a choice
    choice = input("> ")
    #if they chose an item off the menu then it sends them to the related function, else it reprints the menu with a message
    if choice.lower() == "play":
        system('cls')
        play(difficulty)
    elif choice.lower() == "scores":
        system('cls')
        scores()
    elif choice.lower() == "quit":
        system('cls')
        slow_print("GoodBye!")
    else:
        system('cls')
        slow_print("INVALID COMMAND")
        sleep(1)
        menu()

def play(difficulty):
    slow_print("Start")
    slow_print("Difficulty: " + difficulty)
    slow_print("Setup")
    slow_print("Back")
    choice = input("> ")
    if choice.lower() == "start":
        system('cls')
        start()
    elif choice.lower() == "difficulty":
        system('cls')
        if difficulty == "Normal":
            difficulty = "Hard"
        elif difficulty == "Hard":
            difficulty = "Easy"
        else:
            difficulty = "Normal"
        play(difficulty)

    elif choice.lower() == "setup":
        system("cls")
        setup()

    elif choice.lower() == "back":
        system('cls')
        menu()
    else:
        system('cls')
        print("INVALID COMMAND")
        play(difficulty)

def scores():
    system('cls')
    slow_print("Not finished yet")
    input("> ")
    system('cls')
    menu()

def start():
    health = 100
    stamina = 100
    mana = 50
    armour = 0
    armour_resistance = 0
    weapon = fist

def setup():
    pass

def create_map(width, height):
    level = []
    for i in range(height):
        temp = []
        for j in range(width):
            temp.append("")
        level.append(temp)
    
    return level






def populate_map(level, width, height):
    level[0][0] = "entrance"
    level[width - 1][height - 1] = "exit"

    num1 = 0
    num2 = 0
    for i in range(width):
        num2 = 0
        
        for i in range(height):
            num = randint(0, len(rooms) - 1)
            room = rooms[num]
            if level[num1][num2] == "":
                level[num1][num2] = room
            num2 += 1
        num1 += 1



menu()

##test_map = create_map(6, 6)
##populate_map(test_map, 6, 6)

slow_print("Press enter to exit")
input("> ")