import random
from time import sleep
import sys

# Character


class character:
    def __init__(self, health, name):
        self.health = health
        self.name = name


class Captain(character):
    def __init__(self):
        super().__init__(health=150, name="Captain")

    def __str__(self):
        return f"{self.health}, {self.name}"

 # Aliens


class Aliens:
    def __init__(self, health, name, damage):
        self.health = health
        self.name = name
        self.damage = damage


class Bloater(Aliens):
    def __init__(self):
        super().__init__(health=20, name="Bloater", damage=10)

    def __str__(self):
        return f"{self.name}, {'health'}: {self.health}, {'damage'}: {self.damage}"


class Regurgitator(Aliens):
    def __init__(self):
        super().__init__(health=10, name="Regurgitator", damage=10)

    def __str__(self):
        return f"{self.name}, {'health'}: {self.health}, {'damage'}: {self.damage}"


class Necrosis(Aliens):
    def __init__(self):
        super().__init__(health=10, name="Necrosis", damage=15)

    def __str__(self):
        return f"{self.name}, {'health'}: {self.health}, {'damage'}: {self.damage}"

# Weapons


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

# Start of game


class space:
    def __init__(self):
        self.Main_Character = Captain()
        self.aliens = [Bloater, Regurgitator, Necrosis]
        self.current_weapon = None
        self.health = Captain().health

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
            sleep(3)
        else:
            print('You have no weapons equipped')

# Choice, navigate to ship
    def asteroid_navigation(self):
        print('What do you want to do')
        print('A. Go through Asteroid field until you find ship')
        print('B. Run away')
        choice = input('Pick your choice (A/B): ').upper()

    # Error Handling
        while choice not in ['A', 'B']:
            print('Invalid input, please enter A or B')
            choice = input('Pick your choice (A/B): ').upper()

        # Handle choice A
        if choice == 'A':
            print('Be careful to dodge the asteroids, make sure to avoid collisions')
            while choice == 'A':  # loop until 2
                num = random.randint(1, 2)
                if num != 2:
                    print('Navigating through Asteroid Field')
                    sleep(3)
                    print('You are still navigating through the Asteroid Field')
                if num == 2:
                    sleep(4)
                    print('Passing Asteroid field')
                    sleep(1.5)
                    print(
                        'You have successfully passed the Asteroid Field, you have now reached the ship')
                    break

            # Handle choice B
        elif choice == 'B':
            while choice == 'B':  # loop until 2
                num = random.randint(1, 2)
                if num != 2:
                    sleep(3)
                    print('Running away')
                if num == 2:
                    sleep(3)
                    print('You ran away')
                    break
        if choice == 'B':
            sys.exit('GAME OVER')

    def player_v_alien(self):
        self.aliens = [Bloater(), Regurgitator(), Necrosis()]
        player = Captain().health
        aliens_killed = []
    
    #Loop for until you die or Aliens killed is 10 
        while player > 0 and len(aliens_killed) <= 10:
            alien_choose = random.choice(self.aliens)
    # Display Aliens info 
            print(f"A {alien_choose.name} is coming after you")
            health = player - alien_choose.damage
            print(f"Health: {health}")
            attack = alien_choose.health - Captain().damage
            print(f"Alien Health: {attack}")
            if attack == 0:
                aliens_killed.append(alien_choose.name) 
            else:
                print("Keep going you're almost finished!")

        
                

def main():
    game = space()
    game.player_v_alien()


main()
