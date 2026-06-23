import random

global player_names, player_colors

# ANSI Colors 
class BgColor:
    CYAN = "\033[46m"  
    OFF = "\033[0m"     # Reset color

COLOR_AVAILABLE = True

class Colors:
    RESET = "\033[0m"
    CYAN = "\033[46m"      # Background cyan
    RED = "\033[41m"       # Background red
    GREEN = "\033[42m"     # Background green
    YELLOW = "\033[43m"    # Background yellow
    BLUE = "\033[44m"      # Background blue
    MAGENTA = "\033[45m"   # Background magenta
    WHITE = "\033[47m"     # Background white

# Map player color names to ANSI codes
COLOR_MAP = {
    "red": Colors.RED,
    "green": Colors.GREEN,
    "blue": Colors.BLUE,
    "yellow": Colors.YELLOW,
    "cyan": Colors.CYAN,
    "magenta": Colors.MAGENTA,
    "white": Colors.WHITE,
    "default": Colors.CYAN
}

try:
    from playsound import playsound
    SOUND_AVAILABLE = True
except ImportError:
    SOUND_AVAILABLE = False

PROVINCES = [
    "Alaska", "Columbia", "Northwestern Territories", "Prairies", "Hudsonia", "Upper Canada",
    "Northern Quebec", "Lower Canada", "Newfoundland", "Greenland", "Southeastern United States",
    "Midwest", "Great Plains", "Rocky Mountains", "Pacific Coast", "Atlantic Coast", "Mexico",
    "Central America", "Colombia", "Guyana", "Peru", "Amazonia", "Brazil", "Argentina", "Carribean",
    "Iceland", "Jan Martin", "Macronesia", "Iberia", "Normandy", "Occitania", "Benelux",
    "Switzerland", "Western Germany", "Eastern Germany", "Northern Italy", "Southern Italy",
    "Greater Austria", "Poland", "Hungary", "The Balkans", "Romania", "Ruthenia", "The Baltics",
    "Scandinavia", "Anatolia", "The Causases", "Muscovy", "Astrabhan", "Novogrod", "Eastern Muscovy",
    "Urals", "Western Siberia", "Central Siberia", "Eastern Siberia", "Central Asia", "Mongolia",
    "Manchuria", "Xinjiang", "Shanxi", "China", "Tibet", "Korea", "Japan", "Taiwan", "Indochina",
    "Burma", "Eastern India", "Southern India", "Rajputana", "Pakistan", "Central India", "Himalayas",
    "Andaman and Nicobar", "Maldives", "Lanka", "Phillipenes", "Malaysia", "Sumatra", "Borneo",
    "Celebes", "New Guinea", "Western Australia", "Northern Territory", "South Australia",
    "Queensland", "New South Wales", "Victoria and Tasmania", "New Zeeland", "Micronesia", "Fiji",
    "Maghreb", "Western Sahara", "West Africa", "Nigeria", "Equatorial Africa", "Central Africa",
    "South Africa", "Rhodesia", "Mozambique", "Madagascar", "East Africa", "Ethiopia", "Somalia",
    "Somalialand"
]

# Basic Adjacency Logic (RISK-style connections)
ADJACENCY = {
    "Alaska": ["Northwestern Territories", "Pacific Coast"],
    "Columbia": ["Alaska", "Northwestern Territories", "Pacific Coast"],
    "Northwestern Territories": ["Alaska", "Columbia", "Prairies", "Hudsonia"],
    "Prairies": ["Northwestern Territories", "Great Plains", "Hudsonia"],
    "Hudsonia": ["Northwestern Territories", "Prairies", "Upper Canada"],
    "Upper Canada": ["Hudsonia", "Northern Quebec", "Lower Canada"],
    "Northern Quebec": ["Upper Canada", "Lower Canada", "Newfoundland"],
    "Lower Canada": ["Upper Canada", "Northern Quebec", "Atlantic Coast"],
    "Newfoundland": ["Northern Quebec", "Greenland"],
    "Greenland": ["Newfoundland", "Iceland"],
    "Southeastern United States": ["Atlantic Coast", "Midwest"],
    "Midwest": ["Southeastern United States", "Great Plains"],
    "Great Plains": ["Prairies", "Midwest", "Rocky Mountains"],
    "Rocky Mountains": ["Great Plains", "Pacific Coast"],
    "Pacific Coast": ["Alaska", "Columbia", "Rocky Mountains"],
    "Atlantic Coast": ["Lower Canada", "Southeastern United States"],
    "Mexico": ["Pacific Coast", "Central America"],
    "Central America": ["Mexico", "Colombia"],
    "Colombia": ["Central America", "Guyana"],
    "Guyana": ["Colombia", "Brazil"],
    "Peru": ["Colombia", "Amazonia", "Brazil"],
    "Amazonia": ["Peru", "Brazil"],
    "Brazil": ["Guyana", "Peru", "Amazonia", "Argentina"],
    "Argentina": ["Brazil"],
    "Carribean": ["Mexico", "Atlantic Coast"],
    # Europe / Asia connections (simplified)
    "Iceland": ["Greenland", "Scandinavia"],
    "Scandinavia": ["Iceland", "The Baltics"],
    "The Baltics": ["Scandinavia", "Poland", "Muscovy"],
    "Poland": ["The Baltics", "Eastern Germany", "Ruthenia"],
    "Muscovy": ["The Baltics", "Novogrod", "Eastern Muscovy"],
    # Add more as needed for basic gameplay
    "China": ["Mongolia", "Xinjiang", "Tibet", "Indochina"],
    "Japan": ["Korea"],
    "Australia regions": ["New Guinea", "Western Australia", "Queensland"]  # grouped for simplicity
}

