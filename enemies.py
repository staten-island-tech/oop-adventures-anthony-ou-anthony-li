##Characters
class character:
    def __init__(self, health, name, damage):
        self.health = health
        self.name = name
        self.damage = damage
class Player(character):
    def __init__(self, health, name, damage):
        super().__init__(health=150, name="CAPT> SPACE BOY", damage = 0)
class Bloater(character):
    def __init__(self, health, name, damage):
        super().__init__(health=20, name="Bloater", damage = 10)
class Regurgitator(character):
    def __init__(self, health, name, damage):
        super().__init__(health=20, name="Regurgitator", damage = 10)
class Necrosis(character):
    def __init__(self, health, name, damage):
        super().__init__(health=20, name="Necrosis", damage = 15)
class Mothership(character):
    def __init__(self, health, name, damage):
        super().__init__(health=100, name="Mothership", damage = 20)
enemy = Bloater
def enemy_attack():
    if enemy == Bloater:
        health = Player.health - Bloater.damage
        print(health)

    enemy_attack()