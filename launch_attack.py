from PreGameSetup import *
from main import *
from DisplayMap import *
from playsound import *

def Launch_Attack():
    print("You have chosen to launch an attack! Let's hope it's successful!")

def Select_Attack_Province(provinces, playname):
    print("Hello" + playname + "what province do you want to attack?")
    attack_choice = input()
    while attack_choice not in provinces:
        print("Please input a valid province!")
        attack_choice = input()
    DisplayProvinceOwner()

    return attack_choice

def Display_Province_Stats(attack_choice, provinces):
    print("What province's statistics would you like to inspect?")
    choise = input()
    while choise not in provinces:
        choise = input()


def Move_Troops_Attack(roll_index, player_names, num_players, player_colors, big_prov_list, provinces):
    opt = ""

def Select_Attacker_Province(roll_index, player_names, num_players, player_colors, big_prov_list, provinces):
    opt = ""

def Check_If_Province_Valid(roll_index, player_names, num_players, player_colors, big_prov_list, provinces):
    opt = ""

RollDice()

def Play_War_Music():
    

def Find_Roll_Sum(roll_index, player_names, num_players, player_colors, big_prov_list, provinces):
    opt = ""

def Check_Army_Ratio(roll_index, player_names, num_players, player_colors, big_prov_list, provinces):
    opt = ""

def Check_Army_Stats(roll_index, player_names, num_players, player_colors, big_prov_list, provinces):
    opt = ""

def Display_Army_Stats(roll_index, player_names, num_players, player_colors, big_prov_list, provinces):
    opt = ""

def Check_Highest_Roll(roll_index, player_names, num_players, player_colors, big_prov_list, provinces):
    opt = ""

Play_War_Music()

def Find_Roll_Diff(roll_index, player_names, num_players, player_colors, big_prov_list, provinces):
    opt = ""

def Transfer_Province(roll_index, player_names, num_players, player_colors, big_prov_list, provinces):
    opt = ""

RollDice()

def Check_Roll_Num(roll_index, player_names, num_players, player_colors, big_prov_list, provinces):
    opt = ""

def Change_Army_Stats(roll_index, player_names, num_players, player_colors, big_prov_list, provinces):
    opt = ""
