import NN

class NRobot:

    trump = None
    weights = []
    e = [[30,50,50,25,2],[24,50,50,25,5],[24,50,50,50,24],[48,50,50,50,24],[96,100,75,50,24]]
    r = [5300, 5075, 7400, 8600, 22050]

    def __init__(self, weights):
        self.weights = weights

    def random(self):
        self.weights = []
        for i in self.e:
            self.weights += [NN.create(i)]
    
    def mutate(self, rate):
        newt = []
        for i in range(0,len(self.weights)):
            newt += [NN.mutate(self.e[i], self.weights[i], int(self.r[i]*rate))]
        return NRobot(newt)


    #order it up or no?
    def turnup(self, hand, card):

        #create input
        input = self.order(hand, int(card/6))
        hodl = [0]*6
        hodl[card%6] = 1
        input += hodl

        #get output
        output = NN.process(self.weights[0],input)

        #find max output
        max = 0
        for i in range(0,len(output)):
            if output[i] > output[max]:
                max = i
        return max

    #call a trump or no?
    def pick(self, hand, card):

        #get output
        output = NN.process(self.weights[1],hand)

        #find max output
        max = 0
        options = [0,1,2,3,4]
        options.pop(int(card/6)+1)
        for i in range(0,len(output)):
            if i in options and output[i] > output[max]:
                max = i
        return max

    def discard(self, hand, trump):
        
        #get input
        ho = self.order(hand, trump)

        #get output
        output = NN.process(self.weights[2],ho)

        #find max output
        max = 0
        while ho[max]:
            max+=1
        for i in range(0,len(output)):
            if ho[i] and output[i] > output[max]:
                max = i
        return self.deOrder(max, trump)

    #ask what card to lead a trick
    def lead(self, hand, trump, discard):
        input = []
        ho = self.order(hand, trump)
        input += ho
        input += self.order(discard, trump)

        #get output
        output = NN.process(self.weights[3],input)

        #find max output
        max = 0
        while ho[max]:
            max+=1
        for i in range(0,len(output)):
            if ho[i] and output[i] > output[max]:
                max = i
        return self.deOrder(max,trump)

    def play(self, board, hand, trump, discard):
        
        self.trump = trump

        #create input
        input = []
        
        #my team
        hodl = [0]*24
        i = len(board)-2
        if i >= 0:
            hodl[board[i]] = 1
        input += self.order(hodl, trump)

        #opponent team
        hodl = [0]*24
        i = len(board)-1
        while i >= 0:
            hodl[board[i]] = 1
            i -= 2
        input += self.order(hodl, trump)

        #hand
        ho = self.order(hand, trump)
        input += ho

        #discard
        input += self.order(discard, trump)

        #get output
        output = NN.process(self.weights[4],input)

        #find max output
        max = 0
        legals = self.legalPlays(board, hand)
        max = legals[0]
        for i in range(0,len(output)):
            if i in legals and output[i] > output[max]:
                max = i
        return self.deOrder(max,trump)

    #what cards can I play given the board
    def legalPlays(self, board, hand):
        result = []

        #record which cards in hand follow suit
        for i in range(0, 24):
            if hand[i] and self.eSuit(hand[i]) == self.eSuit(board[0]):
                result += [i]
                break
        
        #return some cards if follow suit
        if len(result) > 0:
            return result
        
        #return all cards in hand
        for i in range(0, 24):
            if hand[i]:
                result += [i]
        return result


    #what is this card's suit (keeping in mind left bauers)
    def eSuit(self, card):
        if card%6 == 2 and (self.trump+2)%4 == int(card/6):
            return self.trump
        return int(card/6)
    
    #order so 1st trump 2nd of trump color
    def order(self, set, trump):
        #define result
        result = []

        #add trump colors
        t = trump
        result += set[t*6:(t+1)*6]
        t = (t+2)%4
        result += set[t*6:(t+1)*6]

        #add rest
        if t%2:
            result += set[0:6] + set[12:18]
        else:
            result += set[6:12] + set[18:24]
        return result
    
    def deOrder(self, n, trump):
        if int(n/6) == 0:
            return n%6+trump*6
        if int(n/6) == 1:
            return n%6+((trump+2)%4)*6
        if int(n/6) == 2:
            if trump%2:
                return n%6
            return n%6+6
        if int(n/6) == 3:
            if trump%2:
                return n%6+12
            return n%6+18
        return -1