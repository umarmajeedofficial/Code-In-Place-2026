from karel.stanfordkarel import *

# File: piles.py
# -----------------------------
# Karel must pick up all beepers on the first row of the world.
# The row contains multiple piles of beepers separated by empty spaces.

def main():
    # Move to first pile
    move()

    # Pick up first pile of beepers (10 beepers)
    for i in range(10):
        pick_beeper()

    # Move to next pile location
    move()
    move()

    # Pick up second pile of beepers (10 beepers)
    for i in range(10):
        pick_beeper()

    # Move to third pile location
    move()
    move()

    # Pick up third pile of beepers (10 beepers)
    for i in range(10):
        pick_beeper()

    # Move forward (end of row)
    move()


# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()
