#!/usr/bin/env python
"""
Benchmark data generator
"""
from itertools import product
import numpy as np
from .noise import normal_noise

__shapes__ = [
    'circle',
    'cliffordTorus'
    ]
__samplings__ = [
    'equal',
    'uniform',
    'noise'
    ]

class PersistenceDiagramBenchmark(object):
    """
    This is a data generator class

    Parameters
    ----------
    shape : str
        Data shape. Currently one of 'circle', 'cliffordTorus'. 
    sampling : str
        Sampling strategy. One of 'equal', 'uniform', 'noise'
    noise_distribution : fct
        Distribution function of noise
    """

    def __init__(self, shape, sampling, noise_distribution=normal_noise(sd=1.0)):
        self.shape = shape
        self.sampling = sampling
        self.noise_distribution = noise_distribution
        if shape == 'circle':
            self.data_generator = circleGenerator(self.sampling)
            self.target_generator = circleTarget
        if shape == 'cliffordTorus':
            self.data_generator = cliffordGenerator(self.sampling)
            self.target_generator = cliffordTarget

    def sample(self, n=100):
        """
        Return a sample from the shape and sampling distribution. 
        
        Parameters
        ----------
        n : int
            Number of samples (in some cases this should be a square).

        Returns
        -------
        data : array
            Data sample from the shape given the sampling distribution. 
        """
        data = self.data_generator(n=n)
        if self.sampling == 'noise':
            data += self.noise_distribution(data)
        return data

    def target(self):
        """
        Return the persistence diagram for this shape. 
        
        Returns
        -------
        pd : list of arrays
            Persistence diagram. 
        """
        return self.target_generator()


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


def circleTarget():
    return [np.array([[0.0, np.inf]]),
            np.array([[0.0, 1.0]])]
    

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


def cliffordTarget():
    return [np.array([[0.0, np.inf]]),
            np.array([[0.0, np.sqrt(2)/2.0],
                      [0.0, np.sqrt(2)/2.0]]),
            np.array([[]]),
            np.array([[np.sqrt(2)/2, 1.0]])]
