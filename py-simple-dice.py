# simple dice rolling simulator
import random


go = True

def roll_dice():
    number = random.randint(1,6)
    print(number)


while go:
    result = roll_dice()
    response = input('Would you like to roll again (y/n)? ')
    if response.upper() == 'Y':
        go = True



