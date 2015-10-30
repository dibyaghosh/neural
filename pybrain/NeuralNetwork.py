from utils import *

class NeuralNetwork:
    learning_factor = .1

    def __init__(self,neuron_layers):
        self.neurons = sum(neuron_layers,[])
        self.layers = neuron_layers
        self.w = dict()
        for i in self.neurons:
            self.w[i] = dict()
            i.prop = self.prop_func
            for j in self.neurons:
                self.w[i][j] = 0
        self.connect_all_layers(neuron_layers)

    def __repr__(self):
        s = "Neural Network with %d neurons in %d layers" % (len(self.neurons),len(self.layers))
        return s

    def prop_func(self,neuron,inputs):
        vals = get_values(inputs)
        s = 0
        for i in range(len(inputs)):
            s += vals[i]*self.w[neuron][inputs[i]]
        return s

    def connect_neurons(self,a,b):
        self.w[b][a] = 1
        a.outputs.append(b)
        b.inputs.append(a)

    def disconnect_neurons(self,a,b):
        self.w[b][a] = 0

    def connect_layers(self,l1,l2):
        for l in l1:
            for m in l2:
                self.connect_neurons(l,m)

    def connect_all_layers(self,layers):
        for i in range(1,len(layers)):
            self.connect_layers(layers[i-1],layers[i])

    def adjustment(self,error):
        for a in self.neurons:
            for b in a.inputs:
                if self.w[a][b] == 0:
                    continue
                self.w[a][b] += self.learning_factor*a.output*error
        return

    def solve(self):
        for i in self.layers[1:]:
            for j in i:
                j.process()
        return get_values(self.layers[-1])