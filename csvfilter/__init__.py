import csv


class Processor(object):
    DROP, PLUCK = 'Drop', 'Pluck'

    def __init__(self, columns=None, mode=PLUCK, delimiter=',', skip=0):
        self.columns = columns
        self.mode = mode
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
            if self.columns:
                if self.mode == self.PLUCK:
                    output = [row[i] for i in self.columns if len(row) > i]
                else:
                    output = [e for i,e in enumerate(row) if i not in self.columns]
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
