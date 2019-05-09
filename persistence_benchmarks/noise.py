#!/usr/bin/env python
"""
Noise generators
"""
import numpy as np

def normal_noise(sd=1.0):
    def noise_generator(X): 
        return np.random.normal(loc=0, scale=sd, size=X.shape)
    return noise_generator

def uniform_noise(maxnoise=1.0):
    def noise_generator(X):
        n, d = X.shape
        return maxnoise * (0.5 - np.random.rand(n, d))
    return noise_generator