class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color.lower() if color else "default"
        self.ansi_color = COLOR_MAP.get(self.color, Colors.CYAN)
        self.provinces = []

class Province:
    def __init__(self, name):
        self.name = name
        self.owner = None
        self.infantry = 2
        self.tank = 1
        self.commando = 0

# ==================== DISPLAY ====================
def load_soldiers():
    print(BgColor.CYAN + """     ░         ▒▒░    ░▒░                                                                                                                                        
    ░░        ▒▒░░  ░▒░░░                                                                                                                                        
   ░░░░ ▒░    ░░░    ░                                                                                                                                           
  ░▒▒▒▒░     ░░░░      ░░                                                                                                                                        
  ░▒▓░     ░ ░░░░      ░░            ░░░░░░░░░░                                                                                                                  
 ░░ ░░░   ░░░░░░░░░     ▒░         ░▒▒▒▓▒▒▓▓▒▒▒▒▒░                                                                                                               
░░      ░  ░░░░ ░░░░░            ░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░                                                                                                              
░░      ░  ░░░░░▒▒▒░░            ▒▓██████▓▓▓▓▒▒▒▒▒▒▒                                                                                                             
░         ░░░░░░▒▒░░░           ▒▓▓███▓▓▓████████████▓                                                                                                           
░        ░░░   ░▒▒░▒░           ▒▓█▓▓█████████████████▒                                                                                                          
░ ░     ░░░░ ░ ░░░░▒░           ░▓▓███████████████████                                                                                                           
        ░░░░░░░░░░░▒░            ▓████████▓▓▓█▓▓▓░▓██                                                                                                            
       ▒░░░░░░░ ░░░░            ░████████▓▓▒▒▒▓▓▓▒░▓                                                                                                             
      ▒▒░░░░░░░░░ ░░░░           ██████████▓▓▓▓██▓▒                                                                                                              
░ ░░░▒▒▒░░░░░░░░░░░░▒░         ░▓█████████████▓▓▓▒                                                                                                               
  ░░▒▒▒░░░░░░░░░░░░░░         ▓▓▒████████████▓▓▓▓░                                                                                                               
░░░░▒▒▒░░░░▒░░░░░░░░░        ▒█▓█████████████████░                                                                                                               
░░░▒▒▒▒▒▒▒▒▒░░░░░░░          ▓██████████████████▓░░░                                                                                                             
░░▒▒▒▒▒▒▒▒▒▒░░░░░░░    ░▒▒▒▒▒▓██████████████████▓░▒▒▒▒                                                               ░░░░░░                                      
████▓▓▓▓▓░▒▒░░░░░░░  ░░▒▒▒▒▓████████████████████▓▒▒▒▒▒▒▒▒░                                          ▒▓▓▓      ░▒▒▒░░░                                            
███████▓▓▓▓▒░▒░░░░░░░▒▒▒▒▓▓████████████████████▓▓▒▒▓▓▓▓▓▓▓▒▒                                  ░▒▓▓▒▒▒▒▒▒░▒▒▒░░                                                   
█▓▓▒▒▒▒▒▒▒▒▒▒░░░░▒░▒▒▒▓▓▓█████████████████████▓▓▒▓▓██████▓▓▒▒                         ░▒▒▓▓▒▓▒▒▒▒▒▓▓▓██▓                                                         
▓▓▓▓▒▒▒▒▒▒▒░░░░░▒▒▒▓▓▓█████████▓███████▓█████▓▓▒▒▒▓▓██▓███▓▓▓▒                ░░▒▒▓███████▓▓░▓██▓▓▒                                                              
▓▓▓▓▓▒▒▒▒▒▒▒░░░▒▒▓▓▓▓████▓▓▒▓▓▒▒▒▓▓▓▒▓▓██▓▓▓▓▓▒▒▒▓▓▓▓▓▓██▓▓▓▓▓▓▓       ░▒▒▓▓█████████▒░                                                                          
▓▓▒▒▒▒▒▒▒▒░░░░▒▓▓▓▓████████▓▓▒▒▒▒▒░░░░░▒▒▒▒▓▓██▒▒▒▒▒▒▓████▓▓▓▒▓▓▒▒▒▒▒▒▓██████▓▒░                                                                                 
▓▓▒▒▒▒▒▒▒▒░░░░▓██████████▓▓▓▒▒▒▒▒▒▒▒▒▒░▒▒▒▓▓▒░░▒░░░░░▒▓▒▒▓▓▓▓▒▒▓▒▓▓███▓█▓░                                          ▒▒░░░                                        
▒▒▒▒▒▒▒▒▒▒░░▒▓███████████▓▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒░▒▒▓▓▒▒▓██████████▓░█▓░                                      ▒██▓▓▓▓▓▓▒▓▓▒                                     
▒▒▒▒▒▒▒▒▒▒▒▒▒█████▓▓█████▓▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▓█▓▓▓▓███████   ▓█░             ▒▒▒▒▒▒▒▒                 ▓█████▓▓▓▓▓██▓▒                                    
▓▓▓▒▒▒▒▒▒▒▒▒▓██▓▓▓▓███▓▓▓▓▒▒░▒▒▒▒▒▒▒▒░░░▒▒▒░░░░░░░░▒▒▒▒▓▓▓████████▒░▓▓            ▒▓▓▓▓▓▓▓▓▒▓▒▒▒             ▓██████████████▓▒                                   
▓▒▒▒▒▒▒▒▒░▒▓█████████▓█▓▒▒▒▒▒▒▒▒▒▒░░▒░░▒▒░░░░ ░░░░░░▒▒▒▓▓▓██████▒░▓█▓           ░▓▓█▓▓▓▓▓▓▒▒▒▒▒▒▒░          ░▓▓████████▓▓▓▒▒▒▒░                                  
▓▒▒▒▒▒▒▒▒▒▒███████████▓▓▓█▓▓▓▓▓▒▓▓▓▒▒▒▒░▒░░░░░░░░░░░░▒▒▒▒▓██████▓▓██░          ░▓▓███▓▓▓▓▓▒▒▒▒▒▒▒▒▒         ░▓█████▓▓▓▓▓███▓████░                                
▓▓▒▒▒▒▒▒▒▒████████████▓███▓███▓▓▓▓▓▓▓▒▒▒▒▓▒▒▒░░░░░░░░░░▒▒▓█████████▒▒          ▓██▓███▓▓▒▒▒▒▒▓▓▓▓▓▒▒         ▓██▓▓█████████████                                  
████▓▒▒▒▒▓█████████████████████▓▓▓▓▒▒█▓▒▒▒▒▒▒░░░░▒░░░░░▒▒█████████▓▓▒          ▓█████████████████████▒       ▒▓████████▓▓▓▓▓▒▓▓                                  
█████▒▒▒▒███████████████▓██████▓▓███████▓██████▒░░▒░░░░░▒██████████▓▒          ▓██▓████████████▓▓████▒       ████████▓▒▓▒▒▓▓▒░                                   
██████▓░   ░███████████████████████████████████▓▒░▓▒▒▒░░▒█████████▓▓░          ▓▓▓██████▓▓▓▓███▒████▓       ▒▓███████▓▓▓██▓█▒                                    
▓▓█▒▒█▓    ▒█████████████████████▓▓████▓▓██████▓▒▒█▓▒▒░░▓█████████▓▓           ▒███████▓▒▒▒░▒▒▒▒▒▒█▒       ░▒▓███████████▓▒▒                                     
▒▒▒▓▓▒     ▒▓▓███████████████████████░▒▓▓▓▓████▓▓▓███▒▒░▓████████▓▒            ███████▓▓▓▒▒▒▒▓██▓░     ▒▒▓▒▒▓▓████████████▒                                      
▓▒▒▒▓▒▒    ▒▒▓█████████▓▓▓█▓████████▒▓▓▓▓███████▓▒█████████████▓▒░            ▒▓██████▓▒▓▒▒▒▒▒▒░░  ░░▒▒▓▒▒▓▓██████████████▒▒░▓█                                  
▓▓▒▒▒▒▓▒░  ▒▓████▒████▓▒▒▒▒▒▒▒▓████▓████████████▓▒██████████▓▒▒▒▒             ▓█████████▓▓▒▒▒▒▓█▒ ░░▒▒▒▒▒▒▒▓████████████▒█▓▒▓▓▒▒▒                                
▓▒▒▒▒▒▓▓▓▒ ░█▒    ░████▓▒░░░░▒▒▒▒▓▓█████████████▓▒█████████▓▓▓██▒░░          ▒▒▓▓███████████▓▒▒▒░ ░░▒▒▒▒▒▓▓▓██████████▒███▓▒▒▒▒▒▒▓░                              
▓▓▓▓▓▓▒▒▒░         ▒█████▓▒▒▒░▓█████████████▓▓▓█▒▒█████████▓▓▓██▓░          ▓▓▒▒▒▒▓▓██████████▒   ░░▒▒▒▒▒▒▓█▓▓▓▒▒▒▓▓█▒████▓▒▒▒▓▒▓▓▒                              
▒▒▓▓█▓▒▒▒▒          ▓█████████████████████████▓▓▓▓█████████▓▓██▓▓█▓        ░▒▓██▓▓▓▒▒▓█████████▒░░░░▒▒▒▒▓▓▓██▓██▓▓▒▒██████▓▓▓▓███▒▒▒░                            
▒▒▒▒▒▒▓▓█▓▓░         ▒▓███████▓▓█████████▓██▓█▓▓▒▒▓█████████▓█████░       ▒░░░▒▒▓████▒░▒▓██████▒▒▒░▒░░░▒▓█▒▒▓▓█▒▒▒██▒▒▒▓████▓▓██▓▒▒░░░    ░░ ░░░░░░▒░     ░░▒▒▒▒▒
▒▒▓▓▓▓▓█████▓▒         ▒▓████████▓▒▓▓▓▓▓██▓▓▒▓▒▒░▓███▓▓▒▓▓▓▓████▓▒     ░▒▒░░░░░▒▒▒▒███▓▒░▒▓▓▓██▒░░░▓▓▒▒▒▒▒▓█▓█▓▓▓███▓▓▓▒▓██▓░  ░▓▓▒▓▓▓▒▒▒░░░▒▒░░░░░▒▒███▒▓▒▓█████
██▓▓▓████▓▓█▓▓▒    ░▒▒▓██████████████▒▒███████▓▒░▓▒▒▒▒▒▒▒▒▒▒▒█▓▒▒    ░▒▒▒░░░▒▒░░▒█▒▓▓███▒░░░▓██▒░░░░█▓▓▒▒░░▒  ▒██▓▒▓▒ ░░░░  ░░░ ░▒▒▒▒▒▒▒░░░░░░░░░░▒▒▓██▒▓▓▓▓▒▓▒▒▓
▓▓▓▓▓▓▓███▓▓▓▓▓░▒▓▓▓▓▒▓▓▓████████████▒████▓█▓▒▒▒▒▒▒▒▒▒▒▒▓▓████▒     ▒▒▓▒░ ░░ ░▒▒▒▓▒▒▓▓████▓▒▒██▒▒░▒░████▓▒▓▓█▓▒▓░░░░ ░░░░▒░░▒▒▒░▒▓▓▒▒▒▓▓▓▓▓▓▒▓███████████▓███▓███
▓▓▓██▓▓▓▓▓▓▓▓▓▓▓█▓▓▒▒▓▓███▓█████████▒▓█▓▓▓▓██▒▒▒▒▒▒▒▒▓██▓▓▓▓▒▒░    ▒▒▒▒▒░░░░░░▒▒▒▒░▒▒▓▒▒▒▓█████░▒▒  ▒███▓▓█████▓   ░░▒░░░▒░▓█▓▓▓███████▓▒▒▓▒▒▒▓█▓▓███████▓▓████▒ 
▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▒▒▒▒▓████▓█▓▓▓▓███▒▒▓███████▓▓▒▒▓▓▓███▓▓▒▒▒▒░    ▒▒▒▒░░░░▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒█▓▒█▓██▓█▒▓▒▒▓█████▒░▒░▒░   ░░░▒███▓██████████▒▓█████▓▓██████████     
▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓░ ▒▓██████▒▓▓▓██████▒▒▓███████▓▓▒▓████▓▓▓▓▓▓▒▒░    ▒▓▒▒▒▒░░░░░░░░░▒▒▒▒▒▒▒▒▒▓▒▒▒█▓▒▓▓▒▒▓██████▒▒▒▒▒▒▒█▓▒░▒▒▓██▓░▒ ▒███████████████▓▓▓███████▒      
▓▓▓██▓▓▓▓▓▓▓▓▓▓▓  ▓██████▓▓▓▓▒▒▓▓▓▓▓▓▓▓█▓▓██▓▓▒▒▓██████▓▒▒▒▒▒▒░   ▒▓▒▒▒▒░░░▒▒▒▒░░░▒▒▒▓██▓▒▓▓█▓▓█▓▓▒▒▓█████▒▓████▒█▓▓█▒▒██▒▒       ░█████████████████████▒        
▓▓▓▓██▓▓▓▓▓▓▓▓▓▓░  ▒█████▒▓▓▓▓▓▓▓▓██▓███████▒▓▓▒▒███▓▓▓▒▒▒▒▒▒▒▒   ▒▓▒▒▒▒▒░░▒▒░░▒▒░▒▓▓▓█▓▓▓▓███▒█▒▒▓█████▓███████▒ ▓▒▓█▓▒▒░▒▓░▓██████▓██████████████▓             
▓▓▓▓███▓▓██▓▓█▓▓░       ░▓▓█▓▓▓▓▓███▓███████▓░▒▒░   ░▒███████▓▒   ░▓▒▒▒▒░░░░░░ ░ ░▒█▓▒▓██▓▒████▒▒▓████████████████▒ ░▓▓▒▓██▓▓██▒▒▒▒▒████████████▒                
▓▓▓▓▓▓▓███▓▓▓▓▓▓▓▒      ░▒▓▓▓▓▓▒▒▒▒▒▒▒▒▒▓▓▓▒░   ░▒▒▒▓██████▓▓▓▓░   ▒▒▒▒▒░░░   ░▒████▓▒▓███▓▒▒░▓▓▓▓██████████████████▒ ▒████████▓▓▒▒▒▓████████████▒        ░░░    
█▓▓▓█▓▓▓▓▓▓▓▓▓█▓▓▓      ░▒▒▒▒░░░░░░░░░▒▒▓▓▒░ ░▒▓▓███████▓▓▓▓▓█▓▒   ▓▒▒▒▒░ ░▒▓██▒▒▒▓▒░░░▒░   ▒▒░▒█▓███████████████████▓░ ██████▓▒▒░░░░░▓█████████▓▓      ░▒▒▒▒    
████▓▓▓▓▓▓▓██▓▓▓▒▓▒░░░░░░▒▒▒▒▒▒▒▒░▒▒░▒▒░░ ░░▒▓███████▓▓▓▓▓▓▓▓▓▓▒▓▓▒▓▓▓▒▒░▒█▒░▒▓░▒▓▓  ░░░   ░▒▒▒▓▓██████████████▓▓▓▓████▒ ░███▓▓▒▒▒▒▒▒░░██▓▓█████▓▓▒     ▒▒▒▒▓▓▓▓█
███▓████▓▓▓▒▓██▓▓▓▒░▓█▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▒▒▓█▒███████████▓▓▓▓▓▓▓▓▓▒▓▓▓▒░▒▓▒▒▒▒▒▒▒▓▒▒░░   ░░▒▒▒▒███████████████▓▓▓▓▓▓██▓▓▓░ ▓█▓███▓▒▒▓▓▓▒▓▓▓██████▓▒    ░▒▒▓▒▒▓▓▓▓
████▓██▓▓▓█▓▓▓█▓▓▓▓▓▓▒▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒█▒████████████▓▓▓▓▓▓▒▒▓▓█▓▒▒▓▓▒▓▓▓░▒▒▓▓░░░▒▒▒▓█▓▓▓███████▓▓▒▒▓▓▓███▓███████▓██▓ ░▓████▒▒▓▒▓█▓▒███████▓▒  ░▒▒▓▓▒▓▒▒▒▒▒
█████▓▓▓▓▓▓▓▓▓▓██▓▒▓▓▓█████████▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓█████████▓▓▓▓▓▓▓▓▒▓█▓▓█▓▒▒▓█░▒█▓██▓▒▓░▒▓███████████████████████████████████████░▓███████████████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒
██▓▓▓▓▓▓▓▓▒▓▓▓▓▒▒▒▓▓▒████████████▓▓▓▓▓▓▓▓▓▓▒▒░▒█████████▓▓▓▓▓▓▓▒█████▓▒▒▓█▓█▓█████████▓▓██████████████████████████████████████░░██████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓████████▓▓▓▓▓▒▒▒▒░▒▒░░░░░▒███████████▓▓▓▓▓▒▒▓████▓▓██▓▓▓████████████████████▓▓████████████████████████████▓ ▒███████████▓▓▓▓▒░░▒▓▓▒▒▒▒▒▒▒▒▒▒
█▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓██████▓▒▒▒▒▒▒░░░░▒▒▒▓▓▓▒▒▓██████████████▓▓▓▒▓▓▓██████████████████████████████▒▒█████████████████████████████▒ ▓███████████▓▓██▒▒▓▒▒▒▒▒▒▒▓▓▒▒
▓▓▓▓▓▓▓▓▓▓▓██▓█▓▓▓▒▓▒██▓▒██████████████████████▓███████████████▓▓▓▓▓▓██████████████████████████████▒▒▓█████████████████████████████▓█████████████▓▒▒▒▒▒▒▒▒▒▒▓▓▓▒▒
█▓▓██▓▓▓▓██████▓▓▓▓▓▒▓▓████████████████▓▓▓███▓▓██▓██████████████████████████████████████████████████████████▓███████████████▓░░░█████████████████▒▓▒▒▒▒▒▒▓▓▓▓▓▓▓▒
▓▓▓███▓▓▓▓██▓▓██▓▓▓▓███████████████▓▓▓▓▒░▒▒▒▓▒▓███▓▓▓███████████████████████████████████████▓███████████████▓██████████████▓▒░░░░ ▒██▒██████████▒▒▓▓▓▒▒▒▒▒▓▓▓▒▒▒▒
▓▓█▓██▓▓▓█▓▓▓▓▓██▓▓▓▓▒█████████▓▓▒░░░▒▓▒ ░░▒▓█████████▓▓████████████████████████████████▓▓▒▓█▓▒▓███▓██████▓█▓▓█████████████▓░▒▓███████▒░░░░░▒▒▒▓▒▒▒▒▓▒▒▒▓▓▓▒▒▒▒▒▒
██████████▓██▓▓█▓░   ▒██████████▓▒▒░▒▓▓▓▒▒▒▓███▓████████▓██▓▓████████████████████████▓▓▓▒▒▒▒░░░░░░████████▒▒░▓████████████▓▒▓███▒▒▒▓██▓▓▓██████▓▒░▒░░▒▒▒░░░░░░░░▒
█████▓█████▓▓▓▓▒░░░▒░▓███████████▓▒▒▒▒▒▒▒▒▒█▓▓▓█████████████████████████████████████▓▓▒▒▒▒▒▒░░░░░░░░▒████▓▒▒▒▒▒▓▒████████▓▓▓▓▓▓▓▒▒▒▓██▓▒▒▓████▓░░░▒▒▒░░░░░░▒░▒▒▒▒
██████████▓▓▓▓▓▓▒▒▒▒▓▓████████████▓▓█▓▓▒▒▒██▓▒████████████████▒▒▓█████████████████▓▓▓▒▒▒▒▒▒▒▒░░░░░  ░▒▒▓██▓▓▓▒▒▒███▓▓▓▓▓▒▒▓▓█████▓▒▒░░░▒▒▓▓███▓░░░░░▒░░▒▒▒▒░▒▒▒▒▒
▓▓██████████▓▓▓▓▓▓▓███████████████████▓▒▒░░░░▓▓▓▓█████████████▒▓█████████████████████▓█▓░░ ░░ ▒▓████▓▒▓█████▒▒▒▓▓▓▓▓▓█████▓▓▓▓▓▒▒▒▒▒▒░▒░░███▓▒░▒░░▒▒▒▒▒░▒░░░▒▒▒▒▒
█▓▓▓▓▓▓█████▓▓▓▓█▓██████████████████▓▓▓█▓░░░░   ░▒▓███████████▒▒▒▓███████████████▓▒░░░░▒▒▒▒▓▓▒▓▓▓███▓▒▒▒░▒▓▓████████▓▓▓▓▓█▓▓▓██▓▒▒▒▓▓███████▒▓▒▒▒▒░░▒▒▒▒░░▒▒▒▒▒▒▒
████▓▓███████▓▓▓██████▓▓███████████████▓▒░░░░▓▒▓██▓██████████▓▒▒▒▓▓█████▒▒▓▒░░░░▒▒▓▓▓▓█████████▒▒▒▓█▓█████████▓█▓▒▓███▓▓▓█▓▓▓▓█████████▓▓▒▓▓█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
█████▓█▓▓▓▓▓▓▓▓▓▓▓▓▓█▓█▓▓█████████████▓▒▒░░░░▒░░░▒▓██████████▒▒▒▒▒▒▒▒░░░░░░▒▓▓█████████████████▓▓▓██████▓▓███▓▒▒▓▒▒███████▓██████████████████▓░░░░▒▒▒▒▒▒▒▒▓▓▓▒▒▒▒
█▓█▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓█▓█▓▓▒█████████▓▓▓▒▒░░░░▒▒░▒░ ░█████▓▒▒▒░░░░▒▒▒▓▓▒▒▓███████████████████████████████▒▒████▓▒▒░▒░▒▓██████████████████████▒▓▒░    ▒██▓▒▒▒▒▒▒▒▒▒
▓██▓▓██▓██▓▓▓▓▓▓▓█████▓██▓▓████████▓█▓▒▓▒▒▒▒░▒▒▒▒▒▒▒▒▓▒░░▒▒▒▓▓▓▓▓▓▓▓▓████████████████████████████████████████▓▓▓▒▒▒░░▒███████████████▓█████████▓▒▒▒░░  ▓▓▒▒▒▒▒▒▒▒▒
█▓██▒▒▓▓▓▓▓▓▓▓███▓▓▓██▓██▓▒▓██▓▓███▒▓▓▒██▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▓▓▓███████████████████████████████████████████████████▓▓▒▒░▒█████████▓██▓▓███▓▓▓▓▓██▒░░▒▓▓▓▒▒██▓▓▓▒▒▒▒▒
██▓▓▓██▓█▓▓▓▓█▒▒▓██▓▒█████▓▒█████▒▒▒▓░▒▓▒▒░▒▓█▓▓████▓▒▒███▓▓████████████▓▒████▓█████████████████████████████████▓▓▒▓░ ▓██████▓▓█▓▓▓▓███▒▒░▒▒▓█▓▓█▓██▓▓████▓██▓▒▒░
██▓██████████▒▒▒▓██▓▓▓█▓██████▓▒▒▒▒░░▒▒▒▒▒▓████▓▒▓▓▓▓▒▓███▓▓▒███▓████████▒░████████████████████████████████████▓▓▒░░░   ▓████▓▒▒▓▓█▓▓▓▓▓▒▒▒▒▓▓▒▒▒▓▓▓▒▒▓██████▓█▓▓
▓██▓▓▓▓▓▓▓█████████▓▓▓███████▓██████▓▓▓▓█████████▓▒▒▓███████▓▓▓▓█████████▓░▒██▓▓▓▓██████████████████████████████▓▓▒░░░░░ ░░▒██▓▒▒▒▒██▓████▓▓▓▓▒▓▒▓▓▒▒▓█▓▓▓▓█████▓
███▓▓▓▓▓▓▓█████████████████▓█████████████████████▓▓▓█▓▓▓█████▓████████████▒▒██▓█████████████████████████████████▓▓▒░░░░░▒▒▒███▓▒▒▒▒▒████████▓▒▒█▓▒▒▓▒▓█▓▓█████▓▓█
███▓▓██▓███████████████████▓▓████████████████████▒▓▓▓▓▓▓▓▓▓▓█████▓██████████████████▓▓▓▒▓███████████████████████▓▒█████▓▓▓█████▒▒▒▒▒▓███████████████████▓█▓▓█▓▓██
▓▓██▓▓▓▓▓▓███████████████████████████████████████▓▓████████▓▓▓▓▓███████████████▓▓▒▒▒▓▒▒░▒███████████▓▓██████████▓▓█████████████▓▒▒▒▒▒█████▓▓▓▓█▓▓████████▓▓▓▓█▓▒▓
█▓██▓▓▓▓▓▓▓▓▓▓▓█████████▓▒▒▒▓▓████████████████████████████▓▒▓███████████████████▓▓▓▓▓▓▓▓▓▓█▓██████████▓▓▒▒▒▓████████▓███▓▒██████▓▒▒▒▒▓████████▓█▓▒▓██████████████
████▓▓▓▓▓██████████████████████████████▓▒▒▒▒██████████████▓▒░▒█████▓▓████████████████████████████▓▓▓▒▒▒▒▒▒▒▒░▒▒▒▓▓▓█▒▓▓▓▓████████▓▒▒▒▓█▓▓▓▓▓▒▓▒▓██▓▓█▓███████████
▓▓▓██▓▓▓▓▓▓██████████████████████████░░░░░░ ░▒▒▒▒▓█████████▓▓█▓███▓█████████████████████████▓▓▓▓▓▓▓▒▒▒▒░▓██▒▒▒▒░▒░▒▒▒░░▒░░░░░░▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓█▓▓████▓▓███▓███████
▓███▓▓▓▓▓▒▒▓████████████████████████▒░░░░░░░▒▒▒▒▒░░▒░░▒▒▒▓█▓▒█▓███▓▓▒▒▒▒▒▓████████████████▓▓▓▓▓▓▓███▒▒▒▒▓█▓▓▒▓███▓▓▓▓▓▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▓▓▓█▓███████
▓▓▓▓▓█▓▓▓▒▓▓▓▓████████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░ ░░░▒█▓███▓█▓▒▒▒▒░▒▓████████████████▓▒▒▒▒▒▓█▓▓▒▒██████▓██████████████▓▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▓▒▒▒
▓▓▓▓▓██▓▓▓▓▓▒▒███████████████▓▓▓▒▓█▓▓▒▓▓▒▓▓▓▓▒▓▒▒▒▒▒▒▒░░░░▒▒▒▓██████▓▒░▒▒▒▒▒▓███████████████▓▒▒▓▓▒▒▒▒▒▓▒▒▒▓█████▒▓█████▓▒▓████████████████▓▓▓████████████████▓▓▓▓
▓█▓▓▓▓▓█▓▓▓▓▓▓▓██▓████████████████▓▓▒▓▓▒▓▓█▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▓████████▒▒▒▒▒░▒░░░▒▓███▓██████▓▓▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓██▓▒████▓▓████████████████████████████████████████""" + BgColor.OFF)

