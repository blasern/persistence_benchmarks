#!/usr/bin/env python
"""
Diagram benchmarks
"""
from itertools import product
import numpy as np
from .noise import normal_noise
from .benchmark_data import circleGenerator, cliffordGenerator, linkedTwistGenerator

__shapes__ = [
    'circle',
    'cliffordTorus',
    'linkedTwist', 
    ]
__samplings__ = [
    'equal',
    'uniform',
    'noise'
    ]

class Benchmark(object):
    """
    This is a data generator class

    Parameters
    ----------
    shape : str
        Data shape. Currently one of 'circle', 'cliffordTorus', 'linkedTwist'.
    sampling : str
        Sampling strategy. One of 'equal', 'uniform', 'noise'.
    noise_distribution : fct
        Distribution function of noise.
    """

    def __init__(self, shape, sampling, noise_distribution=normal_noise(sd=1.0)):
        self.shape = shape
        self.sampling = sampling
        self.noise_distribution = noise_distribution
        if shape == 'circle':
            self.data_generator = circleGenerator(self.sampling)
        if shape == 'cliffordTorus':
            self.data_generator = cliffordGenerator(self.sampling)
        if shape == 'linkedTwist':
            self.data_generator = linkedTwistGenerator(self.sampling)


    def sample(self, n=100, **kwargs):
        """
        Return a sample from the shape and sampling distribution. 
        
        Parameters
        ----------
        n : int
            Number of samples (in some cases this should be a square).
        **kwargs : 
            Other arguments depending on the shape.

        Returns
        -------
        data : array
            Data sample from the shape given the sampling distribution. 
        """
        data = self.data_generator(n=n, **kwargs)
        if self.sampling == 'noise':
            data += self.noise_distribution(data)
        return data

