import Deck

class Match:

    players = None
    score = [0,0]
    hands = []
    board = []
    trump = None
    dealer = 0
    winner = None
    caller = None
    
    def __init__(self, players):
        self.hands = Deck.deal()
        self.players = players
    
    def __str__(self):
        result = ""
        for h in self.hands:
            result+=str(h)+"\n"
        return result
    
    def play(self):
        while self.score[0] < 10 and self.score[1] < 10:
            self.round()

    def round(self):
        #trump
        self.turnup()
        if self.trump == None:
            self.pick()
   
        #tricks
        for i in range(0,5):
            self.trick()

        #cleanup
        self.caller = None
        self.trump  = None
        self.dealer += 1
        self.dealer %= 4

    def turnup(self):
        counter = (self.dealer+1)%4
        while counter != self.dealer:
            hodl = self.players[counter].turnup()
            if hodl != None:
                self.trump = hodl
                self.caller = counter%2
                return None
        return None

    def pick(self):
        counter = (self.dealer+1)%4
        while counter != self.dealer:
            hodl = self.players[counter].pick()
            if hodl != None:
                self.trump = hodl
                return hodl
        return None

    def trick(self):
        counter = self.winner
        self.players[self.winner].lead()
        counter+=1
        counter%=4
        while counter != self.winner:
            self.players[counter].play()
            counter+=1
            counter%=4
        #determine the winner
    
    #find winner of trick
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