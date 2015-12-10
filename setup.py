#!/usr/bin/env python

from setuptools import setup


setup(name='dtw',
      version='1.2',
      description='Python DTW Module',
      author='Pierre Rouanet',
      author_email='pierre.rouanet@gmail.com',
      url='https://github.com/pierre-rouanet/dtw',
      license='GNU GENERAL PUBLIC LICENSE Version 3',

      install_requires=['numpy'],
      setup_requires=['setuptools_git >= 0.3', ],

      py_modules=['dtw'],
      )
