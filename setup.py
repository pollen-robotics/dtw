#!/usr/bin/env python

import imp
from setuptools import setup

version = imp.load_source('dtw.version', 'dtw/version.py')


setup(name='dtw',
      version=version.version,
      description='Python DTW Module',
      author='Pierre Rouanet',
      author_email='pierre.rouanet@gmail.com',
      url='https://github.com/pierre-rouanet/dtw',
      license='GNU GENERAL PUBLIC LICENSE Version 3',

      install_requires=['numpy', 'scipy'],

      py_modules=['dtw'],
      test_suite='tests'
      )
