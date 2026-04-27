# This tells PyCharm who Karel is
# Every Karel file has a line just like it
from karel.stanfordkarel import *

# This program runs inside the main function
def main():
    # Move to the beeper
    move()

    # Pick up the beeper from the ground
    pick_beeper()

    # Move forward toward the wall/ledge area
    move()

    # Turn left to face upward (north direction)
    turn_left()

    # Move up onto the ledge path
    move()

    # Turn right (3 left turns) to face correct direction
    turn_left()
    turn_left()
    turn_left()

    # Move to the placement position
    move()

    # Place the beeper on the ledge
    put_beeper()

    # Move forward after placing the beeper
    move()


# This is boilerplate code which runs main() when you press Run
if __name__ == '__main__':
    main()
