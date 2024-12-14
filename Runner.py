import Match
import NRobot

dolly = NRobot.NRobot([])
dolly.random()

plays = [dolly,dolly,dolly,dolly]
m = Match.Match(plays)

counter = 0
for i in range(0,100):
    if m.game()[0] >= 10:
        counter+=1
print(counter)
