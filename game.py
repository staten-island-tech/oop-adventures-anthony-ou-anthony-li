import random
from time import sleep
import sys
from weapons import Rifle, Sniper, SMG
from enemies import Bloater, Necrosis, Regurgitator, Captain
from story import space


def main():
    game = space()
    game.start()
    game.choose_weapon()
    game.display_weapon()
    game.asteroid_navigation()
    game.player_v_alien()

main()
    