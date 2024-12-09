import numpy as np

class NNetwork:

    weights = []
    dimensions = []

    def sigmoid(self, z):
        return 1/(1 + np.exp(-z))

    def __init__(self, dimensions):
        self.dimensions = dimensions
        for i in range(len(self.dimensions)-1):
            self.weights += [np.random.rand(self.dimensions[i],self.dimensions[i+1])]

    def process(self, arr):
        hodl = np.array([arr])
        for i in range(len(self.dimensions)-1):
            hodl = np.matmul(hodl, self.weights[i])
            hodl = self.sigmoid(hodl)
        return hodl
    
    def show(self):
        print(self.weights)
