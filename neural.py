import random
import numpy as np

class Network:
    def __init__(self,sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)
                        for x, y in zip(sizes[:-1], sizes[1:])]

    def ff(self,a):
        a = np.array(a).reshape((1,self.sizes[0]))
        for b,w in zip(self.biases,self.weights):
            a = sigmoid(np.dot(w,a)+b)
        return a


def sigmoid(a):
    return 1/(1 + np.exp(a))

