import Deck

class Match:

    #define variables
    players = None
    score = [0,0]
    hands = []
    board = []
    trump = None
    dealer = 0
    winnie = 1
    caller = None
    
    #define bots vs human players
    def __init__(self, players):
        self.players = players
    
    #print out the hands
    def __str__(self):
        result = ""
        for h in self.hands:
            result+=str(h)+"\n"
        return result
    
    #play one whole match
    def play(self):
        while self.score[0] < 10 and self.score[1] < 10:
            self.round()

    #play a round in four parts
    def round(self):

        #deal
        self.hands = Deck.deal()

        #trump
        self.turnup()
        if self.trump == None:
            screwDealer = self.pick()
            #screw the dealer is off
            #if dealer doesn't pick then it is a misdeal
            if screwDealer == -1:
                return
   
        #tricks
        '''for i in range(0,5):
            self.trick()

        #cleanup
        self.caller = None
        self.trump  = None
        self.dealer += 1
        self.dealer %= 4'''

    #call turnup protocols for players
    def turnup(self):
        counter = self.dealer+1
        while counter != self.dealer+5:
            hodl = self.players[counter%4].turnup( self.hands[counter%4], self.hands[4][0] )
            if hodl != 0:
                self.trump = hodl
                self.caller = counter%2
                return None
            counter += 1
        return -1
    
    #call pick protocols for players
    def pick(self):
        counter = self.dealer+1
        while counter != self.dealer+5:
            hodl = self.players[counter%4].pick( self.hands[counter%4], self.hands[4][0] )
            if hodl != 0:
                self.trump = hodl
                return hodl
            counter += 1
        return -1

    #call trick protocols for players
    def trick(self):
        counter = self.winnie
        if self.winnie is None:
            self.winnie = 1
        self.players[self.winnie].lead(self.hands[counter])
        counter+=1
        counter%=4
        while counter != self.winnie:
            self.players[counter].play(self.board, self.hands[counter])
            counter+=1
            counter%=4
        #determine the winner
        self.winner()
    
    #find winner of trick
    def winner(self):

        #check first card for bauers
        if self.board[0] == ["Jack", self.trump]:
            return 0
        if self.board[0] == ["Jack", Deck.colors[self.trump]]:
            if ["Jack", self.trump] not in self.board:
                return i

        #look through cards
        r = 0
        for i in range(1,4):
            
            #check for bauers
            if self.board[i] == ["Jack", self.trump]:
                return i
            if self.board[i] == ["Jack", Deck.colors[self.trump]]:
                if ["Jack", self.trump] not in self.board:
                    return i
                continue
            
            #same suit
            if self.board[i][1] == self.board[r][1]:
                if Deck.rankings[self.board[i][0]] > Deck.rankings[self.board[r][0]]:
                    r = i
                    continue
            
            #next card is trump and leading is not
            if self.board[r][1] == self.trump:
                r = i
                continue

        self.winner = r
    
    #give points
    def points(self):
        if self.winner%2 == self.caller%2:
            self.points[self.winner%2] +=1
        else:
            self.points[self.winner+1%2] +=2