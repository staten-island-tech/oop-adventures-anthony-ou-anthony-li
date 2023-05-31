from enemies import player_v_alien
from story import space, start, asteroid_navigation
from weapons import choose_weapon, display_weapon
from time import sleep
import sys

def main():
    game = space()
    game.start()
    game.choose_weapon()
    game.display_weapon()
    game.asteroid_navigation()
    game.player_v_alien()

main()
    