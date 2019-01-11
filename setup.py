#!/usr/bin/env python

import imp
from setuptools import setup, find_packages

version = imp.load_source('dtw.version', 'dtw/version.py')


setup(name='dtw',
      version=version.version,

      description='Python DTW Module',
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
