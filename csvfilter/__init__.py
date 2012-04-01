import csv

VERSION = '0.2.1'


class Processor(object):

    def __init__(self, fields=None, invert=False, delimiter=',', skip=0):
        self.fields = fields
        self.invert = invert
        self.delimiter = delimiter
        self.skip = skip
        self.validators = []

    def add_validator(self, f):
        self.validators.append(f)

    def process(self, file_handle):
        reader = csv.reader(file_handle, delimiter=self.delimiter)
        for row in reader:
            output = None
            if reader.line_num <= self.skip:
                continue
            if self.fields:
                if not self.invert:
                    output = [row[i] for i in self.fields if len(row) > i]
                else:
                    output = [e for i,e in enumerate(row) if i not in self.fields]
            else:
                output = row
            if not self.is_valid(output):
                continue
            if output:
                yield output

    def is_valid(self, row):
        for validator in self.validators:
            if not validator(row):
                return False
        return True
