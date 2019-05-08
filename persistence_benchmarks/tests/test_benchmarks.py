import numpy as np
from itertools import product
from persistence_benchmarks.benchmark_data import PersistenceBenchmark


def product_dict(**kwargs):
    'Source: https://stackoverflow.com/a/5228294/2591234'
    keys = kwargs.keys()
    vals = kwargs.values()
    for instance in product(*vals):
        yield dict(zip(keys, instance))


def test_shapes():
    parameter_dicts = product_dict(
        target = ['PD', 'class', 'regression'], 
        shape = ['circle', 'cliffordTorus'], 
        sampling = ['equal', 'uniform', 'noise'])

    for parameters in parameter_dicts:
        if parameters['shape'] == 'circle':
            def noise_distribution(n, d=2):
                return np.random.normal(0, 0.1, (n, d))
        if parameters['shape'] == 'cliffordTorus':
            def noise_distribution(n, d=4):
                return np.random.normal(0, 0.1, (n, d))
        pb = PersistenceBenchmark(**parameters, noise_distribution=noise_distribution)
        X = pb.sample(100)
        # check that number of points is correct
        assert X.shape[0] == 100
