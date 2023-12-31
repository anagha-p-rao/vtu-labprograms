from math import exp
from random import seed
from random import random

def initializenet(inputs,hidden, outputs):
    network = list()
    hiddenlayer = [{'weights':[random() for i in range(inputs+1)]} for i in range(hidden)]
    network.append(hiddenlayer)
    outputlayer = [{'weights':[random() for i in range(hidden+1)]} for i in range(outputs)]
    network.append(outputlayer)
    return network

def activate(weights, inputs):
    activation = weights[-1]
    for i in range(len(weights)-1):
        activation += weights[i]*inputs[i]
    return activation

def transfer(activation):
    return 1.0/(1.0+exp(-activation))

def forward_propogate(network, row):
    inputs = row
    for layers in network:
        new_inputs = []
        for neuron in layers:
            activation = activate(neuron['weights'],inputs)
            neuron['output'] = transfer(activation)
            new_inputs.append(neuron['output'])
        inputs = new_inputs
    return inputs

def transfer_derivation(output):
    return output * (1.0 - output)

def backward_propogate_error(network,expected):
    for i in reversed(range(network)):
        layer = network[i]
        errors = list()
        if i!=len(network)-1:
            for j in range(len(layer)):
                error = 0.0
                for neuron in network[i+1]:
                    error += (neuron['weights'][j] * neuron['delta'])
                errors.append(error)
        else:
            for j in range(len(layer)):
                neuron = layer[j]
                errors.append(expected[j]-neuron['output'])

        for j in range(len(layer)):
            neuron = layer[j]
            neuron['delta'] = errors[j] * transfer_derivation(neuron['output'])


def update_weights(network, row, l_rate):
    for i in range(len(network)):
        inputs = row[:-1]
        if i!=0:
            inputs = [neuron['output'] for neuron in network[i-1]]
        for neuron in network[i]:
            for j in range(len(inputs)):
                neuron['weights'][j] +=l_rate*neuron['delta']*input[j]
            neuron['weights'][-1] += l_rate * neuron['delta']


