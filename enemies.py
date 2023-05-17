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

def boss_fight():
    player = Player(150, "CAPT> SPACE BOY", 0)
    mothership = Mothership(100, "Mothership", 20)
    if player.health <= 20:
        print("You were instantly annihilated by the motherships death rays!")
        print("Game Over!")
    elif player.health >= 20:
        while player.health >= 20:
            weapon 
##Weapons
class weapon:
    def __init__(self, damage, name):
        self.damage = damage
        self.name = name
class Laser(weapon):
    def __init__(self, damage, name):
        super().__init__(damage=10, name="Proton Arc")
class Flamethrower(weapon):
    def __init__(self):
        super().__init__(damage=7, name="Ronson_WP_Flamethrower")
class Sniper(weapon):
    def __init__(self):
        super().__init__(damage=15, name="RIA 75")
class Plasma(weapon):
    def __init__(self):
        super().__init__(damage=20, name="CM_Gigavolt")

##Weapon_Selection
Choices = ["Laser", "Flamethrower", "Sniper", "Plasma"]
weapons = []
def weapon_selection():
    if len(weapons) >= 2:
        print("Invalid, user has too many weapons.")
    else:
        for weapon in Choices:
            print(weapon)
        choice = input("What would you like?")
        if choice == "Laser":
            print("Stats: 10 damage, name: Proton Arc")
            weapons.append(Laser)
        elif choice == "Flamethrower":
            print("Stats: 7 damage, name: Ronson_WP_Flamethrower")
            weapons.append(Flamethrower)
        elif choice == "Sniper":
            print("Stats: 15 damage, name: RIA 75")
            weapons.append(Sniper)
        elif choice == "Plasma":
            print("Stats: 20 damage, name: CM_Gigavolt")
            weapons.append(Plasma)
        else:
            print("Weapon choice is invalid, please try again.")

weapon_selection()