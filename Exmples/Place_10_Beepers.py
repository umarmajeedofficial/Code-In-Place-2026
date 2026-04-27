"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

# Karel will place 10 beepers on the current corner

def main():
    # Repeat 10 times to place 10 beepers
    for i in range(10):
        put_beeper()


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
