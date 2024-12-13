import random
import NN

class NRobot:

    trump = None
    weights = []

    def __init__(self, weights):
        self.weights = weights

    #order it up or no?
    def turnup(self, hand, card):
        input = []

        #add trump colors
        t = int(card/6)
        input += hand[t*6:(t+1)*6]
        t = (t+2)%4
        input += hand[t*6:(t+1)*6]

        #add rest
        if t%2:
            input += hand[0:6] + hand[12:18]
        else:
            input += hand[6:12] + hand[18:24]

        #add value
        hodl = [0]*6
        hodl[card%6] = 1
        input += hodl

        #get output
        output = NN.process(self.weights[0],input)

        #find max output
        max = 0
        for i in range(0,len(output)):
            if output[i] > output[max]:
                max = i
        return max

    #call a trump or no?
    def pick(self, hand, card):

        #get output
        output = NN.process(self.weights[1],hand)

        #find max output
        max = 0
        options = [0,1,2,3,4]
        options.pop(int(card/6)+1)
        for i in range(0,len(output)):
            if i in options and output[i] > output[max]:
                max = i
        return max

    def discard(self, hand, trump):
        
        input = []

        #add trump colors
        input += hand[trump*6:(trump+1)*6]
        t = (trump+2)%4
        input += hand[t*6:(t+1)*6]

        #add rest
        if t%2:
            input += hand[0:6] + hand[12:18]
        else:
            input += hand[6:12] + hand[18:24]

        #get output
        output = NN.process(self.weights[2],input)

        #find max output
        max = 0
        for i in range(0,len(output)):
            if output[i] > output[max]:
                max = i
        return max

    def lead(self, hand, trump):

        #create input
        input += hand
        hodl = [0]*4
        hodl[trump] = 1
        input += hodl

        #get output
        output = NN.process(self.weights[2],input)

        #find max output
        max = 0
        for i in range(0,len(output)):
            if output[i] > output[max]:
                max = i
        return max

    def play(self, board, hand, trump):
        return -1

    #what cards can I play given the board
    def legalPlays(self, board, hand):
        #define variables
        hodl = []
        result = []
        followSuit = False

        #check to if if you can follow suit
        for i in range(0,len(hand)):
            if hand[i]:
                hodl += [i]
                if self.eSuit(i) == self.eSuit(board[0]):
                    followSuit = True

        #if you cant then you can play anything in your hand
        if not followSuit:
            return hodl

        #put together cards that can follow suit
        for i in range(0,len(hodl)):
            if self.eSuit(hodl[i]) == self.eSuit(board[0]):
                result += [i]
        return result
    

    #what is this card's suit (keeping in mind left bauers)
    def eSuit(self, card):
        if card%6 == 2 and (self.trump+2)%4 == int(card/6):
            return self.trump
        return int(card/6)