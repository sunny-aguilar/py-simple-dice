# simple dice rolling simulator
import random


go = True

while go:
    result = roll_dice()
    go = input('Would you like to roll again? ')

def roll_dice():
    number = random.randint(1,6)
    print(number)
