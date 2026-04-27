from karel.stanfordkarel import *

# Karel is lost and must follow a trail of beepers to find home.
# The beepers form a straight line, but we don't know how long it is.

def main():
    # Keep moving forward as long as there is a beeper on the current corner
    # (i.e., Karel is still on the trail)
    while beepers_present():
        move()   # Follow the path one step forward


if __name__ == '__main__':
    main()
