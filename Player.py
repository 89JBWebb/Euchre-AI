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

    #order it up or no?
    def turnup(self, hand, card):
        print("hand: " + str(hand))
        print("card: " + str(card))
        print("0: no")
        print("1: yes")
        imp = input("> ")
        while not imp.isnumeric() and (imp == 0 or imp == 1):
            imp = input("> ")
        return int(imp)
    
    #call a trump or no?
    def pick(self, hand, card):
        print("hand: " + str(hand))
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

        #recruit
        imp = input("> ")
        while not imp.isnumeric() or int(imp) < 0 or int(imp) > 4 or int(imp) == canNotSelect:
            imp = input("> ")

        return int(imp)
    
    #what card do you lead?
    def lead(self, hand):
        print("hand: " + str(hand))
        return 0
    
    #what card do you play given the board?
    def play(self, board, hand):
        print("hand: " + str(hand))
        print("board: " + str(board))
        return 0