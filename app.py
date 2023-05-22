import random
from time import sleep
#Enemies
class character:
    def __init__(self, health, name, damage):
        self.health = health
        self.name = name
        self.damage = damage
class Captain(character):
    def __init__(self):
        super().__init__(health=150, name="Captain", damage = 0)
    def __str__(self):
        return f"{self.health}, {self.name}, {self.damage}"
class Bloater(character):
    def __init__(self):
        super().__init__(health=20, name="Bloater", damage = 10)
    def __str__(self):
        return f"{self.health}, {self.name}, {self.damage}"
class Regurgitator(character):
    def __init__(self):
        super().__init__(health=10, name="Regurgitator", damage = 10)
    def __str__(self):
        return f"{self.health}, {self.name}, {self.damage}"
class Necrosis(character):
    def __init__(self):
        super().__init__(health=10, name="Necrosis", damage = 15)
    def __str__(self):
        return f"{self.health}, {self.name}, {self.damage}"
class Mothership(character):
    def __init__(self):
        super().__init__(health=100, name="Mothership", damage = 20)
    def __str__(self):
        return f"{self.health}, {self.name}, {self.damage}"

#Weapons
class weapon:
    def __init__(self, damage, name):
        self.damage = damage
        self.name = name
class Rifle(weapon):
    def __init__(self):
        super().__init__(damage=10, name="Rifle")
    def __str__(self):
        return f"{self.name}: {self.damage} {'damage'}"
class Sniper(weapon):
    def __init__(self):
        super().__init__(damage=15, name="Sniper")
    def __str__(self):
        return f"{self.name}: {self.damage} {'damage'}"
class SMG(weapon):
    def __init__(self):
        super().__init__(damage=10, name="SMG")
    def __str__(self):
        return f"{self.name}: {self.damage} {'damage'}"
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
        self.Main_Character = Captain
        self.aliens = [Bloater, Regurgitator, Necrosis]
        self.mothership = [Mothership]
        self.current_weapon = None
        self.health = [150]

    def start(self):
        print('Space Explorer')
        print('You are a captain to a spaceship.')
        print('You are your crew are sent on a mission to explore a distant planet.')
        print('Along the way, you receive a distress call from a nearby ship.')
        print('The message is obscure, but you can make out that they are under attack by aliens.')

    def choose_weapon(self):
        available_weapons = [Rifle(), Sniper(), SMG()]
        for name in available_weapons:
            print(name)
        while self.current_weapon is None:
            weapon_choice = input('Enter in your weapon choice: ')
            self.current_weapon = self.get_weapon(weapon_choice)
            if self.current_weapon == None:
                print('Invalid weapon choice, please enter in a valid weapon')
    
    def get_weapon(self, name):
        available_weapons = [Rifle(), Sniper(), SMG()]
        for weapon_choice in available_weapons:
            if weapon_choice.name.lower() == name.lower():
                return weapon_choice
            
    def display_weapon(self):
        if self.current_weapon is not None:
            print('Your chosen weapon: ')
            print(self.current_weapon)
        else:
            print('You have no weapons equipped')


# Choice, navigate to ship
    def asteroid_navigation(self):
        print('What do you want to do')
        print('A. Go through Asteroid field until you find ship')
        print('B. Call for backup')
        choice = input('Pick your choice (A/B): ').upper()

    #Error Handling 
        while choice not in ['A','B']:
            print('Invalid input, please enter A or B')
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



def main():
    game = space()
    game.choose_weapon()
    game.display_weapon()
    game.asteroid_navigation()

main()