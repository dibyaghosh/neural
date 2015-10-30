# Utility functions for Neuron Processing

def get_values(l):
    return [a.get_value() for a in l]

def solve(neurons,outputs):
    for i in neurons:
        i.process()
    for j in outputs:
        j.process()
    return get_values(outputs)

def solvelayers(layers):
    for i in layers[1:]:
        for j in i:
            j.process()
    return get_values(layers[-1])

