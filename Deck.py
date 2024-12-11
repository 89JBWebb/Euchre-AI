import random

suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
values = ["Ace", "King", "Queen", "Jack", "10", "9"]
toValue = {
    5: "Ace",
    4: "King",
    3: "Queen",
    2: "Jack",
    1: "10",
    0: "9"
}
toSuit = {
    0: "Spades",
    1: "Hearts",
    2: "Clubs",
    3: "Diamonds"
}
valueRankings = {
    "Ace": 5,
    "King": 4,
    "Queen": 3,
    "Jack": 2,
    "10": 1,
    "9": 0
}

def shuffle():
    result = []
    for i in range(0,24):
        result += [i]
    return random.shuffle(result)

def deal():
    board = []
    for i in range(0,4):
        board += [[0]*24]
    order = []
    for i in range(0,24):
        order += [i]
    random.shuffle(order)
    i = 0
    while i < 4:
        j = 0
        while j < 5:
            board[i][order.pop()] = 1
            j += 1
        i += 1
    board += [order.pop()]
    print(board)
    return board

def toStr(x):
    return toValue[x%6] + " of " + toSuit[int(x/6)]