##Characters
class character:
    def __init__(self, health, name, damage):
        self.health = health
        self.name = name
        self.damage = damage
class Player(character):
    def __init__(self, health, name, damage):
        super().__init__(health ,name, damage)
        self.health = health
        self.name = name
        self.damage = damage
class Bloater(character):
    def __init__(self, health, name, damage):
        super().__init__(health ,name, damage)
        self.health = health
        self.name = name
        self.damage = damage
class Regurgitator(character):
    def __init__(self):
        super().__init__(health=20, name="Regurgitator", damage = 10)
class Necrosis(character):
    def __init__(self):
        super().__init__(health=20, name="Necrosis", damage = 15)
class Mothership(character):
    def __init__(self):
        super().__init__(health=100, name="Mothership", damage = 20)

def bloater_attack():
    Bloater(20, "Bloater", 10)
    Player(150, "CAPT> SPACE BOY, 0")
    health = Player.health - Bloater.damage
    print(f"Your current health after the attack is {health}.")

    bloater_attack()