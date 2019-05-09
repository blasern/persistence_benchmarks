#!/usr/bin/env python
"""
Diagram benchmarks
"""
from itertools import product
import numpy as np
from .noise import normal_noise
from .base_benchmarks import Benchmark
from .benchmark_data import circleTarget, cliffordTarget, unknownTarget

class PersistenceDiagramBenchmark(Benchmark):
    def __init__(self, shape, sampling, noise_distribution=normal_noise(sd=1.0)):
        super().__init__(
            shape=shape,
            sampling=sampling,
            noise_distribution=noise_distribution)
        if shape == 'circle':
            self.target_generator = circleTarget
        if shape == 'cliffordTorus':
            self.target_generator = cliffordTarget
        if shape == 'linkedTwist':
            self.target_generator = unknownTarget

        
    def target(self):
        """
        Return the persistence diagram for this shape. 
        
        Returns
        -------
        pd : list of arrays
            Persistence diagram. 
        """
        return self.target_generator()
