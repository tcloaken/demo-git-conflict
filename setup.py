#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: To use the 'upload' functionality of this file, you must:
#   $ pip install twine

import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup

# Package meta-data.
NAME = 'uobioinfo'
DESCRIPTION = "Demo for Bioinformatics and Genomics Master's Program"
VERSION = None

# Where the magic happens:
setup(
    name=NAME,
    version='0.1',
    description=DESCRIPTION,
    packages=find_packages(exclude=('tests',)),
    entry_points={
        'console_scripts': ['uobioinfo=uobioinfo.main:cli'],
    },
    include_package_data=True,
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
