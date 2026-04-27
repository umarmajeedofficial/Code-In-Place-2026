from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def main():
    # Loop runs 4 times because there are 4 columns to repair
    for i in range(4):
        buildline()  # Build one full column (5 units high)

        # Move Karel to the next column position (4 steps apart)
        for j in range(4):
            if front_is_clear():  # Safety check to avoid crashing into a wall
                move()

def buildline():
    turn_left()  # Turn north to start building the column upward

    # Move upward while placing beepers on each square
    while front_is_clear():
        put_beeper()  # Place stone (beeper) at current position
        move()        # Move up one step

    put_beeper()  # Place beeper at the top of the column

    # Turn around to come back down to the base
    turn_left()
    turn_left()

    # Move back down to the bottom of the column
    while front_is_clear():
        move()

    turn_left()  # Face east again, ready for next column


if __name__ == '__main__':
    main()
