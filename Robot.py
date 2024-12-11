#turnup
#   0: no
#   1: yes
#pick
#   0: None
#   1: Spades
#   2: Hearts
#   3: Clubs
#   4: Diamonds
#lead
#   0 through 4
#play
#   0 through 4

import Deck
import random

class RRobot:

    trump = None

    #order it up or no?
    def turnup(self, hand, card):
        return random.randint(0,1)
    
    #call a trump or no?
    def pick(self, hand, card):
        options = [0,1,2,3,4]
        options.pop(Deck.suits.index(card[1])+1)
        return options[random.randint(0,3)]
    
    def discard(self, hand, trump):
        return random.randint(0,5)
    
    #what card do you lead?
    def lead(self, hand, trump):
        return random.randint(0, len(hand)-1)
    
    #what card do you play given the board?
    def play(self, board, hand, trump):
        self.trump = trump
        options = self.legalPlays(board, hand)
        return options[random.randint(0, len(options)-1)]
    
    #what cards can I play given the board
    def legalPlays(self, board, hand):
        result = []
        followSuit = False

        for i in range(0,len(hand)):
            if self.eSuit(hand[i]) == self.eSuit(board[0]):
                followSuit = True
                break

        if not followSuit:
            return range(0,len(hand))

        for i in range(0,len(hand)):
            if self.eSuit(hand[i]) == self.eSuit(board[0]):
                result += [i]
        return result
    
    #what cards can I play given trump
    def eSuit(self, card):
        if card%6 == 2 and (self.trump+2)%4 == int(card/6):
            return self.trump
        return int(card/6)
