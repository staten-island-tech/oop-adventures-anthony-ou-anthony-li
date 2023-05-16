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
##Functions
def enemy_attack():
    bloater = Bloater(20, "Bloater", 10)
    player = Player(150, "CAPT> SPACE BOY", 0)
    regurgitator = Regurgitator(20, "Regurgitator", 10)
    necrosis = Necrosis(20, "Necrosis", 15)
    if enemy == bloater:
        health = player.health - bloater.damage
        print(f"Your current health now is {health}")
    elif enemy == regurgitator:
        health = player.health - regurgitator.damage
        print(f"Your current health now is {health}")
    elif enemy == necrosis:
        health = player.health - necrosis.damage
        print(f"Your current health now is {health}")
    else:
        print("There are no enemies in your sight.")

def boss_fight():
    player = Player(150, "CAPT> SPACE BOY", 0)
    mothership = Mothership(100, "Mothership", 20)
    if player.health <= 20:
        print("You were instantly annihilated by the motherships death rays!")
        print("Game Over!")
    elif player.health >= 20:
        while player.health >= 20:
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
