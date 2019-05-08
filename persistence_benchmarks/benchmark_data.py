#!/usr/bin/env python
"""
Benchmark data generator
"""
from itertools import product
import numpy as np

class PersistenceBenchmark(object):
    """
    This is a data generator class

    Parameters
    ----------
    target : str 
        Target variable, one of 'PD', 'class', 'regression'. 
    shape : str
        Data shape. Currently one of 'circle', 'cliffordTorus'. 
    sampling : str
        Sampling strategy. One of 'equal', 'uniform', 'noise'
    noise_distribution : fct
        Distribution function of noise
    """

    def __init__(self, target, shape, sampling, noise_distribution=None):
        self.target = target
        self.shape = shape
        self.sampling = sampling
        self.noise_distribution = noise_distribution
        if shape == 'circle':
            self.data_generator = circleGenerator(self.sampling)
        if shape == 'cliffordTorus':
            self.data_generator = cliffordGenerator(self.sampling)

    def sample(self, n=100):
        data = self.data_generator(n=n)
        if self.sampling == 'noise':
            data = data + self.noise_distribution(n)
        return data


def circleGenerator(sampling):
    def generate_angle(n):
        if sampling=='equal':
            return np.linspace(0, 2*np.pi, num=n, endpoint=False)
        if sampling in ['uniform', 'noise']:
            return 2 * np.pi * np.random.rand(n)

    def generate_radius(n):        
        return np.repeat(1.0, n)

    def generate_circle(n):
        radius = generate_radius(n)
        angle = generate_angle(n)
        circle = np.array((radius * np.cos(angle), 
                           radius * np.sin(angle))).transpose()
        return circle

    return generate_circle


def cliffordGenerator(sampling):
    def generate_angles(n):
        if sampling=='equal':
            sqrt_n = int(np.sqrt(n))
            if sqrt_n ** 2 != n:
                raise ValueError('n must be a square for equal sampling')
            angles = np.array(list(product(*2*[
                np.linspace(0, 2*np.pi, sqrt_n, endpoint=False)])))
        if sampling in ['uniform', 'noise']:
            angles = np.hstack((2 * np.pi * np.random.rand(n, 1),
                                2 * np.pi * np.random.rand(n, 1)))
        return angles

    def generate_clifford(n):
        angles = generate_angles(n)
        phi = angles[:, 0].reshape(n, 1)
        psi = angles[:, 1].reshape(n, 1)
        return np.hstack((np.cos(phi), np.sin(phi),
                          np.cos(psi), np.sin(psi))) / np.sqrt(2)

    return generate_clifford
