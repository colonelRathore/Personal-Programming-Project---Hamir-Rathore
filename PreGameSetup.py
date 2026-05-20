import random
from main import *
from DisplayMap import *

def GetNumPlayers():
    num_players = int(input("How many people are playing RISK today?\n"))
    return num_players

def FetchPlayerNames(num_players):
    player_names = []
    for i in range(num_players):
        name = input("What is your name?\n")
        player_names.append(name)
    return player_names

def GetPlayersColors(player_names, num_players):
    valid_colours = ["white", "black", "navy blue", "green", "red", "dark red", "purple", "orange", "yellow", "lime green", ""]
    player_index = 0
    player_colors = []
    for i in range(num_players):
        color = input((player_names[player_index]), ", what 16-bit color do you want?\n")
        player_index += 1
        while color not in valid_colours:
            color = input("Please enter a valid color:\n")
    player_colors.append(color)
    player_index = 0
    return player_colors, player_index

def RollDice(num_players, player_names, player_index):
    rolls = []
    for i in range(num_players):
        roll_go = input("Hello", (player_names[player_index]), "press r to roll your dice! ")
        if roll_go == 'r':
            roll = random.randint(1,6)
        print((player_names[player_index]), "you rolled", roll)
    rolls.append(roll)
    player_index += 1
    return rolls

def CheckHighestRoll(rolls, player_names):
    roll_sort = rolls.sort()
    max_roll = roll_sort[0]
    for roll in rolls:
        if roll == max_roll:
            roll_index = roll.index(max_roll)
    print((player_names[roll_index]), "you got the highest roll!")
    return roll_index

def Gen_Prov_List(num_players):
    big_prov_list = []
    for i in range (num_players):
        big_prov_list.append([])
    return big_prov_list

def ClaimProvince(roll_index, player_names, num_players, big_prov_list, provinces):
    roll_index = 0
    indx = 0
    while provinces != """""":
        DisplayMap()
        DisplayProvinces()
        print("The game has begun!", (player_names[roll_index]), ", what province do you want?")
        select = input()
        while select not in provinces:
            print("Please select a valid province:")
            DisplayProvinces()
            select = input()
        big_prov_list = [[]]
        big_prov_list.insert(select, [roll_index, indx])
        roll_index += 1
        indx += 1
        if roll_index > num_players - 1:
            roll_index = 0
    return big_prov_list, roll_index, select

def Init_Move_Troops(big_prov_list, provinces):
    print("Each province starts with 2 infantry armies, 1 tank armies, and 0 commando armies")
    print("Each player has 3 commando armies in reserve")
    choise = input("If anybody would like to move these armies out of reserve, please type in M")
    if input == "M":
        print("Which province would you like to move this army to?")
        mo_choise = input()
        while mo_choise not in provinces or big_prov_list:
            mo_choise = input("Please enter a valid input! ")
    prov_with_commando = []
    prov_with_commando.append(mo_choise)