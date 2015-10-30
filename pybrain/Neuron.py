import math
from utils import get_values

blank_func = lambda x: 0

# Propagation Functions

def weighted_sum(weights,values):
    return sum([w*v for w,v in zip(weights,values)])


# Activation Functions

activation = lambda x: lambda y: 1 if y>x else -1
sigmoid = lambda x: 1/(1+math.pow(math.e,-x))

# Output Functions

identity = lambda x: x

class Neuron:

    last_id = 0

    def __init__(self,bias = 0, propagation_function = weighted_sum,activation_function = sigmoid,output_function=identity):
        self.inputs = []
        self.weights = []
        self.outputs = []
        self.bias = bias
        self.prop = propagation_function
        self.act = activation_function
        self.out = output_function
        self.nid = Neuron.last_id
        Neuron.last_id += 1
        self.output = 0

    def __repr__(self):
        return "Neuron %s" % (self.nid)

    def __str__(self):
        s1 = "Neuron %s" % (self.nid) + "\n"
        s1 += "Inputs: " + ",".join([repr(a) for a in self.inputs]) + "\n"
        s1 += "Outputs: " + ",".join([repr(a) for a in self.outputs])
        return s1

    def add_input(self,neuron):
        self.inputs.append(neuron)
        self.weights.append(1)

    def remove_input(self,neuron):
        if neuron in self.inputs:
            g = self.inputs.index(neuron)
            self.inputs.pop(g)
            self.weights.pop(g)

    def get_value(self):
        return self.output

    def process(self):
        inta = self.prop(self.weights,get_values(self.inputs))+self.bias
        act = self.act(inta)
        self.output = self.out(act)
        return


class Var(Neuron):
    """Represents an Input Neuron"""

    def __init__(self,varnum):
        Neuron.__init__(self,identity,identity,identity)
        self.output = varnum

    def set_value(self,num):
        self.output = num
