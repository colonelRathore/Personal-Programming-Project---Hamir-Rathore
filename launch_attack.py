from PreGameSetup import *
from main import *
from DisplayMap import *
from playsound import *
from TakeTurn import *
from random import *

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
    print(f"You chose {choise} to attack! Good luck!")

    return choise

owns = DisplayProvinceOwner(choise)

print(f"The province you have decided to attack is owned by {owns}.")


def AttackRollDice(playname):
    choice1 = input("Press r to roll the dice the first time!!")
    while choice1 != "r" or "R":
        print("Please press r.")
        choice1 = input()
    choice2 = input("Press r to roll the dice the second time")
    while choice2 != "r" or "R":
        print("Please press r.")
        choice2 = input()

    return choice1, choice2

def sumAttackRoll(choice1, choice2):
    sum_attack = choice1 + choice2
    
    return sum_attack

def DefendRollDice(own):
    choice1 = input("Press r to roll the dice the first time!!")
    while choice1 != "r" or "R":
        print("Please press r.")
        choice1 = input()
    choice2 = input("Press r to roll the dice the second time")
    while choice2 != "r" or "R":
        print("Please press r.")
        choice2 = input()
    
    return choice1, choice2

def sumDefendRoll(choice1, choice2):
    sum_defend = choice1 + choice2

    return sum_defend

def CheckHighestRoll(sum_attack, sum_defend):
    attack_bigger = True

    if sum_attack > sum_defend:
        attack_bigger = True
    elif sum_defend > sum_attack:
        attack_bigger = False
    elif sum_attack == sum_defend:
        calls = randint(1,2)
        if calls == 1:
            print("Both rolls were equal!")
            print("Attacking player, you get to call!")
            call = input("Heads or Tails")
        elif calls == 2:
            print("Both rolls were equal!")
            print("Defending player, you get to call!")
            call = input("Heads or Tails?")
        toss = randint(1,2)
        if toss == 1:
            toss = "Heads"
        elif toss == 2:
            toss = "Tails"
        
        if call == toss and calls == 1:
            print("Attacking player, you won the toss!")
            attack_bigger = True
        elif call != toss and calls == 2:
            print("Defending player, you won the toss!")
            attack_bigger = False
        elif call == toss and calls == 2:
            print("Defending player, you won the toss!")
            attack_bigger = False
        elif call != toss and calls == 1:
            print("Attacking player, you won the toss!")
            attack_bigger = True
    
    return attack_bigger


def Play_War_Music():
    playsound("leningrad.mp3")
    playsound("lmusic1.mp3")
    playsound("lmusic2.mp3")


Play_War_Music()

def Find_Roll_Diff(sum_attack, sum_defend, attack_bigger):
    opt = ""

def Exec_Battle():
    ""

def Transfer_Province(big_prov_list, playname, owns):
    opt = ""

RollDice()

def Check_Roll_Num(roll_index, player_names, num_players, player_colors, big_prov_list, provinces):
    opt = ""

def Change_Army_Stats(roll_index, player_names, num_players, player_colors, big_prov_list, provinces):
    opt = ""

Play_War_Music()