from karel.stanfordkarel import *

# Karel starts at bottom-left of a world with 3 vertical obstacles.
# Task:
# - Move across the world
# - Place beepers to the right of each obstacle
# - Reach bottom-right corner at the end

def main():
    # Move to first obstacle area
    move()

    # Go up to climb the obstacle
    turn_left()
    move()

    # Turn right to move across the obstacle
    turn_right()
    move()

    # Place beepers on the squares to the right of the wall (3 times)
    put_a_beeper()
    put_a_beeper()
    put_a_beeper()

    # Turn right and move down after finishing obstacle work
    turn_right()
    move()

    # Turn left to continue final movement
    turn_left()

    # Move to final bottom-right position
    move()


def put_a_beeper():
    # Move around obstacle and place a beeper on the right side

    turn_right()   # face downward/right direction
    move()         # move to target cell

    put_beeper()   # place beeper on right side of obstacle

    # Return back around obstacle
    turn_right()
    turn_right()

    move()
    turn_right()

    move()


def turn_right():
    # Helper function since Karel only supports turn_left()
    turn_left()
    turn_left()
    turn_left()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
