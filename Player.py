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

class Player:

    trump = None

    #order it up or no?
    def turnup(self, hand, card):
        print("order up trump")
        self.printHand(hand)
        print("card: " + str(card))
        print("0: no")
        print("1: yes")
        imp = input("> ")
        while not imp.isnumeric() and (imp == 0 or imp == 1):
            imp = input("> ")
        return int(imp)
    
    #call a trump or no?
    def pick(self, hand, card):
        print("pick trump?")

        #print
        self.printHand(hand)
        print("You can not select " + str(card[1]))
        print("0: no")
        
        #remeber the number of the suit you can not select
        canNotSelect = None

        #print suit options
        for i in range(0, 4):
            if str(card[1]) != Deck.suits[i]:
                print(str(i+1) + ": " + str(Deck.suits[i]))
            else:
                canNotSelect = i+1

        #get input
        imp = input("> ")
        while not imp.isnumeric() or int(imp) < 0 or int(imp) > 4 or int(imp) == canNotSelect:
            imp = input("> ")

        return int(imp)
    
    def discard(self, hand, trump):
        self.trump = trump

        #print hand
        print("discard a card")
        print("trump: "+ trump)
        self.printHandOptions(hand)

        #get legal input
        imp = input("> ")
        while not imp.isnumeric() or int(imp) < 0 or int(imp) > len(hand):
            imp = input("> ")
        return int(imp)
    
    #what card do you lead?
    def lead(self, hand, trump, discard):

        #print
        print("what card do you lead")
        print("trump: "+ trump)
        self.printHandOptions(hand)

        #get legal input
        imp = input("> ")
        while not imp.isnumeric() or int(imp) < 0 or int(imp) > len(hand):
            imp = input("> ")
        return int(imp)
    
    #what card do you play given the board?
    def play(self, board, hand, trump, discard):
        self.trump = trump
        print("what card do you play")
        print("trump: "+ trump)
        self.printHandOptions(hand)
        print("board: " + str(board))
        print("trump: " + trump)
        self.trump = trump

        print(self.legalPlays(board, hand))

        #get legal input
        imp = input("> ")
        while not imp.isnumeric() or int(imp) not in self.legalPlays(board, hand):
            imp = input("> ")
        return int(imp)
    
    #what cards can I play given the board
    def legalPlays(self, board, hand):
        result = []
        followSuit = False

        for i in range(0,len(hand)):
            if self.eSuit(hand[i]) == board[0][1]:
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
        if card[0] == "Jack" and Deck.colors[self.trump] == card[1]:
            return self.trump
        return card[1]
    
    #print hand
    def printHandOptions(self, hand):
        for i in range(0, len(hand)):
            print(str(i) + ": " + hand[i][0] + " of " + hand[i][1])
    
    def printHand(self, hand):
        print("hand: ")
        for i in range(0, len(hand)):
            print("\t" + hand[i][0] + " of " + hand[i][1])
