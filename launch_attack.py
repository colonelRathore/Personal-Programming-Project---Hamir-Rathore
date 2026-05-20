from PreGameSetup import *
from main import *
from DisplayMap import *
from playsound import *
from TakeTurn import *

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

def Display_Province_Stats(provinces, prov_with_commando):
    print("What province's statistics would you like to inspect?")
    choise = input()
    while choise not in provinces:
        choise = input()
    if choise in prov_with_commando:
        print("The province you have chosen has 2 infantry armies and one tank army.")
        print("It has at least one commando army")
    else:
         print("The province you have chosen has 2 infantry armies and one tank army.")

def Select_Attacker_Province(provinces):
    print("What province would you like to attack?")
    choise = input()
    while choise not in provinces:
        print("Please enter a valid option. Mr. Hall if you're doing this to test the robustness, hello from Hamir.")


#RollDice()

def Play_War_Music():
    playsound("leningrad.mp3")
    playsound("lmusic1.mp3")
    playsound("lmusic2.mp3")

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

Play_War_Music()