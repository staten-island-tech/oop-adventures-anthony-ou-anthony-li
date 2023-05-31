import sys
import random
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
        super().__init__(health=20, name="Bloater", damage=9)

    def __str__(self):
        return f"{self.name}, {'health'}: {self.health}, {'damage'}: {self.damage}"


class Regurgitator(Aliens):
    def __init__(self):
        super().__init__(health=10, name="Regurgitator", damage=8)

    def __str__(self):
        return f"{self.name}, {'health'}: {self.health}, {'damage'}: {self.damage}"


class Necrosis(Aliens):
    def __init__(self):
        super().__init__(health=10, name="Necrosis", damage=11)

    def __str__(self):
        return f"{self.name}, {'health'}: {self.health}, {'damage'}: {self.damage}"
##Functions
def player_v_alien(self):
        alien_limit = 10

        while self.Main_Character.health > 0 and len(self.aliens_killed) < alien_limit:
            alien_choose = random.choice(self.aliens)()
            print(f'A {alien_choose.name} is coming after you')
            damage = self.current_weapon.damage
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

player_v_alien()




        