import Deck

class Match:

    #define variables
    players = None
    score = [0, 0]
    trickScore = [0, 0]
    hands = []
    board = []
    trump = None
    dealer = 0
    trickWinner = 1
    caller = None
    verbose = False
    
    #define bots vs human players
    def __init__(self, players):
        self.players = players
    
    #play one whole match
    def game(self):
        while self.score[0] < 10 and self.score[1] < 10:
            self.round()
        print(self.score)

    #play a round in four parts
    def round(self):

        #define variables
        self.trickScore = [0, 0]

        #deal
        self.hands = Deck.deal()

        #trump
        hodl = self.turnup()
        if hodl != -1:
            self.discard()
        if self.trump == None:
            screwDealer = self.pick()
            #screw the dealer is off
            #if dealer doesn't pick then it is a misdeal
            if screwDealer == -1:
                return
   
        #tricks
        for i in range(0,5):
            self.trick()

        #add round winner to the score
        roundWinner = 0
        if self.trickScore[1] > self.trickScore[0]:
            roundWinner = 1
        if self.trickScore[roundWinner] == 5 or roundWinner != self.caller:
            self.score[roundWinner] += 2
        else:
            self.score[roundWinner] += 1

        #cleanup
        self.caller = None
        self.trump  = None
        self.dealer += 1
        self.dealer %= 4


    #call turnup protocols for players
    def turnup(self):
        counter = self.dealer+1
        while counter != self.dealer+5:
            hodl = self.players[counter%4].turnup( self.hands[counter%4], int(self.hands[4]/6) )
            if hodl != 0:
                self.trump = int(self.hands[4]/6)
                self.hands[self.dealer][self.hands[4]] = 1
                self.caller = counter%2
                return None
            counter += 1
        return -1


    #if the card is called up, call on the dealer to discard
    def discard(self):
        hodl = self.players[self.dealer].discard(self.hands[self.dealer], self.trump)
        self.hands[self.dealer][hodl] = 0

    
    #call pick protocols for players
    def pick(self):
        counter = self.dealer+1
        while counter != self.dealer+5:
            hodl = self.players[counter%4].pick( self.hands[counter%4], self.hands[4][0] )
            if hodl != 0:
                self.trump = Deck.suits[hodl-1]
                return hodl
            counter += 1
        return -1

    #call trick protocols for players
    def trick(self):
        counter = self.trickWinner
        if self.trickWinner is None:
            self.trickWinner = 1
        
        #get leader's decision
        p = self.players[counter].lead(self.hands[counter], self.trump)
        self.board += [p]
        self.hands[counter][p] = 0
        counter+=1

        #get other decision
        while counter < self.trickWinner + 4:
            p = self.players[counter%4].play(self.board, self.hands[counter%4], self.trump)
            self.board += [p]
            self.hands[counter%4][p] = 0
            counter+=1
        
        if self.verbose:
            #print board
            i = 4-self.trickWinner
            while i < 8-self.trickWinner:
                print(Deck.toStr(self.board[i%4]))
                i+=1
            print()

        #determine the winner
        self.findTrickWinner()
        self.board = []

    
    def findTrickWinner(self):
        self.trickWinner += self.ftwHelper()
        self.trickWinner %= 4
        self.trickScore[self.trickWinner%2] += 1
        
    #find winner of trick
    def ftwHelper(self):

        #check for bauers
        if self.trump*6+2 in self.board:
            return self.board.index(self.trump*6+2)
        if ((self.trump+2)%4)*6+2 in self.board:
            return self.board.index(((self.trump+2)%4)*6+2)

        #look through cards
        r = 0
        for i in range(1,4):
            #same suit
            if self.eSuit(self.board[i]) == self.eSuit(self.board[r]):
                if self.board[i] > self.board[r]:
                    r = i
                    continue
            #next card is trump and leading is not
            if self.eSuit(self.board[i]) == self.trump and self.eSuit(self.board[r]) != self.trump:
                r = i
                continue
        return r
    
    #give points
    def points(self):
        
        #determine scoring team
        scoringTeam = 0
        if self.trickScore[1] > self.trickScore[0]:
            scoringTeam = 1

        #determine points
        if scoringTeam != self.caller or self.trickScore[scoringTeam] == 5:
            self.score[scoringTeam] += 2
        else:
            self.score[scoringTeam] += 1
        
        self.trickScore = [0,0]
    
    def eSuit(self, card):
        if card%6==2 and self.trump == int(card/6):
            return self.trump
        return int(card/6)
