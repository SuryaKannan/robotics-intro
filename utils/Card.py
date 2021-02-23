'''
MCAV - JMSS Co-Curricular 

Blackjack Card Class 
- used to create individual cards 

'''
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value 
    
    def show_card(self):
        print(self.value+" of "+self.suit+"\n")