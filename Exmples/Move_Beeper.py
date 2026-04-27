from karel.stanfordkarel import *

# Karel starts in a 3x3 world in front of a beeper.
# Task:
# 1. Pick up the beeper
# 2. Move to the top of column 2
# 3. Place the beeper there
# 4. End in the top-right corner

def main():
    # Move forward to reach the beeper
    move()

    # Pick up the beeper from its starting position
    pick_beeper()

    # Turn north to start moving upward
    turn_left()

    # Move all the way to the top of the world
    while front_is_clear():
        move()

    # Place the beeper at the top of column 2
    put_beeper()

    # Turn around to move east toward final position
    turn_left()
    turn_left()
    turn_left()

    # Move to the top-right corner
    move()


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
