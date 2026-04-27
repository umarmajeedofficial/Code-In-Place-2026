from karel.stanfordkarel import *

# File: shelter.py
# -----------------------------
# This program makes Karel:
# 1. Go outside the house to reach the beeper
# 2. Pick up the beeper (food)
# 3. Return back to the starting position (inside the house)

def main():
    # Move forward until reaching the wall (end of house corridor)
    while front_is_clear():
        move()

    turn_right()   # Turn south toward the door
    move()         # Move through the doorway
    turn_left()    # Face east (toward the beeper)
    move()         # Move to the beeper location

    pick_beeper()  # Pick up the beeper (food)

    # Turn around to go back home
    turn_left()
    turn_left()

    # Move back toward the doorway
    while front_is_clear():
        move()

    turn_right()   # Turn north to re-enter house
    move()         # Move inside
    turn_right()   # Face original direction (east)


    # add your code here


def turn_right():
    # Helper function: simulate right turn using 3 left turns
    turn_left()
    turn_left()
    turn_left()


# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()
