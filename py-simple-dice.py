# simple dice rolling simulator
import random

# flag to check if user wants to roll again
go = True

# function that rolls the dice and prints the value
def roll_dice():
    number = random.randint(1,6)
    print(number)

# loop that lets a user roll the dice until they quit
while go:
    result = roll_dice()
    response = input('Would you like to roll again (y/n)? ')
    if response.upper() == 'Y':
        go = True
    else if response.upper() == 'N':
        go = False



