import random
from PreGameSetup import *
from colorist import Color, Effect, BrightColor, BgColor, BgBrightColor

def Gen_Prov_List(num_players):
    big_prov_list = []
    for i in range (num_players):
        big_prov_list.append([])
    return big_prov_list


def DisplayMap():
    world_map = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣄⣠⣀⡀⣀⣠⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⢠⣠⣼⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⢠⣤⣦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣟⣾⣿⣽⣿⣿⣅⠈⠉⠻⣿⣿⣿⣿⣿⡿⠇⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⢀⡶⠒⢉⡀⢠⣤⣶⣶⣿⣷⣆⣀⡀⠀⢲⣖⠒⠀⠀⠀⠀⠀⠀⠀
                    ⢀⣤⣾⣶⣦⣤⣤⣶⣿⣿⣿⣿⣿⣿⣽⡿⠻⣷⣀⠀⢻⣿⣿⣿⡿⠟⠀⠀⠀⠀⠀⠀⣤⣶⣶⣤⣀⣀⣬⣷⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣦⣼⣀⠀
                    ⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠓⣿⣿⠟⠁⠘⣿⡟⠁⠀⠘⠛⠁⠀⠀⢠⣾⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠏⠙⠁
                    ⠀⠸⠟⠋⠀⠈⠙⣿⣿⣿⣿⣿⣿⣷⣦⡄⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⣼⣆⢘⣿⣯⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡉⠉⢱⡿⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡿⠦⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡗⠀⠈⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣉⣿⡿⢿⢷⣾⣾⣿⣞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⣠⠟⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⠿⠿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣾⣿⣿⣷⣦⣶⣦⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠈⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣤⡖⠛⠶⠤⡀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠙⣿⣿⠿⢻⣿⣿⡿⠋⢩⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠧⣤⣦⣤⣄⡀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠘⣧⠀⠈⣹⡻⠇⢀⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣤⣀⡀⠀⠀⠀⠀⠀⠀⠈⢽⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⣴⣿⣷⢲⣦⣤⡀⢀⡀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣷⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠂⠛⣆⣤⡜⣟⠋⠙⠂⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⠉⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⣿⣿⣿⣿⣆⠀⠰⠄⠀⠉⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⠿⠿⣿⣿⣿⠇⠀⠀⢀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⡇⠀⠀⢀⣼⠗⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠃⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠁⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""
    return world_map
    print(world_map)

