import random
from time import sleep
import sys
class space:
    def __init__(self):
        self.Main_Character = Captain()
        self.aliens = [Bloater, Regurgitator, Necrosis]
        self.current_weapon = None
        self.aliens_killed = []
        

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
        ##Error Handling
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
        ##Error Handling
        else:
            print('You have no weapons equipped')

    def player_v_alien(self):
        alien_limit = 10

        while self.Main_Character.health > 0 and len(self.aliens_killed) < alien_limit:
            alien_choose = random.choice(self.aliens)()
            print(f'A {alien_choose.name} is coming after you')
            # Apply damage to the alien
            self.apply_damage(self.current_weapon, alien_choose)
            print(f"Alien Health: {alien_choose.health}")
            # Apply damage to the player
            self.Main_Character.health -= alien_choose.damage
            print(f"Health: {self.Main_Character.health}")
            if alien_choose.health == 0:
                self.aliens_killed.append(alien_choose.name)
            else:
                print("Keep going you're almost finished!")
            if self.Main_Character.health <= 0:
                sys.exit('GAME OVER YOU DIED')
            if len(self.aliens_killed) == alien_limit:
                sys.exit('CONGRATULATIONS YOU WON THE GAME')

    def apply_damage(self, weapon, alien):
        damage = weapon.damage
        alien.health -= damage
        if alien.health <= 0:
            alien.health = 0


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
                    print('You have successfully passed the Asteroid Field, you have now reached the ship')
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
