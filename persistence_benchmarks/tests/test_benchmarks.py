import numpy as np
from itertools import product
from persistence_benchmarks import benchmark_data
from persistence_benchmarks.noise import normal_noise

def product_dict(**kwargs):
    'Source: https://stackoverflow.com/a/5228294/2591234'
    keys = kwargs.keys()
    vals = kwargs.values()
    for instance in product(*vals):
        yield dict(zip(keys, instance))

def checkEqualPD(iterator):
    'Source: https://stackoverflow.com/a/3844832/2591234'
    iterator = iter(iterator)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return np.all([np.all([np.allclose(x, y) for x, y in zip(first, rest)])
                   for rest in iterator])

# set up parameters to test
parameter_dicts = list(product_dict(
    shape = benchmark_data.__shapes__, 
    sampling = benchmark_data.__samplings__))

def test_shapes():
    for parameters in parameter_dicts:
        pb = benchmark_data.PersistenceDiagramBenchmark(
            **parameters,
            noise_distribution=normal_noise(sd=0.1))
        X = pb.sample(100)
        # check that number of points is correct
        assert X.shape[0] == 100

def test_targets():
    targets = {key: [] for key in benchmark_data.__shapes__}
    #dict.fromkeys(benchmark_data.__shapes__, [])
    for parameters in parameter_dicts:
        pb = benchmark_data.PersistenceDiagramBenchmark(
            **parameters)
        targets[parameters['shape']].append(pb.target())

    # check that the target is independent of sampling
    assert np.all([checkEqualPD(shape_target)
                   for _,shape_target in targets.items()])
