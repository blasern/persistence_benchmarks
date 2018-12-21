# Persistence benchmarks

This repository provides functions to generate benchmark datasets for testing different aspects of the persistence pipline. 

## Type of data

We provide several different types of data that can be used for calculating persistent homology. Currently the types of data in this repository include the following. 

- Data sampled on a manifold.
- Data sampled on a manifold with noise.
- Data from given probability distributions.

## Objectives

Persistent homology can be used in piplines for different objectives. Currently the types of objectives included are the following. 

- Data with known persistence diagram (minimize bottleneck / Wasserstein distance). 
- Data with class labels (maximize accuracy / minimize log loss).
- Data with regression targets (minimize mean squared error / mean absolute error). 

## Development
 
If you find issues, please [let me know](https://github.com/blasern/persistence_benchmarks/issues). 
If you would like to contribute, please [create a pull request](https://github.com/blasern/persistence_benchmarks/compare).
