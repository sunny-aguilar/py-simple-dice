# simple dice rolling simulator
import random


go = True

while go:
    result = roll_dice()


def roll_dice():
    number = random.randint(1,6)
    print(number)
