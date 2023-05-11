##Characters
class character:
    def __init__(self, health, name, damage):
        self.health = health
        self.name = name
        self.damage = damage
class Player(character):
    def __init__(self):
        super().__init__(health=150, name="CAPT> SPACE BOY", damage = 0)
class Mechs(character):
    def __init__(self):
        super().__init__(health=40, name="Zombodroid", damage = 20)
class Bloater(character):
    def __init__(self):
        super().__init__(health=20, name="Bloater", damage = 10)
class Regurgitator(character):
    def __init__(self):
        super().__init__(health=20, name="Regurgitator", damage = 10)
class Necrosis(character):
    def __init__(self):
        super().__init__(health=20, name="Necrosis", damage = 15)
class Mothership(character):
    def __init__(self):
        super().__init__(health=100, name="Mothership", damage = 20)
##Attack
def mech_attack(damage):
    health = Player(damage)-Mechs(damage)
    print(f"Your current health is {health}")

