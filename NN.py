import numpy as np
import random

def create(dimensions):
    result = []
    for i in range(len(dimensions)-1):
        result += [np.random.rand(dimensions[i],dimensions[i+1])]
    return result

def getDim(weights):
    dim = [weights[0].shape[0]]
    for w in weights:
        dim += [w.shape[1]]
    return dim

def mutate(dim, weights, n):
    for i in range(n):
        pos = [0,0,0]
        pos[0] = random.randint(0,len(dim)-2)
        pos[1] = random.randint(0,dim[pos[0]]-1)
        pos[2] = random.randint(0,dim[pos[0]+1]-1)
        weights[pos[0]][pos[1]][pos[2]] += random.random()*2-1

def process(weights, arr):
    hodl = np.array([arr])
    for i in range(len(weights)):
        hodl = np.matmul(hodl, weights[i])
        hodl = sigmoid(hodl)
    hodl /= np.sum(hodl)
    return hodl

def sigmoid(self, z):
        return 1/(1 + np.exp(-z))