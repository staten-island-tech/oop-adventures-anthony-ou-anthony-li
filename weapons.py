
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
