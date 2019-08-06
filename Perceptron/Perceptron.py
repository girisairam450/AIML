# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 22:45:12 2019

@author: gragam
"""

import numpy as np

class Perceptron(object):

    def __init__(self, no_of_features, threshold=100, learning_rate=0.01):
        self.threshold = 5#threshold
        self.learning_rate = learning_rate
        self.weights = np.zeros(no_of_features + 1)
           
    def predict(self, inputs):
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]
        if summation > 0:
          activation = 1
        else:
          activation = 0            
        return activation

    def train(self, training_inputs, labels):
        print(self.weights)
        for _ in range(self.threshold):
            prediction_arr =[]
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                prediction_arr.append(prediction)
                self.weights[1:] += self.learning_rate * (label - prediction) * inputs
                self.weights[0] += self.learning_rate * (label - prediction)
                print(self.weights)
            print(prediction_arr)
