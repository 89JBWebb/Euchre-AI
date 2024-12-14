import copy
import numpy as np
import random


def costSS(ideal, weights):
    result = 0
    for case in ideal:
        guess = process(weights, case[0])
        diff = guess-case[1]
        result += sum([pow(ment,2) for ment in diff])
    return result

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

def weightNum(weights):
    hodl = getDim(weights)
    result = 0
    for i in range(0, len(hodl)-1):
        result+= hodl[i]*hodl[i+1]
    return result

def mutate(dim, weights, n):
    result = copy.deepcopy(weights)
    for i in range(n):
        pos = [0,0,0]
        pos[0] = random.randint(0,len(dim)-2)
        pos[1] = random.randint(0,dim[pos[0]]-1)
        pos[2] = random.randint(0,dim[pos[0]+1]-1)
        result[pos[0]][pos[1]][pos[2]] += random.random()*2-1
    return result

def process(weights, arr):
    hodl = np.array(arr)
    for i in range(len(weights)):
        hodl = np.matmul(hodl, weights[i])
        hodl = sigmoid(hodl)
    hodl /= np.sum(hodl)
    return hodl

def sigmoid(z):
        return 1/(1 + np.exp(-z))

def test(ideal, weights):
    for case in ideal:
        print(str(process(weights, case[0])) + " " + str(case[1]))