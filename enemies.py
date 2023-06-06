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






        