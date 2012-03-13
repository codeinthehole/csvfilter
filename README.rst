================================
csvfilter - Simple CSV filtering
================================

A simple wrapper around Python's CSV module to provide a command-line tool for
filtering columns from a CSV file.  This is useful as standard tools like awk
don't account for the quoting and escaping used in CSV files.  

Installation
------------

From PyPi::

    pip install csvfilter

Usage
-----

Pluck fields 1, 3 and 5::

    csvfilter -c 1,3,5 in.csv > out.csv

Pluck all fields apart from column 2::

    cat in.csv | csvfilter -c 2 -i > out.csv

Skip the header row::

    cat in.csv | csvfilter --skip=1

CSV data can be supplied through STDIN or by running ``csvfilter`` directly on a
file.

Help::

    $ csvfilter --help
    Usage: csvfilter [options]

    Options:
    -h, --help            show this help message and exit
    -c COLUMNS, --columns=COLUMNS
                            Specify which columns to pluck
    -s SKIP, --skip=SKIP  Number of rows to skip
    -d DELIMITER, --delimiter=DELIMITER
                            Delimiter of incoming CSV data
    -i, --inverse         Invert the filter - ie drop the selected columns


Contributing
------------

After cloning, install ``nose`` and run the test suite using::

    nosetests

To experiment with the executable, install in develop mode::

    ./setup.py develop

and use the fixture files::

    cat fixtures/au.csv | csvfilter -c 3,1,2 -s 1
    csvfilter fixutres/au.csv -c 1,2 -i