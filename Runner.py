import Match
import Player
import Robot

plays = [Robot.RRobot(), Robot.RRobot(), Robot.RRobot(), Robot.RRobot()]
m = Match.Match(plays)

m.game()

'''m.trump = "Spades"
m.board = [['10', 'Hearts']]
m.hands = [[['Jack', 'Clubs'], ['King', 'Spades'], ['10', 'Clubs'], ['Jack', 'Diamonds'], ['Jack', 'Spades']]]
p.play(m.board, m.hands[0], m.trump)'''
