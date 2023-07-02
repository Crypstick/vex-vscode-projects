# PLEASE INTEGRATE INTO MAIN.PY WHEN GOING FOR COMP PLEASEEEEE
# Library imports
from vex import *

#Brain should be defined by default
brain = Brain()

# Begin project code

def pre_autonomous():
    # actions to do when the program starts
    brain.screen.clear_screen()
    brain.screen.print("pre auton code")
    wait(1, SECONDS)

def autonomous():
    brain.screen.clear_screen()
    brain.screen.print("autonomous code")
    # place automonous code here

def user_control():
    brain.screen.clear_screen()
    # place driver control in this while loop
    while True:
        wait(20, MSEC)

# create competition instance
comp = Competition(user_control, autonomous)
pre_autonomous()
