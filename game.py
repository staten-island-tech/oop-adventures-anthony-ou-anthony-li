import random
from time import sleep
import sys
from weapons import Rifle, Sniper, SMG
from enemies import Bloater, Necrosis, Regurgitator, Captain
from story import space


def main(self):
    game = space(self)
    game.start(self)
    game.choose_weapon(self)
    game.display_weapon(self)
    game.asteroid_navigation(self)
    game.player_v_alien(self)

main()
    