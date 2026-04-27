from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should be able to find
the midpoint
"""

def main():
    # Check if world has more than 1 cell
    if front_is_clear():
        move()

        # Check if world has more than 2 cells (general case)
        if front_is_clear():
            move_to_start()     # Go back to starting position
            fill_row()          # Fill entire row with beepers
            move_to_start()     # Return to start again

            corner()            # Remove beepers from both ends once
            edge()              # Move inward and remove next layer

            # Keep removing beepers from edges until center is reached
            while beepers_present():
                edge()

            put_beeper()        # Place final midpoint beeper
            face_east()         # Ensure Karel ends facing east

        else:
            # Case: world has exactly 2 cells → midpoint is left cell
            move_to_start()
            put_beeper()


def edge():
    pick_beeper()        # Pick current edge beeper
    move()               # Move inward

    # Move until reaching the next empty space (center boundary)
    while beepers_present():
        move()

    # When empty cell is found, step back to last beeper
    if no_beepers_present():
        turn_around()
        move()


def fill_row():
    put_beeper()         # Place beeper at starting cell

    # Fill entire row with beepers
    while front_is_clear():
        move()
        put_beeper()


def move_to_start():
    turn_around()        # Turn to face west

    # Move to the leftmost position
    while front_is_clear():
        move()

    turn_around()        # Face east again


def corner():
    pick_beeper()        # Remove beeper from left end

    # Move to rightmost end
    while front_is_clear():
        move()

    pick_beeper()        # Remove beeper from right end
    turn_around()
    move()               # Step inward


def face_east():
    # Ensure final direction is east
    if facing_west():
        turn_around()


def turn_around():
    # Turn 180 degrees
    turn_left()
    turn_left()


if __name__ == '__main__':
    main()
