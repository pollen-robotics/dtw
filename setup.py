#!/usr/bin/env python

import imp
from setuptools import setup, find_packages

version = imp.load_source('dtw.version', 'dtw/version.py')


long_description = '''
Dtw is a Python Module for computing Dynamic Time Warping distance. It can be used as a similarity measured between temporal sequences.

More info can be found at: https://github.com/pierre-rouanet/dtw

It is compatible with Python 2.7-3.6 and is distributed under the GPLv3 license.
'''

setup(name='dtw',
      version=version.version,

      description='Python DTW Module',
      long_description=long_description,
      author='Pierre Rouanet',
      author_email='pierre.rouanet@gmail.com',
      url='https://github.com/pierre-rouanet/dtw',
      license='GNU GENERAL PUBLIC LICENSE Version 3',

      packages=find_packages(),
      install_requires=['numpy', 'scipy'],

      test_suite='tests',

      classifiers=[
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 3",
          "Topic :: Scientific/Engineering", ],
      )
