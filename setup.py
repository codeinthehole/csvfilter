#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='csvfilter',
      version='0.1.1',
      url='https://github.com/codeinthehole/csvfilter',
      author="David Winterbottom",
      author_email="david.winterbottom@tangentlabs.co.uk",
      description="A command-line tool and Python API for manipulating CSV data, eg plucking columns and reordering them",
      long_description=open('README.rst').read(),
      keywords="CSV",
      platforms=['linux'],
      packages=find_packages(),
      scripts = ['bin/csvfilter'])
