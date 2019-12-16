#importing all the other libraries and classes
from ItemsClass import *
from EnemiesClass import *
from time import sleep
from os import system
from random import randint


finished = False
enemy_counter = 0
search_map = []

# entrance = Room("Entrance", 0, 0, 0, 0, 0, "nesw")
# exit_room = Room("Exit", 0, 0, 0, 0, 0, "nesw")

x = 0
y = 0
current_room = "None"
width = 6
height = 6

def generate_search_map():
    global search_map
    search_map = []
    for i in range(6):
        search_map.append(["", "", "", "", "", ""])

def slow_print(string):
    for char in string + "\n":
        print(char, end="", flush=True)
        sleep(0.000002)

difficulty = "Normal"

rooms = ["empty_room", "great_hall", "tomb", "corridor", "armoury", "kitchen", "torture_chamber", "dining_hall"]

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


#function to call the menu
def menu():
    #print a welcome message to the user
    slow_print("Hello, welcome to the dungeon!")
    slow_print("I hope you enjoy your stay.\n")
    #show a little graphic to spruce up the menu(I am not very good at ascii art so I chose something simple)
    slow_print("""
         /\\
        /  \\  
       |    |
       |    |
       |    |
       |    |
    ___|    |___
   |___      ___|
       |    |
       |____| """)
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
        slow_print("::INVALID COMMAND:: \n")
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
        pre_game()
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
        slow_print("INVALID COMMAND")
        play(difficulty)

def scores():
    system('cls')
    slow_print("Not finished yet")
    input("> ")
    system('cls')
    menu()

def start(level, health, armour, armour_resistance, weapon):
    while finished != True:
        system('cls')
        observe()
        nesw = check_directions()
        slow_print("The available directions are: " + nesw)
        command()
        health += 1
        get_location(level)
        is_exit()
    

def pre_game():
    global current_room
    generate_search_map()
    new_map = create_map()
    #level = premade_map1
    current_room = level[0][0]
    populate_map(new_map)
    get_location(level)
    health = 100
    armour = 0
    armour_resistance = 0
    weapon = fist
    start(level, health, armour, armour_resistance, weapon)

def setup():
    pass

def create_map():
    global level
    level = []
    for i in range(height):
        temp = []
        for j in range(width):
            temp.append("")
        level.append(temp)

    return level

def populate_map(level):
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

def command():
    user_inp = ""
    while user_inp == "":
        user_inp = input("> ").upper()
    command = ""
    parameter = ""
    space = False
    for i in user_inp:
        if i == " ":
            space = True
            continue
        if space == False:
            command = command + i
        else:
            parameter = parameter + i

    if command == "MOVE":
        move(parameter)


    elif command in ["SEARCH", "LOOK"]:
        search()
    
    elif command in ["OBSERVE","DESC", "DESCRIPTION"]:
        observe()

    elif command in ["DIRECTIONS", "DIR"]:
        nesw = check_directions()
        print("The available directions are: " + nesw)

def move(parameter):
    global y
    global x
    if parameter in ["NORTH", "SOUTH", "EAST", "WEST"]:
            if parameter == "NORTH":
                if y != 0:
                    y -= 1
                else:
                    slow_print("You can not go that way")
            elif parameter == "SOUTH":
                if y != height - 1:
                    y += 1
                else:
                    slow_print("You can not go that way")
            elif parameter == "EAST":
                if x != width - 1:
                    x += 1
                else:
                    slow_print("You can not go that way")
            elif parameter == "WEST":
                if x != 0:
                    x -= 1
                else:
                    slow_print("You can not go that way")
            else:
                system('cls')
                slow_print("MOVE command does not have the parameter " + parameter)
            get_location(level)
    
def search():
    pass

def observe():
    if current_room == "corridor":
        system('cls')
        slow_print("You find yourself in a dark wet corridor, there is just enough light from the torches held\non the wall to make it through without tripping")
    elif current_room == "lcorridor":
        system('cls')
        slow_print(("You find yourself in a dark wet corridor thats shaped like an L."))
    elif current_room == "armoury":
        system('cls')
        slow_print("You found yourself in an armoury.\nHowever its really old so there isn't much left, maybe you can find a new weapon if you search the room.")
    elif current_room == "kitchen":
        system('cls')
        slow_print("You found yourself in a kitchen")
    elif current_room == "entrance":
        system('cls')
        slow_print("You awake in a brightly lit room, you need to get out...")
    elif current_room == "exit":
        system('cls')
        slow_print("You found the exit!")
    elif current_room == "great_hall":
        slow_print("You look around to see you're in some sort of hall, probably used for \nspeeches and such when this place was used.")
    elif current_room == "tomb":
        slow_print("It seems to be a tomb with a coffin in the middle, its sealed tight though,\nso don't expect anything to popout.")
    elif current_room == "empty_room":
        slow_print("Its a very bare looking room. There doesn't seem to be anything of interest.")
    else:
        input("Something broke, press enter to exit: ")

def check_directions():
    nesw = ""
    if y != 0:
        if level[x][y-1] != "":
            nesw = nesw + "North "
    if x != width - 1:
        if level[x+1][y] != "":
            nesw = nesw + "East "
    if y != height - 1: 
        if level[x][y+1] != "":
            nesw = nesw + "South "
    if x != 0:
        if level[x-1][y] != "":
            nesw = nesw + "West"
    
    return nesw

def attack(target, weapon):
    num = randint(0, 10)
    num2 = randint(0, 100)
    if num >= 0 and num <= 7:
        multiplier = 1
    else:
        multiplier = 2
    if num2 >= 80:
        multiplier = multiplier * 2
    damage = weapon.damage * multiplier
    target.health = target.health - damage
    if multiplier == 2:
        print("Critical hit!")
    if multiplier == 4:
        print("Super critical hit!")

def populate_enemy():
    enemy_pool = []
    for i in range(100):
        enemy = Imp()
        enemy_pool.append(enemy)
        enemy = Succubus()
        enemy_pool.append(enemy)
        enemy = knight()
        enemy_pool.append(enemy)
        enemy = Zombie()
        enemy_pool.append(enemy)
        enemy = Ogre()
        enemy_pool.append(enemy)
        enemy = Troll()
        enemy_pool.append(enemy)


def combat_counter():
    global enemy_counter
    if enemy_counter != 0:
        enemy_counter -= 1
    elif enemy_counter == 0:
        if difficulty == "Easy":
            enemy_counter = 10
        elif difficulty == "Normal":
            enemy_counter = 5
        elif difficulty == "Hard":
            enemy_counter = 2
        enemy_encounter()

def enemy_encounter():
    pass

def take_damage(health, armour, armour_resistance, enemy):
    num = randint(0, 10)
    if num >= 0 and num <= 7:
        multiplier = 1
    else:
        multiplier = 2
    health_damage = (enemy.damage * multiplier) / armour_resistance
    armour_damage = (enemy.damage * multiplier) % armour_resistance
    health -= health_damage
    armour.durability -= armour_damage
    if multiplier == 2:
        print("Critical hit!")
    if armour.durability <= 0:
        armour.durability = 0
        armour_resistance = 0
        print("Your", armour.name, "broke!")
    if health <= 0:
        death()

def is_exit():
    global finished
    if current_room == "exit":
        system('cls')
        observe()
        slow_print("Well done you win!")
        finished = True

def get_location(level):
    global current_room
    current_room = level[x][y]

def death():
    global finished
    print("You died, sorry")
    finished = True

menu()
slow_print("Press enter to exit")
input("> ")