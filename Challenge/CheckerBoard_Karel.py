from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers in a checkerboard pattern.
"""


def main():
    # Alternate between two row patterns while there is space to move up
    while left_is_clear():
        row1()   # First row pattern (starts with a beeper)
        row2()   # Second row pattern (shifted pattern)

    # Handle the final row (edge case for odd number of rows)
    check_last_line()
    # go_back_to_origan()  # (optional, handled inside functions)


def check_last_line():
    # Move to check if last row needs to be filled differently
    turn_right()
    move()

    # If current cell has no beeper, it means last row needs row1 pattern
    if no_beepers_present():
        turn_left()
        turn_left()
        move()
        turn_right()

        row1()               # Fill last row using row1 pattern
        move_to_start()      # Return to starting column
        go_back_to_origan()  # Return to original position

    else:
        # If already aligned correctly, just return to origin
        turn_left()
        go_back_to_origan()


def go_back_to_origan():
    # Move to the far right, then face original direction
    turn_right()
    while front_is_clear():
        move()
    turn_left()


def row1():
    # First row pattern: place beeper on first cell
    put_beeper()

    # Place beepers on every alternate cell
    while front_is_clear():
        if front_is_clear():
            move()
        if front_is_clear():
            move()
            put_beeper()

    move_to_start()   # Return to start of row
    go_above_line()   # Move to next row


def row2():
    # Second row pattern: start with a gap, then place beeper
    if front_is_clear():
        move()
        put_beeper()

    # Continue placing beepers on alternate cells
    while front_is_clear():
        if front_is_clear():
            move()
        if front_is_clear():
            move()
            put_beeper()

    move_to_start()   # Return to start of row
    go_above_line()   # Move to next row


def go_above_line():
    # Move up one row (only possible from first column)
    if left_is_clear():
        turn_left()
        move()
        turn_right()


def turn_right():
    # Simulate right turn using three left turns
    turn_left()
    turn_left()
    turn_left()


def move_to_start():
    # Return to leftmost column of current row
    turn_around()
    while front_is_clear():
        move()
    turn_around()


def turn_around():
    # Turn 180 degrees
    turn_left()
    turn_left()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
