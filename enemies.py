import random
#Character
class character:
    def __init__(self, health, name, damage):
        self.health = health
        self.name = name
        self.damage = damage
class Captain(character):
    def __init__(self):
        super().__init__(health=150, name="Captain", damage = 0)
    def __str__(self):
        return f"{self.health}, {self.name}, {self.damage}"

 #Aliens   
class Aliens:
    def __init__(self, health, name, damage):
        self.health = health
        self.name = name
        self.damage = damage
class Bloater(Aliens):
    def __init__(self):
        super().__init__(health=20, name="Bloater", damage = 10)
    def __str__(self):
        return f"{self.name}, {'health'}: {self.health}, {'damage'}: {self.damage}"
class Regurgitator(Aliens):
    def __init__(self):
        super().__init__(health=10, name="Regurgitator", damage = 10)
    def __str__(self):
        return f"{self.name}, {'health'}: {self.health}, {'damage'}: {self.damage}"
class Necrosis(Aliens):
    def __init__(self):
        super().__init__(health=10, name="Necrosis", damage = 15)
    def __str__(self):
        return f"{self.name}, {'health'}: {self.health}, {'damage'}: {self.damage}"

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

player_v_alien()
    



        