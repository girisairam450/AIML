# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 22:48:10 2019

@author: gragam
"""

import numpy as np
from Perceptron import Perceptron

training_inputs = []
training_inputs.append(np.array([1, 0]))
training_inputs.append(np.array([3, 1]))
training_inputs.append(np.array([4, 2]))
training_inputs.append(np.array([0, 1]))
training_inputs.append(np.array([1, 6]))
training_inputs.append(np.array([2, 4]))

labels = np.array([1,1,1,0,0,0])

perceptron = Perceptron(2)
perceptron.train(training_inputs, labels)

inputs = np.array([2, 3])
print(perceptron.predict(inputs)) 


inputs = np.array([6, 1])
print(perceptron.predict(inputs))