def load_title():
    print("""          _____                    _____                    _____                    _____          
         /\    \                  /\    \                  /\    \                  /\    \         
        /::\    \                /::\    \                /::\    \                /::\____\        
       /::::\    \               \:::\    \              /::::\    \              /:::/    /        
      /::::::\    \               \:::\    \            /::::::\    \            /:::/    /         
     /:::/\:::\    \               \:::\    \          /:::/\:::\    \          /:::/    /          
    /:::/__\:::\    \               \:::\    \        /:::/__\:::\    \        /:::/____/           
   /::::\   \:::\    \              /::::\    \       \:::\   \:::\    \      /::::\    \           
  /::::::\   \:::\    \    ____    /::::::\    \    ___\:::\   \:::\    \    /::::::\____\________  
 /:::/\:::\   \:::\____\  /\   \  /:::/\:::\    \  /\   \:::\   \:::\    \  /:::/\:::::::::::\    \ 
/:::/  \:::\   \:::|    |/::\   \/:::/  \:::\____\/::\   \:::\   \:::\____\/:::/  |:::::::::::\____\
\::/   |::::\  /:::|____|\:::\  /:::/    \::/    /\:::\   \:::\   \::/    /\::/   |::|~~~|~~~~~     
 \/____|:::::\/:::/    /  \:::\/:::/    / \/____/  \:::\   \:::\   \/____/  \/____|::|   |          
       |:::::::::/    /    \::::::/    /            \:::\   \:::\    \            |::|   |          
       |::|\::::/    /      \::::/____/              \:::\   \:::\____\           |::|   |          
       |::| \::/____/        \:::\    \               \:::\  /:::/    /           |::|   |          
       |::|  ~|               \:::\    \               \:::\/:::/    /            |::|   |          
       |::|   |                \:::\    \               \::::::/    /             |::|   |          
       \::|   |                 \:::\____\               \::::/    /              \::|   |          
        \:|   |                  \::/    /                \::/    /                \:|   |          
         \|___|                   \/____/                  \/____/                  \|___|          
                                                                                                    """)

