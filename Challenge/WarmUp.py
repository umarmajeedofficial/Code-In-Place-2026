from karel.stanfordkarel import *

# File: warmup.py
# -----------------------------
# The warmup program defines a "main"
# function which currently just has one
# command. We add two more commands so Karel:
# 1. moves forward
# 2. picks a beeper
# 3. moves forward again

def main():
    move()           # Step 1: move forward to reach the beeper
    pick_beeper()    # Step 2: pick the beeper at current position
    move()           # Step 3: move forward again to next cell
    
    # add your code here (already completed above)


# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()
