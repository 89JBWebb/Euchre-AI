import NRobot
import pprint, pickle
import os


dolly = NRobot.NRobot([])
dolly.random()

output = open('./Models/save.pkl', 'wb')
pickle.dump(dolly.weights, output)
output.close()

pkl_file = open('./Models/save.pkl', 'rb')
data1 = pickle.load(pkl_file)
pprint.pprint(data1)
pkl_file.close()
os.remove("./Models/save.pkl")

