import random
from time import sleep

#Enemies
class character:
    def __init__(self, health, name, damage):
        self.health = health
        self.name = name
        self.damage = damage
class Player(character):
    def __init__(self):
        super().__init__(health=50, name="CAPT> SPACE BOY", damage = 3)
class Mechs(character):
    def __init__(self):
        super().__init__(health=50, name="Zombodroid", damage = 20)
class Bloater(character):
    def __init__(self):
        super().__init__(health=20, name="Bloater", damage = 10)
class Regurgitator(character):
    def __init__(self):
        super().__init__(health=10, name="Regurgitator", damage = 10)
class Necrosis(character):
    def __init__(self):
        super().__init__(health=10, name="Necrosis", damage = 15)
class Mothership(character):
    def __init__(self):
        super().__init__(health=100, name="Mothership", damage = 20)

##Weapons
class weapon:
    def __init__(self, damage, name):
        self.damage = damage
        self.name = name
class Laser(weapon):
    def __init__(self):
        super().__init__(damage=10, name="Proton Arc")
class Knife(weapon):
    def __init__(self):
        super().__init__(damage=15, name="Lightsaber")
class Flamethrower(weapon):
    def __init__(self):
        super().__init__(damage=7, name="Ronson_WP_Flamethrower")
class Sniper(weapon):
    def __init__(self):
        super().__init__(damage=15, name="Hornet")
        super().__init__(damage=15, name="RIA 75")
class Plasma(weapon):
    def __init__(self):
        super().__init__(damage=20, name="CM_Gigavolt")
#Spaceship player's ship
class Spaceship:
    def __init__(self, energy, shield_strength):
        self.energy = energy
        self.shield_strength = shield_strength

#Space Station Under attack
class Space_Station:
    def __init__(self, surviors, system_damage):
        self.survivors = surviors
        self.system_damage = system_damage

#Alien Ship         # Space Station V Alien Ship
class Alien_Ship:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

# Start of game
class space:
    def __init__(self):
        self.Main_Character = Player
        self.aliens = [Mechs, Bloater, Regurgitator, Necrosis]
        self.mothership = [Mothership]
        self.current_weapon = None

    def start(self):
        print('Space Explorer')
        sleep(1)
        print('You are a captain to a spaceship.')
        sleep(1)
        print('You are your crew are sent on a mission to explore a distant planet.')
        sleep(1)
        print('Along the way, you receive a distress call from a nearby ship.')
        sleep(1)
        print('The message is obscure, but you can make out that they are under attack by aliens.')
        sleep(1.5)

    def choose_weapon(self):
        for all_weapons in weapon:
            print(all_weapons)
        while self.current_weapon is None:
            weapon_choice = input('Enter in your weapon choice')
            self.current_weapon = weapon(weapon_choice)
            if self.current_weapon == None:
                print('Invalid weapon choice, please enter in a valid weapon')
    
    def get_weapon(self, name):
        for weapon_choice in weapon:
            if weapon_choice.lower() == name.lower():
                return weapon
            
    def display_weapon(self):
        print('You have the following weapons')
        sleep(1)
        for every_weapon in self.current_weapon:
            print(f'You have {every_weapon} equipped')
