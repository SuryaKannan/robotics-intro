'''
MCAV - JMSS Co-Curricular 

Blackjack Deck Class 
- used to create, shuffle and monitor deck

'''
from utils.Card import Card
import random 

class Deck:
    def __init__(self):
        self.stack = []
        self.suits = ["Hearts","Diamonds","Clubs","Spades"]
        self.values = ["Ace","2","3","4","5","6","7","8","9","Jack","Queen","King"]
    
    def create_deck(self):
        for suit in self.suits:
            for value in self.values:
                self.stack.append(Card(suit,value))
    
    def show_deck(self):
        for card in self.stack:
            card.show_card()

    def shuffle_deck(self):
        random.shuffle(self.stack)

    def deal_card(self):
        return self.stack.pop()

            
