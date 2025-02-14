import random

class PlayingCard:
    suits = '♠♣♦♥'
    vals = 'A23456789TJQK'
    
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        
    def __str__(self):
        return f'{PlayingCard.vals[self.value]}{PlayingCard.suits[self.suit]}'
    
    def __repr__(self):
        return f'PlayingCard({self.value, self.suit})'
        
class Deck:
    
    def __init__(self):
        self.cards = []
        self.build()
        
    def build(self):
        self.cards.clear()
        for n in range(52):
            value = n % 13
            suit = n // 13
            card = PlayingCard(value, suit)
            self.cards.append(card)
            
    def display(self):
        for n, card in enumerate(self.cards):
            print(card,' ',end='')
            if n % 13 == 12:
                print()
        print()
        
    def shuffle(self):
        random.shuffle(self.cards)
        
    def deal(self):
        return self.cards.pop()
        
        
def show_hand(hand):
    for card in hand:
        print(card, end=' ')
    print()
    
if __name__ == '__main__':
    deck = Deck()
    deck.display()
    deck.shuffle()
    print()
    deck.display()
    
    print('--- Deal two "hands" ---')
    hand1 = []
    hand2 = []
    for n in range(5):
        hand1.append(deck.deal())
        hand2.append(deck.deal())
    print('Hand 1: ', end='')
    show_hand(hand1)
    print('Hand 2: ', end='')
    show_hand(hand2)
    print('Contents of deck: ')
    deck.display()