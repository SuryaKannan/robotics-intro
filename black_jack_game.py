'''
MCAV - JMSS Co-Curricular 
Inspiration taken from https://gist.github.com/saulcosta/13909e2e51f94ff7b37700c74b885ab6 (Look afterwards for implementation)

Main Blackjack game script 

RULES:
- Goal is to beat dealers hand without going over 21 
- Face card (J,Q,K) are worth 10. Aces are worth 1 or 11, whichever makes a better hand
- Each player starts with two cards, one of the dealers card is hidden until the end  
- Player can either "hit", which is to ask for another card or "stand" which is to hold their current total
- If the player stands, the dealer must either draw if they are below 16 or stand if they are above 17 
- If you go over 21 you lose and the Dealer wins regardless
- If you are below 21 and stand while the dealer hits, whoever is closer to 21 wins
- If you get exactly 21 you win 
- Cards that are dealed should be put into a discard pile and once the main deck has less than 15 cards, 
combine the discarded and main deck together and re-shuffle. 

- Code it like a game! make sure scores are displayed correctly and that the player has the option to quit after every game

'''

from utils.Deck import Deck
from utils.Hand import Hand 

class BlackJack:
    def __init__(self):
        pass

    def play(self):
        '''
        ADD CODE HERE

        gameplay loop
        '''

    '''
    Add more functions
    '''

if __name__ == "__main__":
    game = BlackJack()
    game.play()
