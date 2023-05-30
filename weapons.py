from time import sleep
# Weapons


class weapon:
    def __init__(self, damage, name):
        self.damage = damage
        self.name = name


class Rifle(weapon):
    def __init__(self):
        super().__init__(damage=10, name="Rifle")

    def __str__(self):
        return f"{self.name}: {self.damage} {'damage'}"


class Sniper(weapon):
    def __init__(self):
        super().__init__(damage=15, name="Sniper")

    def __str__(self):
        return f"{self.name}: {self.damage} {'damage'}"


class SMG(weapon):
    def __init__(self):
        super().__init__(damage=10, name="SMG")

    def __str__(self):
        return f"{self.name}: {self.damage} {'damage'}"

##Functions
def choose_weapon(self):
        available_weapons = [Rifle(), Sniper(), SMG()]
        for name in available_weapons:
            print(name)
        while self.current_weapon is None:
            weapon_choice = input('Enter in your weapon choice: ')
            self.current_weapon = self.get_weapon(weapon_choice)
            if self.current_weapon == None:
                print('Invalid weapon choice, please enter in a valid weapon')

def get_weapon(self, name):
        available_weapons = [Rifle(), Sniper(), SMG()]
        for weapon_choice in available_weapons:
            if weapon_choice.name.lower() == name.lower():
                return weapon_choice

def display_weapon(self):
        if self.current_weapon is not None:
            print('Your chosen weapon: ')
            print(self.current_weapon)
            sleep(3)
        else:
            print('You have no weapons equipped')

