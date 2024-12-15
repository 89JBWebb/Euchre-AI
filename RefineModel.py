import Match
import NRobot
import pickle
import os

dolly = NRobot.NRobot([])
pkl_file = open('./Models/save.pkl', 'rb')
dolly.weights = pickle.load(pkl_file)
pkl_file.close()
os.remove("./Models/save.pkl")

size = 2
games = 100
score = [0]*size
pop = []
for i in range(0,size):
    pop += [dolly.mutate(0.05)]

for i in range(0,size):
    for j in range(i+1, size):
        plays = [pop[i],pop[j],pop[i],pop[j]]
        m = Match.Match(plays)
        for k in range(0, games):
            hodl = m.game()
            score[i] += hodl[0]
            score[j] += hodl[1]

max = 0
for i in range(0,size):
    if score[max] < score[i]:
        max = i

output = open('./Models/save.pkl', 'wb')
pickle.dump(pop[max].weights, output)
output.close()