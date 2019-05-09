#!/usr/bin/env python
"""
Benchmark data for regression targets 
"""
import numpy as np
from .base_benchmarks import Benchmark

class RegressionBenchmark(Benchmark):
    """
    This is a data generator class

    Parameters
    ----------
    shape : str
        Data shape. Currently 'linkedTwist'. 
    sampling : str
        Sampling strategy. One of 'equal', 'uniform', 'noise'
    noise_distribution : fct
        Distribution function of noise
    """
    def multisample(self, N=100, n=100, parameter_range=(0, 1), parameters=None):
        if parameters is None:
            parameter_min = parameter_range[0]
            parameter_max = parameter_range[1]
            parameter_diff = parameter_max - parameter_min
            parameters = parameter_min + parameter_diff * np.random.rand(N)
        data = [self.sample(n=n, p=p) for p in parameters]
        return parameters, data

    
