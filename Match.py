import Deck

class Match:

    #define variables
    players = None
    score = [0,0]
    intraScore = [0, 0]
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

        #define variables
        self.intraScore = [0, 0]

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
        for i in range(0,5):
            self.trick()

        #cleanup
        self.caller = None
        self.trump  = None
        self.dealer += 1
        self.dealer %= 4
        
        

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
        
        #get leader's decision
        p = self.players[self.winnie].lead(self.hands[counter])
        self.board += self.hands[counter].pop(p-1)
        counter+=1

        #get other decision
        while counter < self.winnie + 4:
            p = self.players[counter%4].play(self.board, self.hands[counter%4])
            self.board += self.hands[counter%4].pop(p-1)
            counter+=1
        
        #determine the winner
        self.winner()
        self.board = []
    
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

        self.winnie = r
        self.intraScore[r%2] += 1
        print("winner: " + str(r))
    
    #give points
    def points(self):
        
        #determine scoring team
        scoringTeam = 0
        if self.intraScore[1] > self.intraScore[0]:
            scoringTeam = 1

        #determine points
        if scoringTeam != self.caller or self.intraScore[scoringTeam] == 5:
            self.score[scoringTeam] += 2
        else:
            self.score[scoringTeam] += 1