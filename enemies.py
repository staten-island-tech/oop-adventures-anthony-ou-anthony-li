##Characters
class character:
    def __init__(self, health, name, damage):
        self.health = health
        self.name = name
        self.damage = damage
class Player(character):
    def __init__(self, health, name, damage):
        super().__init__(health ,name, damage)
class Bloater(character):
    def __init__(self, health, name, damage):
        super().__init__(health ,name, damage)
class Regurgitator(character):
    def __init__(self, health, name, damage):
        super().__init__(health, name, damage)
class Necrosis(character):
    def __init__(self, health, name, damage):
        super().__init__(health, name, damage)        
class Mothership(character):
    def __init__(self, health, name, damage):
        super().__init__(health, name, damage)
##Attack
bloater = Bloater(20, "Bloater", 10)
player = Player(150, "CAPT> SPACE BOY", 0)
regurgitator = Regurgitator(20, "Regurgitator", 10)
necrosis = Necrosis(20, "Necrosis", 15)
            
##Weapons
class weapon:
    def __init__(self, damage, name):
        self.damage = damage
        self.name = name
class Laser(weapon):
    def __init__(self, damage, name):
        super().__init__(damage, name)
class Sniper(weapon):
    def __init__(self, damage, name):
        super().__init__(damage, name)
class Plasma(weapon):
    def __init__(self, damage, name):
        super().__init__(damage, name)

##Weapon_Selection
laser = Laser(10, "Proton Arc")
sniper = Sniper(15, "Hornet")
plasma = Plasma(10, "CM_Gigavolt")

Choices = ["Laser", "Sniper", "Plasma"]
weapons = []
def weapon_selection():
    while len(weapons) < 2:
        for weapon in Choices:
            print(weapon)
        choice = input("What would you like?")
        if choice == "Laser":
            print(laser.name)
            print(laser.damage)
            weapons.append("Laser")
        elif choice == "Sniper":
            print(sniper.name)
            print(sniper.damage)
            weapons.append("Sniper")
        elif choice == "Plasma":
            print(plasma.name)
            print(plasma.damage)
            weapons.append("Plasma")
        else:
            print("Weapon choice is invalid, please try again.")

def incombat_weapon():
    for weapon in weapons:
        print(weapon)
    choice = input("What would you like?")
    if choice in weapons:
        print(f"You will now use {choice} while in combat")
        
weapon_selection()
incombat_weapon()

        