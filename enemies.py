#Enemies
class character:
    def __init__(self, health, name):
        self.health = health
        self.name = name
class MainCharacter(character):
    def __init__(self):
        super().__init__(health=50, name="CAPT> SPACE BOY")
class Mechs(character):
    def __init__(self):
        super().__init__(health=50, name="Zombodroid")
        self.damage = 50
class Bloater(character):
    def __init__(self):
        super().__init__(health=20, name="Bloater")
        self.damage = 10
class Regurgitator(character):
    def __init__(self):
        super().__init__(health=10, name="Regurgitator")
        self.damage = 10
class Necrosis(character):
    def __init__(self):
        super().__init__(health=10, name="Necrosis")
        self.damage = 15
class Mothership(character):
    def __init__(self):
        super().__init__(health=100, name="Mothership")
        self.damage = 20
##Attack
def mech_attack(self):
        print(self.damage(MainCharacter)-self.damage(Mechs))

mech_attack()