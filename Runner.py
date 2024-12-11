import Deck
import Match
import Player
import Robot


print(Deck.deal())

plays = [Robot.RRobot(), Robot.RRobot(), Robot.RRobot(), Robot.RRobot()]
m = Match.Match(plays)

m.game()