def DisplayProvinces(province_objects=None):
    for p in PROVINCES:
        if province_objects:
            prov = next((x for x in province_objects if x.name == p), None)
            if prov and prov.owner:
                color_code = prov.owner.ansi_color
                print(f"{color_code}{p}{Colors.RESET}")
            else:
                print(p)
        else:
            print(p)

def DisplayMap():
    print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣄⣠⣀⡀⣀⣠⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
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
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")

def DisplayProvinceOwner(province_objects, prov_name):
    for prov in province_objects:
        if prov.name == prov_name:
            if prov.owner:
                color_code = prov.owner.ansi_color
                print(f"{color_code}{prov.name} is owned by {prov.owner.name}{Colors.RESET}")
            else:
                print(f"{prov.name} has no owner.")
            return
    print("Province not found.")

def DisplayTroopStatus(province_objects):
    for prov in province_objects:
        if prov.owner:
            color_code = prov.owner.ansi_color
            print(f"{color_code}{prov.name}: Infantry={prov.infantry}, Tank={prov.tank}, Commando={prov.commando} | Owner: {prov.owner.name}{Colors.RESET}")
        else:
            print(f"{prov.name}: Infantry={prov.infantry}, Tank={prov.tank}, Commando={prov.commando} | No owner")

# ==================== SETUP ====================
def GetNumPlayers():
    return int(input("How many people are playing RISK today?\n"))

