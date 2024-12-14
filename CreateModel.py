import NRobot
import pickle

dolly = NRobot.NRobot([])
dolly.random()

output = open('./Models/save.pkl', 'wb')
pickle.dump(dolly.weights, output)
output.close()