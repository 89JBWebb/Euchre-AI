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
    def turnup(hand, card):
        print("hand: " + str(hand))
        print("card: " + str(card))
        return 0
    def pick(hand, card):
        print("hand: " + str(hand))
        print("card: " + str(card))
        return -1
    def lead(hand, discard):
        print("hand: " + str(hand))
        return 0
    def play(board, hand):
        print("hand: " + str(hand))
        print("board: " + str(board))
        return 0