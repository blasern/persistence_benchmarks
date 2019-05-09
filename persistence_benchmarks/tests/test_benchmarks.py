import numpy as np
from itertools import product
from persistence_benchmarks import benchmark_data
from persistence_benchmarks import base_benchmarks
from persistence_benchmarks import diagram_benchmarks
from persistence_benchmarks import noise

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
    if first is not None: 
        return np.all([np.all([np.allclose(x, y) for x, y in zip(first, rest)])
                       for rest in iterator])
    else:
        return np.all([rest is None for rest in iterator])

# set up parameters to test
parameter_dicts = list(product_dict(
    shape = base_benchmarks.__shapes__, 
    sampling = base_benchmarks.__samplings__,
    noise_distribution = [noise.normal_noise(sd=0.1),
                          noise.uniform_noise(maxnoise=0.5)]
))

def test_shapes():
    for parameters in parameter_dicts:
        pb = diagram_benchmarks.PersistenceDiagramBenchmark(
            **parameters)
        X = pb.sample(100)
        # check that number of points is correct
        assert X.shape[0] == 100

def test_targets():
    targets = {key: [] for key in base_benchmarks.__shapes__}
    for parameters in parameter_dicts:
        pb = diagram_benchmarks.PersistenceDiagramBenchmark(
            **parameters)
        targets[parameters['shape']].append(pb.target())

    # check that the target is independent of sampling
    assert np.all([checkEqualPD(shape_target)
                   for _,shape_target in targets.items()])
