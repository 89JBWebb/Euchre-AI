import Deck
import Match
import Player
import random

p = Player.Player()
plays = [Player.Player(), Player.Player(), Player.Player(), Player.Player()]
m = Match.Match(plays)

m.round()
