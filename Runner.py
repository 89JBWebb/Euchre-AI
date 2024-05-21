import Deck
import Match
import random

#def winner(hand, trump):

d = Deck.deal()

print(d[0])
print(["Jack", "Clubs"] in d[0])

def winner(board, trump):

    if board[0] == [["Jack"], [trump]]:
            return 0

    #look through cards
    r = 0
    for i in range(1,3):
        
        ##right bauer
        if board[i] == [["Jack"], [trump]]:
            return i
        
        ##left bauer
        if board[i] == [["Jack"], [Deck.colors[trump]]]:
            r = i
            continue
        
        #same suit
        if board[i][1] == board[r][1]:
            if Deck.rankings[board[i][0]] > Deck.rankings[board[r][0]]:
                r = i
                continue
        
        #next card is trump and leading is not
        if board[r][1] == trump:
            r = i
            continue

    return r