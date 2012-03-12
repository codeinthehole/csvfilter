================================
csvfilter - Simple CSV filtering
================================

A simple wrapper around Python's CSV module to provide a command-line tool for
filtering columns from a CSV file.

Installation
------------

From PyPi::

    pip install csvfilter

Usage
-----

Pluck fields 1, 3 and 5 from ``stock.csv``::

    csvfilter -c 1,3,5 in.csv > out.csv

Contributing
------------

Install ``nose`` and run the test suite using::

    nosetests