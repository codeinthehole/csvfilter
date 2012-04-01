#!/usr/bin/env python
from setuptools import setup, find_packages
from csvfilter import VERSION


setup(name='csvfilter',
      version=VERSION,
      url='https://github.com/codeinthehole/csvfilter',
      author="David Winterbottom",
      author_email="david.winterbottom@tangentlabs.co.uk",
      description="A command-line utility and Python API for manipulating CSV data, eg plucking columns and reordering them.  It's a bit like the unix utility 'cut'",
      long_description=open('README.rst').read(),
      packages=find_packages(),
      scripts=['bin/csvfilter'])
