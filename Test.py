from copy import copy, deepcopy
import numpy as np
import random

dimensions = [20,30,20]
weights = []

for i in range(len(dimensions)-1):
    weights += [np.random.rand(dimensions[i],dimensions[i+1])]

dim = [weights[0].shape[0]]
for w in weights:
    dim += [w.shape[1]]

print(dim)

#print(weights)

'''pos = [0,0,0]
pos[0] = random.randint(0,len(dimensions)-2)
pos[1] = random.randint(0,dimensions[pos[0]]-1)
pos[2] = random.randint(0,dimensions[pos[0]+1]-1)
print(pos)
weights[pos[0]][pos[1]][pos[2]] += random.random()*2-1'''
#print(weights)
