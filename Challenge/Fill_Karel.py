from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""

def main():
    # Repeat for each row except the last
    while left_is_clear():
        fill_row()
        go_back()
        move_up()
    
    # Fill the final row
    fill_row()


def fill_row():
    # Fill current row from left → right
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()


def go_back():
    # Return to first column
    turn_left()
    turn_left()
    while front_is_clear():
        move()
    turn_left()
    turn_left()


def move_up():
    # Move to next row (only possible from first column)
    turn_left()
    move()
    turn_right()


def turn_right():
    # Simulate right turn using 3 left turns
    for _ in range(3):
        turn_left()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
