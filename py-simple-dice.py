# simple dice rolling simulator
import random

# flag to check if user wants to roll again
go = True

#
def roll_dice():
    number = random.randint(1,6)
    print(number)


while go:
    result = roll_dice()
    response = input('Would you like to roll again (y/n)? ')
    if response.upper() == 'Y':
        go = True
    else:
        go = False