def DisplayProvinces():
    provinces = f"""{BgColor.CYAN}Alaska{BgColor.OFF}
{BgColor.GREEN}Columbia{BgColor.OFF}
{BgColor.YELLOW}Northwestern Territories{BgColor.OFF}
{BgColor.RED}Prairies{BgColor.OFF}
{BgColor.MAGENTA}Hudsonia{BgColor.OFF}
{BgColor.BLUE}Upper Canada{BgColor.OFF}
{BgColor.CYAN}Northern Quebec{BgColor.OFF}
{BgColor.GREEN}Lower Canada{BgColor.OFF}
{BgColor.YELLOW}Newfoundland{BgColor.OFF}
{BgColor.RED}Greenland{BgColor.OFF}
{BgColor.MAGENTA}Southeastern United States{BgColor.OFF}
{BgColor.BLUE}Midwest{BgColor.OFF}
{BgColor.CYAN}Great Plains{BgColor.OFF}
{BgColor.WHITE}Rocky Mountains{BgColor.OFF}
{BgColor.GREEN}Pacific Coast{BgColor.OFF}
{BgColor.YELLOW}Atlantic Coast{BgColor.OFF}
{BgColor.RED}Mexico{BgColor.OFF}
{BgColor.MAGENTA}Central America{BgColor.OFF}
{BgColor.BLUE}Colombia{BgColor.OFF}
{BgColor.CYAN}Guyana{BgColor.OFF}
{BgColor.WHITE}Peru{BgColor.OFF}
{BgColor.GREEN}Amazonia{BgColor.OFF}
{BgColor.YELLOW}Brazil{BgColor.OFF}
{BgColor.RED}Argentina{BgColor.OFF}
{BgColor.MAGENTA}Carribean{BgColor.OFF}
{BgColor.BLUE}Iceland{BgColor.OFF}
{BgColor.CYAN}Jan Martin{BgColor.OFF}
{BgColor.WHITE}Macronesia{BgColor.OFF}
{BgColor.GREEN}Iberia{BgColor.OFF}
{BgColor.YELLOW}Normandy{BgColor.OFF}
{BgColor.RED}Occitania{BgColor.OFF}
{BgColor.MAGENTA}Benelux{BgColor.OFF}
{BgColor.BLACK}Switzerland{BgColor.OFF}
{BgColor.WHITE}Western Germany{BgColor.OFF}
{BgColor.GREEN}Eastern Germany{BgColor.OFF}
{BgColor.YELLOW}Northern Italy{BgColor.OFF}
{BgColor.RED}Southern Italy{BgColor.OFF}
{BgColor.MAGENTA}Greater Austria{BgColor.OFF}
{BgColor.BLUE}Poland{BgColor.OFF}
{BgColor.CYAN}Hungary{BgColor.OFF}
{BgColor.GREEN}The Balkans{BgColor.OFF}
{BgColor.YELLOW}Romania{BgColor.OFF}
{BgColor.RED}Ruthenia{BgColor.OFF}
{BgColor.MAGENTA}The Baltics{BgColor.OFF}
{BgColor.BLUE}Scandinavia{BgColor.OFF}
{BgColor.CYAN}Anatolia{BgColor.OFF}
{BgColor.GREEN}The Causases{BgColor.OFF}
{BgColor.YELLOW}Muscovy{BgColor.OFF}
{BgColor.RED}Astrabhan{BgColor.OFF}
{BgColor.MAGENTA}Novogrod{BgColor.OFF}
{BgColor.BLUE}Eastern Muscovy{BgColor.OFF}
{BgColor.CYAN}Urals{BgColor.OFF}
{BgColor.GREEN}Western Siberia{BgColor.OFF}
{BgColor.YELLOW}Central Siberia{BgColor.OFF}
{BgColor.RED}Eastern Siberia{BgColor.OFF}
{BgColor.MAGENTA}Central Asia{BgColor.OFF}
{BgColor.BLUE}Mongolia{BgColor.OFF}
{BgColor.CYAN}Manchuria{BgColor.OFF}
{BgColor.GREEN}Xinjiang{BgColor.OFF}
{BgColor.YELLOW}Shanxi{BgColor.OFF}
{BgColor.RED}China{BgColor.OFF}
{BgColor.MAGENTA}Tibet{BgColor.OFF}
{BgColor.BLUE}Korea{BgColor.OFF}
{BgColor.CYAN}Japan{BgColor.OFF}
{BgColor.GREEN}Taiwan{BgColor.OFF}
{BgColor.YELLOW}Indochina{BgColor.OFF}
{BgColor.RED}Burma{BgColor.OFF}
{BgColor.MAGENTA}Eastern India{BgColor.OFF}
{BgColor.BLUE}Southern India{BgColor.OFF}
{BgColor.CYAN}Rajputana{BgColor.OFF}
{BgColor.GREEN}Pakistan{BgColor.OFF}
{BgColor.YELLOW}Central India{BgColor.OFF}
{BgColor.RED}Himalayas{BgColor.OFF}
{BgColor.MAGENTA}Andaman and Nicobar{BgColor.OFF}
{BgColor.BLUE}Maldives{BgColor.OFF}
{BgColor.CYAN}Lanka{BgColor.OFF}
{BgColor.GREEN}Phillipenes{BgColor.OFF}
{BgColor.YELLOW}Malaysia{BgColor.OFF}
{BgColor.RED}Sumatra{BgColor.OFF}
{BgColor.MAGENTA}Borneo{BgColor.OFF}
{BgColor.BLUE}Celebes{BgColor.OFF}
{BgColor.CYAN}New Guinea{BgColor.OFF}
{BgColor.GREEN}Western Australia{BgColor.OFF}
{BgColor.YELLOW}Northern Territory{BgColor.OFF}
{BgColor.RED}South Australia{BgColor.OFF}
{BgColor.MAGENTA}Queensland{BgColor.OFF}
{BgColor.BLUE}New South Wales{BgColor.OFF}
{BgColor.CYAN}Victoria and Tasmania{BgColor.OFF}
{BgColor.GREEN}New Zeeland{BgColor.OFF}
{BgColor.YELLOW}Micronesia{BgColor.OFF}
{BgColor.RED}Fiji{BgColor.OFF}
{BgColor.MAGENTA}Maghreb{BgColor.OFF}
{BgColor.BLUE}Western Sahara{BgColor.OFF}
{BgColor.CYAN}West Africa{BgColor.OFF}
{BgColor.GREEN}Nigeria{BgColor.OFF}
{BgColor.YELLOW}Equatorial Africa{BgColor.OFF}
{BgColor.RED}Central Africa{BgColor.OFF}
{BgColor.MAGENTA}South Africa{BgColor.OFF}
{BgColor.BLUE}Rhodesia{BgColor.OFF}
{BgColor.CYAN}Mozambique{BgColor.OFF}
{BgColor.GREEN}Madagascar{BgColor.OFF}
{BgColor.YELLOW}East Africa{BgColor.OFF}
{BgColor.RED}Ethiopia{BgColor.OFF}
{BgColor.MAGENTA}Somalia{BgColor.OFF}
{BgColor.BLUE}Somalialand{BgColor.OFF}
"""
    print(provinces)
    return provinces

DisplayProvinces()

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
        big_prov_list.insert(select, [roll_index, indx])
        roll_index += 1
        indx += 1
        if roll_index > num_players - 1:
            roll_index = 0

def TakeTurn(roll_index, player_names, num_players, player_colors, big_prov_list, provinces):
    playname = player_names[roll_index]
    print(playname + "it's your turn!")

