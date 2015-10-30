from utils import *
from NeuralNetwork import *
from Neuron import *



act0 = activation(0)
a,b = Var(10), Neuron(identity,act0,identity)
w = NeuralNetwork([[a],[b]])

variables = [Var(10),Var(10)]
neurons = [Neuron(identity,act0,identity) for i in range(10)]
neurons2 = [Neuron(identity,act0,identity) for i in range(10)]
outputs = [Neuron(identity,identity,identity)]
total = [variables,neurons,neurons2,outputs]
nn = NeuralNetwork(total)


