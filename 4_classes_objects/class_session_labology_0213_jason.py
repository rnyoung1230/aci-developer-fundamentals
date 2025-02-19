# LABOLOGY SESSION - 2/13
# ------------------------

# Jason's Dice Game exercise
'''
Directions:

'''
import random

class Dice:
    # class variables and methods

    # instance variables and methods
    def __init__(self, value=None): # sometimes it's a good idea to have a default value assigned to your constructor args.
        if value is None:
            self.roll()
        else:
            self.value = value

    def __str__(self):
        return str(self.value)  # overriding this method allows you to then print(object) and not receive the memory location

    def roll(self):
        self.value = random.randint(1,6)

if __name__ == '__main__':
    dice = [Dice(), Dice(), Dice(), Dice(), Dice()]

    # for i in range(len(dice)):
    #     print(f"{i}: {dice[i]}")

    for index, die in enumerate(dice):
        print(f"{index}: {die}")
