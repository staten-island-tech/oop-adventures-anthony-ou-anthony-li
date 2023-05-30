from time import sleep
import sys
import random
# Choice, navigate to ship
def asteroid_navigation(self):
    print('What do you want to do')
    print('A. Go through Asteroid field until you find ship')
    print('B. Run away')
    choice = input('Pick your choice (A/B): ').upper()

    while choice not in ['A', 'B']:
        print('Invalid input, please enter A or B')
        choice = input('Pick your choice (A/B): ').upper()

    # Handle choice A
    if choice == 'A':
        print('Be careful to dodge the asteroids, make sure to avoid collisions')
        while choice == 'A':  # loop until 2
            num = random.randint(1, 2)
            if num != 2:
                print('Navigating through Asteroid Field')
                sleep(3)
                print('You are still navigating through the Asteroid Field')
            if num == 2:
                sleep(4)
                print('Passing Asteroid field')
                sleep(1.5)
                print('You have successfully passed the Asteroid Field, you have now reached the ship')
                break

        # Handle choice B
            elif choice == 'B':
                while choice == 'B':  # loop until 2
                    num = random.randint(1, 2)
                    if num != 2:
                        sleep(3)
                        print('Running away')
                    if num == 2:
                        sleep(3)
                        print('You ran away')
                        break
            if choice == 'B':
                sys.exit('GAME OVER')