def FetchPlayerNames(num_players):
    return [input(f"Player {i+1} name: ") for i in range(num_players)]

def GetPlayersColors(player_names):
    colors = []
    for name in player_names:
        color = input(f"{name}, choose your color (red/green/blue/yellow/cyan/magenta/white): ").lower()
        colors.append(color)
    return colors

def ClaimProvince(players, province_objects):
    """Randomly assign provinces to players"""
    import random
    random.shuffle(PROVINCES)
    
    num_players = len(players)
    provinces_per_player = len(PROVINCES) // num_players
    extra = len(PROVINCES) % num_players
    
    idx = 0
    print("\n=== Randomly Assigning Provinces ===\n")
    
    for i, player in enumerate(players):
        num_to_give = provinces_per_player + (1 if i < extra else 0)
        for _ in range(num_to_give):
            if idx < len(PROVINCES):
                prov_name = PROVINCES[idx]
                prov = next((p for p in province_objects if p.name == prov_name), None)
                if prov:
                    prov.owner = player
                    player.provinces.append(prov)
                    print(f"{prov.name} assigned to {player.name}")
                idx += 1

# ==================== ACTIONS ====================
def is_adjacent(prov1, prov2):
    if prov1 in ADJACENCY and prov2 in ADJACENCY[prov1]:
        return True
    return prov2 in ADJACENCY and prov1 in ADJACENCY[prov2]

