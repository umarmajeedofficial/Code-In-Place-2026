from karel.stanfordkarel import *

# Karel starts on the left side of an archway.
# Task:
# - Climb up the left side of the arch
# - Cross over the top
# - Move down the right side
# - End facing East on the ground

def main():
    # Turn north to start climbing the arch
    turn_left()

    # Move up the left side of the arch until blocked
    while front_is_clear():
        move()

    # Turn right (3 left turns) to face across the top
    turn_left()
    turn_left()
    turn_left()

    # Move across the top of the arch
    while front_is_clear():
        move()

    # Turn right again to start descending
    turn_left()
    turn_left()
    turn_left()

    # Move down the right side of the arch
    while front_is_clear():
        move()

    # Final orientation adjustment to face East
    turn_left()


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
