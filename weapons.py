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
        super().__init__(health=50, name="CAPT> SPACE BOY", danage = 3)
class Mechs(character):
    def __init__(self):
        super().__init__(health=50, name="Zombodroid", damage = 20)
class Bloater(character):
    def __init__(self):
        super().__init__(health=20, name="Bloater", danage = 10)
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
        super().__init__(damage=10, name="Hotspot")
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
        self.shield_strenth = shield_strength

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
class Space_Explorer:
        def __init__(self):
            self.Main_Character = Player
            self.aliens = [Mechs, Bloater, Regurgitator, Necrosis]
            self.mothership = [Mothership]

        def start():
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
        start()

        def choose_weapon(self):
            while self.current_weapon == None:
                weapon_choice = input('Enter in your weapon choice')
                self.current_weapon = weapon(weapon_choice)
                if self.current_weapon == None:
                    print('Invalid weapon choice, please enter in a valid weapon')
        
        def get_weapon(self):
            

        #Naviage through the asteroids
        def asteroid_navigation():
            print('What do you want to do')
            sleep(2)
            print('A. Go through Asteroid field until you find ship')
            print('B. Call for backup')
            choice = input('Pick your choice (A/B): ').upper()

        #Error Handling 
            while choice not in ['A','B']:
                print('Invalid input, please enter A or B')
                sleep(0.5)
                choice = input('Pick your choice (A/B): ').upper()
            
            # Handle choice A
            if choice == 'A':
                print('Be careful to dodge the asteroids, make sure to avoid collisions')
                while choice == 'A': #loop until 2
                    num = random.randint(1,2)
                    if num != 2:
                        print('Navigating through Asteroid Field')
                        sleep(3)
                        print('You are still navigating through the Asteroid Field')
                    if num == 2:
                        sleep(4)
                        print('Passing Asteroid field')
                        sleep(1.5)
                        print('You have successfully passed the Asteroid Field, you have now reached the ship')
                        break

                # Handle choice B
            elif choice == 'B':
                while choice == 'B': #loop until 2
                    num = random.randint(1,2)
                    if num != 2:
                        sleep(3)
                        print('Connecting')
                    if num == 2:
                        sleep(3)
                        print('Reinforcements are arriving soon')
                        break

        # Run
        asteroid_navigation()
        choose_weapon()