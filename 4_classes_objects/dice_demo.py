import random

class Dice:
    
    def __init__(self, value=None, locked=False):
        self.value = value
        self.locked = locked
        if value == None:
            self.roll()
        
    def __str__(self):
        result = str(self.value)
        if self.locked:
            result = result + '*'
        return result
        
    def __repr__(self):
        return f'Die(value={self.value}, locked={self.locked})'
        
    def __lt__(self, other):
        return self.value < other.value
        
    def roll(self):
        if not self.locked:
            self.value = random.randint(1, 6)
        return self.value
        
    def lock(self):
        self.locked = True
        
    def unlock(self):
        self.locked = False
    
if __name__ == '__main__':
    dice = [Dice(), Dice(), Dice(), Dice(), Dice()]
    for die in dice:
        print(repr(die))
    
    while True:
        dice.sort()
        for index, die in enumerate(dice):
            print(f'{index}: {die}')
            
        print('Lock #, Unlock #, Roll, Quit?')
        choice = input("> ").strip().lower()
        if choice == 'quit':
            break
        elif choice == 'roll':
            for die in dice:
                die.roll()
        elif choice[0:4] == 'lock':
            index = int(choice[-1])
            dice[index].lock()
        elif choice[0:6] == 'unlock':
            index = int(choice[-1])
            dice[index].unlock()
        else:
            print(f'"{choice}" is not a valid command.')