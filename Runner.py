import Deck
import Match
import NNetwork
import Player
import random

'''p = Player.Player()
plays = [Player.Player(), Player.Player(), Player.Player(), Player.Player()]
m = Match.Match(plays)

m.round()'''

'''m.trump = "Spades"
m.board = [['10', 'Hearts']]
m.hands = [[['Jack', 'Clubs'], ['King', 'Spades'], ['10', 'Clubs'], ['Jack', 'Diamonds'], ['Jack', 'Spades']]]
p.play(m.board, m.hands[0], m.trump)'''

a = NNetwork.NNetwork([2,3,2])
a.show()
print(a.process([1,0]))