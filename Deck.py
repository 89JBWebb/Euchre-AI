import random

suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
values = ["Ace", "King", "Queen", "Jack", "10", "9"]
colors = {
    "Spades": "Clubs",
    "Clubs": "Spades",
    "Hearts": "Diamonds",
    "Diamonds": "Hearts"
}

def shuffle():
    deck = []
    deck2 = []
    for i in suits:
        for j in values:
            deck += [[j, i]]
    
    while len(deck) != 0:
        a = random.randint(0, len(deck)-1)
        deck2 += [deck.pop(a)]
    
    return deck2

def deal():
    hand = [[], [], [], [], []]
    deck = shuffle()
    for i in range(0,4):
        for j in range(0,5):
            hand[i] += [deck.pop()]
    hand[4] = deck
    return hand

#first round
#second round
#tricks