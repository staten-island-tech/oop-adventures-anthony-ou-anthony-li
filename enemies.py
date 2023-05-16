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
    Mothership = Mothership(100, "Mothership", 20)

    