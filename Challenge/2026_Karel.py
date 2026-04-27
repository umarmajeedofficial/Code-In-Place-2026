from karel.stanfordkarel import *

"""
When you finish writing this file, Karel should be able to 
place 20 beepers, then 26 beepers, and end facing East to 
the right of the 26 beepers.
"""

def main():
    # Step 1: Place 20 beepers in a row
    for i in range(20):
        put_beeper()

    # Move one step forward before starting next group
    move()

    # Step 2: Place 26 beepers in a row
    for i in range(26):
        put_beeper()

    # Move one step forward to end position (right of beepers)
    move()


if __name__ == '__main__':
    main()
