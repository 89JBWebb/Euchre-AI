import Deck
import Match
import random

def winner(board, trump):

    #check first card for bauers
    if board[0] == ["Jack", trump]:
        return 0
    if board[0] == ["Jack", Deck.colors[trump]]:
        if ["Jack", trump] not in board:
            return i

    #look through cards
    r = 0
    for i in range(1,4):
        
        #check for bauers
        if board[i] == ["Jack", trump]:
            return i
        if board[i] == ["Jack", Deck.colors[trump]]:
            if ["Jack", trump] not in board:
                return i
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

d = [['9', 'Spades'], ['10', 'Spades'], ['Jack', 'Spades'], ['Jack', 'Clubs']]
print(d)
print("Clubs")
print(winner(d, "Clubs"))