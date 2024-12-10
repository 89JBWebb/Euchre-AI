from copy import copy, deepcopy
import numpy as np
import NN


ideal = [[[1,0],[1,0]],[[0,1],[0,1]],[[1,1],[0.5,0.5]],[[0,0],[0.5,0.5]]]
size = 100
pop = []
for i in range(size):
    pop += [NN.create([2,3,2])]

for i in range(100):
    results = []
    cos = []

    for i in range(size):
        cos += [NN.costSS(ideal, pop[i])]

    print(sum(cos) / size)

    min = 0
    for i in range(size):
        if cos[i] < cos[min]:
            min = i

    father = pop[min]
    pop = []
    for i in range(size):
        pop += [NN.mutate([2,3,2], father, 5)]

NN.costSStest(ideal, pop[0])