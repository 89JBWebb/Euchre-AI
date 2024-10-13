#turnup
#   1 yes
#   0 no
#pick
#  -1: None
#   0: Spades
#   1: Hearts
#   2: Clubs
#   3: Diamonds
#lead
#   0 through 4
#play
#   0 through 4

class Player:

    #order it up or no?
    def turnup(self, hand, card):
        print("hand: " + str(hand))
        print("card: " + str(card))
        print("no = 0")
        print("yes = 1")
        imp = input("> ")
        while not imp.isnumeric() and (imp == 0 or imp == 1):
            imp = input("> ")
        return int(imp)
    
    #call a trump or no?
    def pick(self, hand, card):
        print("hand: " + str(hand))
        print("card: " + str(card))
        return -1
    
    #what card do you lead?
    def lead(self, hand):
        print("hand: " + str(hand))
        return 0
    
    #what card do you play given the board?
    def play(self, board, hand):
        print("hand: " + str(hand))
        print("board: " + str(board))
        return 0