def LaunchAttack(current_player, province_objects):
    print("Launching Attack!")
    DisplayProvinces()
    from_prov = input("Attack from which province? ")
    to_prov = input("Attack which province? ")
    
    from_p = next((p for p in province_objects if p.name == from_prov and p.owner and p.owner.name == current_player.name), None)
    to_p = next((p for p in province_objects if p.name == to_prov), None)
    
    if not from_p or not to_p or not to_p.owner or to_p.owner.name == current_player.name:
        print("Invalid attack.")
        return
    if not is_adjacent(from_prov, to_prov):
        print("Provinces are not adjacent!")
        return
    
    attack_roll = random.randint(1,6) + random.randint(1,6)
    defend_roll = random.randint(1,6) + random.randint(1,6)
    print(f"Attack roll: {attack_roll} | Defense roll: {defend_roll}")
    
    if attack_roll > defend_roll:
        print("Victory! Province captured.")
        to_p.owner = current_player
    else:
        print("Attack failed.")

def RecruitSoldiers():
    print("Recruiting...")
    r1, r2 = random.randint(1,6), random.randint(1,6)
    print(f"Rolls: {r1} {r2}")
    if (r1 + r2) % 2 == 0:
        print("Extra troops recruited!")

# ==================== MAIN ====================
def main():
    load_soldiers()
    load_title()
    
    num_players = GetNumPlayers()
    player_names = FetchPlayerNames(num_players)
    player_colors = GetPlayersColors(player_names)
    
    # Create Player objects with colors
    players = [Player(name, color) for name, color in zip(player_names, player_colors)]
    
    # Create Province objects
    province_objects = [Province(name) for name in PROVINCES]
    
    # Randomly assign provinces
    ClaimProvince(players, province_objects)
    
    print("\n=== GAME START ===")
    turn = 0
    while True:
        current = players[turn % len(players)]
        print(f"\n{current.name}'s Turn!")
        DisplayMap()
        DisplayTroopStatus(province_objects)
        
        action = input("Action (A=Attack, R=Recruit, Q=Quit): ").upper()
        if action == "A":
            LaunchAttack(current, province_objects)
        elif action == "R":
            RecruitSoldiers()
        elif action == "Q":
            break
        turn += 1

if __name__ == "__main__":
    main()
