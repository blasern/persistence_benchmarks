#!/usr/bin/env python
"""Persistence benchmarks

An python library for generating benchmark datasets for 
benchmarking persistent homology. 

Installation

To install the latest version of this python library:

    git clone https://github.com/blasern/persistence_benchmarks.git
    cd persistence_benchmarks
    pip install .

"""

# import modules
from setuptools import setup

setup(
    name="persistence_benchmarks", 
    version="0.0.1",
    description="An python library for generating datasets" +
    " for benchmarking persistent homology algorithms",
    url="https://github.com/blasern/persistence_benchmarks",
    author="Nello Blaser",
    author_email="nello.blaser@uib.no",
    license="GPL-3",
    packages=["persistence_benchmarks"],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Data scientists',
        'Topic :: Topological data analysis :: Persistent homology',

        # Pick your license as you wish (should match "license" above)
        'License :: GPL-3',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        # 'Programming Language :: Python :: 2',
        # 'Programming Language :: Python :: 2.6',
        # 'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        # 'Programming Language :: Python :: 3.2',
        # 'Programming Language :: Python :: 3.3',
        # 'Programming Language :: Python :: 3.4'
    ],
    keywords="tda",
    install_requires=["numpy"]
)
