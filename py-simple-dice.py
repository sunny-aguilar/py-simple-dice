# simple dice rolling simulator
import random


go = False

while go:
    result = roll_dice()
    response = input('Would you like to roll again (y/n)? ')
    if response.upper() == 'Y':
        go = True


def roll_dice():
    number = random.randint(1,6)
    print(number)
