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
        
bloater = Bloater(20, "Bloater", 10)
player = Player(150, "CAPT> SPACE BOY", 0)
regurgitator = Regurgitator(20, "Regurgitator", 10)
necrosis = Necrosis(20, "Necrosis", 15)
mothership = Mothership(100, "Mothership", 20)

enemy = bloater
def enemy_attack():
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

enemy_attack()