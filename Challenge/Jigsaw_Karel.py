from karel.stanfordkarel import *

"""
Karel should finish the puzzle by picking up the last beeper 
(puzzle piece) and placing it in the right spot. Karel should 
end in the same position Karel starts in -- the bottom left 
corner of the world.
"""


def main():
    # Step 1: Move to the last puzzle piece (row 1, column 3)
    move()
    move()
    pick_beeper()   # Pick up the puzzle piece

    # Step 2: Move to target position (row 3, column 4)
    move()
    turn_left()
    move()
    move()
    put_beeper()    # Place puzzle piece in correct location

    # Step 3: Return to starting position

    # Turn around and move back toward left side
    turn_left()
    turn_left()
    move()
    move()

    # Adjust orientation to navigate back to bottom row
    turn_left()
    turn_left()
    turn_left()

    # Move all the way back to left boundary
    while front_is_clear():
        move()

    # Face East again (final required orientation)
    turn_left()
    turn_left()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
