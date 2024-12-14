import Match
import NRobot
import pickle
import os

dolly = NRobot.NRobot([])
pkl_file = open('./Models/save.pkl', 'rb')
dolly.weights = pickle.load(pkl_file)
pkl_file.close()
os.remove("./Models/save.pkl")

pop = []
for i in range(0,2):
    pop += [dolly.mutate(0.05)]

plays = [pop[0],pop[1],pop[0],pop[1]]
m = Match.Match(plays)
print(m.game())

output = open('./Models/save.pkl', 'wb')
pickle.dump(dolly.weights, output)
output.close()