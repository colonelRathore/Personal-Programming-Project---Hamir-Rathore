from main import *
from PreGameSetup import *
from DisplayMap import *
from random import *
from launch_attack import *

def TakeTurn(roll_index, player_names, num_players, player_colors, big_prov_list, provinces):
    playname = player_names[roll_index]
    print(playname + "it's your turn!")
    return playname

def Recruit_Soldiers(roll_index, player_names, num_players, player_colors, big_prov_list, provinces):
    opt = input()

def Move_Troops(roll_index, player_names, num_players, player_colors, big_prov_list, provinces):
    opt = input()

def Trade_Troops(roll_index, player_names, num_players, player_colors, big_prov_list, provinces):
    opt = input()

def Trade_Provinces(roll_index, player_names, num_players, player_colors, big_prov_list, provinces):
    opt = input()

def ChooseAction(roll_index, player_names, num_players, player_colors, big_prov_list, provinces, playname):
    print(playname + "what would you like to do? Not sure? Here are your options:")
    print("""To Launch an Attack on another player's provice, press L.
          To Recruit Soldiers from a Province you own, press R.
          To Move Troops from two provinces you own, press M.
          To Trade Troops with another player, press T.
          To Trade Provinces with another player, press P.""")
    action_chose = input()
    print("Are you sure with your choice? Press the enter key to continue, press any other key to choose another option.")
    opt = input()
    if opt != "":
         action_chose = input()
    valid = False
    while valid == False:
        if action_chose == "l":
            Launch_Attack(roll_index, player_names, num_players, player_colors, big_prov_list, provinces)
            valid = True
        elif action_chose == "r":
            Recruit_Soldiers(roll_index, player_names, num_players, player_colors, big_prov_list, provinces)
            valid = True
        elif action_chose == "m":
            Move_Troops(roll_index, player_names, num_players, player_colors, big_prov_list, provinces)
            valid = True
        elif action_chose == "t":
            Trade_Troops(roll_index, player_names, num_players, player_colors, big_prov_list, provinces)
            valid = True
        elif action_chose == "p":
            Trade_Provinces(roll_index, player_names, num_players, player_colors, big_prov_list, provinces)
            valid = True
        else: 
            print("Please enter a valid input.")
            action_chose = input()



