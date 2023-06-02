import random
from time import sleep
import sys
from weapons import Rifle, Sniper, SMG, choose_weapon, display_weapon
from enemies import Bloater, Necrosis, Regurgitator, Captain, player_v_alien
from story import space, asteroid_navigation


def main():
    game = space()
    game.start()
    game.choose_weapon()
    game.display_weapon()
    game.asteroid_navigation()
    game.player_v_alien()

main()
    