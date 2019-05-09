#!/usr/bin/env python
"""
Benchmark data generators
"""
from itertools import product
import numpy as np

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


def linkedTwistGenerator(sampling):
    def generate_linked_twist_map(n, p=4.0, x0=None, y0=None):
        """
        Linked twist map
        
        Parameters
        -----------
        n : int 
            Number of points
        p : float (default : 4.0)
            Linkage parameter
        x0,y0 : float (default : None)
            Initial point. Randomly generated if None. 
        """
        if x0 is None:
            x0=np.random.rand(1)
        if y0 is None:
            y0=np.random.rand(1)
        x = np.zeros(n)
        y = np.zeros(n)
        x[0] = x0
        y[0] = y0
        for i in range(1, n):
            x[i] = np.modf(x[i-1] + p*y[i-1]*(1-y[i-1]))[0]
            y[i] = np.modf(y[i-1] + p*x[i]*(1-x[i]))[0] 
        return np.vstack((x, y)).transpose()

    return generate_linked_twist_map

def unknownTarget():
    'unknown target'
    return None
   
